# api/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.orchestrator import PreemptiveOrchestrator

app = FastAPI(title="Preemptive Debugger API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize orchestrator
orchestrator = PreemptiveOrchestrator()

class CodeAnalysisRequest(BaseModel):
    code: str

@app.post("/api/preemptive-debug")
async def preemptive_debug(request: CodeAnalysisRequest):
    """Main endpoint for preemptive debugging"""
    try:
        result = await orchestrator.preemptive_debug(request.code)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "preemptive-debugger"}

@app.get("/")
async def root():
    return {"message": "Preemptive Debugger API - Multi-Agent Code Healing System"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)