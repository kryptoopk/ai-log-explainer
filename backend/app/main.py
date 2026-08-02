from fastapi import FastAPI

app = FastAPI(
    title="AI Log Explainer API",
    description="API for analyzing and explaining IT system logs.",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "AI Log Explainer API"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}