Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/origamyllc/hulk-cut

Flagged locations (secret values are not included):

  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:22
    type: CustomRegex   preview: ho****************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:31
    type: CustomRegex   preview: ma****************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:58
    type: CustomRegex   preview: ma***************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:40
    type: CustomRegex   preview: ba***************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:49
    type: CustomRegex   preview: li***************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:58
    type: CustomRegex   preview: ma*****************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:22
    type: CustomRegex   preview: ho****************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:40
    type: CustomRegex   preview: ba***************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:49
    type: CustomRegex   preview: li***************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:58
    type: CustomRegex   preview: ma*****************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:31
    type: CustomRegex   preview: ma****************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:31
    type: CustomRegex   preview: ma**************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:58
    type: CustomRegex   preview: ma***************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:49
    type: CustomRegex   preview: li*************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:40
    type: CustomRegex   preview: ba*************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:22
    type: CustomRegex   preview: ho**************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:22
    type: CustomRegex   preview: ho**************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:49
    type: CustomRegex   preview: li*************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:31
    type: CustomRegex   preview: ma**************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:49
    type: CustomRegex   preview: li*************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:31
    type: CustomRegex   preview: ma**************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:58
    type: CustomRegex   preview: ma***************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:40
    type: CustomRegex   preview: ba*************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:22
    type: CustomRegex   preview: ho**************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:40
    type: CustomRegex   preview: ba*************************************,
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:28
    type: CustomRegex   preview: so**************************************;
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:29
    type: CustomRegex   preview: ba************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:47
    type: CustomRegex   preview: ma**************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:29
    type: CustomRegex   preview: ba************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:29
    type: CustomRegex   preview: ba**************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:20
    type: CustomRegex   preview: ma***************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:47
    type: CustomRegex   preview: ma**************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:28
    type: CustomRegex   preview: so************************************n
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:47
    type: CustomRegex   preview: ma****************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:47
    type: CustomRegex   preview: ma****************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:47
    type: CustomRegex   preview: ma**************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:11
    type: CustomRegex   preview: ho***************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:20
    type: CustomRegex   preview: ma*************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:20
    type: CustomRegex   preview: ma***************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:28
    type: CustomRegex   preview: so************************************************************;
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:29
    type: CustomRegex   preview: ba**************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:38
    type: CustomRegex   preview: li************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:38
    type: CustomRegex   preview: li**************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:28
    type: CustomRegex   preview: so************************************n
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:28
    type: CustomRegex   preview: so**************************************;
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:28
    type: CustomRegex   preview: so************************************************************;
    first seen in commit: 93c16b71e5a6
  - cut/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:28
    type: CustomRegex   preview: so*********************************t
    first seen in commit: 41d782587411
  - cut/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:28
    type: CustomRegex   preview: so*********************************t
    first seen in commit: 93c16b71e5a6
  - src/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:23
    type: CustomRegex   preview: so*********************************t
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:11
    type: CustomRegex   preview: ho***************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:23
    type: CustomRegex   preview: so************************************n
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:38
    type: CustomRegex   preview: li**************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:31
    type: CustomRegex   preview: ma**************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:40
    type: CustomRegex   preview: ba*************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:49
    type: CustomRegex   preview: li*************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:58
    type: CustomRegex   preview: ma***************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:22
    type: CustomRegex   preview: ho**************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:31
    type: CustomRegex   preview: ma**************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:40
    type: CustomRegex   preview: ba*************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:49
    type: CustomRegex   preview: li*************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:58
    type: CustomRegex   preview: ma***************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:22
    type: CustomRegex   preview: ho****************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:20
    type: CustomRegex   preview: ma*************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:22
    type: CustomRegex   preview: ho**************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:49
    type: CustomRegex   preview: li***************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:31
    type: CustomRegex   preview: ma****************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:40
    type: CustomRegex   preview: ba***************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:22
    type: CustomRegex   preview: ho****************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:31
    type: CustomRegex   preview: ma****************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:58
    type: CustomRegex   preview: ma*****************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:58
    type: CustomRegex   preview: ma*****************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:31
    type: CustomRegex   preview: ma**************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:40
    type: CustomRegex   preview: ba*************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:22
    type: CustomRegex   preview: ho**************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:49
    type: CustomRegex   preview: li*************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:40
    type: CustomRegex   preview: ba***************************************,
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:49
    type: CustomRegex   preview: li***************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:38
    type: CustomRegex   preview: li************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:38
    type: CustomRegex   preview: li************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:11
    type: CustomRegex   preview: ho*************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:11
    type: CustomRegex   preview: ho*************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:20
    type: CustomRegex   preview: ma*************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:29
    type: CustomRegex   preview: ba************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:23
    type: CustomRegex   preview: so************************************************************;
    first seen in commit: 41d782587411
  - cut/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:58
    type: CustomRegex   preview: ma***************************************,
    first seen in commit: 41d782587411
  - src/components/db/mongo/models/cut.componenets.db.mongo.models.user.model.js:23
    type: CustomRegex   preview: so**************************************;
    first seen in commit: 41d782587411
  - src/components/db/mongo/seeds/cut.components.db.mongo.seed.user.js:11
    type: CustomRegex   preview: ho*************************************,
    first seen in commit: 41d782587411

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

