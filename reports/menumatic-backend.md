Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/Laafayeette/menumatic-backend

Flagged locations (secret values are not included):

  - README.md:140
    type: JDBC   preview: jd***************************************c
    first seen in commit: 58e72a5f8ce7
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd***************************************c
    first seen in commit: 35d054436234
  - target/classes/application.properties:2
    type: JDBC   preview: jd***************************************c
    first seen in commit: 35d054436234
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd***********************************************e
    first seen in commit: 5136dc410599
  - target/classes/application.properties:2
    type: JDBC   preview: jd***********************************************e
    first seen in commit: 5136dc410599
  - .idea/dataSources.xml:78
    type: JDBC   preview: jd***********************************************e
    first seen in commit: 5136dc410599
  - target/classes/application.properties:2
    type: JDBC   preview: jd*****************************************n
    first seen in commit: 0beb6568a7f7
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd*****************************************n
    first seen in commit: 0beb6568a7f7
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd**********************************************2
    first seen in commit: f309e72202f0
  - target/classes/application.properties:2
    type: JDBC   preview: jd**********************************************2
    first seen in commit: f309e72202f0
  - .idea/dataSources.xml:66
    type: JDBC   preview: jd*****************************************n
    first seen in commit: 45115a9d8f5c
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd*****************************************n
    first seen in commit: 764e25bdcdeb
  - target/classes/application.properties:2
    type: JDBC   preview: jd*****************************************n
    first seen in commit: 764e25bdcdeb
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd***************************************c
    first seen in commit: 5bf6f5608974
  - target/classes/application.properties:2
    type: JDBC   preview: jd***************************************c
    first seen in commit: 5bf6f5608974
  - target/classes/application.properties:2
    type: JDBC   preview: jd*****************************************e
    first seen in commit: fc8068d8dd3a
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd*****************************************e
    first seen in commit: fc8068d8dd3a
  - target/classes/application.properties:2
    type: JDBC   preview: jd***************************************c
    first seen in commit: f3f0d87e4de6
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd***************************************c
    first seen in commit: f3f0d87e4de6
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd*****************************************b
    first seen in commit: 6bf19de37758
  - target/classes/application.properties:2
    type: JDBC   preview: jd*****************************************b
    first seen in commit: 6bf19de37758
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd****************************************b
    first seen in commit: a2782377610c
  - target/classes/application.properties:2
    type: JDBC   preview: jd****************************************b
    first seen in commit: a2782377610c
  - .idea/dataSources.xml:50
    type: JDBC   preview: jd****************************************b
    first seen in commit: a2782377610c
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd********************************************************6
    first seen in commit: cf884f7d0975
  - .idea/dataSources.xml:36
    type: JDBC   preview: jd********************************************************5
    first seen in commit: cf884f7d0975
  - target/classes/application.properties:2
    type: JDBC   preview: jd********************************************************6
    first seen in commit: cf884f7d0975
  - target/classes/application.properties:2
    type: JDBC   preview: jd********************************************************3
    first seen in commit: f817b3c38b24
  - .idea/dataSources.xml:22
    type: JDBC   preview: jd********************************************************3
    first seen in commit: f817b3c38b24
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd********************************************************3
    first seen in commit: f817b3c38b24
  - target/classes/application.properties:2
    type: JDBC   preview: jd****************************************************3
    first seen in commit: b06cc4d4e965
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd****************************************************3
    first seen in commit: b06cc4d4e965
  - target/classes/application.properties:2
    type: JDBC   preview: jd************************************a
    first seen in commit: 624cb5e38353
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd************************************a
    first seen in commit: 624cb5e38353
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd********************************************3
    first seen in commit: b716ddf698f1
  - target/classes/application.properties:2
    type: JDBC   preview: jd********************************************3
    first seen in commit: b716ddf698f1
  - target/classes/application.properties:2
    type: JDBC   preview: jd***************************************c
    first seen in commit: 0928fa79eb85
  - .idea/dataSources.xml:8
    type: JDBC   preview: jd***************************************c
    first seen in commit: 0928fa79eb85
  - src/main/resources/application.properties:2
    type: JDBC   preview: jd***************************************c
    first seen in commit: 0928fa79eb85
  - .idea/dataSources.xml:34
    type: JDBC   preview: jd********************************************2
    first seen in commit: 468e0fa222a7
  - .idea/dataSources.xml:22
    type: JDBC   preview: jd********************************************1
    first seen in commit: c5979e54970d
  - .idea/dataSources.xml:8
    type: JDBC   preview: jd**************************************s
    first seen in commit: 533539ad92d3
  - src/main/resources/application.properties:3
    type: JDBC   preview: jd*************************************t
    first seen in commit: 20b1af85b9e3
  - target/classes/application.properties:3
    type: JDBC   preview: jd*************************************t
    first seen in commit: 20b1af85b9e3

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

