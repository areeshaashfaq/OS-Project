Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/mauriciodeoliveirareis/Stat-Program-and-Applications-MATH9902

Flagged locations (secret values are not included):

  - linearGeneralRegModel/ca2/ca2.html:620
    type: Box   preview: Qg*****************************h
    first seen in commit: 4cc9f07b2304
  - topicsInAppliedStats/millerLabSurvival/millerLabSurvival.html:611
    type: Box   preview: 11*****************************N
    first seen in commit: 4cc9f07b2304
  - topicsInAppliedStats/millerLabSurvival/millerLabSurvival.html:611
    type: Box   preview: ts*****************************M
    first seen in commit: 4cc9f07b2304
  - topicsInAppliedStats/millerLabSurvival/millerLabSurvival.html:1249
    type: Box   preview: dQ*****************************G
    first seen in commit: 4cc9f07b2304
  - topicsInAppliedStats/ca1/ca1.html:363
    type: Box   preview: O5*****************************f
    first seen in commit: 7965ee743e1c
  - topicsInAppliedStats/ca1/ca1.html:331
    type: Sirv   preview: /r*************************************************************************************1
    first seen in commit: 36db936c2de3
  - topicsInAppliedStats/ca1/ca1.html:255
    type: Box   preview: n3*****************************e
    first seen in commit: d0bb6dc16002

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

