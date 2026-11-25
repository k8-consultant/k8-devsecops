# Kubernetes and Helm

Status: Completed exercise

## Mini write-up

Packaged workload with two replicas, CPU request/limit 50m/250m, memory 64/256 MiB, UID 10001, seccomp RuntimeDefault, dropped capabilities, disabled privilege escalation and health probes. Helm commands run from GitOps repository.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
kubectl get nodes
kubectl get namespaces
kubectl get pods -n devsecops
kubectl get svc -n devsecops
kubectl get events -n devsecops
helm lint environments/dev
helm template devsecops-api environments/dev --namespace devsecops
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops-gitops/tree/main/environments/dev)

[Back to revision index](../README.md)
