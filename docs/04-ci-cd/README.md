# GitHub Actions and DevSecOps

Status: Completed exercise

## Mini write-up

Tests, architecture-specific builds, Trivy and GHCR publishing. Resolved package permission error with packages: write and repository access. HIGH/CRITICAL gate uses exit-code 1 and ignore-unfixed true; passing is not proof of zero vulnerabilities. Never commit tokens.

## Commands

Commands include reconstructed revision examples, not a verbatim terminal transcript. Replace placeholders before use; run long-lived commands in separate terminals.

```bash
git add .
git commit -m "Update application"
git push origin main
echo "$CR_PAT" | docker login ghcr.io -u k8-consultant --password-stdin
```

## GitHub evidence

[Implementation reference](https://github.com/k8-consultant/k8-devsecops/blob/main/.github/workflows/devsecops-ci.yml)

[Back to revision index](../README.md)
