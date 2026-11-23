Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/Ruthmwangi26/DevOpsC4G2

Flagged locations (secret values are not included):

  - Week-9/docker-compose.yaml:19
    type: CustomRegex   preview: mo*******************************************'
    first seen in commit: 5e6eee353501
  - Week-9/docker-compose.yaml:19
    type: MongoDB   preview: mo******************************************7
    first seen in commit: 5e6eee353501
  - Week-7/docker-compose.yaml:23
    type: CustomRegex   preview: mo*******************************************'
    first seen in commit: eec1065fcc5a
  - Week-7/docker-compose.yaml:23
    type: MongoDB   preview: mo******************************************7
    first seen in commit: eec1065fcc5a
  - Week-2/login.js:23
    type: CustomRegex   preview: em*********************************************;
    first seen in commit: 2fc43baf6d16
  - Week-2/login.js:23
    type: CustomRegex   preview: em*************************************)
    first seen in commit: 2fc43baf6d16
  - Week-2/login.js:23
    type: CustomRegex   preview: em*****************************s
    first seen in commit: 2fc43baf6d16
  - Week-2/login.js:23
    type: CustomRegex   preview: em**********************************************)
    first seen in commit: 2fc43baf6d16

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

