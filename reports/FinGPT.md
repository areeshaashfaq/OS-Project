Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/charmingLitteDeveloper/FinGPT

Flagged locations (secret values are not included):

  - fingpt/FinGPT_Forecaster/train_lora.py:30
    type: WeightsAndBiases   preview: ec*************************************4
    first seen in commit: 1190b8cebdd6
  - fingpt/FinGPT_MultiAgentsRAG/Fine_tune_model/fine_tune_GLM2.ipynb:1
    type: WeightsAndBiases   preview: 87*************************************b
    first seen in commit: 01140e566094
  - fingpt/FinGPT_MultiAgentsRAG/Fine_tune_model/fine_tune_GLM2.ipynb:1
    type: HuggingFace   preview: hf**********************************X
    first seen in commit: 01140e566094
  - fingpt/FinGPT-Benchmark/eval_ckpts.py:28
    type: WeightsAndBiases   preview: ec*************************************4
    first seen in commit: 93434010912a
  - fingpt/FinGPT-Benchmark/train_lora.py:27
    type: WeightsAndBiases   preview: ec*************************************4
    first seen in commit: 93434010912a
  - fingpt/FinGPT_MultiAgentsRAG/Fine_tune_model/fine_tune_Llama2.ipynb:1
    type: HuggingFace   preview: hf**********************************X
    first seen in commit: 01140e566094
  - fingpt/FinGPT_MultiAgentsRAG/Fine_tune_model/fine_tune_Llama2.ipynb:1
    type: WeightsAndBiases   preview: 87*************************************b
    first seen in commit: 01140e566094
  - fingpt/FinGPT_sentiment/instruct-FinGPT/load_data.ipynb:22
    type: PhraseAccessToken   preview: 55*************************************************************1
    first seen in commit: 67476059d3a1
  - fingpt/FinGPT-v3/benchmark/benchmarks.ipynb:138
    type: PhraseAccessToken   preview: 55*************************************************************1
    first seen in commit: a6824b6357d1
  - fingpt/FinGPT-v3/data/making_data.ipynb:42
    type: PhraseAccessToken   preview: 55*************************************************************1
    first seen in commit: a6824b6357d1
  - fingpt/FinGPT_sentiment/requests_url.py:23
    type: ZenRows   preview: 60*************************************f
    first seen in commit: 0fc8fc89dcdc
  - fingpt/FinGPT_sentiment/ChatGPT_sentiment_analysis_benchmark.ipynb:115
    type: PhraseAccessToken   preview: 55*************************************************************1
    first seen in commit: 7e1857f0eda6
  - fingpt/FinGPT_sentiment/ChatGPT_sentiment_analysis_benchmark.ipynb:124
    type: PhraseAccessToken   preview: 55*************************************************************1
    first seen in commit: 3909b4061aec
  - fingpt/FinGPT-v1/making_dataset/make_dataset_by_date.ipynb:286
    type: Qase   preview: mH*************************************2
    first seen in commit: b8a16fce57fa
  - demos/FinGPT-v1/data_preparations/download_contents.py:30
    type: CustomRegex   preview: ht******************************s
    first seen in commit: 3e19a734be4a
  - demos/FinGPT-v1/data_preparations/download_contents.py:29
    type: CustomRegex   preview: ht******************************s
    first seen in commit: 3e19a734be4a
  - demo/chatgpt-trading/openai_token/token_.py:2
    type: OpenAI   preview: sk************************************************q
    first seen in commit: 6c6d24a098ce

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

