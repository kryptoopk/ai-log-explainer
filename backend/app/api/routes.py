from fastapi import APIRouter
from app.models.log_request import LogRequest
from app.models.log_response import LogResponse
from app.services.log_analyzer import LogAnalyzer

router = APIRouter()
log_analyzer = LogAnalyzer() # creates an object of the log analyzer class

@router.get("/")
def root() -> dict[str, str]:
    return {"message": "AI Log Explainer API"}

@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}

@router.post("/analyze", response_model=LogResponse)
def analyze_log(request: LogRequest) -> LogResponse:
    return log_analyzer.analyze(request.log)