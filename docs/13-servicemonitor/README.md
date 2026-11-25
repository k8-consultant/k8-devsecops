# ServiceMonitor discovery

Status: Completed exercise

## Mini write-up

Added active Service monitoring label and named http port. ServiceMonitor discovers active endpoints and scrapes /metrics every 15s; avoids preview duplication. Verified two healthy scrape targets.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
kubectl get servicemonitor -n devsecops
kubectl describe servicemonitor devsecops-api -n devsecops
kubectl get application devsecops-api -n argocd
```

## PromQL verification
```promql
up{namespace="devsecops"}
sum(up{namespace="devsecops",job="devsecops-api"})
http_requests_total{namespace="devsecops"}
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops-gitops/blob/main/environments/dev/templates/servicemonitor.yaml)

[Back to revision index](../README.md)
