Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/Tim96995/tim-first-project

Flagged locations (secret values are not included):

  - LandingPage.html:545
    type: GoogleGeminiAPIKey   preview: AI************************************4
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/README.md:62
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/README.md:68
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/README.md:62
    type: CustomRegex   preview: to**********************************************n
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3028
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3064
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3075
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3077
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3102
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3113
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3116
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3281
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3270
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:4540
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:4551
    type: CustomRegex   preview: ne********************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:4540
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:4551
    type: CustomRegex   preview: ne***********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:4540
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:4551
    type: CustomRegex   preview: ne*********************************t
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:3551
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:3576
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:3587
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:3590
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3976
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:3502
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3976
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3987
    type: CustomRegex   preview: ne***********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3987
    type: CustomRegex   preview: ne********************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3976
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth-public.d.ts:3987
    type: CustomRegex   preview: ne*********************************t
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:3538
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/auth.d.ts:3549
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js:5999
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js:5985
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js:5996
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js:5744
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js:5744
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js:5755
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js:5757
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js:5744
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/src/core/strategies/email_and_password.d.ts:42
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/src/core/strategies/email_and_password.d.ts:44
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to********************************************g
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to******************************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to************************************************;
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:2652
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:2858
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:2663
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:2665
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:2690
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:2701
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:2704
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:2869
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:2872
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:3322
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:3322
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:3333
    type: CustomRegex   preview: ne*********************************t
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:3333
    type: CustomRegex   preview: ne********************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:2652
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:2663
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3881
    type: CustomRegex   preview: ne***********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3870
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3881
    type: CustomRegex   preview: ne********************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3870
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:3333
    type: CustomRegex   preview: ne***********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova-public.d.ts:3322
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3318
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3329
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3076
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3112
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3123
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3125
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3150
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3161
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3164
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3125
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3076
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/auth-cordova.d.ts:3161
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7971
    type: CustomRegex   preview: us********************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7878
    type: CustomRegex   preview: us********************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7889
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7892
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7957
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7968
    type: CustomRegex   preview: us********************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7577
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7577
    type: CustomRegex   preview: us**********************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7588
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7590
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7577
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js:7577
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/src/core/strategies/email_and_password.d.ts:42
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/src/core/strategies/email_and_password.d.ts:44
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to********************************************g
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to******************************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to************************************************;
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js:5742
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js:5742
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js:5753
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js:5755
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js:5742
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js:5997
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js:5983
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js:5994
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/src/core/strategies/email_and_password.d.ts:42
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/src/core/strategies/email_and_password.d.ts:44
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to********************************************g
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to******************************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to************************************************;
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/index-f4676a0c.js:6760
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/index-f4676a0c.js:6771
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/index-f4676a0c.js:6773
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/index-f4676a0c.js:6760
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/index-f4676a0c.js:6760
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/src/core/strategies/email_and_password.d.ts:44
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/src/core/strategies/email_and_password.d.ts:42
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to********************************************g
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to******************************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to************************************************;
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth-compat/dist/firebase-auth.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth-compat/dist/firebase-auth.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth-compat/dist/firebase-auth.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth-compat/dist/firebase-auth.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/index.webworker.esm5.js:7763
    type: CustomRegex   preview: us**********************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/index.webworker.esm5.js:7774
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/index.webworker.esm5.js:7776
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/index.webworker.esm5.js:7763
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/browser-cjs/index-553d85d7.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/src/core/strategies/email_and_password.d.ts:42
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/src/core/strategies/email_and_password.d.ts:44
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to********************************************g
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to******************************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to************************************************;
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js:5707
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js:5718
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js:5720
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js:5707
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js:5707
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js:5962
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js:5948
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js:5959
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/cordova/popup_redirect-c351c83e.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/src/core/strategies/email_and_password.d.ts:42
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/src/core/strategies/email_and_password.d.ts:44
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to********************************************g
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to******************************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to************************************************;
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/totp-debd69bc.js:6715
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/totp-debd69bc.js:6726
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/totp-debd69bc.js:6728
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/totp-debd69bc.js:6715
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/totp-debd69bc.js:6715
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm2017/index-a694d6c6.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/index-f4676a0c.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/index-f4676a0c.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/index-f4676a0c.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js:6964
    type: CustomRegex   preview: us********************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js:6975
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js:6978
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js:6964
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/index-f4676a0c.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/index-f4676a0c.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/esm5/index-f4676a0c.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js:6663
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js:6663
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js:6663
    type: CustomRegex   preview: us**********************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js:6674
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js:6676
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js:6663
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node-esm/totp-0b2bfc5c.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/index.webworker.esm5.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/index.webworker.esm5.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/index.webworker.esm5.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/index.webworker.esm5.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/index.webworker.esm5.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/index.webworker.esm5.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/src/core/strategies/email_and_password.d.ts:42
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/src/core/strategies/email_and_password.d.ts:44
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to********************************************g
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to******************************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to************************************************;
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/src/core/strategies/email_and_password.d.ts:42
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/src/core/strategies/email_and_password.d.ts:44
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to********************************************g
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to******************************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to************************************************;
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js:5658
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js:5645
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js:5645
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js:5645
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js:5656
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/src/core/strategies/email_and_password.d.ts:42
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/src/core/strategies/email_and_password.d.ts:44
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to********************************************g
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to******************************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to************************************************;
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js:5900
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js:5886
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js:5897
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:2364
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/totp-debd69bc.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/totp-debd69bc.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:2400
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:2411
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:2413
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:2438
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:2449
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:2452
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/totp-debd69bc.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:3135
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:3146
    type: CustomRegex   preview: ne********************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:3135
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:3146
    type: CustomRegex   preview: ne***********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:3135
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:3146
    type: CustomRegex   preview: ne*********************************t
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:2411
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:2438
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:2452
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension-public.d.ts:2364
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/totp-debd69bc.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:3696
    type: CustomRegex   preview: ne********************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:3685
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:3685
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/totp-debd69bc.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:3696
    type: CustomRegex   preview: ne***********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:3685
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:3696
    type: CustomRegex   preview: ne*********************************t
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:2909
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:2898
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/node/totp-debd69bc.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:2860
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:2871
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:2873
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/auth-web-extension.d.ts:2824
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/rn/index-e030c65c.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js:5898
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js:5884
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js:5895
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js:5643
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js:5643
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js:5643
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js:5654
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js:5656
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us*******************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/src/core/strategies/email_and_password.d.ts:42
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/src/core/strategies/email_and_password.d.ts:44
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/src/core/strategies/email_and_password.d.ts:31
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/src/core/strategies/email_and_password.d.ts:44
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to********************************************g
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to******************************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to************************************************;
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/test/helpers/integration/helpers.d.ts:24
    type: CustomRegex   preview: to*****************************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-cjs/register-f18466d7.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/@firebase/auth/dist/web-extension-esm2017/register-7b7c68e6.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/@types/node/http.d.ts:1649
    type: URI   preview: ht***********************m
    first seen in commit: 05290a302808
  - node_modules/@types/node/https.d.ts:400
    type: URI   preview: ht************************m
    first seen in commit: 05290a302808
  - node_modules/@types/node/url.d.ts:730
    type: URI   preview: ht************************m
    first seen in commit: 05290a302808
  - node_modules/@types/node/url.d.ts:724
    type: URI   preview: ht************************m
    first seen in commit: 05290a302808
  - node_modules/@types/node/url.d.ts:565
    type: URI   preview: ht************************m
    first seen in commit: 05290a302808
  - node_modules/@types/node/url.d.ts:559
    type: URI   preview: ht************************m
    first seen in commit: 05290a302808
  - node_modules/@types/node/url.d.ts:559
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 05290a302808
  - node_modules/@types/node/url.d.ts:565
    type: CustomRegex   preview: 12****************************n
    first seen in commit: 05290a302808
  - node_modules/@types/node/url.d.ts:559
    type: CustomRegex   preview: xy****************************n
    first seen in commit: 05290a302808
  - node_modules/@types/node/url.d.ts:559
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 05290a302808
  - node_modules/@types/node/url.d.ts:565
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 05290a302808
  - node_modules/@types/node/url.d.ts:565
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 05290a302808
  - node_modules/faye-websocket/README.md:122
    type: CustomRegex   preview: ht*****************************************,
    first seen in commit: 05290a302808
  - node_modules/faye-websocket/README.md:122
    type: URI   preview: ht***************************************m
    first seen in commit: 05290a302808
  - node_modules/firebase/compat/index.d.ts:2839
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/firebase/compat/index.d.ts:2907
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/firebase/compat/index.d.ts:2895
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/firebase/compat/index.d.ts:2839
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/firebase/compat/index.d.ts:2907
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-compat.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-compat.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-compat.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-compat.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-web-extension.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-web-extension.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-web-extension.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-web-extension.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-web-extension.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-web-extension.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-cordova.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-cordova.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-cordova.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-cordova.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-cordova.js.map:1
    type: CustomRegex   preview: us****************************.
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-auth-cordova.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/websocket-driver/README.md:177
    type: URI   preview: ht***************************************m
    first seen in commit: 05290a302808
  - node_modules/websocket-driver/README.md:177
    type: CustomRegex   preview: ht******************************************,
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-compat.js.map:1
    type: CustomRegex   preview: us*********************************:
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-compat.js.map:1
    type: CustomRegex   preview: us****************************,
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-compat.js.map:1
    type: CustomRegex   preview: us*******************************d
    first seen in commit: 05290a302808
  - node_modules/firebase/firebase-compat.js.map:1
    type: CustomRegex   preview: us****************************y
    first seen in commit: 05290a302808

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

