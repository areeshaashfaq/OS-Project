Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/pentestbr/vulndb

Flagged locations (secret values are not included):

  - test/data/cve_data.json:1
    type: Gitlab   preview: 2-*******************g
    first seen in commit: 5a70559c85f4
  - test/data/cve_data.json:1
    type: CustomRegex   preview: cv**************************,
    first seen in commit: 5a70559c85f4
  - test/data/cve_data.json:1
    type: CustomRegex   preview: cv*************************e
    first seen in commit: 5a70559c85f4
  - test/data/cve_data.json:1
    type: CustomRegex   preview: cv*****************************n
    first seen in commit: 5a70559c85f4
  - test/data/cve_data.json:1
    type: CustomRegex   preview: cv*****************************n
    first seen in commit: 5a70559c85f4
  - test/data/cve_data.json:1
    type: CustomRegex   preview: cv**************************)
    first seen in commit: 5a70559c85f4
  - test/data/cve_data.json:1
    type: CustomRegex   preview: cv*************************.
    first seen in commit: 5a70559c85f4
  - test/data/cve_data.json:1
    type: CustomRegex   preview: cv***************************h
    first seen in commit: 5a70559c85f4

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

