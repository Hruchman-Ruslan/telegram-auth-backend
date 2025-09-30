import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
MAX_ATTEMPTS = 3

SESSIONS_DIR = Path("app/sessions_private")
SESSIONS_DIR.mkdir(exist_ok=True)
