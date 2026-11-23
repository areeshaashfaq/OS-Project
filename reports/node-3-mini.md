Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/spiltmiruku/node-3-mini

Flagged locations (secret values are not included):

  - README.md:100
    type: Postgres   preview: po***********************************2
    first seen in commit: e181f2d2fb62
  - README.md:100
    type: CustomRegex   preview: po******************************t
    first seen in commit: e181f2d2fb62
  - README.md:94
    type: Postgres   preview: po***********************************2
    first seen in commit: 8117f7b0c970
  - README.md:94
    type: Postgres   preview: po***********************************2
    first seen in commit: 50355efdfd9f
  - README.md:94
    type: CustomRegex   preview: po******************************t
    first seen in commit: 8117f7b0c970
  - README.md:94
    type: CustomRegex   preview: po******************************t
    first seen in commit: 50355efdfd9f
  - README.md:84
    type: CustomRegex   preview: po***********************************t
    first seen in commit: 2c8090741b0b
  - README.md:85
    type: CustomRegex   preview: po***********************************t
    first seen in commit: e26198f8a720

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

