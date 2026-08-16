from pydantic import BaseModel


class RuleResult(BaseModel):
    category: str
    severity: str
    reason: str
    recommendation: str