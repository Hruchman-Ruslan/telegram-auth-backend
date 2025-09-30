from fastapi import APIRouter
from .models import PhoneNumber, CodeData, PasswordData
from .auth import send_code, sign_in, sign_in_password

router = APIRouter()

@router.post("/send_code")
async def api_send_code(data: PhoneNumber):
    return await send_code(data.phone)

@router.post("/sign_in")
async def api_sign_in(data: CodeData):
    return await sign_in(data.phone, data.code)

@router.post("/sign_in_password")
async def api_sign_in_password(data: PasswordData):
    return await sign_in_password(data.phone, data.password)
