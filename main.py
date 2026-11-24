from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import socket

app = FastAPI(title="DevSecOps Mini Project")

Instrumentator().instrument(app).expose(app)


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
        "version": "v4",
        "deployment": "blue-green"
    }


@app.get("/predict")
def predict():
    return {
        "prediction": "approved",
        "status": "success",
        "model_version": "v4"
    }
