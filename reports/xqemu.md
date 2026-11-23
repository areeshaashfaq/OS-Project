Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/isafadi/xqemu

Flagged locations (secret values are not included):

  - tests/qemu-iotests/common.tls:39
    type: PrivateKey   preview: --**********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: a46b68410669
  - (unknown file):19
    type: CustomRegex   preview: mj**************************.
    first seen in commit: 2c42f1e80103
  - (unknown file):15
    type: CustomRegex   preview: an*************************************.
    first seen in commit: 2c42f1e80103
  - (unknown file):16
    type: CustomRegex   preview: pb*******************************.
    first seen in commit: 2c42f1e80103
  - (unknown file):20
    type: CustomRegex   preview: ar*****************************.
    first seen in commit: 2c42f1e80103
  - (unknown file):14
    type: CustomRegex   preview: Ia*************************************.
    first seen in commit: 2c42f1e80103
  - (unknown file):18
    type: CustomRegex   preview: be*******************************.
    first seen in commit: 2c42f1e80103
  - (unknown file):17
    type: CustomRegex   preview: ar*****************************.
    first seen in commit: 2c42f1e80103
  - (unknown file):2
    type: CustomRegex   preview: Ia*************************************.
    first seen in commit: 2c42f1e80103
  - (unknown file):1
    type: CustomRegex   preview: ia*************************************.
    first seen in commit: 2c42f1e80103
  - qemu-doc.texi:455
    type: CustomRegex   preview: ht***************************************m
    first seen in commit: e896d0f9ca6e
  - tests/keys/id_rsa:1
    type: PrivateKey   preview: --***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 57446e32acf7
  - (unknown file):2
    type: CustomRegex   preview: mr********************************g
    first seen in commit: 788cf9f8c8cb
  - (unknown file):1
    type: CustomRegex   preview: be**********************************g
    first seen in commit: 788cf9f8c8cb
  - (unknown file):13
    type: CustomRegex   preview: 20**********************************************************g
    first seen in commit: 788cf9f8c8cb
  - (unknown file):13
    type: CustomRegex   preview: be**********************************g
    first seen in commit: 788cf9f8c8cb
  - (unknown file):12
    type: CustomRegex   preview: be**********************************g
    first seen in commit: 788cf9f8c8cb
  - (unknown file):11
    type: CustomRegex   preview: mr********************************g
    first seen in commit: 788cf9f8c8cb
  - (unknown file):10
    type: CustomRegex   preview: be*******************************g
    first seen in commit: 788cf9f8c8cb
  - (unknown file):14
    type: CustomRegex   preview: mr********************************g
    first seen in commit: 788cf9f8c8cb
  - (unknown file):16
    type: CustomRegex   preview: kw*******************************d
    first seen in commit: 431714202092
  - (unknown file):1
    type: CustomRegex   preview: kw*******************************d
    first seen in commit: 431714202092
  - (unknown file):17
    type: CustomRegex   preview: jc*******************************d
    first seen in commit: 431714202092
  - (unknown file):15
    type: CustomRegex   preview: fa******************************d
    first seen in commit: 431714202092
  - (unknown file):2
    type: CustomRegex   preview: jc*******************************d
    first seen in commit: 431714202092
  - tests/qemu-iotests/149:18
    type: CustomRegex   preview: be********************************)
    first seen in commit: 6278ae035fbd
  - tests/qemu-iotests/149:18
    type: CustomRegex   preview: be*******************************:
    first seen in commit: 6278ae035fbd
  - (unknown file):15
    type: CustomRegex   preview: be**********************************g
    first seen in commit: 4ef130fca87b
  - (unknown file):16
    type: CustomRegex   preview: kw*******************************g
    first seen in commit: 4ef130fca87b
  - (unknown file):14
    type: CustomRegex   preview: eb********************************g
    first seen in commit: 4ef130fca87b
  - (unknown file):2
    type: CustomRegex   preview: kw*******************************g
    first seen in commit: 4ef130fca87b
  - (unknown file):1
    type: CustomRegex   preview: be**********************************g
    first seen in commit: 4ef130fca87b
  - (unknown file):12
    type: CustomRegex   preview: eb*****************************.
    first seen in commit: 6a11d5183fb7
  - (unknown file):1
    type: CustomRegex   preview: be*******************************.
    first seen in commit: 6a11d5183fb7
  - (unknown file):11
    type: CustomRegex   preview: be*******************************.
    first seen in commit: 6a11d5183fb7
  - (unknown file):2
    type: CustomRegex   preview: kw****************************.
    first seen in commit: 6a11d5183fb7
  - (unknown file):13
    type: CustomRegex   preview: kw****************************.
    first seen in commit: 6a11d5183fb7
  - (unknown file):12
    type: CustomRegex   preview: eb*****************************d
    first seen in commit: d57e4e482e39
  - (unknown file):13
    type: CustomRegex   preview: kw****************************d
    first seen in commit: d57e4e482e39
  - (unknown file):2
    type: CustomRegex   preview: kw****************************d
    first seen in commit: d57e4e482e39
  - (unknown file):11
    type: CustomRegex   preview: be*******************************d
    first seen in commit: d57e4e482e39
  - (unknown file):1
    type: CustomRegex   preview: be*******************************d
    first seen in commit: d57e4e482e39
  - (unknown file):2
    type: CustomRegex   preview: md*************************************e
    first seen in commit: 215a2771a7b6
  - (unknown file):2
    type: CustomRegex   preview: md**************************************,
    first seen in commit: 215a2771a7b6
  - (unknown file):1
    type: CustomRegex   preview: be********************************d
    first seen in commit: 215a2771a7b6
  - (unknown file):1
    type: CustomRegex   preview: be*******************************e
    first seen in commit: 215a2771a7b6
  - (unknown file):1
    type: CustomRegex   preview: be********************************,
    first seen in commit: 215a2771a7b6
  - (unknown file):2
    type: CustomRegex   preview: md**************************************d
    first seen in commit: 215a2771a7b6
  - (unknown file):42
    type: CustomRegex   preview: be*******************************e
    first seen in commit: 215a2771a7b6
  - (unknown file):43
    type: CustomRegex   preview: md**************************************d
    first seen in commit: 215a2771a7b6
  - qemu-options.hx:2383
    type: CustomRegex   preview: ht***************************************m
    first seen in commit: 212aefaa53d1
  - (unknown file):2
    type: CustomRegex   preview: kr******************************t
    first seen in commit: cf864569cd91
  - (unknown file):13
    type: CustomRegex   preview: kr******************************t
    first seen in commit: cf864569cd91
  - (unknown file):1
    type: CustomRegex   preview: kr*************************************n
    first seen in commit: cf864569cd91
  - (unknown file):1
    type: CustomRegex   preview: kr******************************t
    first seen in commit: cf864569cd91
  - qemu-options.hx:2258
    type: CustomRegex   preview: ht***************************************m
    first seen in commit: 0a86cb731758
  - tests/qemu-iotests/nbd-fault-injector.py:41
    type: CustomRegex   preview: st*******************************************3
    first seen in commit: 1e8ece0db3e8
  - (unknown file):10
    type: CustomRegex   preview: kw****************************e
    first seen in commit: 8ae8e904fcba
  - (unknown file):2
    type: CustomRegex   preview: kw****************************e
    first seen in commit: 8ae8e904fcba
  - (unknown file):11
    type: CustomRegex   preview: eb*****************************e
    first seen in commit: 8ae8e904fcba
  - (unknown file):1
    type: CustomRegex   preview: kw****************************e
    first seen in commit: 8ae8e904fcba
  - (unknown file):10
    type: CustomRegex   preview: lc*************************************g
    first seen in commit: eef5ad108640
  - (unknown file):2
    type: CustomRegex   preview: lc*************************************g
    first seen in commit: eef5ad108640
  - (unknown file):11
    type: CustomRegex   preview: ar********************************g
    first seen in commit: eef5ad108640
  - (unknown file):1
    type: CustomRegex   preview: lc*************************************g
    first seen in commit: eef5ad108640
  - (unknown file):1
    type: CustomRegex   preview: pm*************************************n
    first seen in commit: 0f66998ff6d5
  - (unknown file):17
    type: CustomRegex   preview: al***************************************n
    first seen in commit: 0f66998ff6d5
  - (unknown file):2
    type: CustomRegex   preview: an*****************************************n
    first seen in commit: 0f66998ff6d5
  - (unknown file):16
    type: CustomRegex   preview: pm*************************************n
    first seen in commit: 0f66998ff6d5
  - (unknown file):2
    type: CustomRegex   preview: an***********************************s
    first seen in commit: 86ee5bc30424
  - (unknown file):1
    type: CustomRegex   preview: mi************************************n
    first seen in commit: 86ee5bc30424
  - (unknown file):1
    type: CustomRegex   preview: mi*********************************s
    first seen in commit: 86ee5bc30424
  - (unknown file):9
    type: CustomRegex   preview: mi************************************n
    first seen in commit: 86ee5bc30424
  - (unknown file):10
    type: CustomRegex   preview: mi*********************************s
    first seen in commit: 86ee5bc30424
  - (unknown file):11
    type: CustomRegex   preview: al************************************n
    first seen in commit: 86ee5bc30424
  - (unknown file):2
    type: CustomRegex   preview: an**************************************n
    first seen in commit: 86ee5bc30424
  - (unknown file):11
    type: CustomRegex   preview: al*********************************s
    first seen in commit: 86ee5bc30424
  - (unknown file):13
    type: CustomRegex   preview: be*********************************)
    first seen in commit: 7dfbfc7927c1
  - (unknown file):2
    type: CustomRegex   preview: an***********************************)
    first seen in commit: 7dfbfc7927c1
  - (unknown file):14
    type: CustomRegex   preview: al*********************************)
    first seen in commit: 7dfbfc7927c1
  - (unknown file):1
    type: CustomRegex   preview: be*********************************)
    first seen in commit: 7dfbfc7927c1
  - (unknown file):1
    type: CustomRegex   preview: wu********************************************c
    first seen in commit: 1c1d46cc0bb6
  - (unknown file):2
    type: CustomRegex   preview: lc****************************************c
    first seen in commit: 1c1d46cc0bb6
  - (unknown file):2
    type: CustomRegex   preview: lc******************************************c
    first seen in commit: 1c1d46cc0bb6
  - (unknown file):26
    type: CustomRegex   preview: al***************************************c
    first seen in commit: 1c1d46cc0bb6
  - (unknown file):28
    type: CustomRegex   preview: lc****************************************c
    first seen in commit: 1c1d46cc0bb6
  - (unknown file):26
    type: CustomRegex   preview: al*************************************c
    first seen in commit: 1c1d46cc0bb6
  - (unknown file):27
    type: CustomRegex   preview: wu******************************************c
    first seen in commit: 1c1d46cc0bb6
  - (unknown file):1
    type: CustomRegex   preview: wu******************************************c
    first seen in commit: 1c1d46cc0bb6
  - (unknown file):26
    type: CustomRegex   preview: is*********************************************]
    first seen in commit: c589b2497279
  - (unknown file):31
    type: CustomRegex   preview: st*******************************************"
    first seen in commit: c589b2497279
  - (unknown file):1
    type: CustomRegex   preview: ro****************************************"
    first seen in commit: c589b2497279
  - (unknown file):2
    type: CustomRegex   preview: kw********************************"
    first seen in commit: c589b2497279
  - (unknown file):25
    type: CustomRegex   preview: ne********************************n
    first seen in commit: 1cd20f8bf0ec
  - (unknown file):26
    type: CustomRegex   preview: al***********************************n
    first seen in commit: 1cd20f8bf0ec
  - (unknown file):26
    type: CustomRegex   preview: al********************************d
    first seen in commit: 1cd20f8bf0ec
  - (unknown file):1
    type: CustomRegex   preview: an*************************************n
    first seen in commit: 1cd20f8bf0ec
  - (unknown file):2
    type: CustomRegex   preview: an**********************************d
    first seen in commit: 1cd20f8bf0ec
  - (unknown file):1
    type: CustomRegex   preview: an**********************************d
    first seen in commit: 1cd20f8bf0ec
  - (unknown file):25
    type: CustomRegex   preview: ne*****************************d
    first seen in commit: 1cd20f8bf0ec
  - (unknown file):13
    type: CustomRegex   preview: kr********************************.
    first seen in commit: e866e23959b4
  - (unknown file):1
    type: CustomRegex   preview: kr********************************.
    first seen in commit: e866e23959b4
  - (unknown file):2
    type: CustomRegex   preview: kr********************************.
    first seen in commit: e866e23959b4
  - (unknown file):1
    type: CustomRegex   preview: kr******************************r
    first seen in commit: 7572150c189c
  - (unknown file):2
    type: CustomRegex   preview: kr****************************r
    first seen in commit: 7572150c189c
  - (unknown file):9
    type: CustomRegex   preview: kr****************************r
    first seen in commit: 7572150c189c
  - (unknown file):1
    type: CustomRegex   preview: kr****************************r
    first seen in commit: 7572150c189c
  - (unknown file):9
    type: CustomRegex   preview: kr*****************************e
    first seen in commit: 3c9405a0f7d7
  - (unknown file):2
    type: CustomRegex   preview: kr*****************************e
    first seen in commit: 3c9405a0f7d7
  - (unknown file):1
    type: CustomRegex   preview: kr*****************************e
    first seen in commit: 3c9405a0f7d7
  - (unknown file):5
    type: CustomRegex   preview: sh*****************************d
    first seen in commit: fd04a2aedae3
  - (unknown file):6
    type: CustomRegex   preview: al******************************d
    first seen in commit: fd04a2aedae3
  - (unknown file):2
    type: CustomRegex   preview: an********************************d
    first seen in commit: fd04a2aedae3
  - (unknown file):1
    type: CustomRegex   preview: sh*****************************d
    first seen in commit: fd04a2aedae3
  - (unknown file):18
    type: CustomRegex   preview: lc**********************************0
    first seen in commit: a3a55a2edb7c
  - (unknown file):1
    type: CustomRegex   preview: lc**********************************0
    first seen in commit: a3a55a2edb7c
  - (unknown file):19
    type: CustomRegex   preview: al*******************************0
    first seen in commit: a3a55a2edb7c
  - (unknown file):2
    type: CustomRegex   preview: an*********************************0
    first seen in commit: a3a55a2edb7c
  - (unknown file):2
    type: CustomRegex   preview: bl************************************"
    first seen in commit: 7d69c52ed893
  - (unknown file):1
    type: CustomRegex   preview: we************************************"
    first seen in commit: 7d69c52ed893
  - (unknown file):15
    type: CustomRegex   preview: we************************************"
    first seen in commit: 7d69c52ed893
  - (unknown file):10
    type: CustomRegex   preview: ja*************************************l
    first seen in commit: 8a34a0fb0319
  - (unknown file):1
    type: CustomRegex   preview: an************************************l
    first seen in commit: 8a34a0fb0319
  - (unknown file):11
    type: CustomRegex   preview: al**********************************l
    first seen in commit: 8a34a0fb0319
  - (unknown file):2
    type: CustomRegex   preview: an************************************l
    first seen in commit: 8a34a0fb0319
  - (unknown file):15
    type: CustomRegex   preview: ja**********************************s
    first seen in commit: bb5fc20f7c1c
  - (unknown file):1
    type: CustomRegex   preview: an*********************************s
    first seen in commit: bb5fc20f7c1c
  - (unknown file):16
    type: CustomRegex   preview: al*******************************s
    first seen in commit: bb5fc20f7c1c
  - (unknown file):2
    type: CustomRegex   preview: an*********************************s
    first seen in commit: bb5fc20f7c1c
  - (unknown file):19
    type: CustomRegex   preview: ja***********************************y
    first seen in commit: c0f4ce7751f0
  - (unknown file):20
    type: CustomRegex   preview: al********************************y
    first seen in commit: c0f4ce7751f0
  - (unknown file):2
    type: CustomRegex   preview: an**********************************y
    first seen in commit: c0f4ce7751f0
  - (unknown file):1
    type: CustomRegex   preview: an**********************************y
    first seen in commit: c0f4ce7751f0
  - (unknown file):2
    type: CustomRegex   preview: an*************************************.
    first seen in commit: 045df33021d1
  - (unknown file):8
    type: CustomRegex   preview: ja**************************************.
    first seen in commit: 045df33021d1
  - (unknown file):1
    type: CustomRegex   preview: an*************************************.
    first seen in commit: 045df33021d1
  - (unknown file):9
    type: CustomRegex   preview: al***********************************.
    first seen in commit: 045df33021d1
  - (unknown file):8
    type: CustomRegex   preview: ch*******************************r
    first seen in commit: 2569da0cb645
  - (unknown file):9
    type: CustomRegex   preview: al********************************r
    first seen in commit: 2569da0cb645
  - (unknown file):2
    type: CustomRegex   preview: an**********************************r
    first seen in commit: 2569da0cb645
  - (unknown file):1
    type: CustomRegex   preview: an**********************************r
    first seen in commit: 2569da0cb645
  - (unknown file):8
    type: CustomRegex   preview: La*************************************t
    first seen in commit: 61fce45f1296
  - (unknown file):1
    type: CustomRegex   preview: an***********************************t
    first seen in commit: 61fce45f1296
  - (unknown file):2
    type: CustomRegex   preview: an***********************************t
    first seen in commit: 61fce45f1296
  - (unknown file):9
    type: CustomRegex   preview: an***********************************t
    first seen in commit: 61fce45f1296
  - (unknown file):2
    type: CustomRegex   preview: th*************************************,
    first seen in commit: 7084851534c8
  - (unknown file):1
    type: CustomRegex   preview: th*************************************,
    first seen in commit: 7084851534c8

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

