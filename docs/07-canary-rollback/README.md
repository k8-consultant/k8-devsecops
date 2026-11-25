# Canary and automated abort

Status: Completed exercise

## Mini write-up

Historical exercise: configured 20/40/60/80/100 weights with pauses. Without traffic routing, weights are approximate replica allocation. v3 returned HTTP 500 on /predict while /health stayed healthy; smoke-test AnalysisRun aborted rollout, preserved v2, and GitOps tag was restored. Current strategy is blue-green.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
kubectl argo rollouts get rollout devsecops-api -n devsecops
kubectl get analysisruns -n devsecops
kubectl describe analysisrun -n devsecops
curl -i http://localhost:8001/predict
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops-gitops/commit/53fccb6e)

[Back to revision index](../README.md)
