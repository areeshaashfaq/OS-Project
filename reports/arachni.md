Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/pentestbr/arachni

Flagged locations (secret values are not included):

  - spec/support/fixtures/report.afr:77419
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:77419
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:77540
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:77419
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:77540
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:77682
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:77682
    type: CustomRegex   preview: ta**************************************************�
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:77682
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:77682
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:118723
    type: CustomRegex   preview: ta********************************************************************************d
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:118723
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:118833
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 6a4135b062d5
  - spec/support/fixtures/report.afr:63757
    type: CustomRegex   preview: ta**************************************************�
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:63757
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:63757
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:63757
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:63897
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:63757
    type: CustomRegex   preview: ta*************************************************>
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:63897
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:63897
    type: CustomRegex   preview: ta**************************************************�
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:64037
    type: CustomRegex   preview: ta**************************************************�
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:63897
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:63757
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:63757
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:103582
    type: CustomRegex   preview: ta********************************************************************************d
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:103582
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:103648
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 3acc5ae20f9f
  - spec/support/fixtures/report.afr:56646
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56646
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56742
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56646
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56646
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56854
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56854
    type: CustomRegex   preview: ta*****************************************************************************************************************d
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56959
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56854
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56854
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56646
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56646
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56742
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56646
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:94337
    type: CustomRegex   preview: ta********************************************************************************d
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:94188
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:94250
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 4f133217ccd8
  - spec/support/fixtures/report.afr:56998
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56998
    type: CustomRegex   preview: ta*****************************************************************************************************************d
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:57103
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56998
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56998
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56886
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56886
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56886
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56886
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56886
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56886
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56886
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56998
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:94477
    type: CustomRegex   preview: ta********************************************************************************d
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:94390
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:94390
    type: CustomRegex   preview: ta********************************************************************************d
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:94276
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:94326
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 4caaa82e0179
  - spec/support/fixtures/report.afr:56367
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56367
    type: CustomRegex   preview: ta***************************************************************************************************************d
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56472
    type: CustomRegex   preview: ta***********************************************************************************************************************d
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56367
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56367
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56159
    type: CustomRegex   preview: ta***********************************************************************************************************************d
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56159
    type: CustomRegex   preview: ta***********************************************************************************************************************d
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56159
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56255
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56159
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56159
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56159
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56255
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:56159
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 42a13cd59c57
  - (unknown file):2
    type: CustomRegex   preview: ta************************************l
    first seen in commit: 6955956f4e78
  - (unknown file):1
    type: CustomRegex   preview: ta************************************l
    first seen in commit: 6955956f4e78
  - spec/support/fixtures/report.afr:93761
    type: CustomRegex   preview: ta********************************************************************************d
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:93761
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:93848
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 42a13cd59c57
  - spec/support/fixtures/report.afr:57782
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57628
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57688
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57782
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57688
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57782
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57892
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57782
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57782
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57892
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57782
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57782
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:100881
    type: CustomRegex   preview: ta********************************************************************************d
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:100881
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:100966
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 53e95f9f6250
  - spec/support/fixtures/report.afr:57694
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:57694
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:57694
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:57694
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:57806
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:57694
    type: CustomRegex   preview: ta**************************************************************s
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:57806
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:57694
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:57694
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:98606
    type: CustomRegex   preview: ta********************************************************************************d
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:98606
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:98666
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 5ac8e4ee0bf8
  - spec/support/fixtures/report.afr:57815
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57815
    type: CustomRegex   preview: ta*****************************************************************************************************************d
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57918
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57815
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57815
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57618
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57618
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57618
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57618
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57712
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57815
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57618
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57618
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57712
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:57618
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:98771
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:98626
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:98686
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 39b18e254655
  - spec/support/fixtures/report.afr:55150
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:55150
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:55150
    type: CustomRegex   preview: ta**************************************************************************************r
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:55253
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:55150
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:55150
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:54996
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:55056
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:55150
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:55056
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:98249
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:98141
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:98189
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 46b489252249
  - spec/support/fixtures/report.afr:58349
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:58349
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:58349
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:58349
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:58456
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:58456
    type: CustomRegex   preview: ta****************************************************************************************************************d
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:58349
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:58456
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:58349
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:58349
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:101458
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:101349
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:101398
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: e35b057a7b33
  - spec/support/fixtures/report.afr:58373
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58373
    type: CustomRegex   preview: ta*****************************************************************************************************************d
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58478
    type: CustomRegex   preview: ta************************************************************************************************************************d
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58373
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58373
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58172
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58172
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58268
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58373
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58172
    type: CustomRegex   preview: ta************************************************************************************************************************d
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58172
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58172
    type: CustomRegex   preview: ta************************************************************************************************************************d
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58172
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58172
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:58268
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:101579
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:101490
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:101394
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:101490
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:101394
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: feb891815593
  - spec/support/fixtures/report.afr:101394
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: feb891815593
  - (unknown file):2
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 81740f0bc4d5
  - (unknown file):1
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 81740f0bc4d5
  - (unknown file):2
    type: CustomRegex   preview: ta*********************************t
    first seen in commit: d0a69444add0
  - (unknown file):1
    type: CustomRegex   preview: ta*********************************t
    first seen in commit: d0a69444add0
  - lib/arachni/http/proxy_server/ssl-interceptor-cakey.pem:1
    type: PrivateKey   preview: --***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 517a7ecc1682
  - spec/support/fixtures/report.afr:58674
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58674
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58768
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58674
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58674
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58674
    type: CustomRegex   preview: ta*************************************************************************************************************************************************d
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58674
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58674
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58768
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58674
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58674
    type: CustomRegex   preview: ta*************************************************************************************************************************************************d
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58877
    type: CustomRegex   preview: ta**********************************************************************************************************************************************d
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58877
    type: CustomRegex   preview: ta**************************************************************************************************************d
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58986
    type: CustomRegex   preview: ta*************************************************************************************************************************************************d
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58877
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58877
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58877
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:58877
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:103646
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:103646
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:103646
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: ade590d9ea04
  - spec/support/fixtures/report.afr:56662
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56662
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56758
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56871
    type: CustomRegex   preview: ta***********************************************************************************************************************************************d
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56871
    type: CustomRegex   preview: ta***************************************************************************************************************d
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56871
    type: CustomRegex   preview: ta*************************************************************************************************************************************************d
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56871
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56871
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56871
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56871
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56662
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56758
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:102628
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:102628
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:102628
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 453dab6b1695
  - spec/support/fixtures/report.afr:56896
    type: CustomRegex   preview: ta***********************************************************************************************************************************************d
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56896
    type: CustomRegex   preview: ta***************************************************************************************************************d
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:57009
    type: CustomRegex   preview: ta************************************************************************************************************************************************d
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56896
    type: CustomRegex   preview: ta************************************************************************************************************************d
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56896
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56896
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56896
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56783
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56783
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56783
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56783
    type: CustomRegex   preview: ta************************************************************************************************************************************************d
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56783
    type: CustomRegex   preview: ta************************************************************************************************************************d
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56783
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56783
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56896
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56783
    type: CustomRegex   preview: ta************************************************************************************************************************************************d
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56783
    type: CustomRegex   preview: ta************************************************************************************************************************d
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:102555
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:102555
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:102645
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 89a9d6b153af
  - spec/support/fixtures/report.afr:56637
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:56637
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:56731
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:56844
    type: CustomRegex   preview: ta*********************************************************************************************************************************************d
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:56844
    type: CustomRegex   preview: ta*************************************************************************************************************d
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:56957
    type: CustomRegex   preview: ta***********************************************************************************************************************************************d
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:56844
    type: CustomRegex   preview: ta************************************************************************************************************************d
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:56844
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:56844
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:56844
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:56637
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:56731
    type: CustomRegex   preview: ta*********************************************************=
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:102605
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:102605
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:102605
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 8a721f9802c9
  - spec/support/fixtures/report.afr:60131
    type: CustomRegex   preview: ta**********************************************************************************************************************************************d
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:60131
    type: CustomRegex   preview: ta**************************************************************************************************************d
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:60244
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:60131
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:60018
    type: CustomRegex   preview: ta************************************************************************************************************************d
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:60018
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:60018
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:60018
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:60131
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:60018
    type: CustomRegex   preview: ta************************************************************************************************************************************************d
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:104704
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:104704
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:104794
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: 486c55ca86dc
  - spec/support/fixtures/report.afr:100877
    type: CustomRegex   preview: ta***********************************************************************************************************************************************d
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:100877
    type: CustomRegex   preview: ta*************************************************************************************************************d
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:100990
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:100877
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:100877
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:100877
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:100764
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:100764
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:100764
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:100764
    type: CustomRegex   preview: ta*************************************************************************************************************************************************d
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:100764
    type: CustomRegex   preview: ta*************************************************************************************************************************d
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:103087
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:103341
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:103177
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:103087
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:103177
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: dbfec4699cbf
  - spec/support/fixtures/report.afr:96324
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:96324
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:96377
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:98788
    type: CustomRegex   preview: ta*********************************************************************************d
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:98788
    type: CustomRegex   preview: ta*********************************************�
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:98788
    type: CustomRegex   preview: ta**************************************************s
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:96490
    type: CustomRegex   preview: ta*********************************************************************************************************************************************d
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:96490
    type: CustomRegex   preview: ta*************************************************************************************************************d
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:96490
    type: CustomRegex   preview: ta************************************************************************************************************************************************d
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:96490
    type: CustomRegex   preview: ta************************************************************************************************************************d
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:96490
    type: CustomRegex   preview: ta*************************************************************e
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:96490
    type: CustomRegex   preview: ta***************************************************************s
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:96490
    type: CustomRegex   preview: ta********************************************s
    first seen in commit: d7c8fff41b27
  - spec/support/fixtures/report.afr:76585
    type: CustomRegex   preview: ta*****************************************************s
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:76585
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:76636
    type: CustomRegex   preview: ta***************************************************e
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:76745
    type: CustomRegex   preview: ta*************************************************************************************************************************************d
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:76745
    type: CustomRegex   preview: ta*****************************************************************************************************d
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:76854
    type: CustomRegex   preview: ta***************************************************************************************************************************************d
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:76745
    type: CustomRegex   preview: ta***************************************************************************************************************d
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:76745
    type: CustomRegex   preview: ta***************************************************e
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:76745
    type: CustomRegex   preview: ta*****************************************************s
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:76745
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:78689
    type: CustomRegex   preview: ta***********************************************************************d
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:78689
    type: CustomRegex   preview: ta***********************************�
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:78779
    type: CustomRegex   preview: ta***********************************,
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:78937
    type: CustomRegex   preview: ta***********************************************************************d
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:78779
    type: CustomRegex   preview: ta***********************************�
    first seen in commit: 37dd6f8b5462
  - spec/support/fixtures/report.afr:48270
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:47103
    type: CustomRegex   preview: ta****************************************************************************************************d
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:48207
    type: CustomRegex   preview: ta***********************************�
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:46991
    type: CustomRegex   preview: ta***************************************************************************************************************************************d
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:47227
    type: CustomRegex   preview: ta*****************************************************s
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:47103
    type: CustomRegex   preview: ta*****************************************************s
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:46991
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:47189
    type: CustomRegex   preview: ta*****************************************************s
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:46991
    type: CustomRegex   preview: ta***********************************************************n
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:46991
    type: CustomRegex   preview: ta***************************************************************************************************************d
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:46991
    type: CustomRegex   preview: ta*****************************************************s
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:47018
    type: CustomRegex   preview: ta***********************************************************n
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:47103
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:47103
    type: CustomRegex   preview: ta************************************************************************************************************************************d
    first seen in commit: cdd7e84de5da
  - spec/support/fixtures/report.afr:46772
    type: CustomRegex   preview: ta***********************************************************n
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46772
    type: CustomRegex   preview: ta*****************************************************s
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46772
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46799
    type: CustomRegex   preview: ta***********************************************************n
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46886
    type: CustomRegex   preview: ta***********************************************************n
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46772
    type: CustomRegex   preview: ta***************************************************************************************************************************************d
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46772
    type: CustomRegex   preview: ta***************************************************************************************************************d
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:48055
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46886
    type: CustomRegex   preview: ta****************************************************************************************************d
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46886
    type: CustomRegex   preview: ta************************************************************************************************************************************d
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46974
    type: CustomRegex   preview: ta***************************************************************************************************************************************d
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:47012
    type: CustomRegex   preview: ta***************************************************************************************************************************************d
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46886
    type: CustomRegex   preview: ta***************************************************************************************************************d
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46886
    type: CustomRegex   preview: ta*****************************************************s
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:46886
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:47992
    type: CustomRegex   preview: ta***********************************�
    first seen in commit: 5cb18e9a9f98
  - spec/support/fixtures/report.afr:69090
    type: CustomRegex   preview: ta***********************************************s
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:69090
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:69193
    type: CustomRegex   preview: ta******************************************************************************************************d
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:69090
    type: CustomRegex   preview: ta**************************************************************************************************************d
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:69090
    type: CustomRegex   preview: ta*****************************************************n
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:68942
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:68988
    type: CustomRegex   preview: ta*****************************************************n
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:68942
    type: CustomRegex   preview: ta***********************************************s
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:68988
    type: CustomRegex   preview: ta******************************************************************************************************d
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:68942
    type: CustomRegex   preview: ta*****************************************************n
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:69193
    type: CustomRegex   preview: ta****************************************************************************************************d
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:69090
    type: CustomRegex   preview: ta**************************************************************************************T
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:71187
    type: CustomRegex   preview: ta***********************************�
    first seen in commit: 4ff54cd92893
  - spec/support/fixtures/report.afr:57014
    type: CustomRegex   preview: ta***********************************************s
    first seen in commit: bef7a443f30c
  - spec/support/fixtures/report.afr:57014
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: bef7a443f30c
  - spec/support/fixtures/report.afr:57062
    type: CustomRegex   preview: ta*****************************************************n
    first seen in commit: bef7a443f30c
  - spec/support/fixtures/report.afr:57164
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: bef7a443f30c
  - spec/support/fixtures/report.afr:57268
    type: CustomRegex   preview: ta******************************************************************************************************d
    first seen in commit: bef7a443f30c
  - spec/support/fixtures/report.afr:57164
    type: CustomRegex   preview: ta*************************************************************************************************************d
    first seen in commit: bef7a443f30c
  - spec/support/fixtures/report.afr:57164
    type: CustomRegex   preview: ta*****************************************************n
    first seen in commit: bef7a443f30c
  - spec/support/fixtures/report.afr:57164
    type: CustomRegex   preview: ta***********************************************s
    first seen in commit: bef7a443f30c
  - spec/support/fixtures/report.afr:57268
    type: CustomRegex   preview: ta****************************************************************************************************d
    first seen in commit: bef7a443f30c
  - spec/support/fixtures/report.afr:57164
    type: CustomRegex   preview: ta******************************************************************************************************d
    first seen in commit: bef7a443f30c
  - spec/support/fixtures/report.afr:59217
    type: CustomRegex   preview: ta***********************************�
    first seen in commit: bef7a443f30c
  - spec/support/fixtures/report.afr:57158
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 2eb3996765ef
  - spec/support/fixtures/report.afr:57260
    type: CustomRegex   preview: ta*****************************************************n
    first seen in commit: 2eb3996765ef
  - spec/support/fixtures/report.afr:57158
    type: CustomRegex   preview: ta***********************************************s
    first seen in commit: 2eb3996765ef
  - spec/support/fixtures/report.afr:57421
    type: CustomRegex   preview: ta****************************************************************************************************d
    first seen in commit: 2eb3996765ef
  - spec/support/fixtures/report.afr:57363
    type: CustomRegex   preview: ta******************************************************************************************************d
    first seen in commit: 2eb3996765ef
  - spec/support/fixtures/report.afr:57260
    type: CustomRegex   preview: ta******************************************************************************************************d
    first seen in commit: 2eb3996765ef
  - spec/support/fixtures/report.afr:57158
    type: CustomRegex   preview: ta*************************************************************************************************************d
    first seen in commit: 2eb3996765ef
  - spec/support/fixtures/report.afr:57158
    type: CustomRegex   preview: ta*****************************************************n
    first seen in commit: 2eb3996765ef
  - spec/support/fixtures/report.afr:57064
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 2eb3996765ef
  - spec/support/fixtures/report.afr:57110
    type: CustomRegex   preview: ta*****************************************************n
    first seen in commit: 2eb3996765ef
  - spec/support/fixtures/report.afr:59203
    type: CustomRegex   preview: ta***********************************�
    first seen in commit: 2eb3996765ef
  - spec/support/fixtures/auditstore.afr:179622
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 0cfc21507754
  - spec/support/fixtures/auditstore.afr:179785
    type: CustomRegex   preview: ta*****************************************************************************e
    first seen in commit: 0cfc21507754
  - spec/support/fixtures/auditstore.afr:179938
    type: CustomRegex   preview: ta*******************************************************************************e
    first seen in commit: 0cfc21507754
  - spec/support/fixtures/auditstore.afr:180054
    type: CustomRegex   preview: ta*******************************************************************************e
    first seen in commit: 0cfc21507754
  - spec/support/fixtures/auditstore.afr:179785
    type: CustomRegex   preview: ta*******************************************************************************e
    first seen in commit: 0cfc21507754
  - spec/support/fixtures/auditstore.afr:179785
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 0cfc21507754
  - spec/support/fixtures/auditstore.afr:176498
    type: CustomRegex   preview: ta******************************************************************************e
    first seen in commit: d4eca6d2a432
  - spec/support/fixtures/auditstore.afr:176658
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: d4eca6d2a432
  - spec/support/fixtures/auditstore.afr:176498
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: d4eca6d2a432
  - spec/support/fixtures/auditstore.afr:176498
    type: CustomRegex   preview: ta****************************************************************************e
    first seen in commit: d4eca6d2a432
  - spec/support/fixtures/auditstore.afr:234128
    type: CustomRegex   preview: ta************************************n
    first seen in commit: d4eca6d2a432
  - (unknown file):2
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 0533b8043755
  - (unknown file):1
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 0533b8043755
  - (unknown file):2
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 7f1feafc06e6
  - (unknown file):1
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 7f1feafc06e6
  - (unknown file):2
    type: CustomRegex   preview: ta***********************************s
    first seen in commit: e4d8828862d8
  - (unknown file):1
    type: CustomRegex   preview: ta***********************************s
    first seen in commit: e4d8828862d8
  - spec/arachni/uri_spec.rb:48
    type: CustomRegex   preview: ht****************************t
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:58
    type: CustomRegex   preview: ht**********************m
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:46
    type: CustomRegex   preview: ht****************************t
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:64
    type: CustomRegex   preview: ht*************************1
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:49
    type: CustomRegex   preview: ht****************************t
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:65
    type: CustomRegex   preview: ht*************************1
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:62
    type: CustomRegex   preview: ht*************************1
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:58
    type: CustomRegex   preview: ht*************************0
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:57
    type: CustomRegex   preview: ht**********************m
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:47
    type: CustomRegex   preview: ht****************************t
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:74
    type: CustomRegex   preview: ht*****************************1
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:60
    type: CustomRegex   preview: ht*************************1
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:63
    type: CustomRegex   preview: ht*************************1
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:61
    type: CustomRegex   preview: ht*************************1
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:73
    type: CustomRegex   preview: hT*****************************1
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:74
    type: URI   preview: ht*****************************1
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:58
    type: URI   preview: ht*************************0
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:60
    type: URI   preview: ht*************************1
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:46
    type: URI   preview: ht****************************t
    first seen in commit: d6e9febf5234
  - spec/arachni/uri_spec.rb:57
    type: URI   preview: ht**********************m
    first seen in commit: d6e9febf5234
  - (unknown file):2
    type: CustomRegex   preview: ta**********************************:
    first seen in commit: 3f7aeb27e6ce
  - (unknown file):1
    type: CustomRegex   preview: ta**********************************:
    first seen in commit: 3f7aeb27e6ce
  - modules/recon/grep/password_autocomplete.rb:2
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: f52f22685734
  - modules/recon/grep/password_autocomplete.rb:21
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: f52f22685734
  - modules/recon/grep/password_autocomplete.rb:44
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: f52f22685734
  - spec/arachni/uri_spec.rb:54
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:51
    type: CustomRegex   preview: ht**********************m
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:61
    type: CustomRegex   preview: ht*****************************1
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:61
    type: CustomRegex   preview: hT*****************************1
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:53
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:43
    type: CustomRegex   preview: ht****************************t
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:55
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:42
    type: CustomRegex   preview: ht****************************t
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:52
    type: CustomRegex   preview: ht**********************m
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:52
    type: CustomRegex   preview: ht*************************0
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:42
    type: URI   preview: ht****************************t
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:53
    type: URI   preview: ht*************************1
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:61
    type: URI   preview: ht*****************************1
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:51
    type: URI   preview: ht**********************m
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:52
    type: URI   preview: ht*************************0
    first seen in commit: 478d673cc386
  - spec/arachni/uri_spec.rb:61
    type: CustomRegex   preview: hT*****************************1
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:54
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:42
    type: CustomRegex   preview: ht****************************t
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:52
    type: CustomRegex   preview: ht*************************0
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:55
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:53
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:43
    type: CustomRegex   preview: ht****************************t
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:61
    type: URI   preview: ht*****************************1
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:52
    type: CustomRegex   preview: ht**********************m
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:42
    type: URI   preview: ht****************************t
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:61
    type: CustomRegex   preview: ht*****************************1
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:53
    type: URI   preview: ht*************************1
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:51
    type: CustomRegex   preview: ht**********************m
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:51
    type: URI   preview: ht**********************m
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:52
    type: URI   preview: ht*************************0
    first seen in commit: 18f07fb70b52
  - spec/arachni/uri_spec.rb:11
    type: URI   preview: ht****************************t
    first seen in commit: 4735445c5367
  - spec/arachni/uri_spec.rb:11
    type: CustomRegex   preview: ht****************************t
    first seen in commit: 4735445c5367
  - spec/arachni/uri_spec.rb:12
    type: CustomRegex   preview: ht****************************t
    first seen in commit: 4735445c5367
  - (unknown file):2
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: ffb2772ea0d5
  - (unknown file):1
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: ffb2772ea0d5
  - plugins/proxy/ssl-interceptor-pkey.pem:1
    type: PrivateKey   preview: --***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 51ed3e22f61d
  - reports/plugin_formatters/stdout/form_dicattack.rb:22
    type: CustomRegex   preview: ta*****************************************************"
    first seen in commit: 1b3e9d7eef0d
  - reports/plugin_formatters/stdout/http_dicattack.rb:22
    type: CustomRegex   preview: ta*****************************************************"
    first seen in commit: 1b3e9d7eef0d
  - plugins/http_dicattack.rb:102
    type: CustomRegex   preview: ta***************************************"
    first seen in commit: 3de87f341936
  - plugins/http_dicattack.rb:102
    type: CustomRegex   preview: ta****************************************p
    first seen in commit: 3de87f341936
  - plugins/http_dicattack.rb:102
    type: CustomRegex   preview: ta*************************************d
    first seen in commit: 3de87f341936
  - modules/recon/grep/unencrypted_password_forms.rb:22
    type: CustomRegex   preview: ta**********************************,
    first seen in commit: f8dd3f56e7ed
  - modules/recon/grep/unencrypted_password_forms.rb:22
    type: CustomRegex   preview: ta***********************************,
    first seen in commit: f8dd3f56e7ed
  - modules/recon/grep/unencrypted_password_forms.rb:78
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: f8dd3f56e7ed
  - modules/recon/grep/unencrypted_password_forms.rb:22
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: f8dd3f56e7ed
  - spec/arachni/uri_spec.rb:16
    type: CustomRegex   preview: ht*************************0
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/uri_spec.rb:25
    type: CustomRegex   preview: hT*****************************1
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/uri_spec.rb:19
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/uri_spec.rb:18
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/uri_spec.rb:17
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/uri_spec.rb:15
    type: CustomRegex   preview: ht**********************m
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/uri_spec.rb:15
    type: URI   preview: ht**********************m
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/uri_spec.rb:16
    type: URI   preview: ht*************************0
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/uri_spec.rb:17
    type: URI   preview: ht*************************1
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/utilities_spec.rb:234
    type: URI   preview: ht*************************1
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/utilities_spec.rb:232
    type: URI   preview: ht**********************m
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/utilities_spec.rb:233
    type: URI   preview: ht*************************0
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/utilities_spec.rb:236
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/utilities_spec.rb:234
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/utilities_spec.rb:235
    type: CustomRegex   preview: ht*************************1
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/utilities_spec.rb:242
    type: CustomRegex   preview: hT*****************************1
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/utilities_spec.rb:233
    type: CustomRegex   preview: ht*************************0
    first seen in commit: 9cf6f6cdef54
  - spec/arachni/utilities_spec.rb:232
    type: CustomRegex   preview: ht**********************m
    first seen in commit: 9cf6f6cdef54
  - (unknown file):2
    type: CustomRegex   preview: ta***************************************,
    first seen in commit: 8eded908e149
  - (unknown file):1
    type: CustomRegex   preview: ta***************************************,
    first seen in commit: 8eded908e149
  - spec/arachni/module/utilities_spec.rb:238
    type: CustomRegex   preview: ht*************************1
    first seen in commit: f1a764e1e49e
  - spec/arachni/module/utilities_spec.rb:234
    type: CustomRegex   preview: ht**********************m
    first seen in commit: f1a764e1e49e
  - spec/arachni/module/utilities_spec.rb:235
    type: CustomRegex   preview: ht*************************0
    first seen in commit: f1a764e1e49e
  - spec/arachni/module/utilities_spec.rb:244
    type: CustomRegex   preview: hT*****************************1
    first seen in commit: f1a764e1e49e
  - spec/arachni/module/utilities_spec.rb:234
    type: URI   preview: ht**********************m
    first seen in commit: f1a764e1e49e
  - spec/arachni/module/utilities_spec.rb:237
    type: CustomRegex   preview: ht*************************1
    first seen in commit: f1a764e1e49e
  - spec/arachni/module/utilities_spec.rb:235
    type: URI   preview: ht*************************0
    first seen in commit: f1a764e1e49e
  - spec/arachni/module/utilities_spec.rb:236
    type: URI   preview: ht*************************1
    first seen in commit: f1a764e1e49e
  - spec/arachni/module/utilities_spec.rb:236
    type: CustomRegex   preview: ht*************************1
    first seen in commit: f1a764e1e49e
  - spec/pems/client/foo-key.pem:1
    type: PrivateKey   preview: --***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: a87c20a951c4
  - spec/pems/server/key.pem:1
    type: PrivateKey   preview: --***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: a87c20a951c4
  - spec/pems/client/key.pem:1
    type: PrivateKey   preview: --***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: a87c20a951c4
  - (unknown file):2
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 2e8af50eb4ba
  - (unknown file):1
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 2e8af50eb4ba
  - (unknown file):2
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 4fcfb2e24512
  - (unknown file):1
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 4fcfb2e24512
  - plugins/http_dicattack.rb:17
    type: CustomRegex   preview: za************************************"
    first seen in commit: f153fdcae55d
  - plugins/http_dicattack.rb:3
    type: CustomRegex   preview: ta*************************************d
    first seen in commit: f153fdcae55d
  - plugins/http_dicattack.rb:3
    type: CustomRegex   preview: .l**********************************"
    first seen in commit: f153fdcae55d
  - plugins/http_dicattack.rb:17
    type: CustomRegex   preview: za**********************************d
    first seen in commit: f153fdcae55d
  - plugins/http_dicattack.rb:16
    type: CustomRegex   preview: ta***************************************"
    first seen in commit: f153fdcae55d
  - plugins/http_dicattack.rb:78
    type: CustomRegex   preview: ta***************************************"
    first seen in commit: f153fdcae55d
  - plugins/http_dicattack.rb:16
    type: CustomRegex   preview: .l********************************d
    first seen in commit: f153fdcae55d
  - plugins/http_dicattack.rb:78
    type: CustomRegex   preview: .l**********************************"
    first seen in commit: f153fdcae55d
  - modules/recon/unencrypted_password_forms.rb:5
    type: CustomRegex   preview: ta**********************************s
    first seen in commit: 26bcc8bede4d
  - modules/recon/unencrypted_password_forms.rb:25
    type: CustomRegex   preview: za*******************************s
    first seen in commit: 26bcc8bede4d
  - modules/recon/unencrypted_password_forms.rb:25
    type: CustomRegex   preview: za********************************,
    first seen in commit: 26bcc8bede4d
  - modules/recon/unencrypted_password_forms.rb:5
    type: CustomRegex   preview: ta***********************************,
    first seen in commit: 26bcc8bede4d
  - modules/recon/unencrypted_password_forms.rb:24
    type: CustomRegex   preview: ta***********************************,
    first seen in commit: 26bcc8bede4d
  - DIAGRAMS.md:5322
    type: Box   preview: Mz*****************************M
    first seen in commit: 5edf1639ba9d
  - DIAGRAMS.md:3292
    type: TLy   preview: 0X*********************************************************y
    first seen in commit: 5edf1639ba9d
  - DIAGRAMS.md:2951
    type: TLy   preview: 8L*********************************************************l
    first seen in commit: 3b8192deacbe
  - DIAGRAMS.md:1049
    type: TLy   preview: oT*********************************************************X
    first seen in commit: 3b8192deacbe
  - DIAGRAMS.md:18
    type: TLy   preview: CM*********************************************************V
    first seen in commit: 3b8192deacbe
  - DIAGRAMS.md:276
    type: TLy   preview: cX*********************************************************4
    first seen in commit: b76c54882103
  - DIAGRAMS.md:4091
    type: TLy   preview: Ve*********************************************************X
    first seen in commit: b76c54882103
  - DIAGRAMS.md:5962
    type: TLy   preview: Uk*********************************************************u
    first seen in commit: c2c7b800b00b
  - DIAGRAMS.md:5951
    type: TLy   preview: j9*********************************************************T
    first seen in commit: ed426a691311
  - DIAGRAMS.md:1199
    type: TLy   preview: 0K*********************************************************h
    first seen in commit: 217eceea71cf
  - DIAGRAMS.md:3534
    type: Box   preview: 2P*****************************M
    first seen in commit: 217eceea71cf
  - DIAGRAMS.md:276
    type: TLy   preview: Np*********************************************************M
    first seen in commit: 217eceea71cf
  - DIAGRAMS.md:2310
    type: TLy   preview: Jn*********************************************************D
    first seen in commit: 217eceea71cf
  - DIAGRAMS.md:3392
    type: TLy   preview: io*********************************************************G
    first seen in commit: 217eceea71cf
  - DIAGRAMS.md:451
    type: TLy   preview: Z3*********************************************************M
    first seen in commit: 83802b0bc7a8
  - DIAGRAMS.md:2740
    type: TLy   preview: qj*********************************************************M
    first seen in commit: f5119da4c223
  - DIAGRAMS.md:2729
    type: TLy   preview: Ef*********************************************************M
    first seen in commit: f5119da4c223
  - DIAGRAMS.md:566
    type: TLy   preview: 1L*********************************************************7
    first seen in commit: dbbc5adc9bb5
  - DIAGRAMS.md:513
    type: TLy   preview: pM*********************************************************1
    first seen in commit: dbbc5adc9bb5
  - DIAGRAMS.md:9368
    type: TLy   preview: rz*********************************************************o
    first seen in commit: dbbc5adc9bb5
  - DIAGRAMS.md:11086
    type: TLy   preview: zg*********************************************************e
    first seen in commit: dbbc5adc9bb5
  - DIAGRAMS.md:15750
    type: TLy   preview: Sj*********************************************************Y
    first seen in commit: dbbc5adc9bb5
  - DIAGRAMS.md:15699
    type: TLy   preview: mz*********************************************************j
    first seen in commit: dbbc5adc9bb5
  - DIAGRAMS.md:19293
    type: Juro   preview: GN*************************************D
    first seen in commit: dbbc5adc9bb5
  - arachni.rb:101
    type: CustomRegex   preview: sc***********************************"
    first seen in commit: e3324e72e45b
  - arachni.rb:108
    type: CustomRegex   preview: ht********************************m
    first seen in commit: e3324e72e45b
  - arachni.rb:108
    type: URI   preview: ht********************************m
    first seen in commit: e3324e72e45b
  - lib/ui/cli/cli.rb:331
    type: CustomRegex   preview: ht********************************m
    first seen in commit: e3324e72e45b
  - lib/ui/cli/cli.rb:331
    type: URI   preview: ht********************************m
    first seen in commit: e3324e72e45b
  - arachni.rb:251
    type: CustomRegex   preview: sc***********************************"
    first seen in commit: 9629e0c99df7
  - arachni.rb:235
    type: URI   preview: ht********************************m
    first seen in commit: 8cf568a47d31
  - arachni.rb:230
    type: CustomRegex   preview: sc*************************************************t
    first seen in commit: 8cf568a47d31
  - arachni.rb:235
    type: CustomRegex   preview: ht********************************m
    first seen in commit: 8cf568a47d31

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

