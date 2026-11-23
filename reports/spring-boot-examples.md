Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/renyuyu/spring-boot-examples

Flagged locations (secret values are not included):

  - spring-boot-jpa-thymeleaf-curd/src/main/resources/application.properties:1
    type: JDBC   preview: jd***********************************************************************************************e
    first seen in commit: 4597adaf6c89
  - spring-boot-thymeleaf/target/classes/application.properties:1
    type: JDBC   preview: jd***********************************************************************************************e
    first seen in commit: 4597adaf6c89
  - spring-boot-shiro/src/main/resources/application.yml:3
    type: JDBC   preview: jd*****************************t
    first seen in commit: 70d15853208b
  - spring-boot-mybatis-annotation-mulidatasource/src/main/resources/application.properties:10
    type: JDBC   preview: jd**********************************************************************8
    first seen in commit: 8d6a84c6ec67
  - spring-boot-mybatis-annotation-mulidatasource/src/main/resources/application.properties:4
    type: JDBC   preview: jd**********************************************************************8
    first seen in commit: 8d6a84c6ec67
  - spring-boot-mybatis-mulidatasource/src/main/resources/application.properties:10
    type: JDBC   preview: jd**********************************************************************8
    first seen in commit: effaf3f8c695
  - spring-boot-mybatis-mulidatasource/src/main/resources/application.properties:4
    type: JDBC   preview: jd**********************************************************************8
    first seen in commit: effaf3f8c695
  - mybaits-spring-boot/spring-boot-mybaits-annotation/src/main/resources/application.properties:4
    type: JDBC   preview: jd**********************************************************************8
    first seen in commit: 6a98e6a9c12b
  - mybaits-spring-boot/spring-boot-mybaits-xml/src/main/resources/application.properties:6
    type: JDBC   preview: jd**********************************************************************8
    first seen in commit: 6a98e6a9c12b
  - spring-boot-web/src/main/resources/application.properties:1
    type: JDBC   preview: jd*****************************t
    first seen in commit: dbea8ebad5dc

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

