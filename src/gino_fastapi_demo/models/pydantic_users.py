from pydantic import BaseModel


class UserCheck(BaseModel):
    nickname: str
