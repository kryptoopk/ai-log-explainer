from pydantic import BaseModel


class ParsedLog(BaseModel):
    raw: str
    source: str
    message: str