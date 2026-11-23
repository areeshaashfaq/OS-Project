Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/weini/cocos2d-x

Flagged locations (secret values are not included):

  - tools/JenkinsScript/ReportManager.py:17
    type: CustomRegex   preview: 73***************************************'
    first seen in commit: 87a0dbc2da0a
  - tools/JenkinsScript/ReportManager.py:17
    type: CustomRegex   preview: ya***************************************************'
    first seen in commit: 87a0dbc2da0a
  - tools/JenkinsScript/ReportManager.py:16
    type: CustomRegex   preview: re********************************************'
    first seen in commit: 87a0dbc2da0a
  - tools/JenkinsScript/ReportManager.py:17
    type: CustomRegex   preview: ya*****************************************************'
    first seen in commit: 87a0dbc2da0a
  - tools/JenkinsScript/ReportManager.py:28
    type: CustomRegex   preview: re********************************************'
    first seen in commit: 87a0dbc2da0a
  - testjs/spidermonkey-ios/bin/js:8890
    type: Kylas   preview: de*********************************p
    first seen in commit: da261c74cd0f
  - testjs/spidermonkey-ios/bin/js:8886
    type: Kylas   preview: de*********************************p
    first seen in commit: da261c74cd0f
  - cocos2dx/platform/third_party/ios/libraries/libcurl.a:23440
    type: CustomRegex   preview: s:********************y
    first seen in commit: 606ea9f1ae0d
  - cocos2dx/platform/third_party/ios/libraries/libcurl.a:23468
    type: CustomRegex   preview: s:******************y
    first seen in commit: 606ea9f1ae0d

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

