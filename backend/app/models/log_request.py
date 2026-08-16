from pydantic import BaseModel, Field, field_validator


class LogRequest(BaseModel):
    log: str = Field(
        min_length=1,
        description="Raw IT system log text to analyze",
    )

    @field_validator("log")
    @classmethod
    def validate_log(cls, value: str) -> str:
        cleaned_log = value.strip()

        if not cleaned_log:
            raise ValueError("Log text cannot be empty")

        return cleaned_log