from pydantic import BaseModel


class LogResponse(BaseModel):
    received_log: str
    source: str
    category: str
    severity: str
    reason: str
    recommendation: str
    message: str