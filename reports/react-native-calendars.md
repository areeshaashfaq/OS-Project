Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/pkkasu/react-native-calendars

Flagged locations (secret values are not included):

  - ios/Pods/Pods.xcodeproj/project.pbxproj:2550
    type: Wit   preview: DB*****************************B
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:1774
    type: Wit   preview: 17*****************************F
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:1734
    type: Wit   preview: 0C*****************************7
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:1971
    type: Box   preview: 46*****************************0
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:1931
    type: Box   preview: 3E*****************************2
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:1936
    type: Wit   preview: 3F*****************************C
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:6963
    type: Wit   preview: E6*****************************7
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:6962
    type: Wit   preview: 3E*****************************9
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5727
    type: Wit   preview: 1C*****************************D
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5726
    type: Wit   preview: F0*****************************8
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:3926
    type: Wit   preview: B8*****************************2
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:3924
    type: Wit   preview: 0C*****************************F
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:3925
    type: Wit   preview: DB*****************************9
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:3923
    type: Wit   preview: 3F*****************************5
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5677
    type: Box   preview: FA*****************************1
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5137
    type: Box   preview: 3E*****************************4
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5140
    type: Box   preview: 41*****************************9
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5138
    type: Box   preview: CB*****************************6
    first seen in commit: dc9c2d8c4cb0
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5139
    type: Box   preview: A2*****************************C
    first seen in commit: dc9c2d8c4cb0
  - scripts/release.js:43
    type: CustomRegex   preview: ht**********************************************************************;
    first seen in commit: 548e5fab8d57

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

