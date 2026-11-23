Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/GabrielSNeto/desafio_python

Flagged locations (secret values are not included):

  - 13 - APIs Assíncronas com FastAPI/desafio/alembic.ini:63
    type: CustomRegex   preview: dr*************************t
    first seen in commit: 57fa8181981e
  - 13 - APIs Assíncronas com FastAPI/dio-blog/alembic.ini:63
    type: CustomRegex   preview: dr*************************t
    first seen in commit: 57fa8181981e
  - 12 - Desenvolvimento fullstack com Django/mysite/tests/contacts/test_views.py:38
    type: CustomRegex   preview: se*************************************)
    first seen in commit: 2f1e61f9d901
  - 12 - Desenvolvimento fullstack com Django/mysite/tests/contacts/test_views.py:41
    type: CustomRegex   preview: jo**********************************)
    first seen in commit: 2f1e61f9d901
  - 12 - Desenvolvimento fullstack com Django/mysite/tests/contacts/test_views.py:36
    type: CustomRegex   preview: su*************************************)
    first seen in commit: 2f1e61f9d901

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

