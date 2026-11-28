# Grafana SRE dashboard — Lesson 20

Status: Six panels built and verified; improved export committed, re-import test pending.

## Mini write-up
Built a Grafana dashboard backed by Prometheus for scrape availability, throughput, HTTP 5xx rate, P95 latency, CPU and memory. Verified throughput 4.13 req/s and later 3.58 req/s, zero observed server errors and P95 4.77 ms under lab traffic. Scrape count fluctuated between one and two; cause not established. CPU and memory are percentages of container limits (250m and 256 MiB).

## Commands
```bash
kubectl get pods -n monitoring
kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring
# Separate terminal; keep password private
kubectl get secret monitoring-grafana -n monitoring -o jsonpath='{.data.admin-password}' | base64 -d; echo
# Open http://localhost:3000, username admin
kubectl get pods -n devsecops
kubectl argo rollouts get rollout devsecops-api -n devsecops
kubectl port-forward svc/devsecops-api-preview 8001:8000 -n devsecops
# Separate terminal
curl -i http://localhost:8001/health
curl -i http://localhost:8001/predict
curl -s http://localhost:8001/version
# Only after successful preview validation
kubectl argo rollouts promote devsecops-api -n devsecops
kubectl argo rollouts get rollout devsecops-api -n devsecops
```

## PromQL
### Healthy Application Targets

```promql
sum(up{namespace="devsecops",job="devsecops-api"})
```

### 5xxx Error

```promql
100 *
(
  sum(rate(http_requests_total{
    namespace="devsecops",
    handler="/predict",
    status="5xx"
  }[5m])) or vector(0)
)
/
sum(rate(http_requests_total{
  namespace="devsecops",
  handler="/predict"
}[5m]))
```

### Throughput

```promql
sum(rate(http_requests_total{
  namespace="devsecops",
  handler="/predict"
}[5m]))
```

### P95 Latency

```promql
histogram_quantile(
  0.95,
  sum by (le) (
    rate(http_request_duration_seconds_bucket{
      namespace="devsecops",
      handler="/predict"
    }[5m])
  )
) * 1000
```

### CPU Usage

```promql
100 *
sum by (pod) (
  rate(container_cpu_usage_seconds_total{
    namespace="devsecops",
    container="devsecops-api"
  }[5m])
)
/
sum by (pod) (
  kube_pod_container_resource_limits{
    namespace="devsecops",
    container="devsecops-api",
    resource="cpu"
  }
)
```

### memory usage

```promql
100 *
sum by (pod) (
  container_memory_working_set_bytes{
    namespace="devsecops",
    container="devsecops-api"
  }
)
/
sum by (pod) (
  kube_pod_container_resource_limits{
    namespace="devsecops",
    container="devsecops-api",
    resource="memory"
  }
)
```

## Troubleshooting
Four resource-metric pods were explained by blue-green revisions 7 (active) and 8 (preview). ServiceMonitor scrapes active endpoints only, while cAdvisor monitors both revisions. Revision 8 was triggered by documentation commit 9722b2ca and was promoted; two ready replicas confirmed. Historical series may persist. Instant resource queries reduce historical display. CI push path filters now ignore docs/** and **/*.md; pull requests unchanged. The workflow edit itself may trigger a rollout.

## Dashboard import
Use Grafana Dashboards > New > Import and upload [dashboard JSON](devsecops-sre-dashboard.json). Export uses Grafana 13.3.1 dashboard v2; requires compatible Grafana and Prometheus datasource named prometheus. Re-import has not been tested. Removed server-generated metadata and empty query B, set units, 15s refresh and provisional lab thresholds. Availability remains a range time series. Thresholds are not SLOs. No live Grafana settings changed. Error rate undefined without traffic.

[Revision index](../README.md)
