Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/andyv133/andyv133.github.io

Flagged locations (secret values are not included):

  - ruby/2.2.0/cache/addressable-2.5.2.gem:2884
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:2884
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:2885
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:195
    type: CustomRegex   preview: ht*****************************e
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:194
    type: CustomRegex   preview: ht*****************************e
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:428
    type: CustomRegex   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1913
    type: URI   preview: ht***********************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1905
    type: URI   preview: ht************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:428
    type: CustomRegex   preview: ht***********************************'
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:429
    type: CustomRegex   preview: ht************************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1905
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1913
    type: CustomRegex   preview: %2***********************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1890
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1890
    type: CustomRegex   preview: ne*****************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1898
    type: CustomRegex   preview: us***********************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1898
    type: CustomRegex   preview: us******************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1905
    type: CustomRegex   preview: ne*****************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1913
    type: CustomRegex   preview: %2****************************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1924
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1940
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1929
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:1940
    type: URI   preview: ht************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:432
    type: CustomRegex   preview: pa**********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:433
    type: CustomRegex   preview: pa**********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:466
    type: CustomRegex   preview: pa**********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:408
    type: CustomRegex   preview: pa**********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:409
    type: CustomRegex   preview: pa**********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:412
    type: CustomRegex   preview: pa**********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:413
    type: CustomRegex   preview: pa**********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:428
    type: CustomRegex   preview: pa**********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:429
    type: CustomRegex   preview: pa**********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:195
    type: URI   preview: ht*****************************e
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:429
    type: URI   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:428
    type: URI   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4564
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4508
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3241
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:429
    type: URI   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:428
    type: URI   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4508
    type: URI   preview: ht************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4512
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4513
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3242
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4519
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3241
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:432
    type: CustomRegex   preview: ht***********************************'
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4501
    type: CustomRegex   preview: ht******************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:433
    type: CustomRegex   preview: ht************************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4364
    type: CustomRegex   preview: ht******************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4375
    type: CustomRegex   preview: ht*********************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:429
    type: CustomRegex   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4364
    type: URI   preview: ht****************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4501
    type: URI   preview: ht****************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4464
    type: URI   preview: ht*********************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4375
    type: URI   preview: ht*******************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3848
    type: FTP   preview: ft************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3856
    type: CustomRegex   preview: ht*************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3883
    type: CustomRegex   preview: ht***********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3836
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3898
    type: CustomRegex   preview: ht********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4358
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4364
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4319
    type: CustomRegex   preview: us*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4375
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4061
    type: CustomRegex   preview: ht****************************2
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4464
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4375
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4501
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4358
    type: CustomRegex   preview: us*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4390
    type: CustomRegex   preview: us*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4391
    type: CustomRegex   preview: us*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4508
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4390
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4512
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4513
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4397
    type: CustomRegex   preview: us*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4448
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4519
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4564
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4448
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3883
    type: CustomRegex   preview: ht*******************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3848
    type: CustomRegex   preview: ft************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4391
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4364
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4317
    type: CustomRegex   preview: us*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4397
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4466
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3746
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3883
    type: URI   preview: ht*******************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3883
    type: URI   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3836
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3856
    type: URI   preview: ht************************************3
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3836
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3840
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3950
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3891
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3898
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3883
    type: URI   preview: ht*******************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4067
    type: URI   preview: ht******************2
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3840
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3840
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3912
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:4061
    type: URI   preview: ht****************************2
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3925
    type: CustomRegex   preview: pa************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3851
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3918
    type: CustomRegex   preview: pa************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3746
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3874
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3883
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3867
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3848
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3856
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3858
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3873
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3836
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3851
    type: FTP   preview: ft************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3749
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3746
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3756
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3746
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/addressable-2.5.2.gem:3749
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/eventmachine-1.2.6.gem:35
    type: PrivateKey   preview: --*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/eventmachine-1.2.6.gem:97
    type: CustomRegex   preview: mi********************************}
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/eventmachine-1.2.6.gem:97
    type: CustomRegex   preview: mi******************************r
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/eventmachine-1.2.6.gem:1
    type: PrivateKey   preview: --***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/http_parser.rb-0.6.0.gem:882
    type: CustomRegex   preview: ht*********************************4
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/http_parser.rb-0.6.0.gem:891
    type: CustomRegex   preview: ht*********************************4
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/http_parser.rb-0.6.0.gem:752
    type: URI   preview: ht*************************************4
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:3
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:42
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:66
    type: GitHubOauth2   preview: de*****************9
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:67
    type: GitHubOauth2   preview: de*****************9
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:2
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:3
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:5
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:47
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:74
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:49
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:50
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:4
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:74
    type: GitHubOauth2   preview: de*****************9
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:75
    type: GitHubOauth2   preview: de*****************9
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:74
    type: GitHubOauth2   preview: de*****************9
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:4
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:82
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:41
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:39
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:2
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:48
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:40
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/jekyll-gist-1.5.0.gem:5
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/octokit-4.9.0.gem:157
    type: URI   preview: ht***************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/octokit-4.9.0.gem:157
    type: CustomRegex   preview: ba********************************t
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/octokit-4.9.0.gem:157
    type: CustomRegex   preview: ba*******************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/cache/octokit-4.9.0.gem:85
    type: CustomRegex   preview: sf****************************b
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:195
    type: CustomRegex   preview: ht*****************************e
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:194
    type: CustomRegex   preview: ht*****************************e
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:195
    type: URI   preview: ht*****************************e
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1924
    type: URI   preview: ht************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1929
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1924
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1940
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1905
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1913
    type: CustomRegex   preview: %2***********************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1890
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1898
    type: CustomRegex   preview: us******************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1890
    type: CustomRegex   preview: ne*****************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1898
    type: CustomRegex   preview: us***********************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1905
    type: CustomRegex   preview: ne*****************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1913
    type: CustomRegex   preview: %2****************************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:2885
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:2884
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1913
    type: URI   preview: ht***********************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:1905
    type: URI   preview: ht************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3746
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3749
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3746
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:2884
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:428
    type: CustomRegex   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:428
    type: CustomRegex   preview: ht***********************************'
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:429
    type: CustomRegex   preview: ht************************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4364
    type: CustomRegex   preview: ht******************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4375
    type: CustomRegex   preview: ht*********************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4501
    type: CustomRegex   preview: ht******************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3746
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4464
    type: URI   preview: ht*********************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3800
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3807
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3814
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3816
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3801
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3749
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3824
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4375
    type: URI   preview: ht*******************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4364
    type: URI   preview: ht****************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3822
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3808
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3848
    type: FTP   preview: ft************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3794
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4513
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4508
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3793
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4512
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4501
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4519
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4508
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4564
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4375
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4448
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4358
    type: CustomRegex   preview: us*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4364
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4448
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4364
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4464
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4317
    type: CustomRegex   preview: us*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4358
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4391
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3241
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4390
    type: CustomRegex   preview: us*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4319
    type: CustomRegex   preview: us*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4390
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4375
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4397
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4508
    type: URI   preview: ht************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4501
    type: URI   preview: ht****************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3241
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3242
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3836
    type: CustomRegex   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3856
    type: CustomRegex   preview: ht*************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3883
    type: CustomRegex   preview: ht***********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3848
    type: CustomRegex   preview: ft************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3898
    type: CustomRegex   preview: ht********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3883
    type: CustomRegex   preview: ht*******************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4061
    type: CustomRegex   preview: ht****************************2
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:428
    type: URI   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:429
    type: URI   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:432
    type: CustomRegex   preview: ht***********************************'
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:428
    type: URI   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:429
    type: URI   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:433
    type: CustomRegex   preview: ht************************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:429
    type: CustomRegex   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3856
    type: URI   preview: ht************************************3
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3836
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3883
    type: URI   preview: ht**********************************0
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3840
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3836
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3883
    type: URI   preview: ht*******************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3840
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3836
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3883
    type: URI   preview: ht*******************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3950
    type: URI   preview: ht*************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4067
    type: URI   preview: ht******************2
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:4061
    type: URI   preview: ht****************************2
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3836
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3851
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3840
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3912
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3925
    type: CustomRegex   preview: pa************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3918
    type: CustomRegex   preview: pa************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3856
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3858
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3883
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3874
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3898
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3891
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3848
    type: CustomRegex   preview: pa*********************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3867
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/addressable-2.5.2/spec/addressable/uri_spec.rb:3873
    type: CustomRegex   preview: ne************************************"
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/eventmachine-1.2.6/ext/ssl.cpp:35
    type: PrivateKey   preview: --*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/eventmachine-1.2.6/ext/ssl.o:7
    type: PrivateKey   preview: --*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/eventmachine-1.2.6/lib/em/protocols/smtpclient.rb:97
    type: CustomRegex   preview: mi******************************r
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/eventmachine-1.2.6/lib/em/protocols/smtpclient.rb:97
    type: CustomRegex   preview: mi********************************}
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/eventmachine-1.2.6/tests/client.key:1
    type: PrivateKey   preview: --***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/http_parser.rb-0.6.0/ext/ruby_http_parser/vendor/http-parser-java/test.c:891
    type: CustomRegex   preview: ht*********************************4
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/http_parser.rb-0.6.0/ext/ruby_http_parser/vendor/http-parser-java/test.c:882
    type: CustomRegex   preview: ht*********************************4
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/http_parser.rb-0.6.0/ext/ruby_http_parser/vendor/http-parser-java/test.c:751
    type: URI   preview: ht*************************************4
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:2
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:2
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:74
    type: GitHubOauth2   preview: de*****************9
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:75
    type: GitHubOauth2   preview: de*****************9
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:74
    type: GitHubOauth2   preview: de*****************9
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:2
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:3
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:4
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:5
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:39
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:40
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:41
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:42
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:74
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:2
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:66
    type: GitHubOauth2   preview: de*****************9
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/single-file.json:67
    type: GitHubOauth2   preview: de*****************9
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:3
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:4
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:5
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:47
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:48
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:49
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:50
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/jekyll-gist-1.5.0/spec/fixtures/multiple-files.json:82
    type: GitHubOauth2   preview: aa*****************d
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/octokit-4.9.0/lib/octokit/client.rb:157
    type: CustomRegex   preview: ba********************************t
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/octokit-4.9.0/lib/octokit/client.rb:157
    type: CustomRegex   preview: ba*******************************)
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/octokit-4.9.0/lib/octokit/client.rb:157
    type: URI   preview: ht***************************m
    first seen in commit: 37fea7ffe541
  - ruby/2.2.0/gems/octokit-4.9.0/lib/octokit/client/users.rb:85
    type: CustomRegex   preview: sf****************************b
    first seen in commit: 37fea7ffe541

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

