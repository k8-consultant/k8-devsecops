# Automated GitOps image updates

Status: Completed exercise

## Mini write-up

CI updates environments/dev/values.yaml with the full commit SHA after successful tests/build/scans. Fine-grained token scoped to GitOps contents read/write stored as GITOPS_TOKEN. Argo CD deploys preview automatically.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
git add .
git commit -m "Update application"
git push origin main
# In GitOps checkout after CI completes
git pull --ff-only
cat environments/dev/values.yaml
kubectl get application devsecops-api -n argocd
kubectl argo rollouts get rollout devsecops-api -n devsecops
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops/commit/7a3f9bd0)

[Back to revision index](../README.md)
