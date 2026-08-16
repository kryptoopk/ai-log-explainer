from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Log Explainer API",
    description="API for analyzing and explaining IT system logs.",
    version="0.1.0",
)

app.include_router(router)