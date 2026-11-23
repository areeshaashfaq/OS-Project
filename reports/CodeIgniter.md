Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/bjornbjorn/CodeIgniter

Flagged locations (secret values are not included):

  - system/database/DB.php:65
    type: CustomRegex   preview: dr********************************e
    first seen in commit: 37f4b9caa027
  - system/database/DB.php:65
    type: CustomRegex   preview: dr********************************e
    first seen in commit: 4b9c62980599
  - system/database/DB.php:65
    type: CustomRegex   preview: dr********************************e
    first seen in commit: 114ab0988e20
  - system/database/DB.php:56
    type: CustomRegex   preview: dr********************************e
    first seen in commit: dd6719738936
  - system/database/DB.php:56
    type: CustomRegex   preview: dr********************************e
    first seen in commit: 2067d1a727e7
  - user_guide/database/connecting.html:132
    type: CustomRegex   preview: db**********************************e
    first seen in commit: 2067d1a727e7
  - user_guide/database/connecting.html:126
    type: CustomRegex   preview: db**********************************e
    first seen in commit: 2067d1a727e7
  - user_guide/libraries/xmlrpc.html:251
    type: CustomRegex   preview: js**********************************************;
    first seen in commit: 2067d1a727e7
  - user_guide/database/connecting.html:122
    type: CustomRegex   preview: db**********************************e
    first seen in commit: 97bc01074983
  - system/database/DB.php:56
    type: CustomRegex   preview: dr********************************e
    first seen in commit: 7dd3838f188f
  - user_guide/libraries/xmlrpc.html:248
    type: CustomRegex   preview: js**********************************************;
    first seen in commit: 39b622db9bda
  - user_guide/libraries/xmlrpc.html:1
    type: CustomRegex   preview: js**********************************************;
    first seen in commit: 8acc6f679d83
  - system/database/DB_driver.php:72
    type: CustomRegex   preview: dr********************************e
    first seen in commit: d2df9bc7cc9d
  - system/database/DB_driver.php:65
    type: CustomRegex   preview: dr********************************e
    first seen in commit: 7b613c7000a4
  - user_guide/database/connecting.html:118
    type: CustomRegex   preview: db**********************************e
    first seen in commit: fb28bb8d3bb0
  - system/drivers/DB_driver.php:55
    type: CustomRegex   preview: dr********************************e
    first seen in commit: b0dd10f81719
  - user_guide/libraries/database/connecting.html:118
    type: CustomRegex   preview: db**********************************e
    first seen in commit: b0dd10f81719
  - user_guide/libraries/xmlrpc.html:247
    type: CustomRegex   preview: js**********************************************;
    first seen in commit: b0dd10f81719

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

