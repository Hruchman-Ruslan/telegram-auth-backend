import logging
from fastapi import HTTPException
from telethon import TelegramClient, errors
from .config import API_ID, API_HASH, MAX_ATTEMPTS, SESSIONS_DIR

clients = {}
attempts = {}

logging.basicConfig(
    filename="auth.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def mask_phone(phone: str) -> str:
    return f"{phone[:3]}******{phone[-2:]}"

async def send_code(phone: str):
    client = clients.get(phone)
    if not client or not client.is_connected():
        client = TelegramClient(SESSIONS_DIR / phone, API_ID, API_HASH)
        await client.connect()
        clients[phone] = client

    try:
        await client.send_code_request(phone)
        attempts[phone] = 0
        logging.info(f"{mask_phone(phone)} requested code")
        return {"status": "code_sent"}
    except Exception as e:
        logging.error(f"Failed to send code to {mask_phone(phone)}: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to send code: {str(e)}")

async def sign_in(phone: str, code: str):
    client = clients.get(phone)
    if not client:
        raise HTTPException(status_code=400, detail="Session not found")
    if attempts.get(phone, 0) >= MAX_ATTEMPTS:
        raise HTTPException(status_code=400, detail="Too many attempts")

    try:
        await client.sign_in(phone, code)
    except errors.SessionPasswordNeededError:
        return {"status": "need_password"}
    except Exception as e:
        attempts[phone] = attempts.get(phone, 0) + 1
        logging.warning(f"Failed sign-in attempt for {mask_phone(phone)}: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Invalid code or error: {str(e)}")

    await client.disconnect()
    logging.info(f"{mask_phone(phone)} successfully signed in")
    return {"status": "authorized", "session_file": str(SESSIONS_DIR / f"{phone}.session")}

async def sign_in_password(phone: str, password: str):
    client = clients.get(phone)
    if not client:
        raise HTTPException(status_code=400, detail="Session not found")

    try:
        await client.sign_in(password=password)
    except Exception as e:
        logging.warning(f"Failed 2FA for {mask_phone(phone)}: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Invalid password: {str(e)}")

    await client.disconnect()
    logging.info(f"{mask_phone(phone)} successfully signed in with 2FA")
    return {"status": "authorized", "session_file": str(SESSIONS_DIR / f"{phone}.session")}
