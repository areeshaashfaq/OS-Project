Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/eebbesen/pantry-for-good

Flagged locations (secret values are not included):

  - (unknown file):1
    type: CustomRegex   preview: go*****************************************s
    first seen in commit: eba654bc39a3
  - (unknown file):2
    type: CustomRegex   preview: pa*******************************s
    first seen in commit: eba654bc39a3
  - server/tests/integration/customer.spec.js:396
    type: CustomRegex   preview: ad***************************************y
    first seen in commit: 72ccce979d83
  - server/tests/integration/customer.spec.js:407
    type: CustomRegex   preview: vo*******************************************y
    first seen in commit: 72ccce979d83
  - server/tests/integration/volunteer.spec.js:147
    type: CustomRegex   preview: 12**********************************)
    first seen in commit: 72ccce979d83
  - server/tests/integration/volunteer.spec.js:152
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 72ccce979d83
  - server/tests/integration/volunteer.spec.js:170
    type: CustomRegex   preview: 12**********************************)
    first seen in commit: 72ccce979d83
  - server/tests/integration/volunteer.spec.js:147
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 72ccce979d83
  - server/tests/integration/user.spec.js:589
    type: CustomRegex   preview: 12**********************************)
    first seen in commit: 72ccce979d83
  - server/tests/integration/user.spec.js:613
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 72ccce979d83
  - server/tests/integration/user.spec.js:624
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 72ccce979d83
  - server/tests/integration/user.spec.js:589
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 72ccce979d83
  - server/tests/integration/customer.spec.js:396
    type: CustomRegex   preview: ad*******************************'
    first seen in commit: 72ccce979d83
  - server/tests/integration/customer.spec.js:426
    type: CustomRegex   preview: ad*******************************'
    first seen in commit: 72ccce979d83
  - server/tests/integration/customer.spec.js:396
    type: CustomRegex   preview: ad********************************,
    first seen in commit: 72ccce979d83
  - server/tests/integration/customer.spec.js:407
    type: CustomRegex   preview: vo***********************************'
    first seen in commit: 72ccce979d83
  - server/tests/integration/customer.spec.js:407
    type: CustomRegex   preview: vo************************************,
    first seen in commit: 72ccce979d83
  - server/tests/integration/customer.spec.js:412
    type: CustomRegex   preview: vo***********************************'
    first seen in commit: 72ccce979d83
  - server/tests/integration/customer.spec.js:425
    type: CustomRegex   preview: vo***********************************'
    first seen in commit: 72ccce979d83
  - server/tests/integration/user.spec.js:567
    type: CustomRegex   preview: 12********************************'
    first seen in commit: a8fd63e50938
  - server/tests/integration/user.spec.js:420
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 025a5599435a
  - server/tests/integration/user.spec.js:459
    type: CustomRegex   preview: ne**************************************'
    first seen in commit: 025a5599435a
  - server/tests/integration/user.spec.js:488
    type: CustomRegex   preview: 34********************************'
    first seen in commit: 025a5599435a
  - server/tests/integration/user.spec.js:546
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 025a5599435a
  - server/tests/integration/user.spec.js:446
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 025a5599435a
  - server/tests/integration/user.spec.js:559
    type: CustomRegex   preview: ne**************************************'
    first seen in commit: 025a5599435a
  - server/tests/integration/user.spec.js:521
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 025a5599435a
  - server/tests/integration/user.spec.js:500
    type: CustomRegex   preview: ne**************************************'
    first seen in commit: 025a5599435a
  - server/tests/integration/user.spec.js:479
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 025a5599435a
  - server/tests/integration/user.spec.js:362
    type: CustomRegex   preview: ne**************************************'
    first seen in commit: 472bbdc67037
  - server/tests/integration/user.spec.js:348
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 472bbdc67037
  - server/tests/integration/user.spec.js:397
    type: CustomRegex   preview: ne**************************************'
    first seen in commit: 472bbdc67037
  - server/tests/integration/user.spec.js:383
    type: CustomRegex   preview: 12********************************'
    first seen in commit: 472bbdc67037
  - client/modules/users/components/SignIn.spec.js:55
    type: CustomRegex   preview: us***********************************)
    first seen in commit: de53047c5875
  - client/modules/users/components/SignIn.spec.js:53
    type: CustomRegex   preview: us***********************************)
    first seen in commit: de53047c5875
  - client/modules/users/components/SignIn.spec.js:34
    type: CustomRegex   preview: us***********************************)
    first seen in commit: de53047c5875
  - client/modules/users/components/SignIn.spec.js:34
    type: CustomRegex   preview: us*****************************,
    first seen in commit: de53047c5875
  - client/modules/users/components/SignIn.spec.js:36
    type: CustomRegex   preview: us*****************************,
    first seen in commit: de53047c5875
  - client/modules/users/components/SignIn.spec.js:55
    type: CustomRegex   preview: us*****************************,
    first seen in commit: de53047c5875
  - client/modules/users/components/SignIn.spec.js:53
    type: CustomRegex   preview: us*****************************,
    first seen in commit: de53047c5875
  - server/tests/integration/user.spec.js:296
    type: CustomRegex   preview: mw*************************************,
    first seen in commit: 602f903f132e
  - server/tests/integration/user.spec.js:279
    type: CustomRegex   preview: mw*************************************,
    first seen in commit: 602f903f132e
  - server/tests/integration/user.spec.js:246
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 602f903f132e
  - server/tests/integration/user.spec.js:233
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 602f903f132e
  - server/tests/integration/user.spec.js:261
    type: CustomRegex   preview: mw*************************************,
    first seen in commit: 602f903f132e
  - server/tests/integration/user.spec.js:316
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 602f903f132e
  - server/tests/integration/user.spec.js:323
    type: CustomRegex   preview: mw*************************************,
    first seen in commit: 602f903f132e
  - server/tests/integration/user.spec.js:289
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 602f903f132e
  - server/tests/integration/user.spec.js:275
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 602f903f132e
  - server/tests/integration/user.spec.js:308
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 602f903f132e
  - server/tests/integration/user.spec.js:254
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 602f903f132e
  - README.md:8
    type: CustomRegex   preview: ad*********************************`
    first seen in commit: e4cb6a475b36
  - README.md:19
    type: CustomRegex   preview: ad*********************************`
    first seen in commit: 6e43f8c0fd31
  - client/modules/users/reducer.spec.js:72
    type: CustomRegex   preview: fo****************************}
    first seen in commit: fb3b216bc5c7
  - client/modules/users/reducer.spec.js:59
    type: CustomRegex   preview: fo****************************}
    first seen in commit: fb3b216bc5c7
  - client/modules/users/reducer.spec.js:33
    type: CustomRegex   preview: fo****************************}
    first seen in commit: fb3b216bc5c7
  - (unknown file):2
    type: CustomRegex   preview: pa***********************************r
    first seen in commit: e187f744a0ad
  - (unknown file):1
    type: CustomRegex   preview: pa***********************************r
    first seen in commit: e187f744a0ad
  - server/tests/integration/user.spec.js:77
    type: CustomRegex   preview: mw*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:180
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:33
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:45
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:209
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:55
    type: CustomRegex   preview: bl***********************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:218
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:230
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:114
    type: CustomRegex   preview: mw*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:251
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:89
    type: CustomRegex   preview: mw*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:272
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:147
    type: CustomRegex   preview: mw*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:281
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:98
    type: CustomRegex   preview: mw*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:67
    type: CustomRegex   preview: bl***********************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:165
    type: CustomRegex   preview: mw*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:131
    type: CustomRegex   preview: mw*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:191
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 488d25ad0ae9
  - server/tests/integration/user.spec.js:260
    type: CustomRegex   preview: fh*************************************,
    first seen in commit: 488d25ad0ae9
  - README.md:7
    type: CustomRegex   preview: ad**********************************.
    first seen in commit: a342595590be
  - README.md:18
    type: CustomRegex   preview: ad*********************************`
    first seen in commit: a342595590be
  - README.md:32
    type: CustomRegex   preview: ad**********************************.
    first seen in commit: a342595590be
  - server/lib/seed.js:80
    type: CustomRegex   preview: ad***********************************,
    first seen in commit: a342595590be
  - README.md:7
    type: CustomRegex   preview: gi******************************`
    first seen in commit: 3cf126e9dff3
  - README.md:7
    type: CustomRegex   preview: gi*******************************.
    first seen in commit: 3cf126e9dff3
  - client/modules/driver/components/DriverRoutes.js:170
    type: GoogleGeminiAPIKey   preview: AI************************************U
    first seen in commit: be666f6112a0
  - (unknown file):1
    type: CustomRegex   preview: ke*************************************************n
    first seen in commit: 70344e0ea2be
  - (unknown file):2
    type: CustomRegex   preview: pa*************************************n
    first seen in commit: 70344e0ea2be
  - client/modules/driver/location-reducer.js:3
    type: GoogleGeminiAPIKey   preview: AI************************************U
    first seen in commit: fbea4a3ec0b0
  - public/store/location.js:3
    type: GoogleGeminiAPIKey   preview: AI************************************U
    first seen in commit: 05b776fdc507
  - (unknown file):1
    type: CustomRegex   preview: pa***********************************r
    first seen in commit: e694a0dd15d9
  - (unknown file):2
    type: CustomRegex   preview: pa***********************************r
    first seen in commit: e694a0dd15d9
  - app-config.json:6
    type: CustomRegex   preview: mo**********************************************************9
    first seen in commit: a5dc85b21560
  - template-config.json:12
    type: CustomRegex   preview: mo**********************************************************9
    first seen in commit: 066d4d10b619
  - app-config.json:6
    type: MongoDB   preview: mo**************************************************************************x
    first seen in commit: a5dc85b21560
  - template-config.json:12
    type: MongoDB   preview: mo**************************************************************************x
    first seen in commit: 066d4d10b619

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

