from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "8125003821:AAF43mHBu7ergH08eX1It8kpS1dXTU2PIcA")
BOT_USERNAME = getenv("BOT_USERNAME", "https://t.me/Anime_Vc_Music_Bot")
admins = {}
API_ID = int(getenv("API_ID", "8726992"))
API_HASH = getenv("API_HASH", "fbf4bc635f74937b9669af1d715171c9")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
