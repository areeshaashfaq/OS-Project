Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/Tilenozz/react-native-awesome-alerts

Flagged locations (secret values are not included):

  - examples/android/app/build/intermediates/transforms/dex/debug/folders/1000/1f/main/classes.dex:30898
    type: CustomRegex   preview: s:******************************************************************:
    first seen in commit: fb038221392d
  - examples/android/app/build/intermediates/transforms/dex/debug/folders/1000/1f/main/classes.dex:31055
    type: Honeycomb   preview: Ki*******************l
    first seen in commit: fb038221392d
  - examples/android/app/build/intermediates/transforms/dex/debug/folders/1000/1f/main/classes.dex:31031
    type: Honeycomb   preview: Ho*******************y
    first seen in commit: fb038221392d
  - examples/android/app/build/outputs/apk/app-debug.apk:43118
    type: Honeycomb   preview: is*******************d
    first seen in commit: fb038221392d

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

