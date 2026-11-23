Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/kodiidok/FAIR-Play

Flagged locations (secret values are not included):

  - README.md:4
    type: Box   preview: t7*****************************8
    first seen in commit: 99a1c30c1b8c
  - README.md:4
    type: Box   preview: t7*****************************8
    first seen in commit: 8302b9f5795e
  - README.md:4
    type: Box   preview: 1o*****************************l
    first seen in commit: 7211c683b2a4
  - README.md:31
    type: Box   preview: 1o*****************************l
    first seen in commit: dc796f80a249

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

