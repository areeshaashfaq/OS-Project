Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/vidalgithub/azure-devops-github-acr-aks-app1

Flagged locations (secret values are not included):

  - 01-docker-build-and-push-to-acr-pipeline.yml:13
    type: Dockerhub   preview: 4e*********************************4
    first seen in commit: cce04e8b3ffc
  - 03-custom1-pipeline-buildandpush-to-acr-and-publish-artifacts.yml:13
    type: Dockerhub   preview: cf*********************************d
    first seen in commit: 35c354202fc5
  - 02-docker-build-push-to-acs-deploy-to-aks-pipeline.yml:14
    type: Dockerhub   preview: 56*********************************e
    first seen in commit: 516e02fb1c9a

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

