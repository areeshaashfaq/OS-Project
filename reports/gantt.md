Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/amatevosyan-github/gantt

Flagged locations (secret values are not included):

  - node_modules/@types/node/http.d.ts:1217
    type: URI   preview: ht***********************m
    first seen in commit: c0ed1677af96
  - node_modules/@types/node/https.d.ts:255
    type: URI   preview: ht************************m
    first seen in commit: c0ed1677af96
  - node_modules/@types/node/url.d.ts:675
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: c0ed1677af96
  - node_modules/@types/node/url.d.ts:510
    type: URI   preview: ht************************m
    first seen in commit: c0ed1677af96
  - node_modules/@types/node/url.d.ts:504
    type: URI   preview: ht************************m
    first seen in commit: c0ed1677af96
  - node_modules/@types/node/url.d.ts:510
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: c0ed1677af96
  - node_modules/@types/node/url.d.ts:504
    type: CustomRegex   preview: xy****************************n
    first seen in commit: c0ed1677af96
  - node_modules/@types/node/url.d.ts:510
    type: CustomRegex   preview: 12****************************n
    first seen in commit: c0ed1677af96
  - node_modules/@types/node/url.d.ts:675
    type: URI   preview: ht************************m
    first seen in commit: c0ed1677af96
  - node_modules/@types/node/url.d.ts:669
    type: CustomRegex   preview: xy*****************************;
    first seen in commit: c0ed1677af96
  - node_modules/@types/node/url.d.ts:510
    type: CustomRegex   preview: 12*****************************;
    first seen in commit: c0ed1677af96

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

