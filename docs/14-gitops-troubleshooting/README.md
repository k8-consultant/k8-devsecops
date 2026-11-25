# GitOps synchronization troubleshooting

Status: Completed exercise

## Mini write-up

OutOfSync/Healthy traced to obsolete canary Service and AnalysisTemplate because prune was disabled. Confirmed current blue-green rollout did not reference them; targeted deletion restored Synced/Healthy. Do not repeat deletion unless resources are confirmed obsolete.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
kubectl get application devsecops-api -n argocd -o jsonpath='{range .status.resources[*]}{.kind}{"\t"}{.name}{"\t"}{.status}{"\n"}{end}'
kubectl delete service devsecops-api-canary -n devsecops
kubectl delete analysistemplate devsecops-api-smoke-test -n devsecops
kubectl get application devsecops-api -n argocd
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops-gitops/blob/main/applications/devsecops-api.yaml)

[Back to revision index](../README.md)
