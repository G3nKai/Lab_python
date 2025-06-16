from pydantic import BaseModel, EmailStr
from typing import Optional

class PersonDTO(BaseModel):
    name: str
    description: Optional[str] = None
    phone: Optional[str] = None
    email: EmailStr
    address: Optional[str] = None