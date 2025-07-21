from huggingface_hub import InferenceClient

# client = InferenceClient(token="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")
client = InferenceClient(token="YOUR_HF_TOKEN_HERE")  # <-- Set your token here before running, or use update_token.py if supported.
response = client.text_generation(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    prompt="What is artificial intelligence?",
    max_new_tokens=200,
    temperature=0.7,
)
print("Response from Mistral-7B-Instruct-v0.2:")
print(response) 