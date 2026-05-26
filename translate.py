from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
from peft import PeftModel

base_model_name = "facebook/nllb-200-distilled-600M"

lora_path = "vi_to_lao_nllb_lora"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(lora_path)

print("Loading base model...")
base_model = AutoModelForSeq2SeqLM.from_pretrained(base_model_name)

print("Loading LoRA...")
model = PeftModel.from_pretrained(
    base_model,
    lora_path
)

def translate_vi_to_lao(text):
    tokenizer.src_lang = "vie_Latn"

    encoded = tokenizer(
        text,
        return_tensors="pt"
    )

    generated_tokens = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids("lao_Laoo"),
        max_length=128,
        num_beams=5
    )

    result = tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True
    )

    return result[0]

while True:
    text = input("Nhập tiếng Việt: ")

    if text.lower() == "exit":
        break

    result = translate_vi_to_lao(text)

    print("Tiếng Lào:", result)
    print()
