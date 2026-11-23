Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/carloslema/vue-express-mongo-boilerplate

Flagged locations (secret values are not included):

  - server/bundle.js:1
    type: CustomRegex   preview: te*************************************************************************************************************************************************t
    first seen in commit: e3e8d4d9932f
  - server/bundle.js:1
    type: CustomRegex   preview: ad**************************************************************************************************************n
    first seen in commit: e3e8d4d9932f
  - server/bundle.js:1
    type: CustomRegex   preview: ad**************************************************************************************************************************************************t
    first seen in commit: e3e8d4d9932f
  - server/bundle.js:1
    type: CustomRegex   preview: ad*******************************************************************************************************************************r
    first seen in commit: e3e8d4d9932f
  - server/bundle.js:1
    type: CustomRegex   preview: te*************************************************************************************************************n
    first seen in commit: e3e8d4d9932f
  - server/bundle.js:1
    type: CustomRegex   preview: te******************************************************************************************************************************r
    first seen in commit: e3e8d4d9932f
  - server/core/seed-db.js:33
    type: CustomRegex   preview: te******************************************,
    first seen in commit: 216b277fa200
  - server/core/seed-db.js:32
    type: CustomRegex   preview: te******************************************,
    first seen in commit: 5449a2ed086b
  - server/bundle.js:1
    type: CustomRegex   preview: te***************************************************************************************************************************************************************************************************************************************************r
    first seen in commit: 42248b5ebbd4
  - server/bundle.js:1
    type: CustomRegex   preview: ad*******************************************************************************************************************************n
    first seen in commit: 42248b5ebbd4
  - server/bundle.js:1
    type: CustomRegex   preview: ad******************************************************************************d
    first seen in commit: 42248b5ebbd4
  - server/bundle.js:1
    type: CustomRegex   preview: te**************************************************************************************************************************n
    first seen in commit: 42248b5ebbd4
  - server/bundle.js:1
    type: CustomRegex   preview: te******************************************************************************************************************************n
    first seen in commit: 42248b5ebbd4
  - server/bundle.js:1
    type: CustomRegex   preview: ad****************************************************************************************************************************************************************************************************************************************************r
    first seen in commit: 42248b5ebbd4
  - server/bundle.js:1
    type: CustomRegex   preview: te*****************************************************************************d
    first seen in commit: 42248b5ebbd4
  - server/bundle.js:1
    type: CustomRegex   preview: ad***************************************************************************************************************************n
    first seen in commit: 42248b5ebbd4
  - server/bundle.js:1
    type: CustomRegex   preview: te***************************************************************************************************************************************************************************************************************************************************r
    first seen in commit: bc4ddd1adb75
  - server/bundle.js:1
    type: CustomRegex   preview: te******************************************************************************************************************************n
    first seen in commit: bc4ddd1adb75
  - server/bundle.js:1
    type: CustomRegex   preview: ad*******************************************************************************************************************************n
    first seen in commit: bc4ddd1adb75
  - server/bundle.js:1
    type: CustomRegex   preview: te**************************************************************************************************************************n
    first seen in commit: bc4ddd1adb75
  - server/bundle.js:1
    type: CustomRegex   preview: ad***************************************************************************************************************************n
    first seen in commit: bc4ddd1adb75
  - server/bundle.js:1
    type: CustomRegex   preview: ad******************************************************************************d
    first seen in commit: bc4ddd1adb75
  - server/bundle.js:1
    type: CustomRegex   preview: ad****************************************************************************************************************************************************************************************************************************************************r
    first seen in commit: bc4ddd1adb75
  - server/bundle.js:1
    type: CustomRegex   preview: te*****************************************************************************d
    first seen in commit: bc4ddd1adb75
  - server/bundle.js:1
    type: CustomRegex   preview: te***************************************************************************************************************************************************************************************************************************************************r
    first seen in commit: 193a773c45ff
  - server/bundle.js:1
    type: CustomRegex   preview: te******************************************************************************************************************************n
    first seen in commit: 193a773c45ff
  - server/bundle.js:1
    type: CustomRegex   preview: ad*******************************************************************************************************************************n
    first seen in commit: 193a773c45ff
  - server/bundle.js:1
    type: CustomRegex   preview: te**************************************************************************************************************************n
    first seen in commit: 193a773c45ff
  - server/bundle.js:1
    type: CustomRegex   preview: ad***************************************************************************************************************************n
    first seen in commit: 193a773c45ff
  - server/bundle.js:1
    type: CustomRegex   preview: ad******************************************************************************d
    first seen in commit: 193a773c45ff
  - server/bundle.js:1
    type: CustomRegex   preview: te*****************************************************************************d
    first seen in commit: 193a773c45ff
  - server/bundle.js:1
    type: CustomRegex   preview: ad****************************************************************************************************************************************************************************************************************************************************r
    first seen in commit: 193a773c45ff
  - server/bundle.js.map:1
    type: CustomRegex   preview: te*******************************************************************:
    first seen in commit: 6e77a8539e04
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad*******************************************************************:
    first seen in commit: 193a773c45ff
  - server/bundle.js.map:1
    type: CustomRegex   preview: te*******************************************************************:
    first seen in commit: 193a773c45ff
  - server/bundle.js.map:1
    type: CustomRegex   preview: te******************************************************************:
    first seen in commit: 193a773c45ff
  - server/bundle.js.map:1
    type: CustomRegex   preview: te*******************************************************************:
    first seen in commit: 42248b5ebbd4
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad*******************************************************************:
    first seen in commit: 6e77a8539e04
  - server/bundle.js.map:1
    type: CustomRegex   preview: te******************************************************************:
    first seen in commit: 6e77a8539e04
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad********************************************************************:
    first seen in commit: 6e77a8539e04
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad********************************************************************:
    first seen in commit: 193a773c45ff
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad********************************************************************:
    first seen in commit: 193a773c45ff
  - server/bundle.js.map:1
    type: CustomRegex   preview: te*******************************************************************:
    first seen in commit: bc4ddd1adb75
  - server/bundle.js.map:1
    type: CustomRegex   preview: te*******************************************************************:
    first seen in commit: 193a773c45ff
  - server/bundle.js.map:1
    type: CustomRegex   preview: te******************************************************************:
    first seen in commit: bc4ddd1adb75
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad*******************************************************************:
    first seen in commit: 42248b5ebbd4
  - server/bundle.js.map:1
    type: CustomRegex   preview: te******************************************************************:
    first seen in commit: 42248b5ebbd4
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad********************************************************************:
    first seen in commit: bc4ddd1adb75
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad********************************************************************:
    first seen in commit: 42248b5ebbd4
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad*******************************************************************:
    first seen in commit: 193a773c45ff
  - server/bundle.js.map:1
    type: CustomRegex   preview: te******************************************************************:
    first seen in commit: 193a773c45ff
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad*******************************************************************:
    first seen in commit: bc4ddd1adb75
  - server/bundle.js.map:1
    type: CustomRegex   preview: te*******************************************************************:
    first seen in commit: 6e77a8539e04
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad*******************************************************************:
    first seen in commit: bc4ddd1adb75
  - server/bundle.js.map:1
    type: CustomRegex   preview: te*******************************************************************:
    first seen in commit: bc4ddd1adb75
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad********************************************************************:
    first seen in commit: 6e77a8539e04
  - server/bundle.js.map:1
    type: CustomRegex   preview: te******************************************************************:
    first seen in commit: bc4ddd1adb75
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad*******************************************************************:
    first seen in commit: 6e77a8539e04
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad********************************************************************:
    first seen in commit: bc4ddd1adb75
  - server/bundle.js.map:1
    type: CustomRegex   preview: te*******************************************************************:
    first seen in commit: 42248b5ebbd4
  - server/bundle.js.map:1
    type: CustomRegex   preview: te******************************************************************:
    first seen in commit: 6e77a8539e04
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad*******************************************************************:
    first seen in commit: 42248b5ebbd4
  - server/bundle.js.map:1
    type: CustomRegex   preview: te******************************************************************:
    first seen in commit: 42248b5ebbd4
  - server/bundle.js.map:1
    type: CustomRegex   preview: ad********************************************************************:
    first seen in commit: 42248b5ebbd4
  - core/seed.js:15
    type: CustomRegex   preview: ad*******************************************,
    first seen in commit: e0563d0b588d
  - core/seed.js:28
    type: CustomRegex   preview: te******************************************,
    first seen in commit: e0563d0b588d
  - core/seed.js:15
    type: CustomRegex   preview: ad********************************************,
    first seen in commit: e0563d0b588d
  - core/seed.js:28
    type: CustomRegex   preview: te*******************************************,
    first seen in commit: e0563d0b588d

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

