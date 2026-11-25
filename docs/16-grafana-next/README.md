# Grafana dashboard — next lesson

Status: Pending

## Mini write-up

Grafana installed but dashboard not yet configured or login confirmed. Next: reuse golden signal queries, then alerting, Slack, SLOs and metric-driven rollout analysis. Do not share the retrieved password.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring
# Separate terminal
kubectl get secret monitoring-grafana -n monitoring -o jsonpath='{.data.admin-password}' | base64 -d; echo
# Open http://localhost:3000 (username admin)
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops-gitops/blob/main/environments/dev/templates/servicemonitor.yaml)

[Back to revision index](../README.md)
