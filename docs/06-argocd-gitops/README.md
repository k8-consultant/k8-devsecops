# Argo CD and GitOps

Status: Completed exercise

## Mini write-up

Separated application source from desired deployment state. Automated sync and selfHeal enabled; prune disabled, so deleted Git resources can remain live.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
kubectl get application -n argocd
kubectl get application devsecops-api -n argocd
kubectl describe application devsecops-api -n argocd
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops-gitops/blob/main/applications/devsecops-api.yaml)

[Back to revision index](../README.md)
