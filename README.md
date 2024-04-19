Dieses Skript ist ein Discord-Bot, der die Anzahl der Spieler auf einem Spielserver überwacht und den Namen von Discord-Kanälen basierend auf dieser Anzahl aktualisiert.

Schritt-für-Schritt-Erklärung:
Importe und Logging-Konfiguration:
Das Skript importiert die erforderlichen Pakete und konfiguriert das Logging, um Fehler und Debug-Informationen zu erfassen.
Laden der Umgebungsvariablen:
Die Umgebungsvariablen werden aus der .env-Datei geladen, um sensible Informationen wie Discord-Token und API-Token zu verwalten.
Definieren der Discord-Bot-Token und des Aktualisierungsintervalls:
Der Discord-Bot-Token und das Intervall, in dem die Kanäle aktualisiert werden sollen, werden aus den Umgebungsvariablen geladen.
Definieren des Mapping zwischen RCON-API-URLs und Discord-Channel-IDs:
Es wird eine Zuordnung zwischen den RCON-API-URLs der Spielserver und den zugehörigen Discord-Channel-IDs definiert. Dieses Mapping wird verwendet, um die Kanalnamen zu aktualisieren.
Definieren der Verbindungsinformationen für die RCON-API:
Das API-Token für die Authentifizierung bei der RCON-API wird aus den Umgebungsvariablen geladen.
Definieren des Discord-Clients mit den erforderlichen Intents:
Ein Discord-Client wird mit den erforderlichen Intents erstellt, um auf Ereignisse wie das Starten des Bots und das Abrufen von Kanälen zu reagieren.
Funktion zur Überprüfung der Anzahl der Spieler auf dem Server:
Es wird eine Funktion definiert, die die Anzahl der Spieler auf einem Spielserver über die RCON-API abruft.
Funktion zum Aktualisieren des Kanalstatus:
Es wird eine asynchrone Funktion definiert, die die Anzahl der Spieler auf jedem Server überprüft und den Kanalnamen entsprechend aktualisiert.
on_ready-Event-Handler:
Ein Event-Handler wird definiert, der aufgerufen wird, wenn der Bot erfolgreich eingeloggt ist. Dieser Handler ruft die Funktion zur Aktualisierung des Kanalstatus auf und wiederholt sie in regelmäßigen Abständen.
Starten des Discord-Clients:
Der Discord-Client wird mit dem Discord-Bot-Token gestartet, um den Bot online zu bringen und auf Ereignisse zu reagieren.
Funktionsweise des Skripts:
Der Bot ruft in regelmäßigen Abständen die Anzahl der Spieler auf jedem Spielserver über die RCON-API ab.
Basierend auf der Anzahl der Spieler wird ein Statussymbol generiert (rot, gelb oder grün), und der Kanalname des entsprechenden Discord-Kanals wird aktualisiert.
Der Bot bleibt online und aktualisiert die Kanalnamen in regelmäßigen Abständen, solange er eingeloggt ist.
Einrichtung des Skripts:
Legen Sie die erforderlichen Umgebungsvariablen in der .env-Datei fest, einschließlich Discord-Token, API-Token und anderen konfigurationsbezogenen Variablen.
Führen Sie das Skript aus, um den Bot zu starten und die Kanalnamen zu aktualisieren.
Nachdem Sie diese Schritte ausgeführt haben, sollte der Bot erfolgreich gestartet werden und die Kanalnamen basierend auf der Anzahl der Spieler auf den Spielservern aktualisieren.

Hier ist eine Schritt-für-Schritt-Anleitung zur Einrichtung dieses Discord-Bots:

