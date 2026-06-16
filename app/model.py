from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    log: str

class AnalyzeResponse(BaseModel):
    category: str
    severity: str
    summary: str
    recommendation: List[str]