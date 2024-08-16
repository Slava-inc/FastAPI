from pydantic import BaseModel, Field, Optional

class UserBase(BaseModel):
	username: str
	email: str
		
# new record creation schema
class UserCreate(UserBase):
    password: str = Field(json_schema_extra={'example': 'Password123'})

	
# read record schema (may be extend later)
class UserRead(BaseModel):
	id: int
	name: str
	description: str
	
class UserUpdate(UserBase):
	email: Optional[str] = None
	username: Optional[str] = None
	password: Optional[str] = Field(None, json_schema_extra={'example': 'Password123'})
	
class UserInDBBase(UserBase):
	id: Optional[int] = None
	
class User(UserInDBBase):
	pass
	