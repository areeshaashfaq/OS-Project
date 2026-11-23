Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/devrawan/Meals-App2

Flagged locations (secret values are not included):

  - ios/Pods/Pods.xcodeproj/project.pbxproj:214
    type: Box   preview: 0B*****************************1
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5065
    type: Box   preview: 24*****************************6
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5774
    type: Box   preview: 61*****************************0
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5828
    type: Box   preview: 66*****************************E
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5652
    type: Box   preview: 57*****************************D
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:6821
    type: Box   preview: BB*****************************9
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5619
    type: Wit   preview: 54*****************************0
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:6284
    type: Wit   preview: 8E*****************************1
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5738
    type: Wit   preview: 5F*****************************9
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:6599
    type: Wit   preview: A8*****************************1
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5348
    type: Wit   preview: 3C*****************************A
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:7018
    type: Box   preview: CB*****************************8
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:6324
    type: Box   preview: 91*****************************E
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:6314
    type: Box   preview: 90*****************************D
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:6529
    type: Wit   preview: A2*****************************5
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5554
    type: Wit   preview: 4F*****************************A
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:7179
    type: Box   preview: DB*****************************0
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:6309
    type: Wit   preview: 90*****************************9
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:9365
    type: Box   preview: 2D*****************************D
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:9362
    type: Box   preview: CB*****************************0
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:9363
    type: Box   preview: 6E*****************************1
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:11590
    type: Box   preview: AA*****************************E
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:11589
    type: Box   preview: BB*****************************6
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:12138
    type: Box   preview: 66*****************************7
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:12139
    type: Box   preview: 24*****************************7
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:8123
    type: Wit   preview: 53*****************************9
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:8124
    type: Wit   preview: 5F*****************************B
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:8125
    type: Wit   preview: A8*****************************B
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:8126
    type: Wit   preview: 78*****************************4
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:10521
    type: Wit   preview: 24*****************************4
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:10516
    type: Wit   preview: 9A*****************************8
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:13437
    type: Wit   preview: 51*****************************2
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:13436
    type: Wit   preview: 0E*****************************B
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:9599
    type: Wit   preview: 43*****************************E
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:9639
    type: Box   preview: 8A*****************************7
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:8378
    type: Wit   preview: A1*****************************9
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:9635
    type: Box   preview: 91*****************************C
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:9636
    type: Box   preview: 1C*****************************C
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:8376
    type: Wit   preview: 54*****************************B
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:8377
    type: Wit   preview: 3C*****************************0
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:9788
    type: Box   preview: 90*****************************1
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:14372
    type: Wit   preview: 31*****************************F
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:14371
    type: Wit   preview: AD*****************************4
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:16548
    type: Wit   preview: EB*****************************2
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:14247
    type: Wit   preview: 8B*****************************9
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:16620
    type: Wit   preview: 39*****************************6
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:14276
    type: Box   preview: 5D*****************************7
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:14319
    type: Box   preview: 41*****************************D
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:14275
    type: Box   preview: 3C*****************************7
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:14317
    type: Box   preview: D1*****************************A
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:17336
    type: Box   preview: 87*****************************2
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:17332
    type: Box   preview: C5*****************************1
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:17333
    type: Box   preview: 9D*****************************5
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:5612
    type: Wit   preview: 53*****************************5
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:16358
    type: Box   preview: 99*****************************9
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:16393
    type: Wit   preview: ED*****************************8
    first seen in commit: 39b4b4617845
  - ios/Pods/Pods.xcodeproj/project.pbxproj:16392
    type: Wit   preview: B9*****************************F
    first seen in commit: 39b4b4617845
  - ios/Pods/boost-for-react-native/boost/polygon/polygon_set_data.hpp:894
    type: Circle   preview: 14*************************************1
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/main.js:99
    type: Box   preview: dc*****************************e
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/main.js:138
    type: Box   preview: bf*****************************d
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/main.js:141
    type: Box   preview: aa*****************************d
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:56
    type: Box   preview: ec*****************************f
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:59
    type: Box   preview: f6*****************************f
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:80
    type: Box   preview: e1*****************************1
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:89
    type: Box   preview: f7*****************************2
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:92
    type: Box   preview: c6*****************************2
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/main.js:96
    type: Box   preview: a5*****************************3
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/main.js:57
    type: Box   preview: d3*****************************b
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/main.js:63
    type: Box   preview: a5*****************************4
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:32
    type: Box   preview: f1*****************************6
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:53
    type: Box   preview: b7*****************************7
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/main.js:69
    type: Box   preview: ee*****************************f
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:14
    type: Box   preview: d7*****************************6
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:17
    type: Box   preview: f9*****************************9
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:29
    type: Box   preview: b2*****************************6
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/main.js:150
    type: Box   preview: ab*****************************6
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:113
    type: Box   preview: da*****************************9
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:107
    type: Box   preview: dc*****************************8
    first seen in commit: 39b4b4617845
  - node_modules/@react-aria/combobox/dist/module.js:110
    type: Box   preview: b6*****************************9
    first seen in commit: 39b4b4617845
  - node_modules/hosted-git-info/index.js:118
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 39b4b4617845
  - node_modules/hosted-git-info/index.js:118
    type: URI   preview: ht**************************************m
    first seen in commit: 39b4b4617845
  - node_modules/rsvp/CHANGELOG.md:222
    type: GitHubOauth2   preview: 26*****************a
    first seen in commit: 39b4b4617845
  - node_modules/rsvp/CHANGELOG.md:222
    type: GitHubOauth2   preview: 26*****************a
    first seen in commit: 39b4b4617845
  - node_modules/rsvp/CHANGELOG.md:222
    type: GitHubOauth2   preview: 26*****************a
    first seen in commit: 39b4b4617845
  - node_modules/uri-js/README.md:12
    type: CustomRegex   preview: ur****************************3
    first seen in commit: 39b4b4617845
  - node_modules/yargs/CHANGELOG.md:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 39b4b4617845
  - src/assets/filesBase64.js:5
    type: Box   preview: Od*****************************P
    first seen in commit: 39b4b4617845
  - src/assets/filesBase64.js:5
    type: TLy   preview: BB*********************************************************t
    first seen in commit: 39b4b4617845
  - src/assets/filesBase64.js:5
    type: Box   preview: Wo*****************************Q
    first seen in commit: 39b4b4617845
  - src/assets/filesBase64.js:5
    type: TLy   preview: ie*********************************************************V
    first seen in commit: 39b4b4617845

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

