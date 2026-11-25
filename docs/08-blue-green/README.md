# Blue-green deployment

Status: Completed exercise

## Mini write-up

Separate active and preview Services; autoPromotionEnabled false. Validate preview then promote. Revision 7 verified stable and active with two available replicas; old replicas scale down after delay.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
kubectl port-forward svc/devsecops-api-preview 8001:8000 -n devsecops
# Separate terminal
curl http://localhost:8001/health
curl http://localhost:8001/version
curl -i http://localhost:8001/predict
kubectl argo rollouts promote devsecops-api -n devsecops
kubectl argo rollouts get rollout devsecops-api -n devsecops
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops-gitops/blob/main/environments/dev/templates/deployment.yaml)

[Back to revision index](../README.md)
