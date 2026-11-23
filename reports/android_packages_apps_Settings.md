Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/XperiaSTE/android_packages_apps_Settings

Flagged locations (secret values are not included):

  - (unknown file):1
    type: CustomRegex   preview: em*******************************y
    first seen in commit: 79c0355ede2f
  - (unknown file):2
    type: CustomRegex   preview: ge***********************************y
    first seen in commit: 79c0355ede2f
  - (unknown file):2
    type: CustomRegex   preview: ge***********************************s
    first seen in commit: c85c5c7b0e80
  - (unknown file):1
    type: CustomRegex   preview: er**********************************s
    first seen in commit: c85c5c7b0e80
  - (unknown file):10
    type: CustomRegex   preview: er**********************************s
    first seen in commit: c85c5c7b0e80
  - (unknown file):2
    type: CustomRegex   preview: yu***************************g
    first seen in commit: 4170f0e567f0
  - (unknown file):1
    type: CustomRegex   preview: yu***************************g
    first seen in commit: 4170f0e567f0
  - (unknown file):1
    type: CustomRegex   preview: yu****************************s
    first seen in commit: 6b19fa901780
  - (unknown file):1
    type: CustomRegex   preview: yu*****************************.
    first seen in commit: 6b19fa901780
  - (unknown file):2
    type: CustomRegex   preview: yu****************************s
    first seen in commit: 6b19fa901780
  - (unknown file):2
    type: CustomRegex   preview: jm****************************,
    first seen in commit: 36760c108b4b
  - (unknown file):1
    type: CustomRegex   preview: jm****************************,
    first seen in commit: 36760c108b4b
  - (unknown file):3
    type: CustomRegex   preview: ht******************************************************************m
    first seen in commit: 4825ded07f90
  - (unknown file):3
    type: URI   preview: ht******************************************************************m
    first seen in commit: 4825ded07f90
  - (unknown file):2
    type: CustomRegex   preview: jj******************************s
    first seen in commit: 8de05c57b553
  - (unknown file):1
    type: CustomRegex   preview: jj******************************s
    first seen in commit: 8de05c57b553
  - (unknown file):2
    type: CustomRegex   preview: yu******************************d
    first seen in commit: 6a627652cbac
  - (unknown file):1
    type: CustomRegex   preview: yu******************************d
    first seen in commit: 6a627652cbac
  - (unknown file):2
    type: CustomRegex   preview: pa***********************************n
    first seen in commit: 204440427aa1
  - (unknown file):1
    type: CustomRegex   preview: pa***********************************n
    first seen in commit: 204440427aa1
  - (unknown file):1
    type: CustomRegex   preview: pa*************************************:
    first seen in commit: b4564c39b734
  - (unknown file):2
    type: CustomRegex   preview: pa*************************************:
    first seen in commit: b4564c39b734
  - (unknown file):2
    type: CustomRegex   preview: pa***********************************n
    first seen in commit: 73456acfb45b
  - (unknown file):1
    type: CustomRegex   preview: pa***********************************n
    first seen in commit: 73456acfb45b
  - (unknown file):2
    type: CustomRegex   preview: fd********************************g
    first seen in commit: 377dd62bd7d7
  - (unknown file):1
    type: CustomRegex   preview: fd********************************g
    first seen in commit: 377dd62bd7d7
  - (unknown file):2
    type: CustomRegex   preview: pa***************************************n
    first seen in commit: b05f39d186d8
  - (unknown file):1
    type: CustomRegex   preview: pa***************************************n
    first seen in commit: b05f39d186d8
  - (unknown file):2
    type: CustomRegex   preview: cy*****************************************n
    first seen in commit: 2dd150bc2a78
  - (unknown file):1
    type: CustomRegex   preview: cy*****************************************n
    first seen in commit: 2dd150bc2a78
  - (unknown file):1
    type: CustomRegex   preview: cy*****************************************n
    first seen in commit: 00f85d6362ea
  - (unknown file):2
    type: CustomRegex   preview: cy*****************************************n
    first seen in commit: 00f85d6362ea
  - (unknown file):2
    type: CustomRegex   preview: jj*****************************.
    first seen in commit: 4378743a2fa3
  - (unknown file):1
    type: CustomRegex   preview: jj*****************************.
    first seen in commit: 4378743a2fa3
  - (unknown file):5
    type: Circle   preview: 58*************************************d
    first seen in commit: 942daf80e2d0
  - (unknown file):2
    type: CustomRegex   preview: ya*************************************s
    first seen in commit: 12411fba8ed5
  - (unknown file):1
    type: CustomRegex   preview: ya*************************************s
    first seen in commit: 12411fba8ed5
  - (unknown file):9
    type: Circle   preview: 46*************************************2
    first seen in commit: f14e6751c383
  - (unknown file):1
    type: CustomRegex   preview: ya********************************s
    first seen in commit: 265dfd22e368
  - (unknown file):2
    type: CustomRegex   preview: ya*********************************x
    first seen in commit: 265dfd22e368
  - (unknown file):1
    type: CustomRegex   preview: ya*********************************x
    first seen in commit: 265dfd22e368
  - (unknown file):2
    type: CustomRegex   preview: ya*******************************.
    first seen in commit: d2e414c2b6ea
  - (unknown file):1
    type: CustomRegex   preview: ya*******************************.
    first seen in commit: d2e414c2b6ea
  - (unknown file):2
    type: CustomRegex   preview: ct***********************************s
    first seen in commit: 2d6497d2d19f
  - (unknown file):1
    type: CustomRegex   preview: ct***********************************s
    first seen in commit: 2d6497d2d19f
  - (unknown file):2
    type: CustomRegex   preview: ja*******************************s
    first seen in commit: feeafe2e794a
  - (unknown file):1
    type: CustomRegex   preview: ja*******************************s
    first seen in commit: feeafe2e794a
  - (unknown file):2
    type: CustomRegex   preview: vi***************************n
    first seen in commit: de3c9cb41268
  - (unknown file):1
    type: CustomRegex   preview: vi***************************n
    first seen in commit: de3c9cb41268
  - (unknown file):1
    type: CustomRegex   preview: ja********************************e
    first seen in commit: 47f1cd4325e8
  - (unknown file):2
    type: CustomRegex   preview: ja*************************************s
    first seen in commit: 47f1cd4325e8
  - (unknown file):1
    type: CustomRegex   preview: ja*************************************s
    first seen in commit: 47f1cd4325e8
  - (unknown file):1
    type: CustomRegex   preview: pa**************************s
    first seen in commit: a45b09a7657e
  - (unknown file):10
    type: CustomRegex   preview: pa******************************.
    first seen in commit: a45b09a7657e
  - (unknown file):1
    type: CustomRegex   preview: pa******************************.
    first seen in commit: a45b09a7657e
  - (unknown file):2
    type: CustomRegex   preview: pa**************************s
    first seen in commit: a45b09a7657e
  - (unknown file):13
    type: CustomRegex   preview: pa*******************************n
    first seen in commit: ba7ee527d868
  - (unknown file):2
    type: CustomRegex   preview: pa*******************************n
    first seen in commit: ba7ee527d868
  - (unknown file):1
    type: CustomRegex   preview: pa*******************************n
    first seen in commit: ba7ee527d868
  - (unknown file):2
    type: CustomRegex   preview: sv********************************************.
    first seen in commit: 7e8dcbea6535
  - (unknown file):1
    type: CustomRegex   preview: sv********************************************.
    first seen in commit: 7e8dcbea6535
  - (unknown file):2
    type: CustomRegex   preview: dm*******************************e
    first seen in commit: 6f3b1bb1d73e
  - (unknown file):1
    type: CustomRegex   preview: dm*******************************e
    first seen in commit: 6f3b1bb1d73e
  - (unknown file):2
    type: CustomRegex   preview: dm*******************************e
    first seen in commit: 487b16f3400b
  - (unknown file):1
    type: CustomRegex   preview: dm*******************************e
    first seen in commit: 487b16f3400b
  - (unknown file):2
    type: CustomRegex   preview: js********************************.
    first seen in commit: e4599058ddda
  - (unknown file):1
    type: CustomRegex   preview: js********************************.
    first seen in commit: e4599058ddda
  - (unknown file):2
    type: CustomRegex   preview: ja*********************************.
    first seen in commit: 63cf89a49a75
  - (unknown file):1
    type: CustomRegex   preview: ja*********************************.
    first seen in commit: 63cf89a49a75
  - (unknown file):2
    type: CustomRegex   preview: ct*****************************g
    first seen in commit: 4f33878f208e
  - (unknown file):1
    type: CustomRegex   preview: ct*****************************g
    first seen in commit: 4f33878f208e
  - (unknown file):1
    type: CustomRegex   preview: bd**************************t
    first seen in commit: d4023b7cca11
  - (unknown file):2
    type: CustomRegex   preview: bd**************************t
    first seen in commit: d4023b7cca11
  - (unknown file):2
    type: CustomRegex   preview: is*********************************y
    first seen in commit: 21e644a9a817
  - (unknown file):1
    type: CustomRegex   preview: is*********************************y
    first seen in commit: 21e644a9a817
  - (unknown file):2
    type: CustomRegex   preview: ja******************************n
    first seen in commit: 29c9073595e7
  - (unknown file):1
    type: CustomRegex   preview: ja******************************n
    first seen in commit: 29c9073595e7
  - (unknown file):2
    type: CustomRegex   preview: ja******************************h
    first seen in commit: 9afb14de3b8b
  - (unknown file):1
    type: CustomRegex   preview: ja******************************h
    first seen in commit: 9afb14de3b8b
  - (unknown file):2
    type: CustomRegex   preview: st*********************************"
    first seen in commit: 171412000a95
  - (unknown file):1
    type: CustomRegex   preview: st*********************************"
    first seen in commit: 171412000a95
  - (unknown file):2
    type: CustomRegex   preview: st*******************************y
    first seen in commit: 6370c87a6b98
  - (unknown file):1
    type: CustomRegex   preview: st*******************************y
    first seen in commit: 6370c87a6b98
  - (unknown file):1
    type: CustomRegex   preview: jp********************************.
    first seen in commit: ec5a45e79cb7
  - (unknown file):2
    type: CustomRegex   preview: jp********************************.
    first seen in commit: ec5a45e79cb7
  - (unknown file):2
    type: CustomRegex   preview: ja*******************************s
    first seen in commit: d75905991c5a
  - (unknown file):1
    type: CustomRegex   preview: ja*******************************s
    first seen in commit: d75905991c5a
  - (unknown file):2
    type: CustomRegex   preview: kl********************************s
    first seen in commit: 28efa0210412
  - (unknown file):1
    type: CustomRegex   preview: kl********************************s
    first seen in commit: 28efa0210412
  - (unknown file):2
    type: CustomRegex   preview: kl********************************y
    first seen in commit: 015c186a2466
  - (unknown file):1
    type: CustomRegex   preview: kl********************************y
    first seen in commit: 015c186a2466
  - (unknown file):2
    type: CustomRegex   preview: ja******************************e
    first seen in commit: 2deec7edc937
  - (unknown file):1
    type: CustomRegex   preview: ja******************************e
    first seen in commit: 2deec7edc937
  - (unknown file):1
    type: CustomRegex   preview: ja******************************.
    first seen in commit: 9c1e7f8c4c6a
  - (unknown file):2
    type: CustomRegex   preview: ja********************************y
    first seen in commit: 9c1e7f8c4c6a
  - (unknown file):1
    type: CustomRegex   preview: ja********************************y
    first seen in commit: 9c1e7f8c4c6a
  - (unknown file):1
    type: CustomRegex   preview: ja******************************t
    first seen in commit: 9c1e7f8c4c6a
  - (unknown file):1
    type: CustomRegex   preview: ja*******************************y
    first seen in commit: af366a3ed66d
  - (unknown file):2
    type: CustomRegex   preview: ja*******************************y
    first seen in commit: af366a3ed66d
  - (unknown file):1
    type: CustomRegex   preview: ja*******************************.
    first seen in commit: 70d5c3a01398
  - (unknown file):2
    type: CustomRegex   preview: ja*******************************x
    first seen in commit: 70d5c3a01398
  - (unknown file):1
    type: CustomRegex   preview: ja*******************************x
    first seen in commit: 70d5c3a01398
  - (unknown file):2
    type: CustomRegex   preview: ha*************************************y
    first seen in commit: 33111717d521
  - (unknown file):1
    type: CustomRegex   preview: ha*************************************y
    first seen in commit: 33111717d521
  - (unknown file):1
    type: CustomRegex   preview: ha******************************e
    first seen in commit: abc3dc64cf61
  - (unknown file):1
    type: CustomRegex   preview: ha********************************y
    first seen in commit: abc3dc64cf61
  - (unknown file):2
    type: CustomRegex   preview: ha******************************e
    first seen in commit: abc3dc64cf61
  - (unknown file):1
    type: CustomRegex   preview: ty***************************.
    first seen in commit: a3aaf19e0980
  - (unknown file):1
    type: CustomRegex   preview: ty**************************g
    first seen in commit: a3aaf19e0980
  - (unknown file):2
    type: CustomRegex   preview: ty**************************g
    first seen in commit: a3aaf19e0980
  - (unknown file):2
    type: CustomRegex   preview: cy*****************************p
    first seen in commit: 242096832b55
  - (unknown file):1
    type: CustomRegex   preview: cy*****************************p
    first seen in commit: 242096832b55
  - (unknown file):2
    type: CustomRegex   preview: ty*****************************s
    first seen in commit: 33ababd1bdb6
  - (unknown file):1
    type: CustomRegex   preview: ty*****************************s
    first seen in commit: 33ababd1bdb6
  - (unknown file):2
    type: CustomRegex   preview: ty****************************h
    first seen in commit: 7031ab0d7563
  - (unknown file):1
    type: CustomRegex   preview: ty****************************h
    first seen in commit: 7031ab0d7563

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

