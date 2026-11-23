Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/ArulMC123/Rwq

Flagged locations (secret values are not included):

  - Ryuu.js:1
    type: CustomRegex   preview: tp***********************************************************************************************************************************************************************************************:
    first seen in commit: d764c7b66153
  - Ryuu.js:1
    type: CustomRegex   preview: ht**********************************************************************************************************************************************************************m
    first seen in commit: d764c7b66153
  - Ryuu.js:1
    type: CustomRegex   preview: ht**************************************************************************************************************************************************************************************************************************************************************************'
    first seen in commit: 6e1f6a8501d2
  - Ryuu.js:1
    type: CustomRegex   preview: ht***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************'
    first seen in commit: 6e1f6a8501d2

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

