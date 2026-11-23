Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/TTharushiPathiranage/Food_Delivery

Flagged locations (secret values are not included):

  - food-del/backend/config/db.js:4
    type: MongoDB   preview: mo***************************************************************t
    first seen in commit: 453b4ab16580
  - food-del/backend/config/db.js:4
    type: CustomRegex   preview: mo***************************************************************t
    first seen in commit: 453b4ab16580

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

