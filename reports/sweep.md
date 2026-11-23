Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/amorriscode/sweep

Flagged locations (secret values are not included):

  - tests/archive/test_replicate.py:5
    type: Replicate   preview: r8*************************************Y
    first seen in commit: f5a0e779104f
  - sweepai/sandbox/test_sandbox.py:17
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 30a7964df077
  - sweepai/utils/search_utils.py:79
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 34f5133f9be3
  - sweepai/utils/github_utils.py:110
    type: CustomRegex   preview: ht*******************************************m
    first seen in commit: 34f5133f9be3
  - sweepai/utils/github_utils.py:102
    type: CustomRegex   preview: ht*******************************************m
    first seen in commit: 7b451e817379
  - sweepai/test_api.py:10
    type: OpenAI   preview: sk************************************************x
    first seen in commit: 5f846e4f779a
  - self_deploy/test/fixtures/mock-cert.pem:1
    type: PrivateKey   preview: --***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 4a062e264ffc
  - self_deploy/test/fixtures/mock-cert.pem:1
    type: PrivateKey   preview: --***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 49d55bb61032
  - sweepai/utils/search_utils.py:73
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: e8fa9ae5e823
  - sweepai/utils/search_utils.py:73
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 2408b48efca4
  - sweepai/handlers/on_ticket.py:558
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: bf1e27dfb0a1
  - sweepai/handlers/on_ticket.py:558
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: ccf8c74d9432
  - sweepai/handlers/on_ticket.py:558
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 559be2aec83d
  - sweepai/core/sweep_bot.py:427
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 65699e3036e7
  - sweepai/core/sweep_bot.py:427
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 83d9706cb4f2
  - sweepai/api.py:112
    type: CustomRegex   preview: ad******************************g
    first seen in commit: 43835010dfd3
  - tests/js_tests/test_create_issue.js:12
    type: Github   preview: gh*************************************b
    first seen in commit: 645e5fcd11d4
  - tests/js_tests/test_create_issue.js:11
    type: Github   preview: gi******************************************************************************************b
    first seen in commit: 645e5fcd11d4
  - tests/js_tests/test_create_issue.js:12
    type: Github   preview: gh*************************************b
    first seen in commit: 70518c48dcc6
  - tests/js_tests/test_create_issue.js:11
    type: Github   preview: gi******************************************************************************************b
    first seen in commit: 70518c48dcc6
  - extension/pnpm-lock.yaml:1478
    type: Box   preview: cb*****************************n
    first seen in commit: 80ab70ab386c
  - extension/pnpm-lock.yaml:1478
    type: Box   preview: cb*****************************n
    first seen in commit: eba83927964d
  - sweepai/utils/github_utils.py:211
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: d9ef9cb859f1
  - sweepai/utils/github_utils.py:211
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 386aad7de324
  - sweepai/utils/github_utils.py:221
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 125867cf6801
  - sweepai/utils/github_utils.py:221
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: fa63b2975816
  - sweepai/app/ui.py:110
    type: CustomRegex   preview: ht**************************************************m
    first seen in commit: 7344db4a2b3a
  - sweepai/app/ui.py:110
    type: CustomRegex   preview: ht**************************************************m
    first seen in commit: c182b5a29ce5
  - sweepai/app/ui.py:110
    type: CustomRegex   preview: ht**************************************************m
    first seen in commit: 89515eb4f8c4
  - sweepai/utils/github_utils.py:134
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 7672a5020d4d
  - sweepai/utils/github_utils.py:134
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 781420a6c6cc
  - sweepai/utils/github_utils.py:134
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 80f3ef75ae49
  - sweepai/utils/github_utils.py:134
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 0c3b26fffdee
  - sweepai/app/ui.py:98
    type: CustomRegex   preview: ht**************************************************m
    first seen in commit: d94efe20eaa5
  - sweepai/app/ui.py:98
    type: CustomRegex   preview: ht**************************************************m
    first seen in commit: 8373762c1ee3
  - sweepai/app/ui.py:103
    type: CustomRegex   preview: ht**************************************************m
    first seen in commit: 3983100483b1
  - sweepai/app/ui.py:103
    type: CustomRegex   preview: ht**************************************************m
    first seen in commit: d94915c65c96
  - sweepai/app/ui.py:92
    type: CustomRegex   preview: ht**************************************************m
    first seen in commit: a2db4197aad7
  - sweepai/app/ui.py:92
    type: CustomRegex   preview: ht**************************************************m
    first seen in commit: 759ca5726bcf
  - src/core/vector_db.py:140
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 96dbc1f448ef
  - src/core/vector_db.py:242
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 96dbc1f448ef
  - src/core/vector_db.py:248
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 1843308fbc31
  - src/core/vector_db.py:247
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 1843308fbc31
  - tests/test_generate_new_files.py:796
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 93d1f2c9738c
  - tests/test_generate_new_files.py:796
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: a4f464610d4a
  - src/core/vector_db.py:131
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: b441a97c8f3f
  - src/utils/cache.py:4
    type: CustomRegex   preview: re*****************************************************************************************************)
    first seen in commit: fd20241059d3
  - src/utils/cache.py:4
    type: CustomRegex   preview: re*****************************************************************************************************)
    first seen in commit: 458b25dd0812
  - src/utils/github_utils.py:121
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: d4d0453eea9d
  - src/utils/github_utils.py:109
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: d4d0453eea9d
  - src/core/vector_db.py:130
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: d4d0453eea9d
  - src/core/vector_db.py:130
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 82a177f1c49f
  - src/utils/github_utils.py:121
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 82a177f1c49f
  - src/utils/github_utils.py:109
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 82a177f1c49f

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

