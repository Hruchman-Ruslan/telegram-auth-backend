from pydantic import BaseModel, Field
from typing import Annotated

PhoneType = Annotated[str, Field(pattern=r'^\+\d{10,15}$')]
NonEmptyStr = Annotated[str, Field(min_length=1)]

class PhoneNumber(BaseModel):
    phone: PhoneType

class CodeData(BaseModel):
    phone: PhoneType
    code: NonEmptyStr

class PasswordData(BaseModel):
    phone: PhoneType
    password: NonEmptyStr
