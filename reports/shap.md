Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/fred-renner/shap

Flagged locations (secret values are not included):

  - notebooks/benchmarks/tabular/Benchmark XGBoost explanations.ipynb:175
    type: Box   preview: M4*****************************T
    first seen in commit: 9d7de4dee742
  - notebooks/image_examples/image_classification/Explain ResNet50 using the Partition explainer.ipynb:135
    type: Box   preview: Oj*****************************x
    first seen in commit: 9d7de4dee742
  - notebooks/image_examples/image_classification/Image Multi Class.ipynb:208
    type: Box   preview: Oj*****************************x
    first seen in commit: 9d7de4dee742
  - notebooks/image_examples/image_classification/Explain ResNet50 using the Partition explainer.ipynb:240
    type: Qase   preview: bg*************************************W
    first seen in commit: 9d7de4dee742
  - notebooks/image_examples/image_classification/Image Multi Class.ipynb:1651
    type: Qase   preview: bg*************************************W
    first seen in commit: 9d7de4dee742
  - notebooks/image_examples/image_captioning/Image Captioning using Azure Cognitive Services.ipynb:415
    type: Box   preview: fc*****************************4
    first seen in commit: 911ac478d1d4
  - notebooks/image_examples/image_captioning/Image Captioning using Azure Cognitive Services.ipynb:461
    type: Box   preview: 5G*****************************6
    first seen in commit: 911ac478d1d4
  - notebooks/image_examples/image_captioning/Image Captioning using Azure Cognitive Services.ipynb:414
    type: Box   preview: 5G*****************************6
    first seen in commit: 911ac478d1d4
  - notebooks/image_examples/image_captioning/Image Captioning using Azure Cognitive Services.ipynb:462
    type: Aiven   preview: 1h*********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************S
    first seen in commit: 911ac478d1d4
  - notebooks/image_examples/image_captioning/Image Captioning using Open Source.ipynb:500
    type: Box   preview: K1*****************************I
    first seen in commit: 911ac478d1d4
  - notebooks/image_examples/image_captioning/Image Captioning using Open Source.ipynb:482
    type: TLy   preview: qR*********************************************************C
    first seen in commit: 911ac478d1d4
  - notebooks/image_examples/image_captioning/Image Captioning using Open Source.ipynb:547
    type: TLy   preview: WL*********************************************************x
    first seen in commit: 911ac478d1d4
  - notebooks/image_examples/image_captioning/Image Captioning using Azure Cognitive Services.ipynb:483
    type: Box   preview: Np*****************************3
    first seen in commit: 911ac478d1d4
  - notebooks/image_examples/image_captioning/Image Captioning using Azure Cognitive Services.ipynb:483
    type: Box   preview: wX*****************************r
    first seen in commit: 911ac478d1d4
  - notebooks/benchmark/image/Image Multiclass Classification Benchmark Demo.ipynb:204
    type: TLy   preview: LO*********************************************************d
    first seen in commit: 71d218b43b21
  - notebooks/overviews/An introduction to explainable AI with Shapley values.ipynb:872
    type: Box   preview: VZ*****************************B
    first seen in commit: 3c5d8fb656c7
  - notebooks/tabular_examples/tree_based_models/League of Legends Win Prediction with XGBoost.ipynb:672
    type: Box   preview: Q4*****************************Q
    first seen in commit: 3c5d8fb656c7
  - notebooks/tabular_examples/tree_based_models/League of Legends Win Prediction with XGBoost.ipynb:752
    type: Box   preview: nz*****************************V
    first seen in commit: 3c5d8fb656c7
  - notebooks/tabular_examples/tree_based_models/League of Legends Win Prediction with XGBoost.ipynb:864
    type: Box   preview: nE*****************************X
    first seen in commit: 3c5d8fb656c7
  - notebooks/tabular_examples/tree_based_models/League of Legends Win Prediction with XGBoost.ipynb:561
    type: Box   preview: x3*****************************b
    first seen in commit: 3c5d8fb656c7
  - notebooks/partition_explainer/Emotion Data Multiclass Text Explanation Demo.ipynb:325
    type: Box   preview: ky*****************************c
    first seen in commit: bb2a4ed4b203
  - notebooks/partition_explainer/Emotion Data Multiclass Text Explanation Demo.ipynb:300
    type: TLy   preview: Jv*********************************************************Z
    first seen in commit: 5a2f18eff9b9
  - notebooks/multiclass_explainer/Emotion Data Multiclass Text Explanation Demo.ipynb:197
    type: TLy   preview: eG*********************************************************4
    first seen in commit: 2d97e71a6ca4
  - docs/notebooks/plots/bar.ipynb:321
    type: TLy   preview: f0*********************************************************2
    first seen in commit: e3187c11aed1
  - docs/notebooks/plots/bar.ipynb:200
    type: TLy   preview: nA*********************************************************s
    first seen in commit: e3187c11aed1
  - notebooks/plots/bar.ipynb:200
    type: TLy   preview: nA*********************************************************s
    first seen in commit: db928777ef3c
  - notebooks/plots/bar.ipynb:321
    type: TLy   preview: f0*********************************************************2
    first seen in commit: db928777ef3c
  - notebooks/plots/bar.ipynb:133
    type: SumoLogicKey   preview: v3*************************************************************6
    first seen in commit: 13c6141ebe45
  - notebooks/plots/bar.ipynb:97
    type: Box   preview: bs*****************************P
    first seen in commit: 13c6141ebe45
  - notebooks/plots/bar.ipynb:204
    type: Box   preview: vc*****************************f
    first seen in commit: 13c6141ebe45
  - notebooks/general/Explainable AI with Shapley Values.ipynb:1338
    type: Box   preview: Gp*****************************8
    first seen in commit: a03d77c8050c
  - notebooks/plots/scatter.ipynb:339
    type: TLy   preview: vt*********************************************************N
    first seen in commit: df4334a700e4
  - notebooks/plots/scatter.ipynb:581
    type: Qase   preview: Hc*************************************J
    first seen in commit: df4334a700e4
  - notebooks/explainers/Partition.ipynb:177
    type: TLy   preview: x5*********************************************************S
    first seen in commit: 032fc17e50ad
  - notebooks/explainers/Partition.ipynb:203
    type: Box   preview: nK*****************************Z
    first seen in commit: 032fc17e50ad
  - notebooks/plots/heatmap.ipynb:82
    type: Box   preview: cu*****************************f
    first seen in commit: 032fc17e50ad
  - notebooks/plots/heatmap.ipynb:119
    type: Box   preview: VK*****************************N
    first seen in commit: 032fc17e50ad
  - notebooks/plots/scatter.ipynb:722
    type: Box   preview: 76*****************************R
    first seen in commit: 032fc17e50ad
  - notebooks/tree_explainer/League of Legends Win Prediction with XGBoost.ipynb:624
    type: Box   preview: nz*****************************V
    first seen in commit: ed774ddaddd2
  - notebooks/tree_explainer/League of Legends Win Prediction with XGBoost.ipynb:427
    type: Box   preview: x3*****************************b
    first seen in commit: ed774ddaddd2
  - notebooks/tree_explainer/League of Legends Win Prediction with XGBoost.ipynb:544
    type: Box   preview: Q4*****************************Q
    first seen in commit: ed774ddaddd2
  - notebooks/tree_explainer/League of Legends Win Prediction with XGBoost.ipynb:736
    type: Box   preview: nE*****************************X
    first seen in commit: ed774ddaddd2
  - docs/notebooks/plots/decision_plot.html:13681
    type: TLy   preview: 2E*********************************************************y
    first seen in commit: d0ad9d4157ca
  - docs/notebooks/plots/decision_plot.html:14002
    type: TLy   preview: fy*********************************************************5
    first seen in commit: d0ad9d4157ca
  - docs/notebooks/plots/decision_plot.html:14002
    type: Box   preview: lY*****************************A
    first seen in commit: d0ad9d4157ca
  - docs/user_studies/sickness_scores.zip:1
    type: PrivateKey   preview: --*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:127
    type: CustomRegex   preview: ht*****************************************,
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:127
    type: URI   preview: ht***************************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:56
    type: CustomRegex   preview: fo********************************************;
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:285
    type: URI   preview: ht***************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:269
    type: URI   preview: ht***************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:171
    type: CustomRegex   preview: ht***********************************************'
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:196
    type: CustomRegex   preview: HT**************************'
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1
    type: PrivateKey   preview: --*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1
    type: PrivateKey   preview: --*********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1
    type: PrivateKey   preview: --*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1
    type: PrivateKey   preview: --************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1
    type: PrivateKey   preview: --***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1
    type: PrivateKey   preview: --***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1
    type: PrivateKey   preview: --*************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:177
    type: URI   preview: ht***************************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:177
    type: CustomRegex   preview: ht******************************************,
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1533
    type: URI   preview: ht*****************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1532
    type: URI   preview: ht*****************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:17
    type: URI   preview: ht***************************0
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:21
    type: CustomRegex   preview: ht***************************0
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1049
    type: CustomRegex   preview: ht******************************1
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:17
    type: CustomRegex   preview: ht***************************0
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1056
    type: CustomRegex   preview: ht****************************o
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1533
    type: CustomRegex   preview: ht*******************************,
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1532
    type: CustomRegex   preview: ht*****************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1532
    type: CustomRegex   preview: ht*******************************,
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:280
    type: URI   preview: ht****************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:436
    type: URI   preview: ht***********************************0
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:362
    type: URI   preview: ht******************************0
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1056
    type: URI   preview: ht****************************o
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:362
    type: CustomRegex   preview: ht******************************0
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:280
    type: CustomRegex   preview: ht****************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1049
    type: URI   preview: ht******************************1
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:282
    type: CustomRegex   preview: ht****************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:363
    type: CustomRegex   preview: ht******************************0
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:437
    type: CustomRegex   preview: ht***********************************0
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:436
    type: CustomRegex   preview: ht***********************************0
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:754
    type: CustomRegex   preview: ht*****************************************0
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:743
    type: CustomRegex   preview: ht**************************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:754
    type: URI   preview: ht*****************************************0
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:743
    type: URI   preview: ht**************************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:4
    type: PrivateKey   preview: --*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:126
    type: CustomRegex   preview: ht*****************************************,
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:126
    type: URI   preview: ht***************************************m
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1
    type: PrivateKey   preview: --***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1
    type: PrivateKey   preview: --**************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:1
    type: PrivateKey   preview: --*************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores.zip:244
    type: PrivateKey   preview: --***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************-
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores/Approve Hits.ipynb:18
    type: AWS   preview: AK*****************A
    first seen in commit: 01771891384d
  - docs/user_studies/sickness_scores/Analyse Results.ipynb:975
    type: Box   preview: SH*****************************3
    first seen in commit: 01771891384d
  - notebooks/plots/decision_plot.ipynb:718
    type: Box   preview: lY*****************************A
    first seen in commit: 626759e319d1
  - notebooks/plots/decision_plot.ipynb:718
    type: TLy   preview: fy*********************************************************5
    first seen in commit: 626759e319d1
  - notebooks/plots/decision_plot.ipynb:16832
    type: TLy   preview: 2E*********************************************************y
    first seen in commit: 1dd2f5dd6fa7
  - notebooks/plots/decision_plot.ipynb:16704
    type: Box   preview: tb*****************************y
    first seen in commit: 1dd2f5dd6fa7
  - notebooks/plots/decision_plot_01.ipynb:469
    type: TLy   preview: 2E*********************************************************y
    first seen in commit: 787ee4140400
  - notebooks/plots/decision_plot.ipynb:16960
    type: TLy   preview: fy*********************************************************5
    first seen in commit: 1dd2f5dd6fa7
  - notebooks/plots/decision_plot.ipynb:16960
    type: Box   preview: lY*****************************A
    first seen in commit: 1dd2f5dd6fa7
  - docs/notebooks/plots/dependence_plot.html:12011
    type: Box   preview: 76*****************************R
    first seen in commit: c770f3a8e166
  - notebooks/plots/dependence_plot.ipynb:167
    type: Box   preview: 76*****************************R
    first seen in commit: c770f3a8e166
  - docs/notebooks/gradient_explainer/Explain an Intermediate Layer of VGG16 on ImageNet (PyTorch).html:11871
    type: TLy   preview: bP*********************************************************X
    first seen in commit: 7d7537b9b087
  - notebooks/gradient_explainer/Explain an Intermediate Layer of VGG16 on ImageNet (PyTorch).ipynb:52
    type: TLy   preview: bP*********************************************************X
    first seen in commit: 7d7537b9b087
  - docs/notebooks/gradient_explainer/Explain VGG16 on ImageNet (PyTorch).html:11932
    type: Box   preview: AJ*****************************q
    first seen in commit: 48ae3e5cb482
  - docs/notebooks/gradient_explainer/Explain VGG16 on ImageNet (PyTorch).html:11932
    type: Box   preview: bC*****************************t
    first seen in commit: 48ae3e5cb482
  - docs/notebooks/gradient_explainer/Explain VGG16 on ImageNet (PyTorch).html:11879
    type: Box   preview: rY*****************************f
    first seen in commit: 48ae3e5cb482
  - notebooks/gradient_explainer/Explain VGG16 on ImageNet (PyTorch).ipynb:112
    type: Box   preview: bC*****************************t
    first seen in commit: 48ae3e5cb482
  - notebooks/gradient_explainer/Explain VGG16 on ImageNet (PyTorch).ipynb:112
    type: Box   preview: AJ*****************************q
    first seen in commit: 48ae3e5cb482
  - notebooks/gradient_explainer/Explain VGG16 on ImageNet (PyTorch).ipynb:57
    type: Box   preview: rY*****************************f
    first seen in commit: 48ae3e5cb482
  - data/imagenet50_224x224.npy:10285
    type: CustomRegex   preview: B:*************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************�
    first seen in commit: ca2806f20ccf
  - docs/notebooks/Census income classification with scikit-learn.html:12249
    type: Box   preview: CP*****************************0
    first seen in commit: 35e20d11e582
  - docs/notebooks/NHANES I Survival Model.html:12914
    type: Box   preview: 4v*****************************F
    first seen in commit: 35e20d11e582
  - docs/notebooks/NHANES I Survival Model.html:12622
    type: Sirv   preview: +V*************************************************************************************F
    first seen in commit: 35e20d11e582
  - notebooks/tree_explainer/XGBoost Multi-class Example.ipynb:106
    type: Box   preview: 7B*****************************a
    first seen in commit: 35e20d11e582
  - notebooks/kernel_explainer/Census income classification with scikit-learn.ipynb:366
    type: Box   preview: CP*****************************0
    first seen in commit: 4763c87adfee
  - notebooks/tree_explainer/tree_shap_paper/Figures 8-11 NHANES I Survival Model-Copy1.ipynb:3301
    type: TLy   preview: n7*********************************************************i
    first seen in commit: 6e02ab941ce7
  - notebooks/tree_explainer/tree_shap_paper/Figures 8-11 NHANES I Survival Model-Copy1.ipynb:2520
    type: Fmfw   preview: nM*****************************A
    first seen in commit: 6e02ab941ce7
  - notebooks/tree_explainer/tree_shap_paper/Figures 8-11 NHANES I Survival Model-Copy1.ipynb:2520
    type: Box   preview: nI*****************************v
    first seen in commit: 6e02ab941ce7
  - notebooks/tree_explainer/tree_shap_paper/Figures 8-11 NHANES I Survival Model-Copy1.ipynb:2590
    type: Box   preview: H7*****************************Z
    first seen in commit: 6e02ab941ce7
  - notebooks/NHANES I Survival Model.ipynb:559
    type: Sirv   preview: +V*************************************************************************************F
    first seen in commit: 0a3a1526dcaa
  - notebooks/NHANES I Survival Model.ipynb:741
    type: Box   preview: 4v*****************************F
    first seen in commit: 0a3a1526dcaa
  - docs/notebooks/League+of+Legends+Win+Prediction+with+XGBoost.html:12181
    type: Box   preview: x3*****************************b
    first seen in commit: d35ace2441fc
  - notebooks/League of Legends Win Prediction with XGBoost.ipynb:340
    type: Box   preview: x3*****************************b
    first seen in commit: d35ace2441fc
  - notebooks/Scatter Density vs. Violin Plot Comparison.ipynb:235
    type: Box   preview: TT*****************************Q
    first seen in commit: 1a6c273b3488
  - docs/notebooks/Census+income+classification+with+XGBoost.html:23840
    type: Box   preview: fW*****************************1
    first seen in commit: 1e613d7e00ba
  - notebooks/Census income classification with XGBoost.ipynb:442
    type: Box   preview: fW*****************************1
    first seen in commit: 1e613d7e00ba
  - docs/notebooks/Census+income+classification+with+LightGBM.html:35970
    type: TLy   preview: 5u*********************************************************8
    first seen in commit: 4f9e96b27927
  - docs/notebooks/NHANES+I+Survival+Model.html:23979
    type: Box   preview: SC*****************************N
    first seen in commit: 4f9e96b27927
  - notebooks/Census income classification with LightGBM.ipynb:359
    type: TLy   preview: n8*********************************************************O
    first seen in commit: 0a3fcfc0e31a
  - notebooks/NHANES I Survival Model.ipynb:242
    type: TLy   preview: n7*********************************************************h
    first seen in commit: 0a3fcfc0e31a
  - notebooks/NHANES I Survival Model.ipynb:403
    type: Box   preview: SC*****************************N
    first seen in commit: 0a3fcfc0e31a
  - notebooks/NHANES I Survival Model-Copy1.ipynb:52348
    type: Box   preview: Qd*****************************Q
    first seen in commit: 625d7215c898
  - notebooks/NHANES I Survival Model-Copy1.ipynb:52348
    type: Box   preview: 4g*****************************L
    first seen in commit: 625d7215c898
  - docs/notebooks/League+of+Legends+Win+Prediction+with+XGBoost.html:73132
    type: Box   preview: Q4*****************************Q
    first seen in commit: 2b057d3d700a
  - notebooks/League of Legends Win Prediction with XGBoost.ipynb:50744
    type: Box   preview: nz*****************************V
    first seen in commit: 2b057d3d700a
  - notebooks/League of Legends Win Prediction with XGBoost.ipynb:50669
    type: Box   preview: Q4*****************************Q
    first seen in commit: 2b057d3d700a
  - notebooks/League of Legends Win Prediction with XGBoost.ipynb:50849
    type: Box   preview: nE*****************************X
    first seen in commit: 2b057d3d700a
  - docs/notebooks/Census+income+classification+with+LightGBM.html:79217
    type: Miro   preview: 1I************************H
    first seen in commit: d70680819457
  - docs/notebooks/Census+income+classification+with+LightGBM.html:89274
    type: Box   preview: Oi*****************************G
    first seen in commit: d70680819457
  - notebooks/Census income classification with LightGBM.ipynb:51678
    type: Miro   preview: 1I************************H
    first seen in commit: d70680819457
  - notebooks/Census income classification with LightGBM.ipynb:51875
    type: Box   preview: Oi*****************************G
    first seen in commit: d70680819457
  - notebooks/Census income classification with LightGBM.ipynb:51558
    type: Box   preview: nf*****************************8
    first seen in commit: d70680819457
  - docs/notebooks/ImageNet+VGG16+Model+with+Keras.html:14209
    type: Box   preview: qu*****************************8
    first seen in commit: 179df3d589af
  - notebooks/tree_shap_paper/Figure 7 - Airline Tweet Sentiment Analysis.ipynb:369
    type: TLy   preview: Vd*********************************************************0
    first seen in commit: 51092b9623a2
  - notebooks/tree_shap_paper/Figures 8-11 NHANES I Survival Model.ipynb:805
    type: TLy   preview: n7*********************************************************i
    first seen in commit: 51092b9623a2
  - notebooks/tree_shap_paper/Figures 8-11 NHANES I Survival Model.ipynb:154
    type: Box   preview: nI*****************************v
    first seen in commit: 51092b9623a2
  - notebooks/tree_shap_paper/Figures 8-11 NHANES I Survival Model.ipynb:224
    type: Box   preview: H7*****************************Z
    first seen in commit: 51092b9623a2
  - notebooks/tree_shap_paper/Figures 8-11 NHANES I Survival Model.ipynb:154
    type: Fmfw   preview: nM*****************************A
    first seen in commit: 51092b9623a2
  - docs/notebooks/Census+income+classification+with+LightGBM.html:65367
    type: Box   preview: Dx*****************************n
    first seen in commit: b643b49dc37f
  - notebooks/Census income classification with LightGBM.ipynb:51542
    type: Box   preview: Dx*****************************n
    first seen in commit: b643b49dc37f
  - docs/notebooks/NHANES+I+Survival+Model.html:39340
    type: Miro   preview: hw************************5
    first seen in commit: ad6464cb7c19
  - docs/notebooks/NHANES+I+Survival+Model.html:53699
    type: Box   preview: 4g*****************************L
    first seen in commit: ad6464cb7c19
  - docs/notebooks/NHANES+I+Survival+Model.html:53784
    type: Box   preview: Qd*****************************Q
    first seen in commit: ad6464cb7c19
  - notebooks/NHANES I Survival Model.ipynb:931
    type: Box   preview: Qd*****************************Q
    first seen in commit: 31e4536ea8ab
  - notebooks/NHANES I Survival Model.ipynb:931
    type: Box   preview: 4g*****************************L
    first seen in commit: 31e4536ea8ab
  - notebooks/Airline Tweet Sentiment Analysis.ipynb:50616
    type: TLy   preview: Vd*********************************************************0
    first seen in commit: c84afdd569eb
  - docs/notebooks/League+of+Legends+Win+Prediction+with+XGBoost.html:72510
    type: TLy   preview: AJ*********************************************************9
    first seen in commit: 89f404ef2444
  - docs/notebooks/League+of+Legends+Win+Prediction+with+XGBoost.html:90900
    type: UnifyID   preview: Es*****************************************Y
    first seen in commit: 89f404ef2444
  - notebooks/League of Legends Win Prediction with XGBoost.ipynb:50658
    type: TLy   preview: AJ*********************************************************9
    first seen in commit: 89f404ef2444
  - notebooks/League of Legends Win Prediction with XGBoost.ipynb:50798
    type: UnifyID   preview: nE*****************************************M
    first seen in commit: 89f404ef2444
  - notebooks/League of Legends Win Prediction with XGBoost.ipynb:50828
    type: Sirv   preview: \n*************************************************************************************M
    first seen in commit: 89f404ef2444
  - docs/notebooks/python/Census_income_classification_LightGBM.html:72117
    type: TLy   preview: iL*********************************************************w
    first seen in commit: cc776aba79fd

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

