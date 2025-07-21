from huggingface_hub import InferenceClient

llama_models = [
    'meta-llama/Llama-2-7b-chat-hf',
    'meta-llama/Llama-2-7b',
    'meta-llama/Llama-3.1-8B',
    'meta-llama/Llama-3.1-8B-Instruct',
    'meta-llama/Llama-3.2-1B',
    'meta-llama/Llama-3.2-1B-Instruct',
    'meta-llama/Llama-3.2-3B-Instruct',
    'meta-llama/Meta-Llama-3-8B',
    'meta-llama/Meta-Llama-3-8B-Instruct',
    'meta-llama/Llama-3.3-70B-Instruct',
    'meta-llama/Llama-4-Scout-17B-16E-Instruct',
    'meta-llama/Llama-4-Maverick-17B-128E-Instruct',
    'meta-llama/Llama-3-8B-Instruct',
]

# token = "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"
token = "YOUR_HF_TOKEN_HERE"  # <-- Set your token here before running, or use update_token.py if supported.
client = InferenceClient(token=token)

print("Checking which Llama models are available via the Inference API:")
usable = []
for model in llama_models:
    try:
        # Try a minimal request
        client.text_generation(model=model, prompt="Hello", max_new_tokens=2)
        print(f"✅ {model} is available via Inference API")
        usable.append(model)
    except Exception as e:
        print(f"❌ {model} is NOT available: {str(e).splitlines()[0]}")

print("\nUsable Llama models via Inference API:")
for model in usable:
    print(f"  - {model}") 