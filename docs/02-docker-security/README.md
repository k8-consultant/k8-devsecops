# Docker and Trivy

Status: Completed exercise

## Mini write-up

Containerised FastAPI with non-root execution. Rebuilding with --pull refreshes the base image but did not reduce the recorded v1/v2 HIGH counts (51 each); v3 had 99 HIGH and 2 CRITICAL. Verify remediation by scanning.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
docker build -t devsecops-api:v1 .
docker images
trivy image devsecops-api:v1
docker build --pull --no-cache -t devsecops-api:v2 .
trivy image --severity HIGH,CRITICAL devsecops-api:v2
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops/tree/main/reports)

[Back to revision index](../README.md)
