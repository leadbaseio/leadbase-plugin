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

Du brauchst ein Leadbase-Konto mit Zugriff auf einen Arbeitsbereich. Füge dieses Plugin hinzu, verbinde den Leadbase-Connector und melde dich über OAuth an. Wähle deinen Arbeitsbereich. API-Schlüssel oder Passwörter gehören nicht in eine Unterhaltung. Plugin und Leadbase-Connector nutzen denselben Endpunkt; eine Verbindung genügt.

Recherchen verbrauchen vorhandene Credits deines Arbeitsbereichs. Die Grenzen deines Tarifs gelten weiterhin. Das Verbinden, Öffnen von Sheets und Prüfen des Guthabens beauftragt keine kostenpflichtige Recherche. Deinen Tarif verwaltest du auf der Leadbase-Website. Das Plugin kauft keine Credits und versendet keine Kontaktansprache.

## Beispiele

„Finde 5 unabhängige Kaffeeröstereien in Berlin mit offizieller Website. Speichere pro Firma eine Zeile in einem neuen Sheet und zeige es an.“

„Ergänze die leeren Hauptsitz-Zellen für alle Unternehmen in diesem Sheet anhand offizieller Quellen. Behalte vorhandene Werte.“

„Öffne meinen Leadbase-Arbeitsbereich und zeige den Fortschritt meiner letzten Recherche.“

## Sheets und Ergebnisse

Unterstützte Claude-Oberflächen können das interaktive Leadbase-Sheet über MCP Apps anzeigen. Clients ohne UI erhalten strukturierte Ergebnisse und einen Leadbase-Link. Verfügbare Anzeigemodi hängen vom Client ab. Laufender Fortschritt ist von fertigen Ergebnissen zu unterscheiden; der Abschluss der Ausführung ist unabhängig von der endgültigen Credit-Abrechnung. Ergebnisse können unvollständig sein oder ausreichende Belege vermissen lassen. Prüfe die Quellen, bevor du auf Basis der Ergebnisse handelst.

## Daten und Berechtigungen

Dieses Paket enthält zwei Recherche-Skills und einen Verweis auf den gehosteten Leadbase-MCP-Server unter https://www.leadbase.io/api/mcp. Es nutzt denselben Server, dieselben Kontoberechtigungen und denselben Sheet-Editor wie die Codex-Integration. Es startet keine lokalen Server, Shell-Hooks, Hintergrundskripte oder Paketinstallationen.

Bei einem Werkzeugaufruf werden die angeforderten Argumente und der relevante Sheet-Kontext an Leadbase übertragen. Leadbase speichert Sheets und Rechercheergebnisse in deinem Arbeitsbereich und nutzt die in der Datenschutzerklärung beschriebenen Dienstleister für Recherche und Hosting. Das Paket fügt keinen eigenen Datenspeicher und keine eigene Telemetrie hinzu. Leadbase erhält nur den über Werkzeugaufrufe gesendeten Kontext; das Plugin liest deinen Gesprächsverlauf nicht eigenständig aus. Dein verbundenes Konto bestimmt den Lese- und Schreibzugriff. Freigaben, Löschungen und kostenpflichtige Recherchen bleiben ausdrückliche Aktionen.

Die [Datenschutzerklärung](https://www.leadbase.io/de/legal/privacy) beschreibt Datenverarbeitung, Dienstleister, Speicherfristen und Löschanfragen. Für dein Konto gelten die [Nutzungsbedingungen](https://www.leadbase.io/de/legal/terms).

## Hilfe

[Einrichtung und Nutzung](https://www.leadbase.io/de/docs/settings/mcp) · [Support](https://www.leadbase.io/de/contact) · [English](README.md)
