#!/usr/bin/env python3
"""
Simple script to update Hugging Face token in the model file.
"""

import os
import re

# List of files to update (relative to this script's location)
FILES_TO_UPDATE = [
    "model_llama4.py",
    os.path.join("chatbot-testing", "test_online_api.py"),
    os.path.join("chatbot-testing", "test_inference_api.py"),
    os.path.join("chatbot-testing", "check_llama_inference_api.py"),
    os.path.join("chatbot-testing", "check_inference_api_models.py"),
    os.path.join("chatbot-testing", "check_hf_account_status.py"),
]

TOKEN_PLACEHOLDER = "YOUR_HF_TOKEN_HERE"

def update_token_in_file(filepath, new_token):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    new_content, n = re.subn(
        rf'("|\")(?:{TOKEN_PLACEHOLDER})("|\")',
        f'"{new_token}"',
        content
    )
    if n > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ Updated token in {filepath}")
    else:
        print(f"ℹ️  No token placeholder found in {filepath}")

def main():
    print("\n=== Hugging Face Token Updater ===\n")
    new_token = input("Enter your Hugging Face token (starts with 'hf_'): ").strip()
    if not new_token.startswith("hf_"):
        print("⚠️  Warning: Token should start with 'hf_'")
    for rel_path in FILES_TO_UPDATE:
        abs_path = os.path.join(os.path.dirname(__file__), rel_path)
        if os.path.exists(abs_path):
            update_token_in_file(abs_path, new_token)
        else:
            print(f"❌ File not found: {rel_path}")
    print("\nDone! Your token has been updated in all relevant files.")
    print("You can now run the chatbot and tests without exposing your token in the codebase.")

if __name__ == "__main__":
    main() 