from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CustomerIn(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class CustomerOut(CustomerIn):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
