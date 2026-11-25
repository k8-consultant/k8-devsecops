# Dependency vulnerability remediation

Status: Completed exercise

## Mini write-up

Initial instrumentation dependency constrained Starlette. Replaced it with prometheus-client and required starlette>=1.3.1,<2. Python tests, both architecture scans, GHCR publishing and GitOps update passed. No vulnerability exceptions added.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
pip install -r requirements.txt
python -m pytest -q
docker build -t devsecops-api:remediation .
trivy image --severity HIGH,CRITICAL --ignore-unfixed --exit-code 1 devsecops-api:remediation
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops/commit/6fb0e46d)

[Back to revision index](../README.md)
