Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/nbolser/clearance

Flagged locations (secret values are not included):

  - (unknown file):1
    type: CustomRegex   preview: ab*********************************,
    first seen in commit: cfabcf1d252d
  - (unknown file):1
    type: CustomRegex   preview: ab********************************d
    first seen in commit: cfabcf1d252d
  - (unknown file):2
    type: CustomRegex   preview: de*********************************d
    first seen in commit: cfabcf1d252d
  - (unknown file):2
    type: CustomRegex   preview: de**********************************,
    first seen in commit: cfabcf1d252d
  - (unknown file):2
    type: CustomRegex   preview: de********************************.
    first seen in commit: ad294a94e626
  - (unknown file):1
    type: CustomRegex   preview: de********************************.
    first seen in commit: ad294a94e626
  - (unknown file):2
    type: CustomRegex   preview: de********************************.
    first seen in commit: 9ff34271a6fc
  - (unknown file):1
    type: CustomRegex   preview: de********************************.
    first seen in commit: 9ff34271a6fc
  - (unknown file):1
    type: CustomRegex   preview: de**********************************y
    first seen in commit: e297bc4bd230
  - (unknown file):2
    type: CustomRegex   preview: de**********************************y
    first seen in commit: e297bc4bd230
  - (unknown file):1
    type: CustomRegex   preview: de****************************************s
    first seen in commit: 13b31ac41c0f
  - (unknown file):2
    type: CustomRegex   preview: de********************************s
    first seen in commit: 13b31ac41c0f
  - (unknown file):1
    type: CustomRegex   preview: bw******************************r
    first seen in commit: 463f46821ad9
  - (unknown file):2
    type: CustomRegex   preview: de********************************r
    first seen in commit: 463f46821ad9
  - (unknown file):1
    type: CustomRegex   preview: de*********************************)
    first seen in commit: 1a88a0d949d8
  - (unknown file):1
    type: CustomRegex   preview: de**********************************y
    first seen in commit: 1a88a0d949d8
  - (unknown file):2
    type: CustomRegex   preview: de*************************************s
    first seen in commit: 1a88a0d949d8
  - (unknown file):1
    type: CustomRegex   preview: de*************************************s
    first seen in commit: 1a88a0d949d8
  - (unknown file):2
    type: CustomRegex   preview: de************************************s
    first seen in commit: a759cbcf73b6
  - (unknown file):1
    type: CustomRegex   preview: de************************************s
    first seen in commit: a759cbcf73b6
  - (unknown file):2
    type: CustomRegex   preview: me**********************************s
    first seen in commit: 1ac223a78aef
  - (unknown file):1
    type: CustomRegex   preview: me**********************************s
    first seen in commit: 1ac223a78aef
  - (unknown file):2
    type: CustomRegex   preview: me**********************************s
    first seen in commit: fdcede4d245d
  - (unknown file):1
    type: CustomRegex   preview: me**********************************s
    first seen in commit: fdcede4d245d
  - (unknown file):2
    type: CustomRegex   preview: me**********************************s
    first seen in commit: 0103fcc3059d
  - (unknown file):1
    type: CustomRegex   preview: me**********************************s
    first seen in commit: 0103fcc3059d
  - (unknown file):2
    type: CustomRegex   preview: me**********************************s
    first seen in commit: 393be4cc2d9a
  - (unknown file):1
    type: CustomRegex   preview: me**********************************s
    first seen in commit: 393be4cc2d9a
  - (unknown file):2
    type: CustomRegex   preview: me**********************************s
    first seen in commit: 83c2c4c38503
  - (unknown file):1
    type: CustomRegex   preview: me**********************************s
    first seen in commit: 83c2c4c38503
  - (unknown file):2
    type: CustomRegex   preview: me***********************************e
    first seen in commit: efb85c5dbe43
  - (unknown file):1
    type: CustomRegex   preview: me***********************************e
    first seen in commit: efb85c5dbe43
  - (unknown file):1
    type: CustomRegex   preview: me**********************************s
    first seen in commit: 19035fde285c
  - (unknown file):2
    type: CustomRegex   preview: me**********************************s
    first seen in commit: 19035fde285c
  - (unknown file):2
    type: CustomRegex   preview: de********************************r
    first seen in commit: 3ca7a6b20a73
  - (unknown file):1
    type: CustomRegex   preview: de********************************r
    first seen in commit: 3ca7a6b20a73
  - (unknown file):1
    type: CustomRegex   preview: de*************************************.
    first seen in commit: 469e11db475b
  - (unknown file):2
    type: CustomRegex   preview: de************************************s
    first seen in commit: 469e11db475b
  - (unknown file):1
    type: CustomRegex   preview: de************************************s
    first seen in commit: 469e11db475b
  - README.md:114
    type: CustomRegex   preview: re*****************************s
    first seen in commit: c983fe27c505
  - (unknown file):1
    type: CustomRegex   preview: je**************************************y
    first seen in commit: f4193977fe5b
  - (unknown file):2
    type: CustomRegex   preview: je**************************************y
    first seen in commit: f4193977fe5b
  - lib/clearance/configuration.rb:46
    type: CustomRegex   preview: re*******************************y
    first seen in commit: de10fd6a9ef7
  - (unknown file):2
    type: CustomRegex   preview: je****************************************s
    first seen in commit: 21ed00a86513
  - (unknown file):1
    type: CustomRegex   preview: je****************************************s
    first seen in commit: 21ed00a86513
  - NEWS.md:221
    type: CustomRegex   preview: de**********************************n
    first seen in commit: aefdc076fe92
  - NEWS.md:221
    type: CustomRegex   preview: de********************************y
    first seen in commit: aefdc076fe92
  - NEWS.md:221
    type: CustomRegex   preview: de*************************************.
    first seen in commit: aefdc076fe92
  - NEWS.md:221
    type: CustomRegex   preview: de*********************************,
    first seen in commit: aefdc076fe92
  - spec/user_spec.rb:8
    type: CustomRegex   preview: fo*********************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:13
    type: CustomRegex   preview: fo*************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:9
    type: CustomRegex   preview: fo************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:22
    type: CustomRegex   preview: jo*****************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:8
    type: CustomRegex   preview: fo**************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:13
    type: CustomRegex   preview: fo********************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:12
    type: CustomRegex   preview: fo*************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:9
    type: CustomRegex   preview: fo*******************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:10
    type: CustomRegex   preview: fo***********************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:8
    type: CustomRegex   preview: fo********************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:10
    type: CustomRegex   preview: fo**************************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:10
    type: CustomRegex   preview: fo**********************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:9
    type: CustomRegex   preview: fo******************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:22
    type: CustomRegex   preview: jo**************************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:22
    type: CustomRegex   preview: jo**************************************o
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:8
    type: CustomRegex   preview: fo*****************************r
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:12
    type: CustomRegex   preview: fo***********************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:13
    type: CustomRegex   preview: fo***********************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:9
    type: CustomRegex   preview: fo***************************r
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:22
    type: CustomRegex   preview: jo***************************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:12
    type: CustomRegex   preview: fo****************************r
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:10
    type: CustomRegex   preview: fo*******************************r
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:12
    type: CustomRegex   preview: fo*******************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:13
    type: CustomRegex   preview: fo****************************r
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:8
    type: CustomRegex   preview: fo************************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:13
    type: CustomRegex   preview: fo*******************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:22
    type: CustomRegex   preview: jo********************************r
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:22
    type: CustomRegex   preview: jo***********************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:9
    type: CustomRegex   preview: fo**********************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:8
    type: CustomRegex   preview: fo***********************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:9
    type: CustomRegex   preview: fo*********************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:12
    type: CustomRegex   preview: fo**********************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:13
    type: CustomRegex   preview: fo**********************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:10
    type: CustomRegex   preview: fo*************************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:8
    type: CustomRegex   preview: fo***********************************o
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:10
    type: CustomRegex   preview: fo*************************************o
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:12
    type: CustomRegex   preview: fo**********************************o
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:13
    type: CustomRegex   preview: fo**********************************o
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:22
    type: CustomRegex   preview: jo************************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:22
    type: CustomRegex   preview: jo************************************)
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:13
    type: CustomRegex   preview: fo********************************)
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:12
    type: CustomRegex   preview: fo********************************)
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:9
    type: CustomRegex   preview: fo*******************************)
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:8
    type: CustomRegex   preview: fo*********************************)
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:9
    type: CustomRegex   preview: fo*********************************o
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:10
    type: CustomRegex   preview: fo***********************************)
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:10
    type: CustomRegex   preview: fo****************************************d
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:12
    type: CustomRegex   preview: fo********************************"
    first seen in commit: 21ed00a86513
  - spec/user_spec.rb:179
    type: CustomRegex   preview: jo*****************************************d
    first seen in commit: 21ed00a86513
  - (unknown file):1
    type: CustomRegex   preview: sq********************************y
    first seen in commit: ed2c3df72c78
  - (unknown file):2
    type: CustomRegex   preview: de**********************************y
    first seen in commit: ed2c3df72c78
  - (unknown file):2
    type: CustomRegex   preview: de*********************************.
    first seen in commit: 650099600ed6
  - (unknown file):1
    type: CustomRegex   preview: de*********************************.
    first seen in commit: 650099600ed6
  - (unknown file):2
    type: CustomRegex   preview: gr*********************************y
    first seen in commit: 6dbfc12a4171
  - (unknown file):1
    type: CustomRegex   preview: gr*********************************y
    first seen in commit: 6dbfc12a4171
  - NEWS.md:30
    type: CustomRegex   preview: de********************************y
    first seen in commit: 56a5f500186b
  - NEWS.md:30
    type: CustomRegex   preview: de***********************************s
    first seen in commit: 56a5f500186b
  - NEWS.md:30
    type: CustomRegex   preview: de**********************************n
    first seen in commit: 56a5f500186b
  - NEWS.md:30
    type: CustomRegex   preview: de*************************************.
    first seen in commit: 56a5f500186b
  - (unknown file):2
    type: CustomRegex   preview: da**********************************s
    first seen in commit: 1e9cc7c72f9d
  - (unknown file):1
    type: CustomRegex   preview: da**********************************s
    first seen in commit: 1e9cc7c72f9d
  - (unknown file):1
    type: CustomRegex   preview: ed************************************g
    first seen in commit: f529a1a8b686
  - (unknown file):2
    type: CustomRegex   preview: da******************************g
    first seen in commit: f529a1a8b686
  - (unknown file):1
    type: CustomRegex   preview: ky*************************************e
    first seen in commit: e585acc1f16f
  - (unknown file):2
    type: CustomRegex   preview: mi*********************************e
    first seen in commit: e585acc1f16f
  - spec/controllers/passwords_controller_spec.rb:40
    type: CustomRegex   preview: us*****************************'
    first seen in commit: 2900d731ef08
  - spec/models/user_spec.rb:20
    type: CustomRegex   preview: jo***********************************'
    first seen in commit: 2900d731ef08
  - spec/models/user_spec.rb:20
    type: CustomRegex   preview: jo************************************'
    first seen in commit: 2900d731ef08
  - spec/models/user_spec.rb:20
    type: CustomRegex   preview: jo****************************************'
    first seen in commit: 2900d731ef08
  - spec/models/user_spec.rb:19
    type: CustomRegex   preview: Jo************************************'
    first seen in commit: 2900d731ef08
  - spec/models/user_spec.rb:14
    type: CustomRegex   preview: fo*******************************'
    first seen in commit: 2900d731ef08
  - spec/models/user_spec.rb:14
    type: CustomRegex   preview: fo********************************'
    first seen in commit: 2900d731ef08
  - spec/models/user_spec.rb:19
    type: CustomRegex   preview: Jo***********************************'
    first seen in commit: 2900d731ef08
  - spec/models/user_spec.rb:14
    type: CustomRegex   preview: fo************************************'
    first seen in commit: 2900d731ef08
  - spec/models/user_spec.rb:19
    type: CustomRegex   preview: Jo****************************************'
    first seen in commit: 2900d731ef08
  - (unknown file):1
    type: CustomRegex   preview: su**************************************************y
    first seen in commit: be37c354594a
  - (unknown file):2
    type: CustomRegex   preview: mi*********************************y
    first seen in commit: be37c354594a
  - (unknown file):2
    type: CustomRegex   preview: mi**********************************n
    first seen in commit: 40362e92c81f
  - (unknown file):1
    type: CustomRegex   preview: mi**********************************n
    first seen in commit: 40362e92c81f
  - (unknown file):1
    type: CustomRegex   preview: vl*************************************y
    first seen in commit: 643784aecf7b
  - (unknown file):2
    type: CustomRegex   preview: vl*************************************y
    first seen in commit: 643784aecf7b
  - (unknown file):2
    type: CustomRegex   preview: vl**************************************.
    first seen in commit: 0847559e81c7
  - (unknown file):1
    type: CustomRegex   preview: vl***************************************n
    first seen in commit: 0847559e81c7
  - (unknown file):1
    type: CustomRegex   preview: vl**************************************.
    first seen in commit: 0847559e81c7
  - (unknown file):2
    type: CustomRegex   preview: dc***************************************n
    first seen in commit: 4c455ec9f208
  - (unknown file):1
    type: CustomRegex   preview: dc***************************************n
    first seen in commit: 4c455ec9f208
  - lib/clearance/user.rb:30
    type: CustomRegex   preview: em**************************************************d
    first seen in commit: bbe335b09c3d
  - lib/clearance/user.rb:30
    type: CustomRegex   preview: em***********************************n
    first seen in commit: bbe335b09c3d
  - lib/clearance/user.rb:30
    type: CustomRegex   preview: em*******************************************)
    first seen in commit: bbe335b09c3d
  - lib/clearance/user.rb:30
    type: CustomRegex   preview: em******************************************)
    first seen in commit: bbe335b09c3d
  - spec/controllers/passwords_controller_spec.rb:41
    type: CustomRegex   preview: us***************************************"
    first seen in commit: e13e7e45dfb1
  - spec/controllers/passwords_controller_spec.rb:41
    type: CustomRegex   preview: us*****************************"
    first seen in commit: e13e7e45dfb1
  - spec/controllers/passwords_controller_spec.rb:41
    type: CustomRegex   preview: us*********************************************,
    first seen in commit: e13e7e45dfb1
  - spec/controllers/passwords_controller_spec.rb:41
    type: CustomRegex   preview: us************************************"
    first seen in commit: e13e7e45dfb1
  - spec/controllers/passwords_controller_spec.rb:41
    type: CustomRegex   preview: us*******************************r
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:60
    type: CustomRegex   preview: Jo**************************************n
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:15
    type: CustomRegex   preview: fo***********************************n
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:59
    type: CustomRegex   preview: Jo**************************************n
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:16
    type: CustomRegex   preview: fo**********************************'
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:18
    type: CustomRegex   preview: fo***********************************'
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:19
    type: CustomRegex   preview: fo**************************************d
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:16
    type: CustomRegex   preview: fo***********************************************d
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:18
    type: CustomRegex   preview: fo************************************************d
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:59
    type: CustomRegex   preview: Jo***************************************'
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:19
    type: CustomRegex   preview: fo************************************************d
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:59
    type: CustomRegex   preview: Jo******************************************d
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:15
    type: CustomRegex   preview: fo********************************"
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:18
    type: CustomRegex   preview: fo****************************s
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:16
    type: CustomRegex   preview: fo***************************s
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:19
    type: CustomRegex   preview: fo****************************s
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:15
    type: CustomRegex   preview: fo************************************'
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:59
    type: CustomRegex   preview: Jo****************************************************d
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:18
    type: CustomRegex   preview: fo*******************************"
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:59
    type: CustomRegex   preview: Jo***********************************"
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:16
    type: CustomRegex   preview: fo******************************"
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:19
    type: CustomRegex   preview: fo*******************************"
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:19
    type: CustomRegex   preview: fo***********************************'
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:15
    type: CustomRegex   preview: fo*****************************s
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:16
    type: CustomRegex   preview: fo*********************************n
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:15
    type: CustomRegex   preview: fo*************************************************d
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:15
    type: CustomRegex   preview: fo***************************************d
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:59
    type: CustomRegex   preview: Jo********************************s
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:19
    type: CustomRegex   preview: fo**********************************n
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:18
    type: CustomRegex   preview: fo**************************************d
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:16
    type: CustomRegex   preview: fo*************************************d
    first seen in commit: e13e7e45dfb1
  - spec/models/user_spec.rb:18
    type: CustomRegex   preview: fo**********************************n
    first seen in commit: e13e7e45dfb1
  - spec/rails_root/log/test.log:2504
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2506
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2508
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2509
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2510
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2521
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2524
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2525
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2531
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2532
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2534
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2536
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2537
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2538
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2552
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2553
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2556
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2557
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2559
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2561
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2562
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2563
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2475
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2480
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2482
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2503
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2510
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2531
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2538
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2556
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:675
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:665
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:668
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:669
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:665
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:676
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:678
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:681
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:693
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:696
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:760
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:680
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:708
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:697
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:682
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:682
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:675
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:703
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:704
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:706
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:709
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:724
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:725
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:733
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:758
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:703
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:710
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:710
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:728
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:729
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:731
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:734
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:749
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:750
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:680
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:728
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:735
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:735
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:753
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:754
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:756
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:759
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:753
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2482
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2481
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:760
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2493
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2563
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2496
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2475
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2497
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2476
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2478
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2503
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2480
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2708
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2721
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2722
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2724
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2727
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2746
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2765
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2728
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2741
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2742
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2744
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2747
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2784
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2802
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2748
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2760
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2761
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2763
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2766
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2826
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2844
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2767
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2779
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2780
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2782
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2785
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2797
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2800
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2706
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2803
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2786
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2804
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2821
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2822
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2824
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2827
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2839
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2842
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2845
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2828
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2846
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2863
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2862
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2701
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2702
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2704
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2707
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2726
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:564
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:564
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:570
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:570
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:570
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:564
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:591
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:592
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:594
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:597
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:609
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:612
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:613
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:591
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:591
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:652
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:568
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:568
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:598
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:598
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:598
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:619
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:620
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:622
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:625
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:637
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:640
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:641
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:619
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:619
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:568
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:626
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:626
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:626
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:647
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:648
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:650
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:653
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:647
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:647
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:654
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:654
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:654
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:566
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:569
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:581
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:584
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:585
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:596
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:624
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1228
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1080
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1099
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1161
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1155
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1205
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1190
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1206
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1100
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1116
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1208
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1164
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1117
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1121
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1119
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1144
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1211
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1166
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1212
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1132
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1167
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1168
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1122
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1123
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1159
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1177
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1222
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1224
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1181
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1139
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1081
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1227
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1221
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1199
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1183
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1142
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1210
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1145
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1146
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1184
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1203
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1186
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1226
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1189
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2447
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2370
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2372
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2374
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2375
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2376
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2391
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2392
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2394
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2396
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2397
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2398
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2409
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2412
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2413
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2419
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2420
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2422
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2424
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2425
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2426
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2437
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2440
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2441
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2448
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2450
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2453
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1188
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2452
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2465
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2454
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2469
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2447
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2370
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2374
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2376
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2391
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2398
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2419
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2426
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4366
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4275
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4276
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4278
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4281
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4293
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4296
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4297
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4275
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4275
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4280
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4308
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4336
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4282
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4282
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4282
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4303
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4304
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4306
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4309
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4321
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4324
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4325
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4303
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4303
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4364
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4280
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4280
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4310
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4310
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4310
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4331
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4332
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4334
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4337
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4349
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4359
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4352
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4353
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4331
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4360
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4362
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4365
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4331
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4359
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4359
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2468
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1082
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4338
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4338
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4338
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4366
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4366
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1078
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1093
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:5982
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1140
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:5984
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:5987
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:5986
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6003
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1096
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1075
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1136
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1162
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:5981
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1076
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1098
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:5988
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6006
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6008
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6010
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6009
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6030
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6031
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6032
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6047
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6048
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6065
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6068
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6069
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6052
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6028
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6026
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6053
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6054
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6025
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6004
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6050
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6075
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6076
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6080
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6081
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4247
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4175
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4178
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4180
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4181
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4197
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4198
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4182
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4203
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4200
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4219
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4204
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4220
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4176
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4226
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4224
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4202
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4241
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4240
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4253
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4250
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4265
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4268
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4254
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4269
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4247
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4175
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4180
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4197
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4182
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4204
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4219
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4226
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4254
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2447
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4248
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2374
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2370
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2376
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2391
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2419
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4252
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2398
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2426
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4788
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2454
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4649
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4222
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4655
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4656
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4667
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4670
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4672
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4674
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4225
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4690
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4693
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4696
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2454
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4708
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4697
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4711
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4715
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4731
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4732
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4650
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4734
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4737
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4713
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4738
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4749
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4714
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4752
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4736
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4756
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4772
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4755
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4775
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4773
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4778
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4754
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4792
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4811
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4795
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4796
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4798
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4777
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4801
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4695
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4815
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4817
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4818
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4820
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4673
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8623
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8563
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8564
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8566
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8591
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8592
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8594
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8540
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8597
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8598
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8612
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8613
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8616
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4802
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8619
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4691
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8622
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8623
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8528
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8529
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8535
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8536
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8538
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8596
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8541
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8542
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8553
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8556
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8557
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8569
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8581
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8584
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8621
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8585
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8570
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8563
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8591
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8540
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8598
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8528
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8542
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8570
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6131
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6132
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6134
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6137
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6159
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6160
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6162
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6108
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6165
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6166
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6177
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6180
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6093
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6096
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6097
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6103
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6104
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6106
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6136
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6109
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6110
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6121
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6124
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6125
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6149
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6152
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6153
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6164
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6131
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6138
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6159
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6108
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6166
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6093
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6103
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6108
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6110
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6131
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6138
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6159
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6166
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6093
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6103
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6108
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6110
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6110
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6093
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6103
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6138
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11538
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11408
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11409
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11411
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11413
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11414
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11415
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11424
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11428
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11431
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11432
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11434
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11436
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11437
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11438
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11447
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11451
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11453
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11454
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11456
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11458
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11459
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11460
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11469
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11473
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11475
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11476
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11478
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11480
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11481
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11482
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11491
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11495
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11497
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11498
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11500
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11502
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11503
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11504
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11513
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11514
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11516
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11518
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11519
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11520
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11539
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7333
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7335
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7338
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7337
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7358
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7339
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7361
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7364
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7363
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7386
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7365
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7387
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7388
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7390
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7394
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7393
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7403
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7392
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7419
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7420
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7433
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7434
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7436
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7438
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7439
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7449
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7440
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7465
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:7466
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11070
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10968
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10970
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10972
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10973
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10974
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10985
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10988
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10989
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10995
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10996
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10998
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11000
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11001
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11002
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11016
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11017
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11020
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11021
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11023
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11025
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11026
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11027
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11041
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11042
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11045
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11046
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11048
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11050
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11051
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11052
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11066
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11067
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11071
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11073
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11076
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11075
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10855
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10789
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10790
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10792
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10749
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10795
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10796
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10811
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10812
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10814
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10765
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10817
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10818
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10833
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10834
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10836
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10794
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10839
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10840
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10856
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10858
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10861
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10816
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10873
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10862
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6600
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6616
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6436
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6438
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6440
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6441
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6442
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6453
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6456
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6458
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6459
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6460
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6477
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6478
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6480
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6482
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6483
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6484
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6495
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6498
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6500
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6501
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6502
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6518
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6519
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6521
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6523
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6524
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6525
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6536
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6539
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6541
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6542
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6543
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6559
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6560
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6562
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6564
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6565
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6566
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6577
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6580
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6582
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6583
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6584
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6601
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6603
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6606
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6605
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6607
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6620
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6623
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10967
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10876
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10877
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10883
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10884
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10886
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10888
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4779
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8568
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8617
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8616
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6078
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4652
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4654
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4800
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:4237
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8535
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:6082
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10889
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10890
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10901
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10904
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10905
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10911
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10912
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10914
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10916
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10917
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10918
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10929
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10932
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10933
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10939
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10940
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10942
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10944
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10945
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10946
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10957
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10960
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10961
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10967
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10876
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10883
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10888
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10890
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10911
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10918
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10939
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10946
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10967
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10876
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10883
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10888
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10890
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10911
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10918
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10939
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:10946
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8906
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8741
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8742
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8744
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8746
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8747
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8748
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8761
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8762
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8764
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8766
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8767
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8781
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8782
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8784
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8786
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8787
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8788
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8801
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8802
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8804
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8806
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8807
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8808
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8820
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8821
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8823
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8825
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8826
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8827
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8839
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8840
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8842
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8844
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8845
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8846
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8857
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8860
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8862
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8863
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8864
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8881
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8882
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8884
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8886
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8887
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8507
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8888
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8429
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8899
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8430
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8902
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8432
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8904
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8434
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8435
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8905
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8436
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8451
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8768
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8454
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8457
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8458
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8456
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8469
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8473
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8472
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8479
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8482
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8480
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8484
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8485
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8497
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8500
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8501
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8510
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8512
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8513
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8525
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8514
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8429
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8434
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8436
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8451
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8479
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8458
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8486
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8507
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8514
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8451
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8429
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8434
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8486
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8514
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3011
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2865
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2868
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2867
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2880
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2883
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2886
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2887
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2904
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13287
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13200
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2906
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13215
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13216
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13218
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13221
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13215
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13220
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13242
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13222
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13222
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13237
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13238
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13240
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13243
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13237
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13264
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13292
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13244
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13244
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13259
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13260
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13262
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13265
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13277
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13280
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13220
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13281
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13259
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13266
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13266
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13288
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13290
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13293
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13305
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13308
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13309
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13287
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13294
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13294
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9721
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9635
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9636
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9638
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9640
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9641
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9642
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9656
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9657
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9658
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9660
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9662
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9663
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9664
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9677
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9678
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9679
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9681
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9683
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9684
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9685
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9698
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9699
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9700
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9702
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9704
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9705
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9706
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9733
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9736
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9737
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9739
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9742
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9741
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9762
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9743
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9765
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9768
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9767
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9790
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9769
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9791
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9792
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9794
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9797
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9796
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9807
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9798
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11367
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11206
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11208
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11210
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11211
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11212
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2903
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2869
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8479
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8436
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8507
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8508
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13200
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8452
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8486
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8458
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2885
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11224
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11227
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11229
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11230
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11243
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11246
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11225
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11249
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11250
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11261
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11264
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11266
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11267
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11268
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11285
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11286
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11290
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11288
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11291
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11292
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11306
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11308
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11309
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11310
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11326
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11327
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11329
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11331
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11332
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11344
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11333
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11349
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11347
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11350
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11351
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11368
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11370
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11373
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11385
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11374
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11388
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11391
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11390
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11392
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11244
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16290
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16152
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16157
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9071
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16159
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16158
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11372
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16178
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16180
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16181
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16176
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16193
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16196
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16198
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16199
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16200
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16216
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16217
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16219
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16221
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16222
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16223
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16232
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16236
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16239
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16240
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16242
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16244
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16245
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16246
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16255
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16259
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16261
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16262
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16264
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16266
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16267
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16268
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16277
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16281
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16283
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11248
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16286
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16288
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16289
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16299
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16303
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16305
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16306
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16308
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16310
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16311
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16312
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11231
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15747
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15648
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15663
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15664
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15666
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15668
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15669
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15670
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15681
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15684
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15685
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15691
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15692
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15694
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15696
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15697
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15698
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15709
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15712
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15713
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15719
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15720
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15722
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15724
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15725
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15726
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15737
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15740
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15741
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15747
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15647
    type: CustomRegex   preview: se*******************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15648
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15663
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15668
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15670
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15691
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15698
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15663
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15647
    type: CustomRegex   preview: se*******************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16182
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15670
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16175
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15698
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15719
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15828
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2908
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12125
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9020
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15726
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13828
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13689
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14598
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13692
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13694
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13695
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13696
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13707
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13710
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13712
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13713
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16155
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15668
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15748
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15752
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15750
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15754
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15765
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:11303
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15768
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15775
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15769
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15776
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15778
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15780
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15782
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15781
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15793
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15796
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15803
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15691
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15797
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15808
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15806
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15810
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15824
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15726
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15829
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15831
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13690
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15809
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15747
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15833
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15835
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15849
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15828
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15748
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15752
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15754
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15850
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15775
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15782
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15803
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15753
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16284
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15647
    type: CustomRegex   preview: se*******************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15810
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15835
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14577
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2909
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15719
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12103
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12106
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12109
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12110
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12140
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12141
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15834
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12143
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12166
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12146
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15825
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12145
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15804
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12194
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12195
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12104
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12171
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12198
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12211
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12201
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12228
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12241
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12242
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12244
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12247
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12257
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12246
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12248
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14599
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14600
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14602
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14605
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14604
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14615
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14606
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14631
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14632
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14645
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14646
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14648
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14651
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14650
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14661
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14652
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14677
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:14678
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2910
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2921
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2924
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2926
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2927
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2928
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2944
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2945
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2947
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2949
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2972
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2994
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2950
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2951
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2960
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2964
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2967
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2968
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2983
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2970
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2974
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2973
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3016
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3012
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2987
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3033
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2989
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2990
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2992
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2995
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:2996
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3005
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3009
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3014
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3017
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3018
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3027
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3031
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:3034
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9027
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13714
    type: CustomRegex   preview: 4d******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18232
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18166
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18167
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18169
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18126
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18172
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18173
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18188
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18189
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18191
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18142
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18194
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18195
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18210
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18211
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9028
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9030
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8927
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9033
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9034
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9024
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9043
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9049
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9050
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9052
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8945
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9055
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9056
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9047
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9065
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9072
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9074
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9077
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8968
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9078
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9069
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8922
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8923
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8925
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8986
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8928
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8929
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8940
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8943
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9009
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8946
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8947
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8963
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8964
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8966
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9032
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8969
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8970
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8981
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8984
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9054
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8987
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:8988
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9004
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9005
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9007
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9076
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9010
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9011
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:9087
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13730
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18213
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19502
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18915
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18785
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18786
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18788
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18790
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18791
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18792
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18801
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18805
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18808
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18809
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18811
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18813
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18814
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18815
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18824
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18828
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18830
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18831
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18833
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18835
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18836
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18837
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18846
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18850
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18852
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18853
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18855
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18857
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16134
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15973
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15974
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15976
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15978
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15979
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15980
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15993
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15994
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15996
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15998
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15999
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16000
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16013
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16014
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16016
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16018
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16019
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16020
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16032
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16033
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16035
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16037
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18344
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18253
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18254
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18260
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18261
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18263
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18265
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18266
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18267
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18278
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18281
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18282
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18288
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18289
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18291
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18293
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18294
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18295
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18306
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18309
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18310
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18316
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18317
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18319
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18321
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12108
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18322
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18334
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18323
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18337
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18338
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18253
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18344
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18260
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18265
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18267
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16038
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13731
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13735
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13736
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13737
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13748
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13751
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13753
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13754
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13755
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13771
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13772
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13774
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13776
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13777
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13778
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13789
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13792
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13794
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13795
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13796
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13812
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13813
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13815
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13817
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13818
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13819
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13832
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13851
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13835
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13836
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13838
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13840
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13841
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13842
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13855
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13857
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13858
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13860
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18171
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19480
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18858
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18288
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18216
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19481
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16039
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18859
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18295
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18316
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18323
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18344
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18253
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18260
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18265
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18267
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18868
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18447
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18345
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18347
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18349
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18350
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18351
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18362
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18365
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18366
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18372
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18373
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18375
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18377
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18378
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18379
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18393
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18217
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19483
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16051
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16052
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16054
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16056
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16057
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16058
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16069
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16072
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16074
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16075
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16076
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16093
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16094
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16096
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16098
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16099
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16100
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19485
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19486
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19487
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18288
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18295
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18316
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18323
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18872
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18874
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18875
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18877
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18879
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18880
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18881
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18890
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18891
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18893
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18895
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18896
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18897
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18916
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18703
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18583
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18585
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18587
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18588
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18589
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18601
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18602
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18604
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18394
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18233
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18606
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18397
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20861
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18235
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19514
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18193
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18607
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20770
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19517
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16111
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18608
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18238
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18398
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13315
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13316
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13318
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13321
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13320
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13333
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13322
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13336
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13337
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13406
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13343
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13344
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13346
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13348
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22720
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22750
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22762
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22765
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22766
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22768
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22770
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22771
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22772
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22791
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22794
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22796
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22797
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22798
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22819
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22820
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22821
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22823
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22825
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22826
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22827
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22836
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22852
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23430
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23460
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23472
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21241
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21100
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21101
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21103
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21106
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21105
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21125
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21107
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21120
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21121
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21123
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21126
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21144
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21163
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23475
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21127
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21139
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21140
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21142
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21145
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21181
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21205
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21146
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23476
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21158
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21159
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21161
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21164
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21176
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21179
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21223
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21246
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21182
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21165
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21264
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23478
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21183
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23480
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21200
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21201
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21203
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21206
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21218
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21221
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21224
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21207
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23481
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21225
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21242
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21244
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21247
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21259
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23482
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21262
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21265
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21248
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23501
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23504
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12173
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23507
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23508
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23529
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23530
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23531
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23533
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23535
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23536
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23537
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23546
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23562
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24140
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24170
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24182
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24185
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24186
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24188
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24190
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24191
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24192
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24211
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:23506
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13733
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24217
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24218
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24239
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24240
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24241
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24243
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24245
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24246
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24247
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20967
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20872
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20875
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20876
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20882
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20883
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24216
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20887
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20888
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20889
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20900
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20903
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12147
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20904
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20911
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20910
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20913
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20915
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20916
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20917
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20931
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20932
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20935
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20936
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20940
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20938
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20941
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20956
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20957
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20960
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20961
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20963
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20965
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20966
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20967
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20872
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20882
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20887
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20889
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20885
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24214
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20942
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12200
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12172
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:15648
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12227
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12137
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12202
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12169
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:12196
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20910
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20917
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20935
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20942
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20960
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16114
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16116
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16117
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16118
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16135
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16137
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16140
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16139
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16141
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18620
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18239
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20771
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18400
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13349
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19518
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24806
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24850
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24880
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24892
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24895
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24896
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24900
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24898
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24902
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24901
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24921
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24926
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24924
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24928
    type: CustomRegex   preview: 4d******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24927
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24949
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24950
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24951
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24955
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24953
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:24957
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26377
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26210
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26211
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26213
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26216
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26226
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26215
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26270
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26322
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26300
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26312
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26320
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26315
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26348
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26316
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26318
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26321
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26341
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26346
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:26344
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22040
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21983
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21996
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21997
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21998
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22000
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22002
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22003
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22004
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22017
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22018
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22019
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22021
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22023
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22024
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22025
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22052
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22055
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22056
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22058
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22061
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22060
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22081
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22062
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22084
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22087
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22086
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22109
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22088
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22110
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22111
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22113
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22116
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22115
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22126
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22117
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22142
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:22143
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21412
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21282
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21283
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21285
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21287
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21288
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21289
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21300
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21303
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21305
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21306
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21307
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21323
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21328
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21329
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21330
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21339
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21343
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21346
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21347
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21349
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21351
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21352
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21353
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21362
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21366
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21368
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21369
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21371
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21373
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21374
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21375
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21384
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21388
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21390
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21391
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21393
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21395
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21396
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21397
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21406
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21410
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21413
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21415
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21418
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21417
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21419
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21428
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21429
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21431
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21433
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21434
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21435
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:993
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:893
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:894
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:896
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:899
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:898
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:937
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:918
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:900
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:913
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:914
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:916
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:919
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:974
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:956
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:998
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:920
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:932
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:933
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:935
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:938
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1016
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1039
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1057
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:939
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:951
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:952
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:954
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:957
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:969
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:972
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:958
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:976
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:975
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25516
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25560
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25590
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25505
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25602
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:996
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25605
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25606
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:999
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25612
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25608
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1011
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25631
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25634
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25610
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:994
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25636
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25667
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19520
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25659
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19522
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19543
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19524
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19546
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19549
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19548
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19571
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19550
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19572
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19573
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19575
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25611
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19577
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19588
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19579
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19604
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19605
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19618
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19619
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19621
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19624
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19623
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19634
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19625
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18621
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18250
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20773
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18402
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13350
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3011
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18403
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18404
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18418
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18419
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18422
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18423
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18425
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18427
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18428
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18429
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18443
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18444
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18448
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18450
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18453
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18452
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18623
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18625
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18626
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18627
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18638
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20775
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13361
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2865
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25638
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13364
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18641
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20776
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2862
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2701
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2702
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4366
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4275
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4276
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4278
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4281
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4293
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4296
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4297
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4275
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4275
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4280
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4308
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4336
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4282
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4282
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4282
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4303
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4304
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4306
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4309
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4321
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4324
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4325
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4303
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4303
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4364
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4280
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16933
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21326
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4310
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4280
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19578
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4310
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:5982
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6082
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:19523
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25501
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25503
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25506
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1014
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4310
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:5986
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6003
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:5987
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6008
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6006
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6010
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:5984
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6028
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6030
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6031
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6032
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6047
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6009
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:5988
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6050
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6053
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6054
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6026
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6025
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6052
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6068
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6075
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6076
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6080
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6069
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6048
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4334
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4331
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6065
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4352
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4331
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4353
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4331
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4338
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6081
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4338
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4349
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4359
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4360
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4362
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4338
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4337
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4359
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4359
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4366
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:654
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4366
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:566
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4365
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6004
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:5981
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4332
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6078
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:564
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:584
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:564
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:564
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:585
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:1017
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:570
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:592
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:594
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:25637
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:609
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:569
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:612
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:591
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:591
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:613
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16868
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16870
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16872
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16874
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16875
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:570
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16876
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:624
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16891
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16895
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16896
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16893
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16897
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16911
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16912
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16914
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16916
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16917
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16918
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16945
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16948
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16949
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16951
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16954
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16953
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16974
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16955
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16977
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16980
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16979
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:17002
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16981
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:17003
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:17004
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:17006
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:17009
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:568
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:17008
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:17010
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:17019
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2563
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2475
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16910
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2480
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2478
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2481
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2493
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2482
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2496
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2497
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2503
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2504
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2506
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2509
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2510
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2521
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2524
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2525
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2531
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2532
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2534
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:591
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2537
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2538
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2552
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2553
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2556
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2557
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2559
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2561
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2562
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2563
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2475
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2480
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2482
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2503
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2510
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2531
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2538
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2556
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13365
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13371
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13372
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13374
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13376
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13377
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13378
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13389
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13392
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13399
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13400
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13402
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13404
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13405
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13406
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13315
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13320
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13322
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13343
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13350
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13393
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13371
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13378
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13399
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13406
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13315
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13320
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13322
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2867
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2868
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13343
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2869
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2880
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2883
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13350
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2885
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2886
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2887
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2903
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13371
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2904
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18643
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18644
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18645
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18662
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18663
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18665
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18667
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18668
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18669
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:570
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18680
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18685
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18686
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18687
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18704
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18706
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18709
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18708
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18721
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18710
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18744
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18726
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18724
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18728
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18745
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18747
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18750
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18749
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18751
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18762
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18765
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18767
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18768
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18769
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18727
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20777
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2704
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2906
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6600
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20788
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2706
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7333
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7335
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7338
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7337
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7358
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7339
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7361
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7364
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7363
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7386
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7365
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7387
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7388
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7390
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7393
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7392
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7403
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7394
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7419
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7420
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7433
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7434
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7436
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7439
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7438
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7449
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7440
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7465
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:7466
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:993
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:893
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:894
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:896
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:899
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:898
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:918
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:937
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:900
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:913
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:914
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:916
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:919
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:956
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:974
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:998
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:920
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:932
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:933
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:935
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:938
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1016
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1039
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1057
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:939
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:951
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:952
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:954
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:957
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:969
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:972
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:975
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:958
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:976
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:994
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:996
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:999
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1011
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1014
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1017
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4731
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4649
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4650
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4652
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4655
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4667
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4670
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4673
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4654
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4672
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4695
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4713
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:652
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:568
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:568
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:598
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:598
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:598
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:619
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:620
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:622
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:625
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:637
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:640
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:641
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:619
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:619
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:626
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:626
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:626
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4656
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:647
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2908
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2909
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2910
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2921
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2924
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2926
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2927
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2928
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2944
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2945
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2947
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6436
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2949
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2950
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20791
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20792
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20798
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20799
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20801
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20803
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20804
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20805
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20816
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20819
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20820
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20826
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20827
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20829
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20831
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20832
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20833
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20844
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13378
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2707
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:648
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4736
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4754
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4777
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4800
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4674
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6438
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:650
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:653
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:760
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:647
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:665
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:668
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:669
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:675
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:676
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:678
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:680
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:647
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9721
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9635
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6440
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:681
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9636
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9638
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9640
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9641
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9642
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9656
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9657
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9658
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9660
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9662
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9663
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9664
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9677
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9678
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9679
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9681
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9683
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9684
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9685
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9698
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9699
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9700
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9702
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9704
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9705
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9706
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9733
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9736
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9737
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9739
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9742
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9741
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9762
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9743
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9765
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9768
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9767
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9790
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9769
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9791
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9792
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9794
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9797
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9796
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9807
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9798
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4247
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4175
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4176
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4178
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4180
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4181
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4182
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4197
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4198
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4200
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4202
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4203
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4204
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4219
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4220
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4222
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4224
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4225
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4226
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4237
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4240
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4241
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4248
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4250
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4253
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4252
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4265
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4254
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4268
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4269
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4247
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4175
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4180
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4182
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4197
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4204
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4219
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4226
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4254
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8906
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8741
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8742
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:21324
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8744
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8747
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8748
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8761
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8746
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8762
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8764
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8766
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8767
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8768
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8781
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8782
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8784
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8786
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8787
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8788
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:18683
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8804
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8802
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8806
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8808
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8807
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8820
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8821
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8823
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8826
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8825
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8827
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8839
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8842
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8844
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8840
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8845
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8857
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8846
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16889
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8863
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8864
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8862
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8881
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8882
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8884
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8886
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8887
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8888
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8902
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8904
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8801
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8899
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:581
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8528
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8535
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16869
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:596
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8540
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8538
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8541
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8553
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8556
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8557
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8563
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8564
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8566
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8568
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8569
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8570
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8581
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8584
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8585
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8592
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8594
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8597
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8596
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8623
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8598
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8612
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8613
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8616
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8617
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8619
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8621
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8622
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8623
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8528
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8535
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8540
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8542
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8563
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8570
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8591
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8598
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8616
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11070
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10968
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10970
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10972
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10973
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10974
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10985
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10988
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10989
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10995
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10996
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10998
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11000
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11001
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11002
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11016
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11017
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11020
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11021
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11023
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11025
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11026
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11027
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11041
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11042
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11045
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11046
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11048
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11050
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11051
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11052
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11066
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11067
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11071
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11073
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11076
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11075
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8507
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8429
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8430
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8432
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8434
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8435
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8436
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8451
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8452
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8454
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8456
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8457
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8458
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8469
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8472
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8473
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8479
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8480
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8482
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8484
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8485
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8486
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8497
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8500
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8501
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8508
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8510
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8513
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8512
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8525
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8514
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8507
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8429
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8434
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8436
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8451
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8458
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8479
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9071
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2370
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12125
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13828
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14598
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14577
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14599
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14600
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14602
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14605
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14604
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14615
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14606
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14631
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14632
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14645
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14646
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14648
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14651
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14650
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14661
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14652
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14677
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:14678
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1228
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1075
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1076
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1078
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1080
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1081
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1082
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1093
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1096
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1098
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1099
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1100
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1116
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1117
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1119
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1121
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1122
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1123
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1132
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1136
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1139
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1140
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1142
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1144
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1145
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1146
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1155
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1159
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1161
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1162
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1164
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1166
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1167
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1168
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1177
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1181
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1183
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1184
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1186
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1188
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1189
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1190
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1199
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1203
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1205
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1206
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1208
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1210
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1211
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1212
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1221
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1222
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1224
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1226
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:1227
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15747
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15647
    type: CustomRegex   preview: se*******************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15647
    type: CustomRegex   preview: se*******************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15647
    type: CustomRegex   preview: se*******************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15648
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15648
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15648
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15663
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15664
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15666
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15669
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15681
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15684
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15685
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15663
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15663
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15668
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15696
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15724
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15670
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15670
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15670
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15691
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15692
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15694
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15697
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15709
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15712
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15713
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15691
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15691
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15668
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15668
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15698
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15698
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15698
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15719
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15720
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15722
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15725
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15737
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15740
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15741
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15719
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15719
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15726
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15726
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15726
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11367
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11206
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11208
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11210
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11211
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11212
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11224
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11225
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11227
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11229
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11230
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11231
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11243
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11244
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11246
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11248
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11249
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11250
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11261
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11264
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11266
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11267
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11268
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15747
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11285
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11286
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11288
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11290
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15747
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11291
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11292
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11303
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2951
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20847
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2708
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10855
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13689
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6441
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:682
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8922
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2372
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12103
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12104
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12106
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12108
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12109
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12110
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12137
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12140
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12141
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12143
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12146
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12145
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12166
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12147
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12169
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12172
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12171
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12194
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12173
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12195
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12196
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12198
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12201
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12200
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12211
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12202
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12227
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12228
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12241
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12242
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12244
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12247
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12246
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10967
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10876
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10877
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10883
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10884
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10886
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10888
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10889
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10890
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10901
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12257
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10904
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10911
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10905
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10912
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10914
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10917
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10916
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10929
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:12248
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10918
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10932
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10933
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10911
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10939
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10940
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10942
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10944
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10945
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10946
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10957
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10960
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10961
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10967
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10876
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10883
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10888
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10890
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10918
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10939
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10946
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10967
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10876
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10883
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10888
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10890
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10911
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10918
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10939
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10946
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10789
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10790
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10792
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10749
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10795
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10796
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10811
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10812
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10814
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10765
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10817
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10818
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8529
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10834
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10836
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10794
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10839
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10840
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10856
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10858
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2536
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10861
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2476
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10862
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10816
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:693
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:696
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:697
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:704
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:703
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:706
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:709
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:708
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:724
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:725
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8542
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:710
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2508
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:731
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:16890
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:733
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:734
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:735
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:749
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:750
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8591
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:597
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8536
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:728
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10873
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:760
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:729
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:675
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:680
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:682
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:703
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:754
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:728
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8905
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:756
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:758
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:753
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:665
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8860
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:753
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8486
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13690
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13692
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13694
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13695
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13696
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13707
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13710
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8507
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13712
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13713
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13730
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:710
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13733
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13735
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8923
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2375
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11306
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20848
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2960
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11538
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11424
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11408
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13714
    type: CustomRegex   preview: 4d******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11409
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11411
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11413
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11414
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11415
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11428
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2721
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11434
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11436
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11437
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11438
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11447
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11451
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11453
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11431
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18232
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18167
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18169
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18126
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18166
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18172
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18173
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18189
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18191
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18142
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18194
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18195
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18210
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18211
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11308
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18171
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18216
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18188
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18217
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18235
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18238
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18193
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18250
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18239
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19502
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19480
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19481
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19483
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19485
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19486
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19487
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19514
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19517
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19518
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19520
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19523
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19522
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19543
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19524
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19546
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19549
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19548
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19571
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19550
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19572
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19573
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19575
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19578
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19577
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19588
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19579
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19604
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19605
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19618
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19619
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19621
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19624
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19623
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19634
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:19625
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18744
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18583
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18585
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18587
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18588
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18589
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18601
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18602
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18604
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18606
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18607
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18608
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18620
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18621
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18623
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15828
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15829
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15748
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15750
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15752
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15753
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15754
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15765
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15768
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15769
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15775
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15776
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15778
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15780
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15781
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15782
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15793
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15796
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15797
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15803
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15804
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15806
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15808
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15809
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15810
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15824
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15825
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15831
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15834
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15849
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15833
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15850
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15835
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15828
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15748
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15752
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15754
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15775
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15782
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15803
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15810
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15835
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16933
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16868
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16869
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16870
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16872
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16874
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16875
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16876
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16889
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16890
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16891
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16893
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16895
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16896
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16897
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:759
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16911
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16912
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16914
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18233
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13736
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13731
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:10833
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11432
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4690
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18213
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:735
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6442
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16910
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2374
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16917
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16916
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16945
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16948
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16949
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16951
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16954
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16953
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16974
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16955
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16977
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16980
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16979
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:17002
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16981
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:17003
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:17006
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:17019
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:17008
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:17010
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16134
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16135
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:17009
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15973
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15976
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15978
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15980
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15993
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15979
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15998
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15999
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16918
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16000
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16016
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16018
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16013
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16032
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15996
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16033
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16037
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16038
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16039
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16052
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16051
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16056
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16054
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16058
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16069
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16057
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16074
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16072
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16076
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16094
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15974
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16096
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16099
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16035
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16020
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16111
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16098
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16114
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16093
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16117
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16118
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16140
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16139
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16141
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:15994
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16075
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16100
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18785
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18915
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16137
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18790
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18791
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18792
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18801
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18809
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18808
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18811
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18824
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18828
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18830
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18831
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18833
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18835
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18836
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18837
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18846
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18850
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18852
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18853
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18855
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18857
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18858
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18859
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18868
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18872
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18874
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18875
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18879
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18877
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18881
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18890
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18891
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18893
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18895
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18896
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18897
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18916
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18880
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13406
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13315
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13316
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13318
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13320
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13321
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13322
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13333
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13336
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13337
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13343
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13344
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13346
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13348
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13349
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13350
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13361
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13364
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13371
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13372
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13374
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13377
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13376
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13389
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13378
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13392
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13393
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13371
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13399
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13400
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13402
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13404
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13405
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13406
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13315
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13320
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13322
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13365
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13343
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13350
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13287
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13200
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13215
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13216
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13378
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13218
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13220
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13221
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13222
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13237
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13343
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13238
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13240
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21105
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8925
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8927
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8928
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8929
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8940
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8943
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8945
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8946
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8947
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8963
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8964
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8966
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8968
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8969
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8970
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8981
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8984
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8986
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8987
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8988
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9004
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9005
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9007
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9009
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18805
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16014
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6453
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22040
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21983
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21996
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:17004
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16116
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21998
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22000
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22002
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22003
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18814
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22004
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8514
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18253
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8429
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18260
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18261
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18254
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18263
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2964
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20854
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4691
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13737
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18786
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2722
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11309
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2370
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18813
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18788
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22017
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:654
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18266
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13748
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9024
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18815
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2376
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16019
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9010
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9011
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9020
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21997
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6456
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8434
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18625
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:13399
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11459
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11454
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11460
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2967
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11469
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2968
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11473
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11475
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2970
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11476
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20855
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2972
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4693
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2724
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18626
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20872
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22018
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18265
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13751
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9027
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11478
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20857
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6458
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2391
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13753
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2392
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2726
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18278
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2394
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:654
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8436
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11326
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2973
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4696
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20875
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9028
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20859
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2447
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18627
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21412
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18447
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18345
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22019
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21100
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11480
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21282
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8451
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6459
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11327
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4708
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20876
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13754
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21101
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18347
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22021
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13242
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20860
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18267
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2974
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2727
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21125
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11329
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20882
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6460
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18349
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21283
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2396
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13399
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11481
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9030
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18638
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20967
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4711
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2728
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20826
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13755
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20861
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22023
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13243
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21103
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6477
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11331
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18350
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18281
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21285
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9032
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18641
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2983
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2741
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20883
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6131
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6093
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6096
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6103
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11456
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6097
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6108
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6109
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11482
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6121
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6106
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6124
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6125
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6134
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6137
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6110
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6149
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6136
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6153
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6159
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6152
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6164
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6166
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6138
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6180
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6093
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6177
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6103
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6110
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6131
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6138
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6159
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11458
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6104
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8458
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6166
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8479
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8486
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:8514
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6103
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6108
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6110
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6131
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6138
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6159
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6166
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6093
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6103
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6108
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21107
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11332
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18351
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21287
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6132
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18344
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11491
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18643
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9033
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6165
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2742
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21120
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6093
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4714
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13771
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20770
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22024
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13244
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2987
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6160
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6131
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6162
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2376
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18294
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18295
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18306
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18309
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11333
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18310
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18316
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18317
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13259
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6480
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18365
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18366
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18372
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18373
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18375
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18377
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18378
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18379
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18393
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18394
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18397
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18398
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21288
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2397
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6110
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18400
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6482
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11495
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11344
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9034
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18644
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2744
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2989
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20887
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21121
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2409
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13772
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20771
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18402
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21289
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22025
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18319
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20885
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6108
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6478
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18282
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18362
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18289
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18288
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18291
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20770
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11310
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18293
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18321
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18322
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18323
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18334
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18337
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18338
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18344
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18253
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18260
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9043
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2990
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2412
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13774
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22052
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6483
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16159
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16175
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16176
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16178
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16180
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16181
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16182
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18645
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20888
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18403
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13260
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - (unknown file):1
    type: CustomRegex   preview: jo***************************************s
    first seen in commit: 6caee9ccd154
  - (unknown file):2
    type: CustomRegex   preview: jo***************************************s
    first seen in commit: 6caee9ccd154
  - spec/rails_root/vendor/log/test.log:16290
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16152
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16155
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16157
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16217
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16222
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16232
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16193
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16223
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16221
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16239
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16240
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16242
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16245
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16244
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16255
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16246
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16198
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16264
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16262
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16266
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16267
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16199
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16277
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16281
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16284
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16283
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16288
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16289
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16299
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16200
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16303
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16305
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16306
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16308
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16311
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16312
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22055
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22056
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22061
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22060
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22081
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16216
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22062
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22084
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22087
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16219
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22109
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22088
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22110
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16158
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16310
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22113
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22115
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2424
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2413
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2391
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2398
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2419
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2420
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2422
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2452
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2425
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16286
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16236
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16261
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2437
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2441
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2450
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2448
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2453
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2374
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2454
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2468
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2469
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22058
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22086
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22111
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2426
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2465
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2419
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20773
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2426
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20775
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20776
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20777
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20788
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20798
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2440
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20791
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20805
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2447
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16196
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16268
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:16259
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20829
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20861
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21300
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22126
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2454
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20889
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20799
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20804
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18662
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11347
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2746
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13776
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18265
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20792
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13262
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11497
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20775
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6484
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9047
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13406
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21123
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20831
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2992
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21303
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - (unknown file):1
    type: CustomRegex   preview: dc***********************************y
    first seen in commit: 61b4f2fdf342
  - spec/rails_root/vendor/log/test.log:20801
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22117
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11498
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13315
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20900
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13777
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2398
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11349
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20816
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18665
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9049
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2747
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21305
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13264
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21144
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22142
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18418
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2994
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2748
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20819
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20832
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - (unknown file):2
    type: CustomRegex   preview: dc***********************************y
    first seen in commit: 61b4f2fdf342
  - spec/rails_root/vendor/log/test.log:11500
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21306
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20820
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11350
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20827
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18667
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9050
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20777
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20904
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21126
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18404
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6498
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2760
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18267
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11370
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11351
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11372
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18663
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11374
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11368
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2995
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11391
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11388
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20803
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6495
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18419
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11390
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22143
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9052
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21139
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21140
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21142
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21163
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21145
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21146
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21158
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21159
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21161
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21181
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21164
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21165
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21127
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13778
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21179
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21106
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6500
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21223
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21176
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21182
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21200
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21201
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11385
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18669
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21205
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6501
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6519
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6502
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6521
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6524
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6523
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6525
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6539
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6536
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6541
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6542
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18680
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18685
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18683
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18686
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21183
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11392
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18703
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18704
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6543
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6559
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18706
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6562
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6564
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6565
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6566
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6577
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6580
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6582
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6583
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6584
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6601
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6603
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6606
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6605
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6607
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6616
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6620
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6623
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21203
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13322
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13350
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:22116
    type: CustomRegex   preview: em****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13371
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13378
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13399
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18708
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18709
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18721
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18710
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18726
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6518
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18728
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18724
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18745
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18747
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18750
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18749
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18762
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18765
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18751
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18768
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18767
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18769
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11502
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11503
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11513
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11504
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11514
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11516
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11518
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11520
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11519
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20911
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20913
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20910
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20916
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20917
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20931
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20932
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20935
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20936
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21307
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13265
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13320
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:6560
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18668
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2996
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18687
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20833
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20903
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13789
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18727
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2370
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21323
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21246
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2761
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20938
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18422
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13792
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20844
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13266
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21206
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21324
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3005
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9054
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11539
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - (unknown file):1
    type: CustomRegex   preview: cp***************************************n
    first seen in commit: ea5d5e729fb0
  - (unknown file):2
    type: CustomRegex   preview: cp***************************************n
    first seen in commit: ea5d5e729fb0
  - spec/rails_root/vendor/log/test.log:20847
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20848
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20854
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20855
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20857
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20859
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20860
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20861
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20770
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20775
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20777
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20798
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20805
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20826
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20833
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21326
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20854
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21328
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13277
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2763
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20940
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2374
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18423
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13794
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9055
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3009
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21207
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21264
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20941
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18288
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18425
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2376
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18427
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21329
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13280
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2765
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20942
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9056
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13795
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2391
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21330
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13281
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2766
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20956
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18428
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4697
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9065
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3014
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13796
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20957
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2767
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13288
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20805
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20826
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20833
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20854
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20861
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20770
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20775
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20777
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3017
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13290
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20960
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2779
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2782
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20861
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2780
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20770
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20775
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20777
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18443
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18444
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3016
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20798
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20798
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13293
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2784
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13305
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2785
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20963
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13200
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2786
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18448
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20965
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2797
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21218
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21339
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9069
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13215
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13812
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18450
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3018
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20966
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2800
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21343
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21221
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13813
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9072
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21224
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2802
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18453
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3027
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20967
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13815
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18295
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2803
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9074
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21346
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20872
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3031
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13220
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2804
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13817
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20805
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9077
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21347
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13818
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:11373
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20915
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20798
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13292
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3012
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13294
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13308
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13309
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20961
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13287
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18429
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13222
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13237
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13819
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20882
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13244
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20805
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9076
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9078
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:9087
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21351
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13259
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18452
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2821
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13832
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20887
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2398
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2822
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13851
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21349
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18316
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3034
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21353
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21362
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21366
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21368
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21369
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21373
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21374
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21371
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21384
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2824
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13835
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21388
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2826
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2827
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2828
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2839
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20826
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13836
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13266
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13294
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20826
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4715
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4732
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2842
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2845
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2846
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2863
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2844
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4734
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4749
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4752
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4755
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:4737
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21391
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21395
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21393
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21397
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21406
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21410
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21415
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21413
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21418
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21419
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21396
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21428
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21429
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21433
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21434
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21435
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21352
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21417
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20833
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20854
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2419
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2426
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2447
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:2454
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20942
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20960
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20833
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/log/test.log:20854
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13840
    type: CustomRegex   preview: do**********************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13841
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13842
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13855
    type: CustomRegex   preview: us*****************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13857
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13858
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13860
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21225
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21241
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21242
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21244
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21247
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21248
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21259
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21262
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21266
    type: CustomRegex   preview: 4d********************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21265
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18323
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18344
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18253
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18260
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18265
    type: CustomRegex   preview: do************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18267
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18288
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18295
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18316
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:18323
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21390
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21431
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:13838
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20889
    type: CustomRegex   preview: 4d*********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20910
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:21375
    type: CustomRegex   preview: 4d*******************************************************t
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20917
    type: CustomRegex   preview: 4d**********************************************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:20935
    type: CustomRegex   preview: us********************************************************************,
    first seen in commit: 53fbb1d0ab7a
  - spec/rails_root/vendor/log/test.log:3033
    type: CustomRegex   preview: us******************************t
    first seen in commit: 53fbb1d0ab7a
  - (unknown file):2
    type: CustomRegex   preview: dc**************************************n
    first seen in commit: c096f730c242
  - (unknown file):1
    type: CustomRegex   preview: dc**************************************n
    first seen in commit: c096f730c242
  - (unknown file):2
    type: CustomRegex   preview: dc***************************************n
    first seen in commit: 884eadde87fd
  - (unknown file):1
    type: CustomRegex   preview: dc***************************************n
    first seen in commit: 884eadde87fd
  - test/models/user_test.rb:13
    type: CustomRegex   preview: fo*************************************d
    first seen in commit: f3ccfd71c5ae
  - test/models/user_test.rb:13
    type: CustomRegex   preview: fo*********************************n
    first seen in commit: f3ccfd71c5ae
  - test/models/user_test.rb:52
    type: CustomRegex   preview: Jo**************************************n
    first seen in commit: f3ccfd71c5ae
  - test/controllers/passwords_controller_test.rb:43
    type: CustomRegex   preview: us***************************************"
    first seen in commit: f3ccfd71c5ae
  - test/controllers/passwords_controller_test.rb:43
    type: CustomRegex   preview: us*******************************r
    first seen in commit: f3ccfd71c5ae
  - test/models/user_test.rb:51
    type: CustomRegex   preview: Jo******************************************d
    first seen in commit: f3ccfd71c5ae
  - test/controllers/passwords_controller_test.rb:43
    type: CustomRegex   preview: us*****************************"
    first seen in commit: f3ccfd71c5ae
  - test/models/user_test.rb:51
    type: CustomRegex   preview: Jo***********************************"
    first seen in commit: f3ccfd71c5ae
  - test/controllers/passwords_controller_test.rb:43
    type: CustomRegex   preview: us****************************************************)
    first seen in commit: f3ccfd71c5ae
  - test/models/user_test.rb:51
    type: CustomRegex   preview: Jo****************************************************d
    first seen in commit: f3ccfd71c5ae
  - test/models/user_test.rb:13
    type: CustomRegex   preview: fo******************************"
    first seen in commit: f3ccfd71c5ae
  - test/models/user_test.rb:51
    type: CustomRegex   preview: Jo**************************************n
    first seen in commit: f3ccfd71c5ae
  - test/controllers/passwords_controller_test.rb:43
    type: CustomRegex   preview: us************************************"
    first seen in commit: f3ccfd71c5ae
  - test/models/user_test.rb:13
    type: CustomRegex   preview: fo***********************************************d
    first seen in commit: f3ccfd71c5ae
  - lib/clearance/test/unit/user_test.rb:17
    type: CustomRegex   preview: fo*********************************n
    first seen in commit: 88cac0d40977
  - test/rails_root/vendor/rails/actionpack/CHANGELOG:3758
    type: CustomRegex   preview: te**********************************s
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/actionpack/CHANGELOG:3628
    type: CustomRegex   preview: th***************************s
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/actionpack/CHANGELOG:3750
    type: CustomRegex   preview: dw*******************************s
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/actionpack/CHANGELOG:3756
    type: CustomRegex   preview: te**********************************s
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/actionpack/CHANGELOG:3711
    type: CustomRegex   preview: mo******************************s
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/actionpack/CHANGELOG:3754
    type: CustomRegex   preview: st*****************************s
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/actionpack/test/controller/url_rewriter_test.rb:30
    type: URI   preview: ht**************************t
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/actionpack/test/controller/url_rewriter_test.rb:37
    type: URI   preview: ht****************************************************t
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/actionpack/test/controller/url_rewriter_test.rb:30
    type: CustomRegex   preview: ht**************************t
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/actionpack/test/controller/url_rewriter_test.rb:37
    type: CustomRegex   preview: ht****************************************************t
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/lib/active_resource/base.rb:99
    type: CustomRegex   preview: ht*************************************0
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/lib/active_resource/base.rb:99
    type: URI   preview: ht*************************************0
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/lib/active_resource/base.rb:99
    type: CustomRegex   preview: pa*****************************************"
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/lib/active_resource/base.rb:99
    type: CustomRegex   preview: pa************************************.
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/authorization_test.rb:10
    type: CustomRegex   preview: ht*****************************)
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/authorization_test.rb:1
    type: URI   preview: ht********************************t
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/authorization_test.rb:54
    type: CustomRegex   preview: my*****************************'
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/authorization_test.rb:10
    type: URI   preview: ht***************************t
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/authorization_test.rb:40
    type: URI   preview: ht**********************t
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/authorization_test.rb:54
    type: CustomRegex   preview: my*****************************"
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/base_test.rb:1
    type: URI   preview: ht*****************************a
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/base_test.rb:115
    type: URI   preview: ht**************************e
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/base_test.rb:116
    type: URI   preview: ht**************************e
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/base_test.rb:177
    type: CustomRegex   preview: ht************************************'
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/base_test.rb:115
    type: CustomRegex   preview: ba************************************'
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/base_test.rb:178
    type: CustomRegex   preview: my******************************'
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/base_test.rb:115
    type: CustomRegex   preview: ba***********************************'
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/base_test.rb:116
    type: CustomRegex   preview: ba***********************************'
    first seen in commit: 3fe27442ba7d
  - test/rails_root/vendor/rails/activeresource/test/base_test.rb:178
    type: CustomRegex   preview: my*****************************'
    first seen in commit: 3fe27442ba7d
  - (unknown file):2
    type: CustomRegex   preview: eu**************************************h
    first seen in commit: c8da3d69b45c
  - (unknown file):1
    type: CustomRegex   preview: eu**************************************h
    first seen in commit: c8da3d69b45c
  - lib/clearance/test/functional/passwords_controller_test.rb:45
    type: CustomRegex   preview: us*****************************"
    first seen in commit: fc846f842cda
  - lib/clearance/test/functional/passwords_controller_test.rb:45
    type: CustomRegex   preview: us*******************************r
    first seen in commit: fc846f842cda
  - (unknown file):2
    type: CustomRegex   preview: dc****************************************,
    first seen in commit: fbca4ec08440
  - (unknown file):1
    type: CustomRegex   preview: dc****************************************,
    first seen in commit: fbca4ec08440
  - lib/clearance/test/unit/user_test.rb:14
    type: CustomRegex   preview: fo**************************************************"
    first seen in commit: e3a02e591678
  - clearance-0.3.8.gem:31
    type: CustomRegex   preview: a@*************************"
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:31
    type: CustomRegex   preview: a@*******************************n
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:43
    type: CustomRegex   preview: us***************************************'
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:43
    type: CustomRegex   preview: us*************************************************t
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:43
    type: CustomRegex   preview: us*******************************r
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:43
    type: CustomRegex   preview: us*******************************"
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:43
    type: CustomRegex   preview: us************************************'
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:61
    type: CustomRegex   preview: jo********************************************'
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:61
    type: CustomRegex   preview: jo************************************n
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:9
    type: CustomRegex   preview: fo*******************************n
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:9
    type: CustomRegex   preview: fo*************************************d
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:60
    type: CustomRegex   preview: Jo******************************************d
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:60
    type: CustomRegex   preview: Jo************************************n
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:61
    type: CustomRegex   preview: jo******************************************d
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:9
    type: CustomRegex   preview: fo***************************************'
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.8.gem:60
    type: CustomRegex   preview: Jo********************************************'
    first seen in commit: bc8a7ae5bf02
  - clearance-0.3.7.gem:31
    type: CustomRegex   preview: a@*************************"
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:31
    type: CustomRegex   preview: a@*******************************n
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:43
    type: CustomRegex   preview: us***************************************'
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:43
    type: CustomRegex   preview: us************************************'
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:58
    type: CustomRegex   preview: Jo********************************************'
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:58
    type: CustomRegex   preview: Jo******************************************d
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:59
    type: CustomRegex   preview: jo********************************************'
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:59
    type: CustomRegex   preview: jo************************************n
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:58
    type: CustomRegex   preview: Jo************************************n
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:43
    type: CustomRegex   preview: us***********************************************t
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:59
    type: CustomRegex   preview: jo******************************************d
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:9
    type: CustomRegex   preview: fo*************************************d
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:9
    type: CustomRegex   preview: fo*******************************n
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:43
    type: CustomRegex   preview: us*******************************r
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:9
    type: CustomRegex   preview: fo***************************************'
    first seen in commit: 5dd11f4d71fb
  - clearance-0.3.7.gem:43
    type: CustomRegex   preview: us*******************************"
    first seen in commit: 5dd11f4d71fb
  - lib/clearance/test/unit/user_mailer_test.rb:14
    type: CustomRegex   preview: do**********************************"
    first seen in commit: 84a5b71681d6
  - lib/clearance/test/unit/user_mailer_test.rb:14
    type: CustomRegex   preview: do******************************************************}
    first seen in commit: 84a5b71681d6
  - lib/clearance/test/unit/user_mailer_test.rb:15
    type: CustomRegex   preview: do**********************************"
    first seen in commit: 84a5b71681d6
  - lib/clearance/test/functional/passwords_controller_test.rb:39
    type: CustomRegex   preview: us***************************************'
    first seen in commit: 84a5b71681d6
  - lib/clearance/test/functional/passwords_controller_test.rb:39
    type: CustomRegex   preview: us************************************'
    first seen in commit: 84a5b71681d6
  - lib/clearance/test/functional/passwords_controller_test.rb:39
    type: CustomRegex   preview: us*******************************"
    first seen in commit: 84a5b71681d6
  - lib/clearance/test/functional/passwords_controller_test.rb:39
    type: CustomRegex   preview: us*******************************r
    first seen in commit: 84a5b71681d6
  - lib/clearance/test/functional/passwords_controller_test.rb:39
    type: CustomRegex   preview: us***********************************************t
    first seen in commit: 84a5b71681d6
  - lib/clearance/test/functionals/passwords_controller_test.rb:37
    type: CustomRegex   preview: us************************************'
    first seen in commit: 9b0d15fa59a6
  - lib/clearance/test/functionals/passwords_controller_test.rb:37
    type: CustomRegex   preview: us***********************************************t
    first seen in commit: 9b0d15fa59a6
  - lib/clearance/test/functionals/passwords_controller_test.rb:37
    type: CustomRegex   preview: us*******************************r
    first seen in commit: 9b0d15fa59a6
  - lib/clearance/test/functionals/passwords_controller_test.rb:37
    type: CustomRegex   preview: us*******************************"
    first seen in commit: 9b0d15fa59a6
  - lib/clearance/test/functionals/passwords_controller_test.rb:37
    type: CustomRegex   preview: us***************************************'
    first seen in commit: 9b0d15fa59a6
  - test/rails_root/test/functional/passwords_controller_test.rb:42
    type: CustomRegex   preview: us***************************************'
    first seen in commit: e1cf1bb05840
  - test/rails_root/test/functional/passwords_controller_test.rb:42
    type: CustomRegex   preview: us***********************************************t
    first seen in commit: e1cf1bb05840
  - test/rails_root/test/functional/passwords_controller_test.rb:42
    type: CustomRegex   preview: us*********************************,
    first seen in commit: e1cf1bb05840
  - test/rails_root/test/functional/passwords_controller_test.rb:42
    type: CustomRegex   preview: us*******************************r
    first seen in commit: e1cf1bb05840
  - test/rails_root/test/functional/passwords_controller_test.rb:42
    type: CustomRegex   preview: us************************************'
    first seen in commit: e1cf1bb05840
  - test/rails_root/test/unit/mailer_test.rb:12
    type: CustomRegex   preview: do******************************************************}
    first seen in commit: 3da7d2a0a373
  - test/rails_root/test/unit/mailer_test.rb:13
    type: CustomRegex   preview: do**********************************"
    first seen in commit: 3da7d2a0a373
  - test/rails_root/test/unit/mailer_test.rb:12
    type: CustomRegex   preview: do**********************************"
    first seen in commit: 3da7d2a0a373
  - (unknown file):2
    type: CustomRegex   preview: jo***************************************g
    first seen in commit: 8917d79eee25
  - (unknown file):1
    type: CustomRegex   preview: jo***************************************g
    first seen in commit: 8917d79eee25
  - lib/clearance/test/units/mailer_test.rb:12
    type: CustomRegex   preview: do******************************************************}
    first seen in commit: 3ba23d477974
  - lib/clearance/test/units/mailer_test.rb:13
    type: CustomRegex   preview: do**********************************"
    first seen in commit: 3ba23d477974
  - lib/clearance/test/units/mailer_test.rb:12
    type: CustomRegex   preview: do**********************************"
    first seen in commit: 3ba23d477974

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

