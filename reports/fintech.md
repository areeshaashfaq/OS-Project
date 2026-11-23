Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/WillisamJ/fintech

Flagged locations (secret values are not included):

  - .vscode/extensions/ritwickdey.liveserver-5.7.9/node_modules/apache-md5/package.json:9
    type: CustomRegex   preview: ge***********************************n
    first seen in commit: c210272f395c
  - .vscode/extensions/ritwickdey.liveserver-5.7.9/node_modules/apache-crypt/package.json:9
    type: CustomRegex   preview: ge***********************************n
    first seen in commit: c210272f395c
  - .vscode/extensions/ritwickdey.liveserver-5.7.9/node_modules/faye-websocket/README.md:122
    type: CustomRegex   preview: ht*****************************************,
    first seen in commit: c210272f395c
  - .vscode/extensions/ritwickdey.liveserver-5.7.9/node_modules/faye-websocket/README.md:122
    type: URI   preview: ht***************************************m
    first seen in commit: c210272f395c
  - .vscode/extensions/ritwickdey.liveserver-5.7.9/node_modules/hosted-git-info/index.js:118
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: c210272f395c
  - .vscode/extensions/ritwickdey.liveserver-5.7.9/node_modules/hosted-git-info/index.js:118
    type: URI   preview: ht**************************************m
    first seen in commit: c210272f395c
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/http.d.ts:1686
    type: URI   preview: ht***********************m
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/https.d.ts:393
    type: URI   preview: ht************************m
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/url.d.ts:565
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/url.d.ts:565
    type: URI   preview: ht************************m
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/url.d.ts:559
    type: URI   preview: ht************************m
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/url.d.ts:565
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/url.d.ts:559
    type: CustomRegex   preview: xy****************************n
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/url.d.ts:559
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/url.d.ts:559
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/url.d.ts:565
    type: CustomRegex   preview: 12****************************n
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/url.d.ts:730
    type: URI   preview: ht************************m
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/@types/node/url.d.ts:724
    type: URI   preview: ht************************m
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/pg-connection-string/README.md:20
    type: CustomRegex   preview: po******************************************1
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/pg-connection-string/README.md:20
    type: Postgres   preview: po******************************************1
    first seen in commit: a10e8a79adb2
  - Downloads/Greenfield-Solution-main/Greenfield-Solution-main/node_modules/pg-connection-string/README.md:43
    type: CustomRegex   preview: po***************************************>
    first seen in commit: a10e8a79adb2

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

