from transformers import M2M100Tokenizer
from transformers import M2M100ForConditionalGeneration
from peft import PeftModel

base_model_name = "facebook/m2m100_418M"

lora_path = "vi_to_lao_lora"

print("Loading tokenizer...")
tokenizer = M2M100Tokenizer.from_pretrained(lora_path)

print("Loading base model...")
base_model = M2M100ForConditionalGeneration.from_pretrained(
    base_model_name
)

print("Loading LoRA...")
model = PeftModel.from_pretrained(
    base_model,
    lora_path
)

def translate_vi_to_lao(text):

    tokenizer.src_lang = "vi"

    encoded = tokenizer(
        text,
        return_tensors="pt"
    )

    generated_tokens = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.get_lang_id("lo"),
        max_length=96
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