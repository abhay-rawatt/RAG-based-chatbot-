from huggingface_hub import InferenceClient, HfApi

# token = "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"
token = "YOUR_HF_TOKEN_HERE"  # <-- Set your token here before running, or use update_token.py if supported.
client = InferenceClient(token=token)
api = HfApi()

print("Checking Hugging Face token validity...")
try:
    user = api.whoami(token=token)
    print(f"✅ Token is valid. Logged in as: {user['name']}")
except Exception as e:
    print(f"❌ Token is invalid or expired: {e}")
    exit(1)

print("\nTesting Inference API with a public model (gpt2)...")
try:
    response = client.text_generation(
        model="gpt2",
        prompt="Hello, world!",
        max_new_tokens=5,
    )
    print("✅ Inference API is working for public models.")
    print("Sample response:", response)
except Exception as e:
    msg = str(e)
    print(f"❌ Inference API call failed: {msg}")
    if "quota" in msg.lower() or "limit" in msg.lower():
        print("⚠️ You may have exceeded your free tier quota.")
    elif "forbidden" in msg.lower() or "403" in msg:
        print("⚠️ Your token may not have the right permissions or you are over quota.")
    elif "not found" in msg.lower() or "404" in msg:
        print("⚠️ The model is not available via the Inference API.")
    elif "too many requests" in msg.lower() or "429" in msg:
        print("⚠️ You are being rate-limited. Wait and try again later.")
    else:
        print("⚠️ Unknown error. Check your account and network.")

print("\nFor detailed quota and usage, please visit: https://huggingface.co/settings/billing") 