Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/joellcastro/alfresco-pdf-toolkit

Flagged locations (secret values are not included):

  - alfresco/src/main/properties/local/alfresco-global.properties:129
    type: JDBC   preview: jd*****************************************************************************;
    first seen in commit: 4b928b11f504
  - alfresco/src/main/properties/local/alfresco-global.properties:100
    type: JDBC   preview: jd*******************************************************************8
    first seen in commit: 4b928b11f504
  - alfresco/src/main/properties/local/alfresco-global.properties:106
    type: JDBC   preview: jd**************************************o
    first seen in commit: 4b928b11f504
  - alfresco/src/main/properties/local/alfresco-global.properties:116
    type: JDBC   preview: jd******************************************o
    first seen in commit: 4b928b11f504
  - alfresco/src/main/properties/local/alfresco-global.properties:123
    type: JDBC   preview: jd**************************************o
    first seen in commit: 4b928b11f504

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

