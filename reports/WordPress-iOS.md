Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/wtuyp/WordPress-iOS

Flagged locations (secret values are not included):

  - (unknown file):2
    type: CustomRegex   preview: er*******************************d
    first seen in commit: ccd5d7e8c07d
  - (unknown file):1
    type: CustomRegex   preview: er*******************************d
    first seen in commit: ccd5d7e8c07d
  - WordPress/Vendor/PocketAPI/PocketAPI.m:453
    type: CustomRegex   preview: ap**************************************************************{
    first seen in commit: 3690f99139b9
  - WordPress/Vendor/PocketAPI/PocketAPI.m:453
    type: CustomRegex   preview: ap********************************g
    first seen in commit: 3690f99139b9
  - WordPress/Vendor/PocketAPI/PocketAPI.m:453
    type: CustomRegex   preview: ap*******************************d
    first seen in commit: 3690f99139b9
  - WordPress/Vendor/PocketAPI/PocketAPI.m:453
    type: CustomRegex   preview: ap****************************************************************{
    first seen in commit: 3690f99139b9
  - WordPress/Vendor/PocketAPI/PocketAPI.m:453
    type: CustomRegex   preview: ap***********************************.
    first seen in commit: 3690f99139b9
  - WordPress/Vendor/PocketAPI/PocketAPI.m:453
    type: CustomRegex   preview: ap*********************************************{
    first seen in commit: 3690f99139b9
  - (unknown file):2
    type: CustomRegex   preview: jo*********************************d
    first seen in commit: b336e0080bf9
  - (unknown file):1
    type: CustomRegex   preview: jo*********************************d
    first seen in commit: b336e0080bf9
  - (unknown file):2
    type: CustomRegex   preview: ro*************************************e
    first seen in commit: 3d81879dd232
  - (unknown file):1
    type: CustomRegex   preview: ro*************************************e
    first seen in commit: 3d81879dd232
  - (unknown file):2
    type: CustomRegex   preview: jo********************************g
    first seen in commit: 7cdc5b5184d9
  - (unknown file):1
    type: CustomRegex   preview: jo********************************g
    first seen in commit: 7cdc5b5184d9
  - (unknown file):2
    type: CustomRegex   preview: jo********************************d
    first seen in commit: 84ed7d7dfa0b
  - (unknown file):1
    type: CustomRegex   preview: jo********************************d
    first seen in commit: 84ed7d7dfa0b
  - Classes/XMLSignupViewController.m:472
    type: CustomRegex   preview: %@******************************************;
    first seen in commit: 69f9c36ec276
  - Classes/XMLSignupViewController.m:471
    type: CustomRegex   preview: %@******************************************;
    first seen in commit: 69f9c36ec276
  - (unknown file):2
    type: CustomRegex   preview: er*************************************n
    first seen in commit: 8235a5d42b01
  - (unknown file):1
    type: CustomRegex   preview: er*************************************n
    first seen in commit: 8235a5d42b01
  - (unknown file):1
    type: CustomRegex   preview: jo********************************d
    first seen in commit: 381c3cb0ac5c
  - (unknown file):2
    type: CustomRegex   preview: jo********************************d
    first seen in commit: 381c3cb0ac5c
  - AFNetworking/README.md:35
    type: Flickr   preview: b6*****************************7
    first seen in commit: b4eccd543d2e
  - (unknown file):2
    type: CustomRegex   preview: da******************************t
    first seen in commit: 7655ea736095
  - (unknown file):1
    type: CustomRegex   preview: da******************************t
    first seen in commit: 7655ea736095
  - (unknown file):2
    type: CustomRegex   preview: jo***********************************.
    first seen in commit: f87e7186cedf
  - (unknown file):1
    type: CustomRegex   preview: jo***********************************.
    first seen in commit: f87e7186cedf
  - build/Debug-iphonesimulator/WordPress.app/WordPress:163
    type: CustomRegex   preview: %@********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************d
    first seen in commit: 61dff9ccbea6

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

