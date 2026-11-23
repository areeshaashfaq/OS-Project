Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/wgriffey/notes-app-flutter

Flagged locations (secret values are not included):

  - (unknown file):2
    type: CustomRegex   preview: wg***************************************y
    first seen in commit: b51c7f491069
  - (unknown file):1
    type: CustomRegex   preview: wg***************************************y
    first seen in commit: b51c7f491069
  - test/auth_test.dart:78
    type: CustomRegex   preview: fo***********************************,
    first seen in commit: e5aba4cbcda6
  - lib/firebase_options.dart:50
    type: GoogleGeminiAPIKey   preview: AI************************************8
    first seen in commit: 10df44f49492
  - web/index.html:53
    type: GoogleGeminiAPIKey   preview: AI************************************8
    first seen in commit: 10df44f49492
  - test/auth_test.dart:121
    type: CustomRegex   preview: fo*****************************)
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:52
    type: CustomRegex   preview: fo********************************,
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:42
    type: CustomRegex   preview: fo******************************,
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:52
    type: CustomRegex   preview: fo***********************************,
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:42
    type: CustomRegex   preview: fo*******************************;
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:62
    type: CustomRegex   preview: fo***********************************,
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:42
    type: CustomRegex   preview: fo***************************,
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:52
    type: CustomRegex   preview: fo********************************,
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:42
    type: CustomRegex   preview: fo*****************************)
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:52
    type: CustomRegex   preview: fo************************************;
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:52
    type: CustomRegex   preview: fo**********************************)
    first seen in commit: 0dcbaf961edf
  - android/app/google-services.json:18
    type: GoogleGeminiAPIKey   preview: AI************************************8
    first seen in commit: a4abd0095f0c
  - test/auth_test.dart:42
    type: CustomRegex   preview: fo***************************,
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:79
    type: CustomRegex   preview: fo***********************************,
    first seen in commit: 0dcbaf961edf
  - test/auth_test.dart:121
    type: CustomRegex   preview: fo******************************,
    first seen in commit: 0dcbaf961edf
  - ios/Runner/GoogleService-Info.plist:6
    type: GoogleGeminiAPIKey   preview: AI************************************c
    first seen in commit: a4abd0095f0c
  - lib/firebase_options.dart:61
    type: GoogleGeminiAPIKey   preview: AI************************************c
    first seen in commit: a4abd0095f0c
  - lib/firebase_options.dart:53
    type: GoogleGeminiAPIKey   preview: AI************************************8
    first seen in commit: a4abd0095f0c

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

