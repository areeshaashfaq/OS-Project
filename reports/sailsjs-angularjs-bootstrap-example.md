Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/husttom/sailsjs-angularjs-bootstrap-example

Flagged locations (secret values are not included):

  - config/session.js:48
    type: CustomRegex   preview: mo**************************t
    first seen in commit: cd53dd4f6b96
  - config/session.js:48
    type: MongoDB   preview: mo*********************t
    first seen in commit: cd53dd4f6b96

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

