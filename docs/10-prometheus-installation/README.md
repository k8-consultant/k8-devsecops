# Prometheus stack

Status: Completed exercise

## Mini write-up

Installed kube-prometheus-stack 93.9.0 with Grafana, Alertmanager, node exporter and kube-state-metrics. Retention 3d/2GB, scrape interval 15s, Prometheus memory request/limit 512Mi/1Gi. Local values file was not previously in GitHub; reconstructed configuration below.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm upgrade --install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace --version 93.9.0 -f values.yaml --wait --timeout 10m
helm list -A
kubectl get pods -n monitoring
kubectl get svc -n monitoring
kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090 -n monitoring
```

## Reconstructed local values.yaml
```yaml
prometheus:
  prometheusSpec:
    retention: 3d
    retentionSize: "2GB"
    scrapeInterval: 15s
    serviceMonitorSelectorNilUsesHelmValues: false
    resources:
      requests: {cpu: 200m, memory: 512Mi}
      limits: {cpu: "1", memory: 1Gi}
grafana:
  enabled: true
  resources:
    requests: {cpu: 100m, memory: 128Mi}
    limits: {cpu: 500m, memory: 512Mi}
alertmanager:
  enabled: true
nodeExporter:
  enabled: true
kubeStateMetrics:
  enabled: true
kubeControllerManager:
  enabled: false
kubeScheduler:
  enabled: false
kubeEtcd:
  enabled: false
kubeProxy:
  enabled: false
```

## Infrastructure queries
```promql
up
container_memory_working_set_bytes{namespace="devsecops",container="devsecops-api"} / 1024 / 1024
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops-gitops/blob/main/environments/dev/templates/servicemonitor.yaml)

[Back to revision index](../README.md)
