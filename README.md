# MediVoiceAI - KI-gestütztes Praxismanagement System

MediVoiceAI ist ein modernes Praxismanagement-System, das KI-gestützte Anrufbeantwortung und Patientenkommunikation mit einer benutzerfreundlichen Web-Oberfläche kombiniert. Das System ermöglicht die effiziente Verwaltung von Patienten, Terminen und Kommunikation und spart wertvolle Zeit für medizinisches Personal.

## Übersicht der Seiten und Funktionen

### Dashboard (index.html)

Die zentrale Übersichtsseite bietet einen schnellen Überblick über alle wichtigen Praxismetriken und aktuelle Informationen.

**Funktionen:**
- Tagesübersicht mit aktuellen Statistiken (Patienten, Wartezeit, KI-Effizienz, Patientenzufriedenheit)
- Schnellzugriff auf häufig verwendete Funktionen (Termin anlegen, Patient anlegen, etc.)
- Anzeige der heutigen Termine mit Status
- Aktuelle Nachrichten und KI-Interaktionen als Vorschau
- KI-Leistungsübersicht als Chart mit historischen Daten
- Aktivitätsprotokoll der letzten Aktionen im System

### Patientenverwaltung (patients.html)

Zentrale Verwaltung aller Patientendaten und -interaktionen.

**Funktionen:**
- Übersichtsstatistiken (Gesamtzahl Patienten, neue Patienten, anstehende Untersuchungen)
- KI-Interaktionsübersicht der letzten 24 Stunden
- Erweiterte Suchfunktion für Patienten
- Filteroptionen für verschiedene Patientengruppen
- Sortierbare Patientenliste mit wichtigen Informationen
- KI-Interaktionsverlauf mit Patienten
- Schnellzugriff auf Patientenmanagement-Funktionen
- Übersicht kommender Patientengeburtstage

### Terminverwaltung (appointments.html)

Vollständiges Terminmanagement mit Kalenderansicht und KI-Integration.

**Funktionen:**
- Statistik-Übersicht (Termine heute, Termine diese Woche, KI-Terminanfragen)
- Tabellarische Terminübersicht mit Filteroptionen
- Interaktive Wochenkalenderansicht mit farblicher Kennzeichnung verschiedener Termintypen
- Anzeige von KI-geplanten Terminen mit spezieller Markierung
- Unterschiedliche Darstellungen für Werktage, Wochenenden und den aktuellen Tag
- Legende zur Erklärung der verschiedenen Termintypen
- Funktion zum Hinzufügen neuer Termine

### Nachrichten & KI-Anrufbeantworter (messages.html)

Zentrale Kommunikationsschnittstelle mit Nachrichtenverwaltung und KI-Anrufprotokollen.

**Funktionen:**
- KI-Anrufbeantworter-Übersicht mit Statistiken (Anrufe heute, Terminanfragen, unbearbeitete Anfragen)
- Kategorie-Tabs für verschiedene Nachrichtentypen (Alle, KI-Anrufprotokolle, Terminanfragen, Rezeptanfragen)
- Liste aller Nachrichten mit Priorisierung und Lesebestätigungssystem
- Markierung von KI-generierten Nachrichten und Protokollen
- Abspielfunktion für Anrufaufzeichnungen
- Statistik-Charts für Anrufvolumen nach Tageszeit und Verteilung der Anfragetypen
- Funktionen zum Weiterleiten und Bearbeiten von Anfragen

### Berichte & Auswertungen (reports.html)

Umfassende Analyse- und Berichtsfunktionen zur Auswertung aller Praxisdaten.

**Funktionen:**
- Zusammenfassende Kennzahlen (KI-Nutzungseffizienz, Zeitersparnis, Patientenzufriedenheit)
- Einstellbare Berichtsfilter nach Zeitraum und Berichtstyp
- Hauptchart zur Visualisierung der KI-Anrufmanagement-Übersicht
- Anzeige der Anrufauflösung nach Kategorie und häufigsten Anfragegründen
- Tabellarische Übersicht bereits erstellter Berichte mit Download- und Vorschaufunktion
- Export-Funktionalität für Berichte

### Einstellungen (settings.html)

Zentrale Konfigurationsoberfläche für alle Systemeinstellungen.

**Funktionen:**
- Profilmanagement für Ärzte und Praxispersonal
- Passwort- und Sicherheitseinstellungen
- KI-Anrufbeantworter-Konfiguration:
  - Aktivierung/Deaktivierung des KI-Systems
  - Auswahl und Anpassung des KI-Sprachmodells
  - Anpassung der Begrüßungsnachrichten
  - Verwaltung der Praxis-Öffnungszeiten
  - Konfiguration der automatischen Terminvergabe
  - Einstellungen für Rezeptanfragen und Weiterleitung
- Benachrichtigungseinstellungen (E-Mail, Push, tägliche Zusammenfassung)

### Weiterleitung komplexer Anfragen (weiterleitung.html)

Spezialisierte Schnittstelle zur Konfiguration und Verwaltung der intelligenten Weiterleitungsregeln.

**Funktionen:**
- Übersicht und Erklärung des intelligenten Weiterleitungssystems
- Verwaltung von Notfallkontakten für verschiedene Szenarien
- KI-Weiterleitungskonfiguration mit:
  - Aktivierung/Deaktivierung der automatischen Weiterleitung
  - Verwaltung von Schlüsselwörtern für die Erkennung von Weiterleitungsbedarf
  - Regelbasiertes System mit priorisierten Weiterleitungsszenarien
- Statistische Auswertung der Weiterleitungen (heute, diese Woche, Automatisierungsgrad)
- Protokoll der letzten Weiterleitungen mit detaillierten Informationen

## Backend-System

Das Backend von MediVoiceAI basiert auf FastAPI und nutzt fortschrittliche KI-Technologien für die Spracherkennung und -generierung.

**Technologien:**
- AssemblyAI für die Echtzeittranskription von Anrufen
- DeepSeek LLM für die Verarbeitung und Generierung natürlichsprachlicher Antworten
- ElevenLabs für die Sprachsynthese hochwertiger, natürlich klingender Antworten
- Twilio für die Telefonie-Integration
- Echtzeit-Streaming-Verarbeitung für minimale Latenz

## Installation und Setup

1. Frontend-Dateien in einen Webserver-Ordner kopieren
2. Backend-Abhängigkeiten installieren:
```
pip install fastapi uvicorn assemblyai elevenlabs transformers torch
```
3. Umgebungsvariablen konfigurieren:
```
ASSEMBLYAI_API_KEY=dein_api_key
ELEVENLABS_API_KEY=dein_api_key
APP_DOMAIN=deine_domain.com
```
4. Backend-Server starten:
```
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Systemanforderungen

- Moderner Webserver (Apache, Nginx etc.) für das Frontend
- Python 3.8+ für das Backend
- CUDA-fähige GPU für optimale KI-Leistung
- Mindestens 8GB RAM, empfohlen 16GB
