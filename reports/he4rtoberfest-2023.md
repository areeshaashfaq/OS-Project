Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/vitorsantanna2/he4rtoberfest-2023

Flagged locations (secret values are not included):

  - challenges/4-emprestimo/rust/wellers0n/main:1737
    type: Wit   preview: MT*****************************T
    first seen in commit: 35d11af49682
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/https.d.ts:400
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/http.d.ts:1634
    type: URI   preview: ht***********************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/https.d.ts:400
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/http.d.ts:1634
    type: URI   preview: ht***********************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/http.d.ts:1634
    type: URI   preview: ht***********************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/https.d.ts:400
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/url.d.ts:688
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/url.d.ts:682
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/url.d.ts:517
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/url.d.ts:523
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/url.d.ts:517
    type: CustomRegex   preview: xy****************************n
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/url.d.ts:523
    type: CustomRegex   preview: 12****************************n
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/url.d.ts:517
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/url.d.ts:523
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/url.d.ts:517
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/ts4.8/url.d.ts:523
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/url.d.ts:517
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/url.d.ts:523
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/url.d.ts:517
    type: CustomRegex   preview: xy****************************n
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/url.d.ts:523
    type: CustomRegex   preview: 12****************************n
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/url.d.ts:517
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/url.d.ts:523
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/url.d.ts:523
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/url.d.ts:517
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/url.d.ts:688
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/node_modules/@types/node/url.d.ts:682
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/http.d.ts:1634
    type: URI   preview: ht***********************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/https.d.ts:400
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/url.d.ts:523
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/url.d.ts:517
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/url.d.ts:517
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/url.d.ts:523
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/url.d.ts:517
    type: CustomRegex   preview: xy****************************n
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/url.d.ts:523
    type: CustomRegex   preview: 12****************************n
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/url.d.ts:517
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/url.d.ts:523
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/url.d.ts:682
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/ts4.8/url.d.ts:688
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/url.d.ts:688
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/url.d.ts:682
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/url.d.ts:517
    type: CustomRegex   preview: xy****************************n
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/url.d.ts:523
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/url.d.ts:523
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/url.d.ts:517
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/url.d.ts:517
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/url.d.ts:523
    type: CustomRegex   preview: 12****************************n
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/url.d.ts:523
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef
  - challenges/1-cubo-simples/typescript/clintonrocha/node_modules/@types/node/url.d.ts:517
    type: URI   preview: ht************************m
    first seen in commit: c60d5e5f07ef

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

