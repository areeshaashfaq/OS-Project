Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/ncioo/TelegramBot-Boilerplate

Flagged locations (secret values are not included):

  - TelegramBot/database/RedisDb.py:10
    type: CustomRegex   preview: re**************************************************************************"
    first seen in commit: da6045e2dc20
  - TelegramBot/database/RedisDb.py:5
    type: CustomRegex   preview: re**************************************************************************"
    first seen in commit: ee731a887bfc

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

