from transformers import M2M100Tokenizer
from transformers import M2M100ForConditionalGeneration
from peft import PeftModel

BASE_MODEL = "facebook/m2m100_418M"
LORA_PATH = "model"

tokenizer = M2M100Tokenizer.from_pretrained(LORA_PATH)

base_model = M2M100ForConditionalGeneration.from_pretrained(BASE_MODEL)

model = PeftModel.from_pretrained(
    base_model,
    LORA_PATH
)

def translate_vi_to_lao(text):
    tokenizer.src_lang = "vi"

    encoded = tokenizer(
        text,
        return_tensors="pt"
    )

    output = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.get_lang_id("lo"),
        max_length=96
    )

    return tokenizer.decode(output[0], skip_special_tokens=True)

if __name__ == "__main__":
    while True:
        text = input("Nhập tiếng Việt: ")

        if text.lower() == "exit":
            break

        result = translate_vi_to_lao(text)
        print("Tiếng Lào:", result)
