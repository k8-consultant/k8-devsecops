


FROM python:3.12-slim-bookworm

LABEL org.opencontainers.image.source="https://github.com/k8-consultant/k8-devsecops"

WORKDIR /app

RUN groupadd --gid 10001 appgroup \
    && useradd --uid 10001 \
       --gid appgroup \
       --create-home appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appgroup main.py .

USER 10001:10001

EXPOSE 8000

CMD ["uvicorn", "main:app", \
     "--host", "0.0.0.0", \
     "--port", "8000"]