# Vietnamese → Lao Translation Model
This project provides a Vietnamese → Lao translation model fine-tuned with LoRA based on facebook/m2m100_418M.
Fine-tuned Vietnamese to Lao translation model using LoRA on:

```text
facebook/m2m100_418M
```

Developed by: **Phạm Tuấn Anh**

GitHub: **Phamanh12345**

---

# Project Structure

```text
dich-vi_lo/
│
├── model/
│   ├── adapter_config.json
│   ├── adapter_model.safetensors
│   ├── tokenizer_config.json
│   ├── sentencepiece.bpe.model
│   └── vocab.json
│
├── dataset/
│   └── vi_lo_dataset_split.zip
│
├── translate.py
├── requirements.txt
└── README.md
```

---

# Features

- Vietnamese → Lao translation
- LoRA fine-tuning
- Based on M2M100 multilingual model

---

# Installation

```bash
pip install -r requirements.txt
```

---

# Usage

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

# Dataset

The dataset was processed into:

```text
train / validation / test
```

Only Vietnamese → Lao pairs were used.

---

GitHub:

```text
https://github.com/Phamanh12345
```

Please keep credits when reusing the model or source code.
