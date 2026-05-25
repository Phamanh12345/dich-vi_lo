# Vietnamese → Lao Translation Model

This project provides a Vietnamese → Lao translation model fine-tuned with LoRA based on `facebook/m2m100_418M`.

Developed by: **Phạm Tuấn Anh**  
GitHub: **Phamanh12345**

---

## Project Structure

```text
dich-vi_lo/
│
├── model/              # LoRA adapter and tokenizer files
├── dataset/            # Processed Vietnamese-Lao dataset
├── translate.py        # Script for testing translation
├── requirements.txt    # Required Python libraries
└── README.md           # Project documentation
```

---

## Model Details

- Task: Vietnamese → Lao machine translation
- Base model: `facebook/m2m100_418M`
- Fine-tuning method: LoRA
- Framework: PyTorch, Transformers, PEFT

Note: This repository stores a LoRA adapter. The base model will be downloaded automatically when running the script.

---

## Installation

```bash
git clone https://github.com/Phamanh12345/dich-vi_lo.git
cd dich-vi_lo
pip install -r requirements.txt
```

---

## Model Folder Explanation

The `model/` folder contains the LoRA adapter and tokenizer files used for Vietnamese → Lao translation.

```text
model/
│
├── adapter_config.json
├── adapter_model.safetensors
├── added_tokens.json
├── sentencepiece.bpe.model
├── tokenizer_config.json
└── vocab.json
```

---

## Usage

```bash
python translate.py
```

Example:

```text
Input:
Tôi muốn uống nước

Output:
ຂ້ອຍຕ້ອງການດື່ມນ້ໍາ
```

---

## Dataset

The original dataset contains Vietnamese-Lao parallel sentences.  
Only Vietnamese → Lao sentence pairs were used for fine-tuning.

The dataset was split into:

```text
train 90% / validation 5% / test 5%
```

---

## Author

**Phạm Tuấn Anh**  
GitHub: https://github.com/Phamanh12345

---
