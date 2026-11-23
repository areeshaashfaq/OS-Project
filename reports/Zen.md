Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/AliceMazh/Zen

Flagged locations (secret values are not included):

  - app/google-services.json:18
    type: GoogleGeminiAPIKey   preview: AI************************************8
    first seen in commit: 2147fb93bddb
  - app/src/main/res/values/config.xml:3
    type: FigmaPersonalAccessToken   preview: fi******************************************j
    first seen in commit: 2147fb93bddb

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

