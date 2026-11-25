# SRE golden signals

Status: Completed exercise

## Mini write-up

Traffic ~4 req/s; P95 estimated 4.75–4.80 ms; CPU ~5.1% and 1.2% of limits; memory ~13.64% and 13.35%. Error-rate exercise completed but numerical result not supplied. Port-forward selects one pod, not load-balanced traffic. Graph gaps unexplained. PromQL queries stored samples.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
while true; do
  curl -s http://localhost:8001/predict > /dev/null
  sleep 0.2
done
# Ctrl+C to stop
```

## Traffic
```promql
sum(rate(http_requests_total{namespace="devsecops",handler="/predict"}[5m]))
```

## Errors
```promql
100 * (sum(rate(http_requests_total{namespace="devsecops",handler="/predict",status="5xx"}[5m])) or vector(0)) / sum(rate(http_requests_total{namespace="devsecops",handler="/predict"}[5m]))
```

## Latency (P95 milliseconds)
```promql
histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket{namespace="devsecops",handler="/predict"}[5m]))) * 1000
```

## CPU percentage
```promql
100 * sum by (pod) (rate(container_cpu_usage_seconds_total{namespace="devsecops",container="devsecops-api"}[5m])) / sum by (pod) (kube_pod_container_resource_limits{namespace="devsecops",container="devsecops-api",resource="cpu"})
```

## Memory percentage
```promql
100 * sum by (pod) (container_memory_working_set_bytes{namespace="devsecops",container="devsecops-api"}) / sum by (pod) (kube_pod_container_resource_limits{namespace="devsecops",container="devsecops-api",resource="memory"})
```

For P50/P99 substitute 0.50/0.99. Error rate is undefined when traffic is zero.

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops/blob/main/main.py)

[Back to revision index](../README.md)
