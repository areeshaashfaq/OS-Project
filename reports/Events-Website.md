Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/DaliaTarek96/Events-Website

Flagged locations (secret values are not included):

  - node_modules/bcrypt/src/bcrypt.cc:20
    type: CustomRegex   preview: dm***************************g
    first seen in commit: fd5661dbab39
  - node_modules/mongoose/lib/connection.js:281
    type: MongoDB   preview: mo***********************************b
    first seen in commit: fd5661dbab39
  - node_modules/mongoose/lib/index.js:234
    type: CustomRegex   preview: mo****************************************************************t
    first seen in commit: fd5661dbab39
  - node_modules/mongoose/lib/index.js:230
    type: CustomRegex   preview: mo****************************************************************t
    first seen in commit: fd5661dbab39
  - node_modules/mongoose/lib/index.js:223
    type: CustomRegex   preview: mo*******************************t
    first seen in commit: fd5661dbab39
  - node_modules/mongoose/lib/index.js:223
    type: MongoDB   preview: mo**************************t
    first seen in commit: fd5661dbab39
  - node_modules/mongoose/lib/index.js:227
    type: CustomRegex   preview: mo*******************************t
    first seen in commit: fd5661dbab39
  - node_modules/mongoose/lib/index.js:289
    type: MongoDB   preview: mo**************************t
    first seen in commit: fd5661dbab39
  - node_modules/mongoose/lib/index.js:292
    type: CustomRegex   preview: mo****************************************************************t
    first seen in commit: fd5661dbab39
  - node_modules/mongoose/lib/index.js:289
    type: CustomRegex   preview: mo*******************************t
    first seen in commit: fd5661dbab39
  - node_modules/needle/README.md:311
    type: CustomRegex   preview: ht**************************************.
    first seen in commit: fd5661dbab39
  - node_modules/needle/README.md:416
    type: CustomRegex   preview: ht***************************************,
    first seen in commit: fd5661dbab39
  - node_modules/needle/README.md:416
    type: CustomRegex   preview: pa**************************************'
    first seen in commit: fd5661dbab39
  - node_modules/needle/README.md:416
    type: CustomRegex   preview: pa***************************************,
    first seen in commit: fd5661dbab39
  - node_modules/needle/README.md:416
    type: URI   preview: ht*************************************m
    first seen in commit: fd5661dbab39
  - node_modules/needle/README.md:311
    type: URI   preview: ht***********************************8
    first seen in commit: fd5661dbab39

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

