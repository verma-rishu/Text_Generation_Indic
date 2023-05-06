## 1. Motivation

This repository contains the code for the implementation of text generation in Indic Language.

We tend to implement quote generation in Tamil & Punjabi (and further extend it to other Indian languages like Malayalam). As the dataset for these languages is limited therefore we plan to implement translate learning and observe the results.

For implementation we have used a pretrained [indic-gpt](https://huggingface.co/aashay96/indic-gpt) from hugging face.

We decided to use GPT-2 after trying observing the results on LSTM, the link to this implementation can be found [here](https://github.com/verma-rishu/Text_Generation_LSTM) 

## 2. Environment

- Python 3.8.0
- PyTorch 2.0.*
- CUDA 11.7
- [Transformers](https://github.com/huggingface/transformers)

Prepare the anaconda environment:

```bash
conda create -n qtg python=3.8.0
conda activate qtg
pip install -r requirements.txt
```
## References
[1] https://github.com/huggingface/transformers

[2] Divyanshu Kakwani, Anoop Kunchukuttan, Satish
Golla, NC Gokul, Avik Bhattacharyya, Mitesh M
Khapra, and Pratyush Kumar. 2020. IndicNLPSuite:
Monolingual corpora, evaluation benchmarks and
pre-trained multilingual language models for Indian
languages. In Findings of the Association for
Computational Linguistics: EMNLP 2020. 4948–4961

[3] [How to evaluate Text Generation Models](https://towardsdatascience.com/how-to-evaluate-text-generation-models-metrics-for-automatic-evaluation-of-nlp-models-e1c251b04ec1)

[4] [How the Guardian approaches quote extraction with NLP](https://explosion.ai/blog/guardian)
