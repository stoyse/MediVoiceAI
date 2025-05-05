from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import PlainTextResponse
import uvicorn
import assemblyai as aai
from elevenlabs import ElevenLabs
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import base64
import json
import os
import audioop

app = FastAPI()

# Load DeepSeek model and tokenizer (adjust model name as needed)
model_name = "deepseek-ai/deepseek-llm-7b"  # Verify exact name on Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda")

# Set up API keys from environment variables
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
elevenlabs_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Store conversation state
conversation_history = {}
websockets_dict = {}
stream_sids = {}

# Generate AI response with conversation context
def generate_response(history):
    input_text = ""
    for msg in history:
        if msg["role"] == "user":
            input_text += f"<|user|>{msg['content']}<|end|>\n"
        elif msg["role"] == "assistant":
            input_text += f"<|assistant|>{msg['content']}<|end|>\n"
    input_text += "<|assistant|>"
    inputs = tokenizer(input_text, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Twilio webhook to start the call
@app.post("/incoming_call")
async def incoming_call(request: Request):
    twiml = """
    <Response>
        <Say>Hello, please speak after the beep.</Say>
        <Pause length="1"/>
        <Say>Beep.</Say>
        <Start>
            <Stream url="wss://{your-domain}/stream" />
        </Start>
        <Pause length="3600"/>
    </Response>
    """.replace("{your-domain}", os.getenv("APP_DOMAIN", "your-domain.com"))
    return PlainTextResponse(twiml)

# WebSocket handler for audio streaming
@app.websocket("/stream")
async def stream(websocket: WebSocket):
    await websocket.accept()
    connection_id = str(id(websocket))
    conversation_history[connection_id] = []
    websockets_dict[connection_id] = websocket

    # Set up AssemblyAI transcriber
    transcriber = aai.RealtimeTranscriber(
        on_data=lambda transcript, ctx: on_data(transcript, ctx),
        on_error=lambda error, ctx: on_error(error, ctx),
        sample_rate=8000,
        encoding=aai.AudioEncoding.PCM_MULAW,
        context=connection_id
    )
    transcriber.connect()

    try:
        while True:
            message = await websocket.receive_text()
            data = json.loads(message)
            if data["event"] == "media":
                audio_data = base64.b64decode(data["media"]["payload"])
                transcriber.send_audio(audio_data)
            elif data["event"] == "start":
                stream_sids[connection_id] = data["streamSid"]
                print(f"Call started: {connection_id}")
            elif data["event"] == "stop":
                print(f"Call ended: {connection_id}")
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        transcriber.close()
        del conversation_history[connection_id]
        del websockets_dict[connection_id]
        if connection_id in stream_sids:
            del stream_sids[connection_id]

# Process transcription data
def on_data(transcript, context):
    connection_id = context
    if transcript.text and transcript.message_type == aai.TranscriptMessageType.Final:
        history = conversation_history[connection_id]
        history.append({"role": "user", "content": transcript.text})
        response = generate_response(history)
        history.append({"role": "assistant", "content": response})

        # Convert response to speech
        audio_stream = elevenlabs_client.generate(
            text=response,
            voice="your_voice_id",  # Replace with desired voice ID
            model="eleven_monolingual_v1",
            output_format="pcm_16000"
        )
        audio_data = audio_stream.read()
        mulaw_audio = audioop.ratecv(audioop.lin2ulaw(audio_data, 2), 2, 1, 16000, 8000, None)[0]
        send_audio_to_twilio(mulaw_audio, connection_id)

# Handle transcription errors
def on_error(error, context):
    print(f"Transcription error: {error}")

# Send audio back to Twilio
def send_audio_to_twilio(audio_data, connection_id):
    websocket = websockets_dict[connection_id]
    stream_sid = stream_sids[connection_id]
    message = {
        "event": "media",
        "streamSid": stream_sid,
        "media": {"payload": base64.b64encode(audio_data).decode()}
    }
    asyncio.run(websocket.send_text(json.dumps(message)))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)