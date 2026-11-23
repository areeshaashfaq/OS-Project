Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/smatkovi/fahrplan

Flagged locations (secret values are not included):

  - qtc_packaging/debian_fremantle/control:16
    type: Box   preview: Wx*****************************0
    first seen in commit: 8ce16d2fac69
  - qtc_packaging/debian_harmattan/control:16
    type: Box   preview: Wx*****************************0
    first seen in commit: 6f0b4b821f68
  - qtc_packaging/debian_harmattan/control:17
    type: Box   preview: Wx*****************************0
    first seen in commit: 87b6f16ec881
  - qtc_packaging/debian_fremantle/control:16
    type: Box   preview: Wx*****************************0
    first seen in commit: caaef7b50c72
  - qtc_packaging/debian_fremantle/control:17
    type: Box   preview: Wx*****************************0
    first seen in commit: 87b6f16ec881
  - qtc_packaging/debian_harmattan/control:16
    type: Box   preview: Wx*****************************0
    first seen in commit: caaef7b50c72
  - qtc_packaging/debian_fremantle/control:16
    type: Box   preview: Wx*****************************0
    first seen in commit: 1d81c74d22b7
  - qtc_packaging/debian_harmattan/control:16
    type: Box   preview: Wx*****************************0
    first seen in commit: 26dd85d37f24

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

