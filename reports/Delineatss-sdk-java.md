Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/samtimur/Delineatss-sdk-java

Flagged locations (secret values are not included):

  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 6e1a6b8a6d30
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 7beeed6166f2
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 6da2a5e2bb84
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 9d4243ed646d
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 50d230ee4d1b
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 36228e137dba
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: a30409d25c12
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 75089eea02f3
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: cd567f69c526
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 019e207a2c39
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 65538c87b845
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 7d6bff92c4d4
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 27005bf22b13
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 5cd3374b1697
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: ab06a0e52dc9
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: de613deb63a8
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: 483f55ab66c3
  - (unknown file):11
    type: SnykKey   preview: 62*********************************0
    first seen in commit: cce1e7d140f2

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

