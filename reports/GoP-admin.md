Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/phuc0201/GoP-admin

Flagged locations (secret values are not included):

  - src/environments/environment.ts:10
    type: GoogleGeminiAPIKey   preview: AI************************************Y
    first seen in commit: 858cc8f8d594
  - src/app/core/services/management/jsSIP-call.service.ts:39
    type: CustomRegex   preview: 10****************************************,
    first seen in commit: 6f7609598f91
  - src/index.html:15
    type: GoogleGeminiAPIKey   preview: AI************************************s
    first seen in commit: 5ddcd5dc4c36

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

