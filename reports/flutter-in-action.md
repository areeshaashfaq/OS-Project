Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/letitbesowhat/flutter-in-action

Flagged locations (secret values are not included):

  - _book/search_index.json:1
    type: CustomRegex   preview: ht**********************************************************************************************************************************************************************************************************************************************************a
    first seen in commit: 546b89cc980c
  - _book/search_index.json:1
    type: CustomRegex   preview: ht**********************************************************************************************************************************************************************************************************************************************************a
    first seen in commit: d17e5f5c97e8
  - _book/search_index.json:1
    type: CustomRegex   preview: ht**********************************************************************************************************************************************************************************************************************************************************a
    first seen in commit: c70af339d36a

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

