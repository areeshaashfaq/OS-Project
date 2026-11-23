Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/erdldncr/htmx

Flagged locations (secret values are not included):

  - www/content/talk/index.md:31
    type: Github   preview: gi******************************************************************************************7
    first seen in commit: 30a6a40f4e8a
  - www/content/talk/index.md:28
    type: Github   preview: gi******************************************************************************************7
    first seen in commit: 30a6a40f4e8a
  - www-zola/content/talk.md:34
    type: Github   preview: gh*************************************G
    first seen in commit: 720de18cfea8
  - www-zola/content/talk.md:33
    type: Github   preview: gh*************************************G
    first seen in commit: 720de18cfea8
  - www-hugo/content/talk.md:33
    type: Github   preview: gh*************************************G
    first seen in commit: e435790ed960
  - www-hugo/content/talk.md:34
    type: Github   preview: gh*************************************G
    first seen in commit: e435790ed960
  - www/talk.md:33
    type: Github   preview: gh*************************************G
    first seen in commit: 2273f1367700
  - www/talk.md:30
    type: Github   preview: gh*************************************G
    first seen in commit: 2273f1367700

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

