Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/smebberson/notonomous-server

Flagged locations (secret values are not included):

  - node_modules/mongodb/test/bson/bson_test.js:747
    type: CustomRegex   preview: em*********************************,
    first seen in commit: 3c7ae1d91ae8
  - node_modules/mongodb/test/connect_test.js:77
    type: CustomRegex   preview: mo*********************************7
    first seen in commit: 3c7ae1d91ae8
  - node_modules/mongodb/test/collection_test.js:573
    type: CustomRegex   preview: em*********************************,
    first seen in commit: 3c7ae1d91ae8
  - node_modules/mongodb/lib/mongodb/db.js:743
    type: MongoDB   preview: mo*********************t
    first seen in commit: 3c7ae1d91ae8
  - node_modules/mongodb/lib/mongodb/db.js:743
    type: CustomRegex   preview: mo**************************t
    first seen in commit: 3c7ae1d91ae8
  - node_modules/now/node_modules/socket.io/test/fixtures/key.key:1
    type: PrivateKey   preview: --***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 3c7ae1d91ae8

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

