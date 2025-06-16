from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

class PersonDTO(BaseModel):
    id: Optional[uuid.UUID]
    name: str
    description: Optional[str] = None
    phone: Optional[str] = None
    email: EmailStr
    address: Optional[str] = None