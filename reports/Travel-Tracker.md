Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/RS511/Travel-Tracker

Flagged locations (secret values are not included):

  - node_modules/pg-pool/test/connection-strings.js:8
    type: Postgres   preview: po************************4
    first seen in commit: 29f38704d496
  - node_modules/pg-connection-string/README.md:20
    type: CustomRegex   preview: po******************************************1
    first seen in commit: 29f38704d496
  - node_modules/pg-connection-string/README.md:20
    type: Postgres   preview: po******************************************1
    first seen in commit: 29f38704d496
  - node_modules/pg-pool/README.md:72
    type: Postgres   preview: po*********************************2
    first seen in commit: 29f38704d496
  - node_modules/pg-connection-string/README.md:43
    type: CustomRegex   preview: po***************************************>
    first seen in commit: 29f38704d496
  - node_modules/pg-pool/README.md:72
    type: CustomRegex   preview: po**********************************#
    first seen in commit: 29f38704d496

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

