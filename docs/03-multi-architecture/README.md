# Multi-architecture builds

Status: Completed exercise

## Mini write-up

Resolved missing ARM64 manifest by building and scanning AMD64 and ARM64 images. The manual build command is illustrative; CI scans before publishing.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
kubectl get nodes -L kubernetes.io/arch
docker buildx ls
docker buildx build --platform linux/amd64,linux/arm64 -t ghcr.io/k8-consultant/devsecops-api:<tag> --push .
docker buildx imagetools inspect ghcr.io/k8-consultant/devsecops-api:<tag>
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops/commit/fdd1dff8)

[Back to revision index](../README.md)