1. Erstellen eines Discord-Bots:
Öffnen Sie den Discord Developer Portal.
Klicken Sie auf "New Application" und geben Sie Ihrem Bot einen Namen.
Navigieren Sie zur Registerkarte "Bot" und klicken Sie auf "Add Bot".
Kopieren Sie das Token Ihres Bots, das unter dem Bot-Namen angezeigt wird.
2. Hinzufügen des Bots zu Ihrem Discord-Server:
Kopieren Sie die Client-ID Ihres Bots aus dem "General Information"-Abschnitt der "General Information"-Seite in den Entwicklereinstellungen Ihres Bots.
Verwenden Sie diesen Link und ersetzen Sie YOUR_CLIENT_ID durch die Client-ID Ihres Bots.
Wählen Sie den Server aus, zu dem Sie den Bot hinzufügen möchten, und erteilen Sie die erforderlichen Berechtigungen.
3. Einrichten der .env-Datei:
Erstellen Sie eine .env-Datei im selben Verzeichnis wie das Skript.
Legen Sie die Umgebungsvariablen in der .env-Datei fest:
DISCORD_TOKEN: Das Discord-Bot-Token, das Sie zuvor kopiert haben.
UPDATE_INTERVAL_SECONDS (optional): Das Intervall in Sekunden, in dem die Kanalnamen aktualisiert werden sollen (Standardwert: 300).
API_TOKEN: Das Token für die Authentifizierung bei der RCON-API.
Konfigurieren Sie die erforderlichen Umgebungsvariablen gemäß Ihren Server- und Kanalinformationen.
4. Starten des Discord-Bots:
Führen Sie das Skript aus, indem Sie das entsprechende Skript auswählen und python your_script_name.py in der Befehlszeile oder im Terminal eingeben.
Überprüfen Sie die Ausgabe in der Konsole, um sicherzustellen, dass der Bot erfolgreich gestartet wurde und verbunden ist.
5. Überwachung und Fehlerbehebung:
Überwachen Sie die Konsole auf etwaige Fehlermeldungen.
Stellen Sie sicher, dass die Umgebungsvariablen korrekt festgelegt sind und dass alle erforderlichen Pakete installiert sind.
Testen Sie die Funktionalität des Bots, indem Sie Änderungen an der Spieleranzahl auf Ihrem Server vornehmen und die Kanalnamen auf Discord aktualisieren.
Nachdem Sie diese Schritte ausgeführt haben, sollte Ihr Discord-Bot erfolgreich eingerichtet und gestartet sein. Er wird nun die Anzahl der Spieler auf Ihrem Spielserver überwachen und die Kanalnamen in Discord entsprechend aktualisieren.

Die .env-Datei enthält Konfigurationsvariablen und sensible Informationen, die von Ihrem Discord-Bot und Ihrem Skript verwendet werden. Hier ist eine Erklärung der in Ihrer .env-Datei enthaltenen Variablen:

DISCORD_TOKEN=:
Dies ist das Discord-Bot-Token, das Sie beim Erstellen Ihres Discord-Bots im Discord Developer Portal erhalten haben. Es wird verwendet, um den Bot mit Ihrem Discord-Server zu verbinden und auf Ereignisse zu reagieren.
API_TOKEN=:
Dies ist das Token für die Authentifizierung bei der RCON-API (Remote Console), die verwendet wird, um die Anzahl der Spieler auf Ihrem Spielserver abzurufen. Dieses Token ermöglicht Ihrem Bot den Zugriff auf die API und das Abrufen von Spielerdaten.
UPDATE_INTERVAL_SECONDS=300:
Dies ist das Intervall in Sekunden, in dem die Kanalnamen auf Discord aktualisiert werden sollen. Standardmäßig ist es auf 300 Sekunden (5 Minuten) eingestellt. Der Bot überprüft alle 5 Minuten die Spieleranzahl auf Ihrem Server und aktualisiert entsprechend die Kanalnamen.
FLAG_GREEN=40:
Dies ist die Anzahl der Spieler, ab der der Kanalname grün markiert wird. Wenn die Spieleranzahl unter diesem Wert liegt, wird der Kanal grün dargestellt, um anzuzeigen, dass der Server nicht voll ist.
FLAG_YELLOW=3:
Dies ist die Anzahl der Spieler, ab der der Kanalname gelb markiert wird. Wenn die Spieleranzahl über dem Wert FLAG_YELLOW und unterhalb von FLAG_GREEN liegt, wird der Kanalname gelb markiert, um darauf hinzuweisen, dass der Server fast voll ist.
Diese Variablen sind wichtig, um die Funktionalität Ihres Discord-Bots zu steuern und anzupassen. Stellen Sie sicher, dass Sie die Werte entsprechend Ihren Anforderungen und Präferenzen anpassen. Achten Sie darauf, die .env-Datei sicher zu speichern und sensible Informationen wie Tokens niemals öffentlich freizugeben.
