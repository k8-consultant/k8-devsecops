# FastAPI and testing

Status: Completed exercise

## Mini write-up

Developed a simulated inference API with health, version and prediction endpoints; pytest validates application behaviour. This is not a trained model.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest httpx
python -m pytest -q
uvicorn main:app --host 0.0.0.0 --port 8000
# Separate terminal
curl http://localhost:8000/health
curl http://localhost:8000/version
curl http://localhost:8000/predict
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops/blob/main/main.py)

[Back to revision index](../README.md)
