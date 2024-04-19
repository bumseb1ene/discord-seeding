import discord
import asyncio
import requests
import logging
from dotenv import load_dotenv
import os

# Konfiguriere das Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Laden der Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Definiere die Discord-Bot-Token
TOKEN = os.getenv('DISCORD_TOKEN')
UPDATE_INTERVAL_SECONDS = int(os.getenv('UPDATE_INTERVAL_SECONDS', 300))

# Definiere das Mapping zwischen RCON-API-URLs und Discord-Channel-IDs
RCON_DISCORD_MAPPING = {
     # ('RCON http path', 'Discord-Channel-ID': 'Discord Original Channel Name', separated with commas more than one are possible
    ('http://127.0.0.1:8010', '1234567890'): 'Discord Original Channel Name'
}

# Definiere die Verbindungsinformationen für die RCON-API
API_TOKEN = os.getenv('API_TOKEN')

# Definiere den Discord-Client mit den erforderlichen Intents
intents = discord.Intents.default()
intents.guilds = True
client = discord.Client(intents=intents)

# Funktion zur Überprüfung der Anzahl der Spieler auf dem Server
def check_player_count(api_url):
    while True:
        try:
            response = requests.get(f"{api_url}/api/get_status", headers={"Authorization": f"Bearer {API_TOKEN}"})
            if response.status_code == 200:
                gamestate = response.json()["result"]
                total_players = int(gamestate["player_count"])
                logging.debug(f"Server {api_url} - Spieleranzahl erfolgreich abgerufen: {total_players}")
                return total_players
            else:
                logging.error(f"Fehler beim Abrufen des Spielzustands für {api_url} - Status Code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Fehler beim Kommunizieren mit der RCON-API für {api_url}: {e}")
            logging.info("Versuche erneut in 60 Sekunden.")
            time.sleep(60)

async def update_channel_status():
    for (api_url, channel_id), channel_name in RCON_DISCORD_MAPPING.items():
        total_players = check_player_count(api_url)
        if total_players is not None:
            status_symbol = "🔴" if total_players <= int(os.getenv('FLAG_YELLOW')) else "🟡" if total_players <= int(os.getenv('FLAG_GREEN')) else "🟢"
            new_name = f"{status_symbol}{total_players} {channel_name}"
            try:
                channel = await client.fetch_channel(channel_id)
                if new_name != channel.name:
                    await channel.edit(name=new_name)
                    logging.info(f"Kanalname für '{channel_name}' aktualisiert zu: {new_name}")
            except discord.errors.DiscordException as e:
                logging.error(f"Kanalname für '{channel_name}' konnte nicht aktualisiert werden: {e}")
        else:
            logging.error(f"Kanalname für '{channel_name}' konnte nicht aktualisiert werden wegen fehlender Spielerdaten")
                
@client.event
async def on_ready():
    logging.info(f'{client.user} ist eingeloggt.')
    while True:
        await update_channel_status()
        await asyncio.sleep(UPDATE_INTERVAL_SECONDS)

client.run(TOKEN)
