from huggingface_hub import InferenceClient

small_models = [
    'distilgpt2',
    'gpt2',
    'facebook/blenderbot-400M-distill',
    'microsoft/DialoGPT-medium',
    'microsoft/DialoGPT-large',
    'microsoft/DialoGPT-small',
]

# token = "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"
token = "YOUR_HF_TOKEN_HERE"  # <-- Set your token here before running, or use update_token.py if supported.
client = InferenceClient(token=token)

print("Checking which small/older models are available via the Inference API:")
usable = []
for model in small_models:
    try:
        # Try a minimal request
        client.text_generation(model=model, prompt="Hello", max_new_tokens=2)
        print(f"✅ {model} is available via Inference API")
        usable.append(model)
    except Exception as e:
        print(f"❌ {model} is NOT available: {str(e).splitlines()[0]}")

print("\nUsable models via Inference API:")
for model in usable:
    print(f"  - {model}") 