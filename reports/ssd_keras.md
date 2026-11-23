Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/swapnilpote/ssd_keras

Flagged locations (secret values are not included):

  - SSD_training.ipynb:465
    type: Box   preview: nc*****************************K
    first seen in commit: 23638806a2c8
  - SSD_training.ipynb:361
    type: Box   preview: sm*****************************B
    first seen in commit: 90b67fbbdf1d
  - SSD_training.ipynb:361
    type: Box   preview: nB*****************************l
    first seen in commit: 90b67fbbdf1d
  - SSD.ipynb:188
    type: TLy   preview: w7*********************************************************3
    first seen in commit: 5341cae9fa82
  - SSD.ipynb:188
    type: Box   preview: n9*****************************V
    first seen in commit: 5341cae9fa82

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

