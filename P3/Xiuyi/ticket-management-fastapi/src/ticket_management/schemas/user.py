from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    name: Optional[str] = None
    email: Optional[str] = None

class UserInDB(UserBase):
    id: int

class User(UserInDB):
    pass

class UserList(BaseModel):
    users: List[User]