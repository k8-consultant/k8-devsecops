
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
        "version": "v2",
        "deployment": "canary"
    }