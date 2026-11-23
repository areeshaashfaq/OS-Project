Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/cerw/laravel-google-sheets

Flagged locations (secret values are not included):

  - lib/google-apiclient/tests/data/test.json:6
    type: GCP   preview: 12*************************************************m
    first seen in commit: 589385f6c722
  - tests/data/service-account.json:6
    type: GCP   preview: te*******************************m
    first seen in commit: 7b3efd7111b3

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

