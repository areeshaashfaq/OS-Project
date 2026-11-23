Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/guilk/caffe-sl

Flagged locations (secret values are not included):

  - examples/pascal-multilabel-with-datalayer.ipynb:433
    type: Box   preview: fa*****************************U
    first seen in commit: 9f8f7775a890
  - examples/pascal-multilabel-with-datalayer.ipynb:423
    type: Box   preview: nx*****************************1
    first seen in commit: 9f8f7775a890
  - examples/brewing-logreg.ipynb:60
    type: TLy   preview: 95*********************************************************s
    first seen in commit: 08edfddbbae6
  - examples/00-classification.ipynb:217
    type: Box   preview: vZ*****************************X
    first seen in commit: bd6b03f15ee7
  - examples/00-classification.ipynb:217
    type: TLy   preview: 8z*********************************************************j
    first seen in commit: bd6b03f15ee7
  - examples/detection.ipynb:7595
    type: Box   preview: sY*****************************J
    first seen in commit: 2fed2a998ae8
  - examples/detection.ipynb:894
    type: Box   preview: sY*****************************J
    first seen in commit: 26c16bf414dc
  - examples/imagenet_classification.ipynb:121
    type: Sirv   preview: \n*************************************************************************************9
    first seen in commit: f1eb9821ba71
  - examples/filter_visualization.ipynb:232
    type: Sirv   preview: ++*************************************************************************************3
    first seen in commit: 943b98ea4927
  - examples/net_surgery.ipynb:301
    type: Sirv   preview: \n*************************************************************************************9
    first seen in commit: 5840ad951566
  - examples/net_surgery.ipynb:299
    type: Sirv   preview: \n*************************************************************************************9
    first seen in commit: c3440fa48b65
  - examples/filter_visualization/lena_imagenet.ipynb:342
    type: Box   preview: k5*****************************5
    first seen in commit: 708181affc56
  - docs/selective_search_demo.ipynb:683
    type: Box   preview: nt*****************************2
    first seen in commit: 5556c62b3793
  - examples/selective_search_demo.ipynb:696
    type: Box   preview: nt*****************************2
    first seen in commit: 99ecba3a826c
  - python/caffe/imagenet/selective_search_demo.ipynb:266
    type: TLy   preview: na*********************************************************5
    first seen in commit: 4eca379c2fda

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

