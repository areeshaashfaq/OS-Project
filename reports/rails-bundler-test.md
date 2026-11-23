Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/judygogo/rails-bundler-test

Flagged locations (secret values are not included):

  - actionpack/CHANGELOG.md:4586
    type: CustomRegex   preview: st*****************************s
    first seen in commit: 369e28a87419
  - actionpack/CHANGELOG.md:4576
    type: CustomRegex   preview: th***************************s
    first seen in commit: 369e28a87419
  - actionpack/CHANGELOG.md:4582
    type: CustomRegex   preview: dw*******************************s
    first seen in commit: 369e28a87419
  - actionpack/CHANGELOG.md:4543
    type: CustomRegex   preview: mo******************************s
    first seen in commit: 369e28a87419
  - actionpack/test/controller/url_rewriter_test.rb:47
    type: CustomRegex   preview: ht**************************t
    first seen in commit: 369e28a87419
  - actionpack/test/controller/url_rewriter_test.rb:47
    type: URI   preview: ht**************************t
    first seen in commit: 369e28a87419
  - actionpack/test/controller/url_rewriter_test.rb:54
    type: URI   preview: ht****************************************************t
    first seen in commit: 369e28a87419
  - actionpack/test/controller/url_rewriter_test.rb:54
    type: CustomRegex   preview: ht****************************************************t
    first seen in commit: 369e28a87419
  - actionpack/test/dispatch/request_test.rb:26
    type: CustomRegex   preview: ht*************************************,
    first seen in commit: 369e28a87419
  - actionpack/test/dispatch/request_test.rb:26
    type: URI   preview: ht***********************************m
    first seen in commit: 369e28a87419
  - activerecord/lib/active_record/connection_adapters/abstract/connection_specification.rb:120
    type: CustomRegex   preview: po*******************************t
    first seen in commit: 369e28a87419
  - activeresource/lib/active_resource/base.rb:50
    type: CustomRegex   preview: ht****************************************"
    first seen in commit: 369e28a87419
  - activeresource/lib/active_resource/base.rb:124
    type: CustomRegex   preview: ht*************************************0
    first seen in commit: 369e28a87419
  - activeresource/test/fixtures/proxy.rb:3
    type: CustomRegex   preview: ht***********************************"
    first seen in commit: 369e28a87419
  - activeresource/test/fixtures/proxy.rb:3
    type: URI   preview: ht**********************************0
    first seen in commit: 369e28a87419
  - activeresource/test/cases/connection_test.rb:121
    type: CustomRegex   preview: ht***********************************************"
    first seen in commit: 369e28a87419
  - activeresource/test/cases/connection_test.rb:121
    type: URI   preview: ht**********************************************2
    first seen in commit: 369e28a87419
  - activeresource/test/cases/connection_test.rb:121
    type: CustomRegex   preview: ht************************************************)
    first seen in commit: 369e28a87419
  - activeresource/lib/active_resource/base.rb:124
    type: CustomRegex   preview: pa*****************************************"
    first seen in commit: 369e28a87419
  - activeresource/lib/active_resource/base.rb:124
    type: CustomRegex   preview: pa************************************.
    first seen in commit: 369e28a87419
  - activeresource/lib/active_resource/base.rb:124
    type: URI   preview: ht*************************************0
    first seen in commit: 369e28a87419
  - activeresource/lib/active_resource/base.rb:50
    type: URI   preview: ht***************************************0
    first seen in commit: 369e28a87419
  - activeresource/test/cases/authorization_test.rb:11
    type: CustomRegex   preview: ht*****************************)
    first seen in commit: 369e28a87419
  - activeresource/test/cases/authorization_test.rb:11
    type: URI   preview: ht***************************t
    first seen in commit: 369e28a87419
  - activeresource/test/cases/authorization_test.rb:230
    type: CustomRegex   preview: ht*************************************************)
    first seen in commit: 369e28a87419
  - activeresource/test/cases/authorization_test.rb:1
    type: URI   preview: ht********************************t
    first seen in commit: 369e28a87419
  - activeresource/test/cases/authorization_test.rb:79
    type: CustomRegex   preview: ht****************************************)
    first seen in commit: 369e28a87419
  - activeresource/test/cases/authorization_test.rb:84
    type: CustomRegex   preview: my*****************************"
    first seen in commit: 369e28a87419
  - activeresource/test/cases/authorization_test.rb:70
    type: URI   preview: ht**********************t
    first seen in commit: 369e28a87419
  - activeresource/test/cases/authorization_test.rb:84
    type: CustomRegex   preview: my*****************************'
    first seen in commit: 369e28a87419
  - activeresource/test/cases/base_test.rb:63
    type: CustomRegex   preview: ht************************************,
    first seen in commit: 369e28a87419
  - activeresource/test/cases/base_test.rb:63
    type: CustomRegex   preview: pa**************************************'
    first seen in commit: 369e28a87419
  - activeresource/test/cases/base_test.rb:148
    type: CustomRegex   preview: my******************************'
    first seen in commit: 369e28a87419
  - activeresource/test/cases/base_test.rb:63
    type: CustomRegex   preview: pa*************************************'
    first seen in commit: 369e28a87419
  - activeresource/test/cases/base_test.rb:148
    type: CustomRegex   preview: my*****************************'
    first seen in commit: 369e28a87419
  - activeresource/test/cases/base_test.rb:63
    type: URI   preview: ht**********************************0
    first seen in commit: 369e28a87419
  - activeresource/test/cases/base_test.rb:40
    type: URI   preview: ht**************************e
    first seen in commit: 369e28a87419
  - activeresource/test/cases/base_test.rb:1
    type: URI   preview: ht*****************************a
    first seen in commit: 369e28a87419
  - activeresource/test/cases/base_test.rb:41
    type: URI   preview: ht**************************e
    first seen in commit: 369e28a87419

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

