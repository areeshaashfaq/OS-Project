Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/reidwcoleman/eplnewshub.com

Flagged locations (secret values are not included):

  - live-scores.html:464
    type: RapidApi   preview: 01***********************************************3
    first seen in commit: dafc71095aef
  - fpl-team-builder.html:1315
    type: GoogleGeminiAPIKey   preview: AI************************************U
    first seen in commit: efd1924601ea
  - fpl-ai-assistant.html:690
    type: GoogleGeminiAPIKey   preview: AI************************************U
    first seen in commit: 89f9e7089d49
  - fpl-ai-assistant.html:690
    type: GoogleGeminiAPIKey   preview: AI************************************Y
    first seen in commit: 5a1b98e67d7a
  - fpl-ai-assistant.html:51
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 5a1b98e67d7a
  - epl-predictor-game.html:1296
    type: RapidApi   preview: 01***********************************************3
    first seen in commit: b96f4f33cd84
  - live-scores-widget.html:466
    type: RapidApi   preview: 01***********************************************3
    first seen in commit: 1f99322c5570
  - (unknown file):2
    type: CustomRegex   preview: re******************************************,
    first seen in commit: eb0781b3358c
  - (unknown file):12
    type: CustomRegex   preview: no**************************************,
    first seen in commit: eb0781b3358c
  - (unknown file):1
    type: CustomRegex   preview: re******************************************,
    first seen in commit: eb0781b3358c
  - mobile/articles/exclusive-arsenal-transfer-insider-07-25-2025.html:76
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 7d60a85dd17a
  - (unknown file):1
    type: CustomRegex   preview: re****************************************s
    first seen in commit: ce70bfa55314
  - (unknown file):39
    type: CustomRegex   preview: no***************************************s
    first seen in commit: ce70bfa55314
  - (unknown file):1
    type: CustomRegex   preview: re***********************************g
    first seen in commit: ce70bfa55314
  - (unknown file):2
    type: CustomRegex   preview: re***********************************g
    first seen in commit: ce70bfa55314
  - (unknown file):39
    type: CustomRegex   preview: no**********************************g
    first seen in commit: ce70bfa55314
  - (unknown file):1
    type: CustomRegex   preview: re************************************h
    first seen in commit: ce70bfa55314
  - (unknown file):39
    type: CustomRegex   preview: no***********************************h
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:163
    type: CustomRegex   preview: jo*****************************g
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:163
    type: CustomRegex   preview: jo*************************************:
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:163
    type: CustomRegex   preview: jo******************************************'
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:47
    type: CustomRegex   preview: us*************************************:
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:163
    type: CustomRegex   preview: jo****************************s
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:47
    type: CustomRegex   preview: us****************************s
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:163
    type: CustomRegex   preview: jo**********************************n
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:47
    type: CustomRegex   preview: us******************************h
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:163
    type: CustomRegex   preview: jo******************************h
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:163
    type: CustomRegex   preview: jo********************************:
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:47
    type: CustomRegex   preview: us******************************************'
    first seen in commit: ce70bfa55314
  - create-account.html:274
    type: CustomRegex   preview: yo**************************************************;
    first seen in commit: ce70bfa55314
  - create-account.html:274
    type: CustomRegex   preview: yo*******************************n
    first seen in commit: ce70bfa55314
  - create-account.html:274
    type: CustomRegex   preview: yo*******************************************;
    first seen in commit: ce70bfa55314
  - signin.html:245
    type: CustomRegex   preview: yo****************************r
    first seen in commit: ce70bfa55314
  - signin.html:245
    type: CustomRegex   preview: yo****************************r
    first seen in commit: ce70bfa55314
  - signin.html:245
    type: CustomRegex   preview: yo*****************************************************************;
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:47
    type: CustomRegex   preview: us********************************:
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:47
    type: CustomRegex   preview: us*****************************g
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:179
    type: CustomRegex   preview: jo*****************************g
    first seen in commit: ce70bfa55314
  - AUTH_SETUP.md:47
    type: CustomRegex   preview: us**********************************n
    first seen in commit: ce70bfa55314
  - .env:15
    type: Stripe   preview: sk********************************************************************************************************x
    first seen in commit: ef22e1a9580e
  - epl-predictor-game.html:741
    type: GoogleGeminiAPIKey   preview: AI************************************g
    first seen in commit: 2fdb70aa657c
  - account-old.html:32
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 88fe9cece8da
  - create-account-old.html:32
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 88fe9cece8da
  - signin-old.html:32
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 88fe9cece8da
  - membership-old.html:32
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 36e4773bc6a2
  - (unknown file):28
    type: CustomRegex   preview: no**********************************g
    first seen in commit: b4da6cbb497a
  - hf-proxy-server.js:12
    type: HuggingFace   preview: hf**********************************m
    first seen in commit: 1e135c29d25d
  - fpl-ai-assistant.html:2522
    type: HuggingFace   preview: hf**********************************m
    first seen in commit: e5a62770cb3b
  - fpl-ai-huggingface-token.js:10
    type: HuggingFace   preview: hf**********************************m
    first seen in commit: bb44d1938a02
  - .ollama/id_ed25519:1
    type: PrivateKey   preview: --***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 535d82c9adcd
  - fpl-ai-huggingface-token.js:10
    type: HuggingFace   preview: hf**********************************m
    first seen in commit: 1b706b3cfa34
  - fpl-ai-assistant-backup.html:35
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0200056d63c6
  - fpl-ai-assistant.html:791
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0200056d63c6
  - .claude/projects/-home-reidwcoleman/50bc19f8-507a-41bf-9b9f-05e8e8482673.jsonl:12
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 176b3d2dde34
  - .claude/projects/-home-reidwcoleman/50bc19f8-507a-41bf-9b9f-05e8e8482673.jsonl:43
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 176b3d2dde34
  - .claude/projects/-home-reidwcoleman/50bc19f8-507a-41bf-9b9f-05e8e8482673.jsonl:34
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 176b3d2dde34
  - .claude/projects/-home-reidwcoleman/50bc19f8-507a-41bf-9b9f-05e8e8482673.jsonl:57
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 176b3d2dde34
  - .claude/projects/-home-reidwcoleman/7c00e7cc-9b87-4564-95cb-0015d2aed892.jsonl:94
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 370476bb325a
  - .claude/projects/-home-reidwcoleman/7c00e7cc-9b87-4564-95cb-0015d2aed892.jsonl:70
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: d834606ed00e
  - .claude/projects/-home-reidwcoleman/7c00e7cc-9b87-4564-95cb-0015d2aed892.jsonl:29
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 80d425b042fb
  - .claude/projects/-home-reidwcoleman/7c00e7cc-9b87-4564-95cb-0015d2aed892.jsonl:44
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 80d425b042fb
  - .claude/projects/-home-reidwcoleman/3ffad597-979b-4a57-a7de-767ed42e92d1.jsonl:152
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/3ffad597-979b-4a57-a7de-767ed42e92d1.jsonl:189
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/3ffad597-979b-4a57-a7de-767ed42e92d1.jsonl:192
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:80
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:70
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:82
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:92
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:121
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:105
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:104
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:176
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:184
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:177
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:193
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:202
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/405a738a-4fed-40c1-b749-fc3bfa3a204e.jsonl:201
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/c0f6d29d-f4dd-4438-8bf4-648d6311182b.jsonl:1273
    type: RailwayApp   preview: e1*********************************2
    first seen in commit: 8c245dc94268
  - .claude/projects/-home-reidwcoleman/c0f6d29d-f4dd-4438-8bf4-648d6311182b.jsonl:1332
    type: Heroku   preview: 14*********************************8
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/05/d5/635a7af582601b566438ce9bf19c230786be35c29d83a021aa05d9cf72e0d84e8c8db362c82e5527d59fe0f41b0fc88d8a94816411e54f0944b6fe45fdd4:1
    type: Box   preview: iU*****************************Y
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/0c/5c/780553dfd5b81df2bae7909c6d0794a6e23505a6467cdb42cad58a7097c28f4c7b83cf4a1c9696f43034f0a16a45d68da1547df4fc52cf34f7228b683e03:1
    type: TLy   preview: nD*********************************************************7
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/6b/39/596a1405493f0bd92571dccf56f46fe3a6c58da79ff0fc35ba16401613d92ea17730ce5c7a13b38e0ce423897a7c1a72df75e926a300f073de0167367b13:1
    type: Box   preview: ng*****************************s
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/79/df/57866e01fd7410aac658abdede4042b9a679ea25a80a3d4e6faf66c14f8441b88105500e55f47c9a4d657d453db51aedb25fdd83f533a1dffd4f6c1bc8fd:1
    type: TLy   preview: GD*********************************************************M
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/90/d8/8aaf15fb2f26e0fc890330abab946cce1570b8f271366b7b4908a3fa3c611901b942fda941beae5851aceea3153bc7137ca0a7c45000f9ff62cd13538ab7:1
    type: Box   preview: mV*****************************5
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/96/ca/c59a3235d62bec884f82bffd8dad88572d65f9f02b8e3fdfe7a77265e74bcf5b729a699f76867d7bec299e4b332eee9115c8bbd1b61a1d97f9c1124d01ae:1
    type: Box   preview: zw*****************************C
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/91/3b/3cd8eef054d0f5b09985c3c036f10c020b09fd846786bc00a1712daccee0c25021853210dd677b73bcd3d19ab4bcd045ce2b99401ebff78689061fdceed9:1
    type: Qase   preview: Av*************************************C
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/af/d1/f3911306fa87e2e8bc201439d50595252620ff0cc7b526dbf2f00b1b3d5af856a08a0f3cd7f3ebd13cddf14421669a7695a5c56601c327f226533ca2c332:1
    type: Box   preview: 1A*****************************c
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/99/9f/0be753727a45c5146bdb88b1d3a4a0c0a5f5859a5995e50660cb2d9db20f7aa4215acac62e1b51725aef343bc3ff387d849f167822788026b5d08980698d:1
    type: Box   preview: IG*****************************4
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:1294
    type: URI   preview: ht***********************m
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:382
    type: URI   preview: ht************************m
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:468
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:474
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:468
    type: CustomRegex   preview: xy****************************n
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:474
    type: CustomRegex   preview: 12****************************n
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:468
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:474
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:474
    type: URI   preview: ht************************m
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:633
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:468
    type: URI   preview: ht************************m
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/de/82/5b181516b92e9a8529c4ab578dd97ac2c9fe18b1623c3b20afa3b73ae33409369964de63bce2de77a3c95f4e4fb68e2e7d839c9c7dceaa4377dd1e5887b8:639
    type: URI   preview: ht************************m
    first seen in commit: 8c245dc94268
  - .npm/_cacache/content-v2/sha512/ee/b2/94cb2df7435c9cf7ca50d430262edc17d74f45ed321f5a55b561da3c5a5d628b549e1e279e8741c77cf78bd9f3172bacf4b3c79c2acf5fac2b8b26f9dd06:12
    type: CustomRegex   preview: ur****************************3
    first seen in commit: 8c245dc94268
  - .npm/_cacache/index-v5/ca/c1/e5aa41301fa6d75f129f6a1f5bc541dd78b4616140bf23a8847858ea538c:2
    type: Vercel   preview: If*********************z
    first seen in commit: 8c245dc94268
  - .npm/_cacache/index-v5/fe/60/745135e99dd78c6f1d7d0dde5e952d4fc0adaf408cdcf4a62a59a4257dea:2
    type: Vercel   preview: L9*********************n
    first seen in commit: 8c245dc94268
  - articles/exclusive-arsenal-transfer-insider-07-25-2025.html.backup:28
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8c877e2aef7e
  - node_modules/@vercel/node/node_modules/@types/node/http.d.ts:1294
    type: URI   preview: ht***********************m
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/https.d.ts:382
    type: URI   preview: ht************************m
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/ts4.8/http.d.ts:1294
    type: URI   preview: ht***********************m
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/ts4.8/https.d.ts:382
    type: URI   preview: ht************************m
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/ts4.8/url.d.ts:639
    type: URI   preview: ht************************m
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/ts4.8/url.d.ts:639
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/ts4.8/url.d.ts:474
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/ts4.8/url.d.ts:468
    type: CustomRegex   preview: xy****************************n
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/ts4.8/url.d.ts:474
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/ts4.8/url.d.ts:474
    type: CustomRegex   preview: 12****************************n
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/ts4.8/url.d.ts:468
    type: URI   preview: ht************************m
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/ts4.8/url.d.ts:474
    type: URI   preview: ht************************m
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/ts4.8/url.d.ts:633
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/url.d.ts:474
    type: URI   preview: ht************************m
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/url.d.ts:639
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/url.d.ts:468
    type: URI   preview: ht************************m
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/url.d.ts:474
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/url.d.ts:468
    type: CustomRegex   preview: xy****************************n
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/url.d.ts:474
    type: CustomRegex   preview: 12****************************n
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/url.d.ts:633
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/url.d.ts:474
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/url.d.ts:639
    type: URI   preview: ht************************m
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/url.d.ts:633
    type: CustomRegex   preview: xy****************************n
    first seen in commit: 517aab6d25cf
  - node_modules/@vercel/node/node_modules/@types/node/url.d.ts:468
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 517aab6d25cf
  - node_modules/uri-js/README.md:12
    type: CustomRegex   preview: ur****************************3
    first seen in commit: 517aab6d25cf
  - .claude/projects/-home-reidwcoleman/1e87cc11-bb3d-473a-8795-bb91341fb851.jsonl:326
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/1e87cc11-bb3d-473a-8795-bb91341fb851.jsonl:335
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/1e87cc11-bb3d-473a-8795-bb91341fb851.jsonl:330
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/1e87cc11-bb3d-473a-8795-bb91341fb851.jsonl:340
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/1e87cc11-bb3d-473a-8795-bb91341fb851.jsonl:328
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/c0f6d29d-f4dd-4438-8bf4-648d6311182b.jsonl:999
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/c0f6d29d-f4dd-4438-8bf4-648d6311182b.jsonl:1024
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/c0f6d29d-f4dd-4438-8bf4-648d6311182b.jsonl:1033
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/c0f6d29d-f4dd-4438-8bf4-648d6311182b.jsonl:1039
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/c0f6d29d-f4dd-4438-8bf4-648d6311182b.jsonl:1021
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/c0f6d29d-f4dd-4438-8bf4-648d6311182b.jsonl:1131
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/c0f6d29d-f4dd-4438-8bf4-648d6311182b.jsonl:1018
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 72e9c8340cb0
  - .claude/projects/-home-reidwcoleman/17476474-acf0-4459-9c25-8cd6529886c4.jsonl:305
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/1e87cc11-bb3d-473a-8795-bb91341fb851.jsonl:24
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/1e87cc11-bb3d-473a-8795-bb91341fb851.jsonl:69
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/1e87cc11-bb3d-473a-8795-bb91341fb851.jsonl:59
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/26ccdcb9-2d03-42f9-8c11-19d01f207613.jsonl:21
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/4b24ae67-dd77-44ae-bade-77fa3871357a.jsonl:716
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/4b24ae67-dd77-44ae-bade-77fa3871357a.jsonl:742
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/4b24ae67-dd77-44ae-bade-77fa3871357a.jsonl:734
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:85
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:82
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:329
    type: CustomRegex   preview: re*********************************************n
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:555
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:564
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:590
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:629
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:558
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:635
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:593
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:632
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:608
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:605
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:611
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:717
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:725
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:721
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/70891467-527c-4135-b192-d11110444196.jsonl:727
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/8368b9b3-6699-4598-97fa-1d593574131a.jsonl:104
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/8368b9b3-6699-4598-97fa-1d593574131a.jsonl:125
    type: CustomRegex   preview: re********************************************+
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/972a28c3-8521-47d3-b7d5-0bbcf61ffbbe.jsonl:10
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/972a28c3-8521-47d3-b7d5-0bbcf61ffbbe.jsonl:28
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/972a28c3-8521-47d3-b7d5-0bbcf61ffbbe.jsonl:39
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/972a28c3-8521-47d3-b7d5-0bbcf61ffbbe.jsonl:36
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/972a28c3-8521-47d3-b7d5-0bbcf61ffbbe.jsonl:47
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/972a28c3-8521-47d3-b7d5-0bbcf61ffbbe.jsonl:73
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/972a28c3-8521-47d3-b7d5-0bbcf61ffbbe.jsonl:33
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/972a28c3-8521-47d3-b7d5-0bbcf61ffbbe.jsonl:50
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/972a28c3-8521-47d3-b7d5-0bbcf61ffbbe.jsonl:76
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/a6c14747-ede7-40ce-8854-0476acc0ecc7.jsonl:195
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/a6c14747-ede7-40ce-8854-0476acc0ecc7.jsonl:194
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/a6c14747-ede7-40ce-8854-0476acc0ecc7.jsonl:200
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/a6c14747-ede7-40ce-8854-0476acc0ecc7.jsonl:203
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/a6c14747-ede7-40ce-8854-0476acc0ecc7.jsonl:206
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/cd20ae52-66d5-4a65-9006-01422e6d077c.jsonl:30
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/d966a304-c30a-48a2-9a4e-2be8ffa6c060.jsonl:84
    type: CustomRegex   preview: re********************************************+
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/fa591333-5107-4a15-8210-ad151fcf6805.jsonl:179
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .claude/projects/-home-reidwcoleman/fa591333-5107-4a15-8210-ad151fcf6805.jsonl:176
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:1774
    type: URI   preview: ht***********************m
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:395
    type: URI   preview: ht************************m
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:728
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:728
    type: URI   preview: ht************************m
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:722
    type: URI   preview: ht************************m
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:557
    type: URI   preview: ht************************m
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:563
    type: URI   preview: ht************************m
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:563
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:557
    type: CustomRegex   preview: xy****************************n
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:563
    type: CustomRegex   preview: 12****************************n
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:722
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0d/18/792be91ae5e26273c0a31fbb5df10a58115e99a35d207d19231c23b7c1ea991d60ed01a49316d978f9532a389e0de6372e859f7f97ecb2f2b560c3b05079:563
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:391
    type: Box   preview: a9*****************************e
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:392
    type: Box   preview: 60*****************************d
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:389
    type: Box   preview: 5c*****************************2
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:390
    type: Box   preview: 12*****************************f
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:910
    type: Diffbot   preview: 8c*****************************7
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:972
    type: Box   preview: 2c*****************************b
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:2067
    type: Box   preview: 0b*****************************4
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:3204
    type: Box   preview: bf*****************************d
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:3203
    type: Box   preview: 0b*****************************6
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:3540
    type: Box   preview: ee*****************************1
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:2898
    type: PostageApp   preview: f5*****************************b
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:1236
    type: Flickr   preview: 3c*****************************e
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:1234
    type: Flickr   preview: d3*****************************b
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:1235
    type: Flickr   preview: 66*****************************3
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/13/e8/abb8d398f1557db382446ded5a3449ba322b333d1aff51f707333d13421d415d2c472be01257547a5b81e98c1852792fb9e0f22c00c0819b00f4e8b2eca9:2995
    type: Box   preview: 88*****************************9
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/0b/62/d4ec1943932470b78ef79761e4f066d68cffe0d6fa6429a32ea2fccc68638f0d9acff1cc60b6d78370371e4d9bd5ced0986300c441337c8abab77fc646c4:1
    type: Box   preview: Zc*****************************r
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/29/94/68ae441458cb6a938b1933cb2f18b145eb5d4c98311b0d8db971c3598196443d1df29fad459d8889c2f9199b36ec489054eb1131810fe5c4d4bb26e2c139:1
    type: TLy   preview: nB*********************************************************R
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/39/cd/4356e419fc3c0d8594f2bbfd0ef3087c6ff38f55412f2a02bf4bdff8ffebb973e82615344e4c34c491f43966ef4f694b6f8f91ecaab8cf80cff306681089:1
    type: Sirv   preview: \r*************************************************************************************d
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/4a/14/f6a05419d3302f4a0c49bb11d0e1e155699434fd8194b88c3e09b4db5b17581cc3e6e8f54f667851a297f8a8e40bde895d3bb44e14ec364daca67b8db80c:1
    type: Box   preview: Zc*****************************r
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/49/ee/359e4b86c8df202c038b67025aa50fb251b6e1c53d592d33d0f68e6260607a04cabbd7ff922d703ca3cd2c2b8382577a24882a2917dcd4d0cf17ab67d68a:1
    type: Box   preview: 2l*****************************W
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/54/6f/836aac081dde2b45646103888b61e03cfa306cba5b72b39bcde444432c43d9fafc36903b1d134ebe006bd638fbd4eeebcbf660f94b43dbfa52d5b27a9c6b:1
    type: Box   preview: ze*****************************d
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/69/e3/dbc4399c616fbe3daa81b09f8761417009dbf82d5bdd9e1072efc139ecf228afcfce56f84cac00c51440e1f031c3151bff3bd8b794f86c10d8ceed05f4f8:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/93/20/ae10e5a326a66e0db447ccbf15f77373421c0807bd681564b2cd5a3e28f648fa99d03cfc6e71d92b399be42d19eb7f9511b1033e209d3d0f0dbd71100b20:199
    type: CustomRegex   preview: pr****************************************r
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/9b/12/0301bf4bb26e83a0e27bc47fb9f97e32d4b53fe078b9d0bf42e6c22cc0adc9cd42d2e1bc24d45be374182f611e1bcd3e2db944220b5e451367f91db2ef63:118
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/9b/12/0301bf4bb26e83a0e27bc47fb9f97e32d4b53fe078b9d0bf42e6c22cc0adc9cd42d2e1bc24d45be374182f611e1bcd3e2db944220b5e451367f91db2ef63:118
    type: URI   preview: ht**************************************m
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/ae/f1/61717df71f301e0a353a807fcaee6bba190c82ed429fa8d804c94ae0b9845b043e1f10e13abe6f18757c3f0d1afd16900a21436186cab61fdea61097fda7:1
    type: TLy   preview: nJ*********************************************************D
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/b3/b0/32ef64c95a0c9f21943a50275ccd408ac5cb47a223bafe5bb546749834741097eace65ff93495f5c285bf64540bdf214ab8cfff51ed6a0e1548c3b261a1b:1
    type: Box   preview: IG*****************************4
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/dc/74/ba5f31bd25cb5805c4cde5d328a27914eb641d00493192a7e585e22fd8c8efb20484b1bdd53f5eaf46fe82baba89bf260aa0f1b7c914ca6ab074e47dd624:1
    type: Box   preview: 7u*****************************A
    first seen in commit: 0926c6d02c81
  - .npm/_cacache/content-v2/sha512/d2/92/3f6df0355835af98a82b1e33ba34e327b7e0f2eb49537f09bd00f3bc4e871405eae91eac25f75eac5899643a953254ae9ec6c81fdd2a4947bc1614dd0642:1
    type: Box   preview: iU*****************************Y
    first seen in commit: 0926c6d02c81
  - .npm/_libvips/libvips-8.14.5-linux-x64.tar.br:20
    type: CustomRegex   preview: st******************************************,
    first seen in commit: 0926c6d02c81
  - .npm/_libvips/libvips-8.14.5-linux-x64.tar.br:20
    type: CustomRegex   preview: st*******************************************;
    first seen in commit: 0926c6d02c81
  - .npm/_libvips/libvips-8.14.5-linux-x64.tar.br:20
    type: CustomRegex   preview: st***********************************************************e
    first seen in commit: 0926c6d02c81
  - .npm/_libvips/libvips-8.14.5-linux-x64.tar.br:20
    type: CustomRegex   preview: st**************************************,
    first seen in commit: 0926c6d02c81
  - .npm/_libvips/libvips-8.14.5-linux-x64.tar.br:20
    type: CustomRegex   preview: st***************************************;
    first seen in commit: 0926c6d02c81
  - node_modules/@types/node/http.d.ts:1774
    type: URI   preview: ht***********************m
    first seen in commit: 060a8c57fbf5
  - node_modules/@types/node/https.d.ts:395
    type: URI   preview: ht************************m
    first seen in commit: 060a8c57fbf5
  - node_modules/@types/node/url.d.ts:728
    type: URI   preview: ht************************m
    first seen in commit: 060a8c57fbf5
  - node_modules/@types/node/url.d.ts:722
    type: URI   preview: ht************************m
    first seen in commit: 060a8c57fbf5
  - node_modules/@types/node/url.d.ts:563
    type: URI   preview: ht************************m
    first seen in commit: 060a8c57fbf5
  - node_modules/@types/node/url.d.ts:563
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 060a8c57fbf5
  - node_modules/@types/node/url.d.ts:557
    type: URI   preview: ht************************m
    first seen in commit: 060a8c57fbf5
  - node_modules/@types/node/url.d.ts:563
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: 060a8c57fbf5
  - node_modules/@types/node/url.d.ts:557
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 060a8c57fbf5
  - node_modules/@types/node/url.d.ts:557
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: 060a8c57fbf5
  - node_modules/@types/node/url.d.ts:563
    type: CustomRegex   preview: 12****************************n
    first seen in commit: 060a8c57fbf5
  - node_modules/@types/node/url.d.ts:557
    type: CustomRegex   preview: xy****************************n
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:392
    type: Box   preview: 60*****************************d
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:389
    type: Box   preview: 5c*****************************2
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:390
    type: Box   preview: 12*****************************f
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:391
    type: Box   preview: a9*****************************e
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:2067
    type: Box   preview: 0b*****************************4
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:2995
    type: Box   preview: 88*****************************9
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:2898
    type: PostageApp   preview: f5*****************************b
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:910
    type: Diffbot   preview: 8c*****************************7
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:972
    type: Box   preview: 2c*****************************b
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:1236
    type: Flickr   preview: 3c*****************************e
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:1234
    type: Flickr   preview: d3*****************************b
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:1235
    type: Flickr   preview: 66*****************************3
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:3540
    type: Box   preview: ee*****************************1
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:3204
    type: Box   preview: bf*****************************d
    first seen in commit: 060a8c57fbf5
  - node_modules/JSONStream/test/fixtures/all_npm.json:3203
    type: Box   preview: 0b*****************************6
    first seen in commit: 060a8c57fbf5
  - node_modules/hosted-git-info/index.js:199
    type: CustomRegex   preview: pr****************************************r
    first seen in commit: 060a8c57fbf5
  - node_modules/meow/node_modules/hosted-git-info/index.js:118
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 060a8c57fbf5
  - node_modules/meow/node_modules/hosted-git-info/index.js:118
    type: URI   preview: ht**************************************m
    first seen in commit: 060a8c57fbf5
  - node_modules/read-pkg/node_modules/hosted-git-info/index.js:118
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 060a8c57fbf5
  - node_modules/read-pkg/node_modules/hosted-git-info/index.js:118
    type: URI   preview: ht**************************************m
    first seen in commit: 060a8c57fbf5
  - node_modules/replace/node_modules/yargs/CHANGELOG.md:164
    type: GitHubOauth2   preview: sh*****************t
    first seen in commit: 060a8c57fbf5
  - .claude.json:53
    type: CustomRegex   preview: re****************************************,
    first seen in commit: b2766a3f20d1
  - .claude.json.backup:49
    type: CustomRegex   preview: re****************************************,
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:451
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:468
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:456
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:473
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:458
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:590
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:460
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:596
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:631
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:618
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:632
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:649
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:630
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:802
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:858
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:860
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/4e4129ed-e275-4c13-ba4b-404c7eae9bf9.jsonl:852
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:5
    type: CustomRegex   preview: re******************************************************************************************************************************}
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:7
    type: CustomRegex   preview: re**************************************************************************n
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:7
    type: CustomRegex   preview: re***********************************************)
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:7
    type: CustomRegex   preview: re***********************************************n
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:8
    type: CustomRegex   preview: re***********************************************)
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:8
    type: CustomRegex   preview: re***********************************************n
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:8
    type: CustomRegex   preview: re**************************************************************************n
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:7
    type: CustomRegex   preview: re*******************************************.
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:45
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:50
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:47
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/6048111a-ab0b-48ca-a557-fb86eaed034c.jsonl:39
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/733695f7-6551-434c-9d3f-65ff8bfa1349.jsonl:28
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/733695f7-6551-434c-9d3f-65ff8bfa1349.jsonl:15
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/733695f7-6551-434c-9d3f-65ff8bfa1349.jsonl:18
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/841c8d3a-83a3-4e0c-867a-7e7f25156e23.jsonl:21
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/841c8d3a-83a3-4e0c-867a-7e7f25156e23.jsonl:29
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/841c8d3a-83a3-4e0c-867a-7e7f25156e23.jsonl:64
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/a6c14747-ede7-40ce-8854-0476acc0ecc7.jsonl:99
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/a6c14747-ede7-40ce-8854-0476acc0ecc7.jsonl:133
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .claude/projects/-home-reidwcoleman/a6c14747-ede7-40ce-8854-0476acc0ecc7.jsonl:135
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: b2766a3f20d1
  - .ssh/id_ed25519:1
    type: PrivateKey   preview: --*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: b2766a3f20d1
  - fpl-ai-assistant.html:33
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0454e1b7be1d
  - fpl-premium-hub.html:81
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0454e1b7be1d
  - dev-config.js:55
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 99e92930a428
  - developer-signin.html:293
    type: CustomRegex   preview: re************************************************************************;
    first seen in commit: f2429060a3e7
  - developer-signin.html:293
    type: CustomRegex   preview: re*******************************************;
    first seen in commit: f2429060a3e7
  - developer-signin.html:293
    type: CustomRegex   preview: re***********************************************)
    first seen in commit: f2429060a3e7
  - create-account.html:31
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0a2a4ba1e827
  - signin.html:31
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0a2a4ba1e827
  - (unknown file):2
    type: CustomRegex   preview: re***********************************n
    first seen in commit: 701b0690c97d
  - (unknown file):18
    type: CustomRegex   preview: no**********************************n
    first seen in commit: 701b0690c97d
  - (unknown file):1
    type: CustomRegex   preview: re***********************************n
    first seen in commit: 701b0690c97d
  - GOOGLE_SIGNIN_SETUP.md:135
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 88eff7b9283d
  - GOOGLE_SIGNIN_SETUP.md:151
    type: CustomRegex   preview: us********************************
    first seen in commit: 88eff7b9283d
  - GOOGLE_SIGNIN_SETUP.md:151
    type: CustomRegex   preview: us******************************r
    first seen in commit: 88eff7b9283d
  - google-signin-test.html:16
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 88eff7b9283d
  - fantasy.html:32
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 70f0bc97da9d
  - fpl.html:30
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 33f3594113e6
  - fantasy.html:32
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: a49afe53896c
  - membership-success.html:15
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: d7fa13275d52
  - premium.html:28
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: cf8acec7d4f7
  - account.html:28
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: cf8acec7d4f7
  - create-account.html:31
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8a28c38e71a7
  - signin.html:31
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 8a28c38e71a7
  - articles/exclusive-arsenal-transfer-insider-07-25-2025.html:28
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0dead84cdc2f
  - membership.html:29
    type: GoogleGeminiAPIKey   preview: AI************************************I
    first seen in commit: 0dead84cdc2f
  - (unknown file):1
    type: CustomRegex   preview: re************************************h
    first seen in commit: a0bddd71deb4
  - (unknown file):1
    type: CustomRegex   preview: re************************************h
    first seen in commit: a0bddd71deb4
  - (unknown file):24
    type: CustomRegex   preview: no***************************************n
    first seen in commit: a0bddd71deb4
  - (unknown file):24
    type: CustomRegex   preview: no***********************************h
    first seen in commit: a0bddd71deb4
  - (unknown file):24
    type: CustomRegex   preview: no***********************************h
    first seen in commit: a0bddd71deb4
  - (unknown file):24
    type: CustomRegex   preview: no*****************************************n
    first seen in commit: a0bddd71deb4
  - (unknown file):1
    type: CustomRegex   preview: re******************************************n
    first seen in commit: a0bddd71deb4
  - (unknown file):2
    type: CustomRegex   preview: re******************************************n
    first seen in commit: a0bddd71deb4
  - (unknown file):1
    type: CustomRegex   preview: re****************************************n
    first seen in commit: a0bddd71deb4
  - node_modules/json5/README.md:14
    type: GitHubOauth2   preview: 8e*****************1
    first seen in commit: 807a81158f6b
  - node_modules/json5/README.md:14
    type: GitHubOauth2   preview: 8e*****************1
    first seen in commit: 807a81158f6b
  - node_modules/bcrypt/src/bcrypt.cc:20
    type: CustomRegex   preview: dm***************************g
    first seen in commit: 4127e147a8cc
  - (unknown file):1
    type: CustomRegex   preview: re***********************************g
    first seen in commit: d2411b731a50
  - (unknown file):37
    type: CustomRegex   preview: no**********************************g
    first seen in commit: d2411b731a50
  - (unknown file):37
    type: CustomRegex   preview: no***********************************h
    first seen in commit: d2411b731a50
  - (unknown file):1
    type: CustomRegex   preview: re************************************h
    first seen in commit: d2411b731a50
  - (unknown file):2
    type: CustomRegex   preview: re************************************h
    first seen in commit: d2411b731a50
  - SETUP.md:59
    type: CustomRegex   preview: jo*********************************
    first seen in commit: d2411b731a50
  - SETUP.md:59
    type: CustomRegex   preview: jo*****************************g
    first seen in commit: d2411b731a50
  - SETUP.md:75
    type: CustomRegex   preview: jo******************************h
    first seen in commit: d2411b731a50
  - SETUP.md:59
    type: CustomRegex   preview: jo******************************h
    first seen in commit: d2411b731a50
  - SETUP.md:130
    type: CustomRegex   preview: jo******************************h
    first seen in commit: d2411b731a50
  - euro_final.html:39
    type: AzureSasToken   preview: ht***************************************************************************************************g
    first seen in commit: d2103a270049
  - Euro 2024 Final Preview_ Key.html:1
    type: AzureSasToken   preview: ht***************************************************************************************************g
    first seen in commit: 9586077d459f

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

