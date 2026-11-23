Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/heitormon/nobu-service

Flagged locations (secret values are not included):

  - src/main/resources/db/migration/V4__Insert_Data_In_Books.sql:10
    type: CustomRegex   preview: no***************************R
    first seen in commit: 327babb277e7
  - src/main/resources/application.properties:13
    type: JDBC   preview: jd***************************************************************/
    first seen in commit: ff80a661e7dc
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd*****************************************************************************u
    first seen in commit: 9ede3a2b3807

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

