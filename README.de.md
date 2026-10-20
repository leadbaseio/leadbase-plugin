# Leadbase

Finde Leads. Erstelle Listen.

Aus deiner Rechercheanfrage entstehen Unternehmen, Geschäftskontakte, Produkte oder öffentliche Beiträge in einem Sheet, das du prüfen und bearbeiten kannst. Leadbase recherchiert im Web, speichert verfügbare Quellen und hält Ergebnisse im selben Arbeitsbereich wie auf [leadbase.io](https://www.leadbase.io).

## Deine Möglichkeiten

- Erstelle neue Listen mit einem Ergebnis pro Zeile.
- Ergänze fehlende Angaben in vorhandenen Zeilen oder einer ganzen Spalte. Bereits ausgefüllte Zellen bleiben erhalten.
- Verfolge den Fortschritt und prüfe verfügbare Quellen.
- Öffne, durchsuche, filtere und bearbeite Sheets entsprechend deinen Berechtigungen.
- Prüfe Tarif und Credit-Guthaben, ohne eine Recherche zu starten.

## Konto verbinden

Dies ist das gemeinsame Leadbase-Plugin-Paket für mehrere Clients. Alle Formate nutzen dieselben zwei Skills und denselben gehosteten MCP-Dienst. Das Paket enthält keinen privaten Anwendungscode.

| Client | Einstiegspunkt im Paket | Verbindung |
| --- | --- | --- |
| Codex und Clients für Agent Plugins 1.0 | `plugin.json` | `mcp.json` (Streamable HTTP) |
| Cursor | `.cursor-plugin/plugin.json` | `.mcp.json` (HTTP-Kompatibilitätsformat) |
| Claude | `.claude-plugin/plugin.json` | `.mcp.json` (HTTP-Kompatibilitätsformat) |
| Grok Bot und kompatible MCP-Clients | Plugin-Import des Clients oder MCP-Server-URL | `https://www.leadbase.io/api/mcp` |

Beide MCP-Dateien beschreiben denselben OAuth-geschützten Endpunkt mit der für das jeweilige Format nötigen Transportbezeichnung. Paketkompatibilität, Marketplace-Freigabe und angemeldete Tests im Client sind getrennte Prüfungen. Bestehende Einreichungen bei OpenAI und Claude behalten ihre bisherigen Identitäten und eingereichten Versionen; dieses Repository ersetzt sie nicht automatisch.

Für einen lokalen Cursor-Test kopierst du dieses Paket nach `~/.cursor/plugins/local/leadbase-research` und lädst ein Testfenster neu. Prüfe unter **Customize** die zwei Skills und den MCP-Server `leadbase`. Melde dich über den OAuth-Ablauf des Clients an. Dein Konto oder Team muss lokale Plugin-Importe erlauben. In anderen kompatiblen Clients nutzt du deren lokale Plugin-Installation oder fügst den unten genannten HTTPS-MCP-Endpunkt hinzu. Eine Marketplace-Veröffentlichung setzt die Prüfung der jeweiligen Plattform voraus.

Du brauchst ein Leadbase-Konto mit Zugriff auf einen Arbeitsbereich. Füge dieses Plugin hinzu, verbinde den Leadbase-Connector und melde dich über OAuth an. Wähle deinen Arbeitsbereich. API-Schlüssel oder Passwörter gehören nicht in eine Unterhaltung. Plugin und Leadbase-Connector nutzen denselben Endpunkt; eine Verbindung genügt.

Recherchen verbrauchen vorhandene Credits deines Arbeitsbereichs. Die Grenzen deines Tarifs gelten weiterhin. Das Verbinden, Öffnen von Sheets und Prüfen des Guthabens beauftragt keine kostenpflichtige Recherche. Deinen Tarif verwaltest du auf der Leadbase-Website. Das Plugin kauft keine Credits und versendet keine Kontaktansprache.

## Beispiele

„Finde 5 unabhängige Kaffeeröstereien in Berlin mit offizieller Website. Speichere pro Firma eine Zeile in einem neuen Sheet und zeige es an.“

„Ergänze die leeren Hauptsitz-Zellen für alle Unternehmen in diesem Sheet anhand offizieller Quellen. Behalte vorhandene Werte.“

„Öffne meinen Leadbase-Arbeitsbereich und zeige den Fortschritt meiner letzten Recherche.“

## Sheets und Ergebnisse

Clients mit MCP-Apps-Unterstützung können das interaktive Leadbase-Sheet anzeigen. Clients ohne UI erhalten strukturierte Ergebnisse und einen Leadbase-Link. Verfügbare Anzeigemodi hängen vom Client ab. Laufender Fortschritt ist von fertigen Ergebnissen zu unterscheiden; der Abschluss der Ausführung ist unabhängig von der endgültigen Credit-Abrechnung. Ergebnisse können unvollständig sein oder ausreichende Belege vermissen lassen. Prüfe die Quellen, bevor du auf Basis der Ergebnisse handelst.

## Daten und Berechtigungen

Dieses Paket enthält zwei Recherche-Skills und einen Verweis auf den gehosteten Leadbase-MCP-Server unter https://www.leadbase.io/api/mcp. Es nutzt denselben Server, dieselben Kontoberechtigungen und denselben Sheet-Editor wie die Codex-Integration. Es startet keine lokalen Server, Shell-Hooks, Hintergrundskripte oder Paketinstallationen.

Bei einem Werkzeugaufruf werden die angeforderten Argumente und der relevante Sheet-Kontext an Leadbase übertragen. Leadbase speichert Sheets und Rechercheergebnisse in deinem Arbeitsbereich und nutzt die in der Datenschutzerklärung beschriebenen Dienstleister für Recherche und Hosting. Das Paket fügt keinen eigenen Datenspeicher und keine eigene Telemetrie hinzu. Leadbase erhält nur den über Werkzeugaufrufe gesendeten Kontext; das Plugin liest deinen Gesprächsverlauf nicht eigenständig aus. Dein verbundenes Konto bestimmt den Lese- und Schreibzugriff. Freigaben, Löschungen und kostenpflichtige Recherchen bleiben ausdrückliche Aktionen.

Die [Datenschutzerklärung](https://www.leadbase.io/de/legal/privacy) beschreibt Datenverarbeitung, Dienstleister, Speicherfristen und Löschanfragen. Für dein Konto gelten die [Nutzungsbedingungen](https://www.leadbase.io/de/legal/terms).

## Lizenz

Die Dateien in diesem öffentlichen Plugin-Paket stehen unter der [MIT-Lizenz](LICENSE). Der gehostete Leadbase-Dienst und der private Anwendungscode sind davon getrennt und werden durch dieses Repository nicht lizenziert. Für dein Leadbase-Konto gelten weiterhin die Nutzungsbedingungen des Dienstes. Die MIT-Lizenz gewährt keine Markenrechte. Die eingebundenen Schemas behalten ihre mitgelieferte ursprüngliche Lizenz.

## Hilfe

Als Maintainer prüfst du alle Manifeste, die gemeinsame Endpunkt-Konfiguration, Skills und Asset-Pfade mit `python -m pip install -r requirements-validation.txt` und anschließend `python scripts/validate-package.py`. Dieselbe Prüfung läuft in GitHub Actions mit Lesezugriff auf das Repository. Die offiziellen Schemas liegen fest versioniert unter `schemas/`; ihre ursprüngliche Lizenz ist dort enthalten. Bei der Plugin-Installation wird kein Prüfcode ausgeführt.

[Einrichtung und Nutzung](https://www.leadbase.io/de/docs/settings/mcp) · [Support](https://www.leadbase.io/de/contact) · [English](README.md)
