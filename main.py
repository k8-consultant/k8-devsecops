
from fastapi import FastAPI
import socket

app = FastAPI(title="DevSecOps Mini Project")


@app.get("/")
def home():
    return {
        "application": "devsecops-api",
        "status": "running",
        "hostname": socket.gethostname()
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def get_version():
    return {
        "application": "devsecops-api",
        "version": "v3",
        "deployment": "canary"
    }

@app.get("/predict")
def predict():
    # Intentionally faulty endpoint for automated canary-abort lab.
    # The /health endpoint stays healthy to exercise application-level validation.
    from fastapi import HTTPException
    raise HTTPException(status_code=500, detail="Simulated prediction service failure")
