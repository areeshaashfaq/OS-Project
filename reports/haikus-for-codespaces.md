Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/Pakkapon0000/haikus-for-codespaces

Flagged locations (secret values are not included):

  - package-lock.json:10290
    type: TLy   preview: SI*********************************************************w
    first seen in commit: fc4d408c63bd
  - package-lock.json:2234
    type: TLy   preview: SI*********************************************************w
    first seen in commit: 8243208e61de

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

