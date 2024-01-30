from pydantic import BaseModel


class LoginData(BaseModel):
    password: str