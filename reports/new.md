Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/473392097/new

Flagged locations (secret values are not included):

  - .idea/dataSources.xml:8
    type: JDBC   preview: jd**********************************e
    first seen in commit: 79609dd53b20
  - lib/mysql-connector-java-5.1.37-bin.jar:523
    type: JDBC   preview: jd**********************/
    first seen in commit: 79609dd53b20
  - src/hibernate.cfg.xml:3
    type: JDBC   preview: jd*************************************************************************8
    first seen in commit: 79609dd53b20
  - out/production/new/hibernate.cfg.xml:3
    type: JDBC   preview: jd*************************************************************************8
    first seen in commit: 79609dd53b20
  - out/production/new/hibernate.cfg.xml:9
    type: JDBC   preview: jd*****************************************************************************8
    first seen in commit: 79609dd53b20
  - src/hibernate.cfg.xml:9
    type: JDBC   preview: jd*****************************************************************************8
    first seen in commit: 79609dd53b20

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

