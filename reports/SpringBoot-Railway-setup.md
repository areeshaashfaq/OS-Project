Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/AngelVirrueta/SpringBoot-Railway-setup

Flagged locations (secret values are not included):

  - setup-es.md:103
    type: JDBC   preview: jd************************************b
    first seen in commit: 62e566ff4cd3
  - setup-en.md:103
    type: JDBC   preview: jd************************************b
    first seen in commit: 8e85ef3c65cf
  - setup-es.md:103
    type: JDBC   preview: jd************************************b
    first seen in commit: ef659e7473fc

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

