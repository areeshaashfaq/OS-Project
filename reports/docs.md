Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/MatthiasWinter/docs

Flagged locations (secret values are not included):

  - docs/operations/starknet/tools.md:40
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 5058bc58e740
  - docs/operations/starknet/tools.md:40
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 5058bc58e740
  - docs/operations/harmony/tools.md:133
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:202
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:44
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:252
    type: CustomRegex   preview: ht**************************************************************************;
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:487
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:487
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:487
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:44
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:487
    type: CustomRegex   preview: pa*********************************************************************************************'
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:620
    type: CustomRegex   preview: pa************************************************************************************************'
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:620
    type: CustomRegex   preview: pa***************************************************************************'
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:706
    type: CustomRegex   preview: pa*********************************************************************************************'
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:737
    type: CustomRegex   preview: pa************************************************************************'
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:659
    type: CustomRegex   preview: pa************************************************************************'
    first seen in commit: a26dc9bc1ee8
  - docs/operations/harmony/tools.md:487
    type: CustomRegex   preview: pa************************************************************************'
    first seen in commit: a26dc9bc1ee8
  - docs/operations/solana/tools.md:131
    type: CustomRegex   preview: ht*************************************************************************;
    first seen in commit: c7188b872478
  - docs/operations/solana/tools.md:131
    type: CustomRegex   preview: ht************************************************************************)
    first seen in commit: c7188b872478
  - docs/operations/solana/tools.md:35
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: c7188b872478
  - docs/operations/solana/tools.md:35
    type: URI   preview: ht**********************************************************************m
    first seen in commit: c7188b872478
  - docs/operations/solana/tools.md:131
    type: CustomRegex   preview: ht************************************************************************)
    first seen in commit: d8ab38aa6edb
  - docs/operations/solana/tools.md:131
    type: CustomRegex   preview: ht*************************************************************************;
    first seen in commit: d8ab38aa6edb
  - docs/operations/solana/tools.md:35
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: d8ab38aa6edb
  - docs/operations/solana/tools.md:35
    type: URI   preview: ht**********************************************************************m
    first seen in commit: d8ab38aa6edb
  - docs/operations/avalanche/tools.md:252
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:293
    type: CustomRegex   preview: ws***********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:44
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:44
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:133
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:80
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:202
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:619
    type: CustomRegex   preview: pa***************************************************************************'
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:619
    type: CustomRegex   preview: pa************************************************************************************************'
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:486
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:658
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:777
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:486
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:658
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:619
    type: CustomRegex   preview: ws*************************************************************************,
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:705
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:736
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 7bff31e107ef
  - docs/operations/bsc/tools.md:814
    type: URI   preview: ht**********************************************************************m
    first seen in commit: fc90fe51e8c2
  - docs/operations/bsc/tools.md:814
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: fc90fe51e8c2
  - docs/operations/ethereum/tools.md:978
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: fc90fe51e8c2
  - docs/operations/fantom/tools.md:816
    type: URI   preview: ht**********************************************************************m
    first seen in commit: fc90fe51e8c2
  - docs/operations/fantom/tools.md:816
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: fc90fe51e8c2
  - docs/operations/ethereum/tools.md:978
    type: URI   preview: ht**********************************************************************m
    first seen in commit: fc90fe51e8c2
  - docs/operations/avalanche/tools.md:486
    type: CustomRegex   preview: pa*********************************************************************************************'
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:777
    type: CustomRegex   preview: pa************************************************************************'
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:486
    type: CustomRegex   preview: pa************************************************************************'
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:658
    type: CustomRegex   preview: pa************************************************************************'
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:705
    type: CustomRegex   preview: pa************************************************************************'
    first seen in commit: 7bff31e107ef
  - docs/operations/avalanche/tools.md:736
    type: CustomRegex   preview: pa************************************************************************'
    first seen in commit: 7bff31e107ef
  - docs/operations/polygon/tools.md:813
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: fc90fe51e8c2
  - docs/operations/polygon/tools.md:813
    type: URI   preview: ht**********************************************************************m
    first seen in commit: fc90fe51e8c2
  - docs/operations/bsc/tools.md:591
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: 369a9aacddb5
  - docs/operations/fantom/tools.md:597
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 614e35738251
  - docs/operations/ethereum/tools.md:681
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: 369a9aacddb5
  - docs/operations/bsc/tools.md:591
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 369a9aacddb5
  - docs/operations/polygon/tools.md:594
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: 369a9aacddb5
  - docs/operations/fantom/tools.md:243
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: 614e35738251
  - docs/operations/fantom/tools.md:44
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 614e35738251
  - docs/operations/fantom/tools.md:597
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: 614e35738251
  - docs/operations/fantom/tools.md:362
    type: CustomRegex   preview: ht**************************************************************************;
    first seen in commit: 614e35738251
  - docs/operations/polygon/tools.md:594
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 369a9aacddb5
  - docs/operations/fantom/tools.md:312
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: 614e35738251
  - docs/operations/ethereum/tools.md:681
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 369a9aacddb5
  - docs/operations/fantom/tools.md:597
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 614e35738251
  - docs/operations/fantom/tools.md:730
    type: CustomRegex   preview: pa***************************************************************************'
    first seen in commit: 614e35738251
  - docs/operations/fantom/tools.md:730
    type: CustomRegex   preview: pa************************************************************************************************'
    first seen in commit: 614e35738251
  - docs/operations/fantom/tools.md:597
    type: CustomRegex   preview: pa************************************************************************'
    first seen in commit: 614e35738251
  - docs/operations/fantom/tools.md:597
    type: CustomRegex   preview: pa*********************************************************************************************'
    first seen in commit: 614e35738251
  - docs/operations/fantom/tools.md:769
    type: CustomRegex   preview: pa************************************************************************'
    first seen in commit: 614e35738251
  - docs/operations/fantom/tools.md:149
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 614e35738251
  - docs/operations/fantom/tools.md:44
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 614e35738251
  - docs/operations/tezos/tools.md:103
    type: CustomRegex   preview: ht*************************************************************************;
    first seen in commit: 7453514f9ddc
  - docs/operations/tezos/tools.md:39
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 7453514f9ddc
  - docs/operations/tezos/tools.md:39
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 7453514f9ddc
  - docs/operations/ethereum/tools.md:44
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/bsc/tools.md:44
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/bsc/tools.md:44
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/ethereum/tools.md:44
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/ethereum/tools.md:303
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: a284717a6319
  - docs/operations/ethereum/tools.md:303
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/ethereum/tools.md:441
    type: CustomRegex   preview: ht**************************************************************************;
    first seen in commit: a284717a6319
  - docs/operations/ethereum/tools.md:180
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/bsc/tools.md:351
    type: CustomRegex   preview: ht**************************************************************************;
    first seen in commit: a284717a6319
  - docs/operations/bsc/tools.md:301
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: a284717a6319
  - docs/operations/ethereum/tools.md:441
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/ethereum/tools.md:180
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/polygon/tools.md:308
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: a284717a6319
  - docs/operations/polygon/tools.md:358
    type: CustomRegex   preview: ht**************************************************************************;
    first seen in commit: a284717a6319
  - docs/operations/bsc/tools.md:301
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/bsc/tools.md:181
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/polygon/tools.md:308
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/bsc/tools.md:181
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/polygon/tools.md:186
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/polygon/tools.md:186
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/polygon/tools.md:44
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/platform/view-node-access-and-credentials.md:36
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/polygon/tools.md:44
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/quorum/tools.md:48
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/platform/view-node-access-and-credentials.md:36
    type: CustomRegex   preview: ht***********************************************************************`
    first seen in commit: a284717a6319
  - docs/operations/quorum/tools.md:48
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/platform/view-node-access-and-credentials.md:36
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a284717a6319
  - docs/operations/bsc/tools.md:408
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a0491d81998b
  - docs/operations/bsc/tools.md:408
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a0491d81998b
  - docs/operations/bsc/tools.md:121
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 98a3a0e69d15
  - docs/operations/bsc/tools.md:121
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 98a3a0e69d15
  - docs/operations/ethereum/tools.md:521
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a0491d81998b
  - docs/operations/ethereum/tools.md:503
    type: CustomRegex   preview: ht***********************************T
    first seen in commit: a0491d81998b
  - docs/operations/ethereum/tools.md:521
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a0491d81998b
  - docs/operations/ethereum/tools.md:503
    type: URI   preview: ht***********************************T
    first seen in commit: a0491d81998b
  - docs/operations/polygon/tools.md:127
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 98a3a0e69d15
  - docs/operations/polygon/tools.md:127
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 98a3a0e69d15
  - docs/operations/polygon/tools.md:414
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: a0491d81998b
  - docs/operations/polygon/tools.md:397
    type: CustomRegex   preview: ht***********************************T
    first seen in commit: a0491d81998b
  - docs/operations/polygon/tools.md:414
    type: URI   preview: ht**********************************************************************m
    first seen in commit: a0491d81998b
  - docs/operations/polygon/tools.md:397
    type: URI   preview: ht***********************************T
    first seen in commit: a0491d81998b
  - docs/operations/polygon/tools.md:51
    type: CustomRegex   preview: ws***********************************************************************m
    first seen in commit: b1647029d180
  - docs/operations/polygon/tools.md:24
    type: CustomRegex   preview: ht***********************************T
    first seen in commit: b1647029d180
  - docs/operations/polygon/tools.md:111
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: b1647029d180
  - docs/operations/polygon/tools.md:45
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: b1647029d180
  - docs/operations/polygon/tools.md:137
    type: CustomRegex   preview: ht*************************************,
    first seen in commit: b1647029d180
  - docs/operations/polygon/tools.md:45
    type: URI   preview: ht**********************************************************************m
    first seen in commit: b1647029d180
  - docs/operations/polygon/tools.md:24
    type: URI   preview: ht***********************************T
    first seen in commit: b1647029d180
  - docs/operations/polygon/tools.md:51
    type: CustomRegex   preview: pa************************************************************************************************'
    first seen in commit: b1647029d180
  - docs/operations/polygon/tools.md:179
    type: CustomRegex   preview: pa***************************************************************************'
    first seen in commit: b1647029d180
  - docs/operations/polygon/tools.md:313
    type: CustomRegex   preview: pa***************************************************************************'
    first seen in commit: b1647029d180
  - docs/operations/bsc/tools.md:51
    type: CustomRegex   preview: ws***********************************************************************m
    first seen in commit: de0fc1825757
  - docs/operations/bsc/tools.md:105
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: de0fc1825757
  - docs/operations/bsc/tools.md:24
    type: CustomRegex   preview: ht***********************************T
    first seen in commit: de0fc1825757
  - docs/operations/bsc/tools.md:45
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: de0fc1825757
  - docs/operations/bsc/tools.md:131
    type: CustomRegex   preview: ht*************************************,
    first seen in commit: de0fc1825757
  - docs/tutorials/bsc/bep-1155-contract-with-truffle-and-openzeppelin.md:164
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: de0fc1825757
  - docs/tutorials/polygon/bridging-erc20-from-ethereum-to-polygon.md:158
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: b1647029d180
  - docs/tutorials/bsc/bep-1155-contract-with-truffle-and-openzeppelin.md:164
    type: URI   preview: ht**********************************************************************m
    first seen in commit: de0fc1825757
  - docs/tutorials/polygon/bridging-erc20-from-ethereum-to-polygon.md:158
    type: URI   preview: ht**********************************************************************m
    first seen in commit: b1647029d180
  - docs/operations/bsc/tools.md:45
    type: URI   preview: ht**********************************************************************m
    first seen in commit: de0fc1825757
  - docs/operations/bsc/tools.md:51
    type: CustomRegex   preview: pa************************************************************************************************'
    first seen in commit: de0fc1825757
  - docs/operations/bsc/tools.md:173
    type: CustomRegex   preview: pa***************************************************************************'
    first seen in commit: de0fc1825757
  - docs/operations/bsc/tools.md:307
    type: CustomRegex   preview: pa***************************************************************************'
    first seen in commit: de0fc1825757
  - docs/operations/bsc/tools.md:24
    type: URI   preview: ht***********************************T
    first seen in commit: de0fc1825757
  - docs/operations/ethereum/tools.md:202
    type: CustomRegex   preview: ht*************************************,
    first seen in commit: e3406bddc500
  - docs/operations/ethereum/tools.md:202
    type: URI   preview: ht***********************************T
    first seen in commit: e3406bddc500
  - docs/operations/ethereum/tools.md:144
    type: CustomRegex   preview: ht***********************************T
    first seen in commit: 574a2e6e546d
  - docs/operations/ethereum/tools.md:144
    type: URI   preview: ht***********************************T
    first seen in commit: 574a2e6e546d
  - docs/operations/ethereum/tools.md:121
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 12a63d28fee5
  - docs/operations/ethereum/tools.md:121
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 12a63d28fee5
  - docs/operations/ethereum/tools.md:407
    type: CustomRegex   preview: pa***************************************************************************'
    first seen in commit: f3e83d2eb6e0
  - docs/operations/ethereum/tools.md:407
    type: CustomRegex   preview: ws*************************************************************************,
    first seen in commit: f3e83d2eb6e0
  - docs/operations/ethereum/tools.md:389
    type: CustomRegex   preview: ws***********************************,
    first seen in commit: f3e83d2eb6e0
  - docs/operations/ethereum/tools.md:407
    type: CustomRegex   preview: pa************************************************************************************************'
    first seen in commit: f3e83d2eb6e0
  - docs/operations/ethereum/tools.md:123
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: 15a6d5e8fe36
  - docs/operations/ethereum/tools.md:123
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 15a6d5e8fe36
  - docs/operations/quorum/tools.md:173
    type: CustomRegex   preview: ht**************************************************************************;
    first seen in commit: ccf8d2f74d4f
  - docs/operations/quorum/tools.md:159
    type: CustomRegex   preview: ht***************************************;
    first seen in commit: ccf8d2f74d4f
  - docs/operations/quorum/tools.md:173
    type: URI   preview: ht**********************************************************************m
    first seen in commit: ccf8d2f74d4f
  - docs/operations/quorum/tools.md:159
    type: URI   preview: ht***********************************T
    first seen in commit: ccf8d2f74d4f
  - docs/operations/quorum/tools.md:173
    type: CustomRegex   preview: pa**************************************************************************;
    first seen in commit: ccf8d2f74d4f
  - docs/tutorials/quorum/food-supply-temperature-control-with-web3.md:167
    type: URI   preview: ht*****************************************************************************m
    first seen in commit: 9f84414e21ea
  - docs/tutorials/quorum/food-supply-temperature-control-with-web3.md:167
    type: CustomRegex   preview: ht*******************************************************************************.
    first seen in commit: 9f84414e21ea
  - docs/operations/ethereum/tools.md:65
    type: CustomRegex   preview: ws*************************************;
    first seen in commit: c5eeb55bb114
  - docs/operations/ethereum/tools.md:161
    type: CustomRegex   preview: ws***************************************************************************;
    first seen in commit: ca09a99b0ff5
  - docs/operations/ethereum/tools.md:147
    type: CustomRegex   preview: ws*************************************;
    first seen in commit: ca09a99b0ff5
  - docs/operations/ethereum/tools.md:79
    type: CustomRegex   preview: ws***************************************************************************;
    first seen in commit: c5eeb55bb114
  - docs/operations/quorum/configuring-consensus.md:149
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 366a34f560ad
  - docs/operations/quorum/configuring-consensus.md:149
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 366a34f560ad
  - docs/operations/ethereum/tools.md:178
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: aef38e4bf0b6
  - docs/operations/ethereum/tools.md:153
    type: CustomRegex   preview: ht*************************************,
    first seen in commit: aef38e4bf0b6
  - docs/operations/ethereum/tools.md:153
    type: URI   preview: ht***********************************T
    first seen in commit: aef38e4bf0b6
  - docs/operations/ethereum/tools.md:178
    type: URI   preview: ht**********************************************************************m
    first seen in commit: aef38e4bf0b6
  - docs/operations/bitcoin/tools.md:12
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 947bc5783039
  - docs/operations/bitcoin/tools.md:12
    type: CustomRegex   preview: pa**********************************************************************************************"
    first seen in commit: 947bc5783039
  - docs/operations/bitcoin/tools.md:12
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 947bc5783039
  - docs/operations/ethereum/tools.md:63
    type: URI   preview: ht***********************************T
    first seen in commit: 3b2673c5a1a6
  - docs/operations/ethereum/tools.md:63
    type: CustomRegex   preview: ht***********************************T
    first seen in commit: 3b2673c5a1a6
  - docs/operations/ethereum/using-metamask-with-chainstack.md:16
    type: URI   preview: ht***********************************T
    first seen in commit: 9a117992686a
  - docs/operations/ethereum/using-metamask-with-chainstack.md:16
    type: CustomRegex   preview: ht***********************************T
    first seen in commit: 9a117992686a
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:144
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: 92b65c619733
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:144
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 92b65c619733
  - docs/operations/quorum/configuring-consensus.md:94
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:26
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:178
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:203
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:115
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:145
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:77
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:244
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:73
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:145
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:26
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:240
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:26
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:94
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:244
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:203
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:115
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:178
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:290
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:240
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:77
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:26
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:73
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:320
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:102
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:127
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:102
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:158
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:221
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:158
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:127
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:263
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:296
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:290
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:221
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:192
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:320
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:263
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:192
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 4d253938677a
  - docs/operations/quorum/configuring-consensus.md:296
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:270
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:270
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 88f4367c814d
  - docs/operations/quorum/configuring-consensus.md:164
    type: URI   preview: ht******************************************************************************m
    first seen in commit: 70770de7b85c
  - docs/operations/quorum/configuring-consensus.md:164
    type: CustomRegex   preview: ht******************************************************************************m
    first seen in commit: 70770de7b85c
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:100
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 1362d2dcc52b
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:100
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: 1362d2dcc52b
  - docs/operations/quorum/tools.md:61
    type: URI   preview: ht**********************************************************************m
    first seen in commit: b01dd5f9e950
  - docs/operations/quorum/tools.md:61
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: b01dd5f9e950
  - docs/tutorials/loyalty-program-on-quorum.md:217
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: b01dd5f9e950
  - docs/tutorials/loyalty-program-on-quorum.md:237
    type: URI   preview: ht**********************************************************************m
    first seen in commit: b01dd5f9e950
  - docs/tutorials/loyalty-program-on-quorum.md:237
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: b01dd5f9e950
  - docs/tutorials/loyalty-program-on-quorum.md:271
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: b01dd5f9e950
  - docs/tutorials/loyalty-program-on-quorum.md:217
    type: URI   preview: ht**********************************************************************m
    first seen in commit: b01dd5f9e950
  - docs/operations/quorum/tools.md:23
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: b01dd5f9e950
  - docs/tutorials/loyalty-program-on-quorum.md:271
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: b01dd5f9e950
  - docs/operations/quorum/tools.md:23
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: b01dd5f9e950
  - docs/tutorials/loyalty-program-on-quorum.md:271
    type: URI   preview: ht**********************************************************************m
    first seen in commit: b01dd5f9e950
  - docs/operations/quorum/tools.md:23
    type: URI   preview: ht**********************************************************************m
    first seen in commit: b01dd5f9e950
  - docs/operations/quorum/tools.md:127
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: b01dd5f9e950
  - docs/operations/quorum/tools.md:112
    type: URI   preview: ht**********************************************************************m
    first seen in commit: b01dd5f9e950
  - docs/operations/quorum/tools.md:112
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: b01dd5f9e950
  - docs/tutorials/academic-certificates-on-ethereum.md:413
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: 9a77e93e542c
  - docs/tutorials/academic-certificates-on-ethereum.md:396
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: 9a77e93e542c
  - docs/tutorials/academic-certificates-on-ethereum.md:396
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 9a77e93e542c
  - docs/tutorials/academic-certificates-on-ethereum.md:271
    type: CustomRegex   preview: ht************************************************************************)
    first seen in commit: 8e14c3a138f8
  - docs/operations/ethereum/tools.md:70
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: 8e14c3a138f8
  - docs/operations/ethereum/tools.md:70
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 8e14c3a138f8
  - docs/tutorials/academic-certificates-on-ethereum.md:271
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 8e14c3a138f8
  - docs/tutorials/academic-certificates-on-ethereum.md:160
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: 8e14c3a138f8
  - docs/tutorials/academic-certificates-on-ethereum.md:160
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 8e14c3a138f8
  - docs/operations/ethereum/tools.md:41
    type: CustomRegex   preview: ws***********************************************************************m
    first seen in commit: 8e14c3a138f8
  - docs/operations/ethereum/tools.md:14
    type: CustomRegex   preview: ht***********************************T
    first seen in commit: 8e14c3a138f8
  - docs/operations/ethereum/tools.md:35
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 8e14c3a138f8
  - docs/tutorials/asset-tokenization-on-ethereum.md:148
    type: CustomRegex   preview: pa*********************************************************************"
    first seen in commit: 8e14c3a138f8
  - docs/tutorials/asset-tokenization-on-ethereum.md:135
    type: CustomRegex   preview: pa*********************************************************************"
    first seen in commit: 8e14c3a138f8
  - docs/operations/ethereum/tools.md:14
    type: URI   preview: ht***********************************T
    first seen in commit: 8e14c3a138f8
  - docs/operations/ethereum/tools.md:35
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 8e14c3a138f8
  - docs/operations/bitcoin/creating-a-raw-transaction.md:39
    type: CustomRegex   preview: ht***********************************************************************m
    first seen in commit: 81cf7d83d4f9
  - docs/operations/bitcoin/creating-a-raw-transaction.md:39
    type: URI   preview: ht***********************************************************************m
    first seen in commit: 81cf7d83d4f9
  - docs/operations/ethereum/tools.md:178
    type: CustomRegex   preview: ht************************************************************************,
    first seen in commit: b81842d30d5e
  - docs/operations/ethereum/tools.md:153
    type: CustomRegex   preview: ht*************************************,
    first seen in commit: b81842d30d5e
  - docs/operations/ethereum/tools.md:178
    type: URI   preview: ht**********************************************************************m
    first seen in commit: b81842d30d5e
  - docs/operations/ethereum/tools.md:153
    type: URI   preview: ht***********************************T
    first seen in commit: b81842d30d5e
  - docs/operations/bitcoin/tools.md:12
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: b77ca3c116a8
  - docs/operations/bitcoin/tools.md:12
    type: CustomRegex   preview: pa**********************************************************************************************"
    first seen in commit: b77ca3c116a8
  - docs/operations/bitcoin/tools.md:12
    type: URI   preview: ht**********************************************************************m
    first seen in commit: b77ca3c116a8
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:96
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 5ed416e8cd03
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:96
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: 5ed416e8cd03
  - docs/operations/ethereum/tools.md:67
    type: CustomRegex   preview: ht***********************************T
    first seen in commit: 5ed416e8cd03
  - docs/operations/ethereum/tools.md:67
    type: URI   preview: ht***********************************T
    first seen in commit: 5ed416e8cd03
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:144
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: 5bdc5960e638
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:144
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 5bdc5960e638
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:121
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: 6ddb00609322
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:121
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 6ddb00609322
  - docs/operations/ethereum/using-metamask-with-chainstack.md:16
    type: URI   preview: ht***********************************T
    first seen in commit: b786e92fc941
  - docs/operations/ethereum/using-metamask-with-chainstack.md:16
    type: CustomRegex   preview: ht***********************************T
    first seen in commit: b786e92fc941
  - docs/operations/quorum/configuring-consensus.md:115
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:94
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:115
    type: URI   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:26
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:244
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:73
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:296
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:178
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:240
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:145
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:73
    type: URI   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:240
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:270
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:296
    type: URI   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:244
    type: URI   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:178
    type: URI   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:203
    type: URI   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:77
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:203
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:270
    type: URI   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:263
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:145
    type: URI   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:94
    type: URI   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:320
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:221
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:102
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:192
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:26
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:320
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:77
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:158
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:290
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:221
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:290
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:158
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:192
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:127
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:102
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:26
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:263
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:127
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 118100518c89
  - docs/operations/quorum/configuring-consensus.md:26
    type: URI   preview: ht**********************************************************************m
    first seen in commit: f280c4322e0d
  - docs/operations/quorum/configuring-consensus.md:164
    type: URI   preview: ht******************************************************************************m
    first seen in commit: c2077a62ac50
  - docs/operations/quorum/configuring-consensus.md:164
    type: CustomRegex   preview: ht******************************************************************************m
    first seen in commit: c2077a62ac50
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:100
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: 20e06fff6c62
  - docs/tutorials/food-supply-temperature-control-on-quorum.md:100
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 20e06fff6c62
  - docs/tutorials/loyalty-program-on-quorum.md:217
    type: URI   preview: ht**********************************************************************m
    first seen in commit: bf122980043d
  - docs/tutorials/loyalty-program-on-quorum.md:217
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: bf122980043d
  - docs/tutorials/loyalty-program-on-quorum.md:237
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: bf122980043d
  - docs/tutorials/loyalty-program-on-quorum.md:237
    type: URI   preview: ht**********************************************************************m
    first seen in commit: bf122980043d
  - docs/tutorials/loyalty-program-on-quorum.md:271
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: bf122980043d
  - docs/operations/quorum/tools.md:61
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: bf122980043d
  - docs/tutorials/loyalty-program-on-quorum.md:271
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: bf122980043d
  - docs/operations/quorum/tools.md:61
    type: URI   preview: ht**********************************************************************m
    first seen in commit: bf122980043d
  - docs/operations/quorum/tools.md:127
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: bf122980043d
  - docs/operations/quorum/tools.md:112
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: bf122980043d
  - docs/operations/quorum/tools.md:23
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: bf122980043d
  - docs/operations/quorum/tools.md:112
    type: URI   preview: ht**********************************************************************m
    first seen in commit: bf122980043d
  - docs/operations/quorum/tools.md:23
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: bf122980043d
  - docs/tutorials/loyalty-program-on-quorum.md:271
    type: URI   preview: ht**********************************************************************m
    first seen in commit: bf122980043d
  - docs/operations/quorum/tools.md:23
    type: URI   preview: ht**********************************************************************m
    first seen in commit: bf122980043d
  - docs/tutorials/academic-certificates-on-ethereum.md:413
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: 71e691247fd9
  - docs/tutorials/academic-certificates-on-ethereum.md:396
    type: CustomRegex   preview: ht************************************************************************.
    first seen in commit: 71e691247fd9
  - docs/tutorials/academic-certificates-on-ethereum.md:396
    type: URI   preview: ht**********************************************************************m
    first seen in commit: 71e691247fd9
  - docs/tutorials/academic-certificates-on-ethereum.md:271
    type: CustomRegex   preview: ht************************************************************************)
    first seen in commit: cf1ec52047bb
  - docs/operations/ethereum/tools.md:70
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: cf1ec52047bb
  - docs/operations/ethereum/tools.md:70
    type: URI   preview: ht**********************************************************************m
    first seen in commit: cf1ec52047bb
  - docs/tutorials/academic-certificates-on-ethereum.md:160
    type: CustomRegex   preview: ht*************************************************************************,
    first seen in commit: cf1ec52047bb
  - docs/operations/ethereum/tools.md:41
    type: CustomRegex   preview: ws***********************************************************************m
    first seen in commit: cf1ec52047bb
  - docs/operations/ethereum/tools.md:14
    type: CustomRegex   preview: ht***********************************T
    first seen in commit: cf1ec52047bb
  - docs/tutorials/academic-certificates-on-ethereum.md:271
    type: URI   preview: ht**********************************************************************m
    first seen in commit: cf1ec52047bb
  - docs/operations/ethereum/tools.md:35
    type: CustomRegex   preview: ht**********************************************************************m
    first seen in commit: cf1ec52047bb
  - docs/tutorials/academic-certificates-on-ethereum.md:160
    type: URI   preview: ht**********************************************************************m
    first seen in commit: cf1ec52047bb
  - docs/operations/ethereum/tools.md:35
    type: URI   preview: ht**********************************************************************m
    first seen in commit: cf1ec52047bb
  - docs/operations/ethereum/tools.md:14
    type: URI   preview: ht***********************************T
    first seen in commit: cf1ec52047bb
  - docs/tutorials/asset-tokenization-on-ethereum.md:148
    type: CustomRegex   preview: pa*********************************************************************"
    first seen in commit: cf1ec52047bb
  - docs/tutorials/asset-tokenization-on-ethereum.md:135
    type: CustomRegex   preview: pa*********************************************************************"
    first seen in commit: cf1ec52047bb

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

