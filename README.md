## 1. Motivation

This repository contains the code for the implementation of text generation in Indic Language.

We tend to implement quote generation in Tamil (and further extend it to other Indian languages like Punjabi). As the dataset for these languages is limited therefore we plan to implement translate learning and observe the results.

For implementation we have used a pretrained [indic-gpt](https://huggingface.co/aashay96/indic-gpt) from hugging face.

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
