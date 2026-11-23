Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/jimrae-devops/lwc-recipes

Flagged locations (secret values are not included):

  - package-lock.json:5539
    type: TLy   preview: SI*********************************************************w
    first seen in commit: eb40a6cc75a8
  - package-lock.json:7576
    type: TLy   preview: SI*********************************************************w
    first seen in commit: c44ebf60ea6e
  - package-lock.json:4437
    type: TLy   preview: SI*********************************************************w
    first seen in commit: 3872239a59fc

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

