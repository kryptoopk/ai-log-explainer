from fastapi import FastAPI
from model import AnalyzeRequest,AnalyzeResponse
import rule_engine

app=FastAPI(title='Ai log Explainer')

@app.get('/health')
def health_check():
    return {"status":"System up and running"}

@app.post('/analyze',response_model=AnalyzeResponse)
def analyze_log(request:AnalyzeRequest):
    return rule_engine.analyze(request.log)