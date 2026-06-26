from pydantic import BaseModel, EmailStr

# Base properties shared across models
class UserBase(BaseModel):
    email: EmailStr

# Properties to receive on user creation
class UserCreate(UserBase):
    password: str

# Properties to return to client
class User(UserBase):
    id: int
    is_active: bool

    class Config:
        # This tells Pydantic to read data even if it is not a dict, 
        # but an ORM model (like SQLAlchemy's User)
        from_attributes = True
