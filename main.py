from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Request, Response
import time
import socket

app = FastAPI(title="DevSecOps Mini Project")

HTTP_REQUESTS = Counter("http_requests_total", "HTTP requests", ["method", "handler", "status"])
HTTP_DURATION = Histogram("http_request_duration_seconds", "HTTP request duration", ["method", "handler"])


@app.middleware("http")
async def collect_metrics(request: Request, call_next):
    if request.url.path == "/metrics":
        return await call_next(request)
    started = time.perf_counter()
    status = "5xx"
    try:
        response = await call_next(request)
        status = f"{response.status_code // 100}xx"
        return response
    finally:
        route = request.scope.get("route")
        handler = getattr(route, "path", "unmatched")
        HTTP_REQUESTS.labels(request.method, handler, status).inc()
        HTTP_DURATION.labels(request.method, handler).observe(time.perf_counter() - started)


@app.get("/metrics", include_in_schema=False)
def metrics():
    return Response(generate_latest(), headers={"Content-Type": CONTENT_TYPE_LATEST})


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
