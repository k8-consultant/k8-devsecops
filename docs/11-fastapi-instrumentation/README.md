# FastAPI instrumentation

Status: Completed exercise

## Mini write-up

Custom middleware with prometheus-client exposes HTTP request counter and latency histogram at /metrics. Verified 661 health and 200 prediction 2xx requests on one preview pod.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
kubectl port-forward svc/devsecops-api-preview 8001:8000 -n devsecops
# Separate terminal
curl http://localhost:8001/metrics
for i in {1..100}; do
  curl -s http://localhost:8001/predict > /dev/null
done
curl -s http://localhost:8001/metrics | grep '^http_requests_total'
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops/blob/main/main.py)

[Back to revision index](../README.md)
