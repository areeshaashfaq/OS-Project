Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/edgetoo/Authenticator

Flagged locations (secret values are not included):

  - (unknown file):2
    type: CustomRegex   preview: op***********************************,
    first seen in commit: 06def31ca6a4
  - (unknown file):1
    type: CustomRegex   preview: op***********************************,
    first seen in commit: 06def31ca6a4
  - (unknown file):1
    type: CustomRegex   preview: op************************************y
    first seen in commit: 1db35db09a7d
  - (unknown file):2
    type: CustomRegex   preview: op************************************y
    first seen in commit: 1db35db09a7d
  - (unknown file):2
    type: CustomRegex   preview: op***************************************g
    first seen in commit: 8d37e9b9ee4d
  - (unknown file):1
    type: CustomRegex   preview: op***************************************g
    first seen in commit: 8d37e9b9ee4d
  - (unknown file):2
    type: CustomRegex   preview: op***************************************y
    first seen in commit: 93a7759d350d
  - (unknown file):1
    type: CustomRegex   preview: op***************************************y
    first seen in commit: 93a7759d350d
  - (unknown file):2
    type: CustomRegex   preview: op*************************************n
    first seen in commit: ae3f5f8b31a8
  - (unknown file):1
    type: CustomRegex   preview: op*************************************n
    first seen in commit: ae3f5f8b31a8
  - (unknown file):2
    type: CustomRegex   preview: op************************************g
    first seen in commit: 19c2a45322a6
  - (unknown file):1
    type: CustomRegex   preview: op************************************g
    first seen in commit: 19c2a45322a6
  - (unknown file):2
    type: CustomRegex   preview: op**************************************r
    first seen in commit: 00bea33e8a5a
  - (unknown file):1
    type: CustomRegex   preview: op**************************************r
    first seen in commit: 00bea33e8a5a
  - (unknown file):2
    type: CustomRegex   preview: op************************************s
    first seen in commit: 1d0be6b45c9e
  - (unknown file):1
    type: CustomRegex   preview: op************************************s
    first seen in commit: 1d0be6b45c9e
  - (unknown file):2
    type: CustomRegex   preview: op************************************s
    first seen in commit: 65ced1b62d70
  - (unknown file):1
    type: CustomRegex   preview: op************************************s
    first seen in commit: 65ced1b62d70
  - (unknown file):2
    type: CustomRegex   preview: op***********************************n
    first seen in commit: 1aa2857969be
  - (unknown file):1
    type: CustomRegex   preview: op***********************************n
    first seen in commit: 1aa2857969be
  - (unknown file):2
    type: CustomRegex   preview: op*************************************y
    first seen in commit: 0ced9f88e661
  - (unknown file):1
    type: CustomRegex   preview: op*************************************y
    first seen in commit: 0ced9f88e661
  - (unknown file):2
    type: CustomRegex   preview: op**************************************s
    first seen in commit: 7da8de5583de
  - (unknown file):1
    type: CustomRegex   preview: op**************************************s
    first seen in commit: 7da8de5583de
  - (unknown file):2
    type: CustomRegex   preview: op***************************************n
    first seen in commit: 53fca74384de
  - (unknown file):1
    type: CustomRegex   preview: op***************************************n
    first seen in commit: 53fca74384de
  - (unknown file):2
    type: CustomRegex   preview: op***********************************s
    first seen in commit: 037de1225455
  - (unknown file):1
    type: CustomRegex   preview: op***********************************s
    first seen in commit: 037de1225455
  - (unknown file):1
    type: CustomRegex   preview: op****************************************g
    first seen in commit: 26cea4a9cdcc
  - (unknown file):2
    type: CustomRegex   preview: op****************************************g
    first seen in commit: 26cea4a9cdcc
  - (unknown file):2
    type: CustomRegex   preview: op***************************************n
    first seen in commit: 55cd348b07e2
  - (unknown file):1
    type: CustomRegex   preview: op***************************************n
    first seen in commit: 55cd348b07e2
  - (unknown file):2
    type: CustomRegex   preview: op*******************************************n
    first seen in commit: 8cd2fe8e377e
  - (unknown file):1
    type: CustomRegex   preview: op*******************************************n
    first seen in commit: 8cd2fe8e377e
  - (unknown file):1
    type: CustomRegex   preview: ma**********************************y
    first seen in commit: 0c4a75a7894e
  - (unknown file):2
    type: CustomRegex   preview: ma**********************************y
    first seen in commit: 0c4a75a7894e
  - mobile/ios/README:2
    type: CustomRegex   preview: dm**********************************m
    first seen in commit: 56ea6af49c95

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

