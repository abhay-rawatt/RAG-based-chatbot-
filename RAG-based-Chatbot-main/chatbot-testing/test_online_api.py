import os
import requests
from huggingface_hub import InferenceClient, login

def test_hf_token_validity(token):
    """Test if the Hugging Face token is valid"""
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get("https://huggingface.co/api/whoami", headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            print(f"✅ Token is valid for user: {user_info.get('name', 'Unknown')}")
            return True
        else:
            print(f"❌ Token validation failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Token validation error: {e}")
        return False

def test_model_availability(client, model_name):
    """Test if a specific model is available via Inference API"""
    try:
        # Try a simple text generation request
        response = client.text_generation(
            model=model_name,
            prompt="Hello",
            max_new_tokens=10,
            temperature=0.7,
        )
        print(f"✅ {model_name} is available via Inference API")
        return True
    except Exception as e:
        print(f"❌ {model_name} is NOT available via Inference API: {e}")
        return False

def test_available_models():
    """Test various models to see which ones are available"""
    # token = "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"  # <-- Change this token for other accounts
    token = "YOUR_HF_TOKEN_HERE"  # <-- Set your token here before running, or use update_token.py if supported.
    
    print("🔍 Testing Hugging Face token and model availability...")
    print("=" * 60)
    
    # Test token validity
    if not test_hf_token_validity(token):
        print("❌ Token is invalid. Please check your Hugging Face token.")
        return
    
    # Login to Hugging Face
    try:
        login(token=token)
        print("✅ Successfully logged in to Hugging Face")
    except Exception as e:
        print(f"❌ Failed to login: {e}")
        return
    
    # Initialize InferenceClient
    try:
        client = InferenceClient(token=token)
        print("✅ InferenceClient initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize InferenceClient: {e}")
        return
    
    # Test various models
    models_to_test = [
        "meta-llama/Llama-4-Maverick-17B-128E-Instruct",
        "meta-llama/Llama-2-7b-chat-hf",
        "mistralai/Mistral-7B-Instruct-v0.2",
        "microsoft/DialoGPT-medium",
        "gpt2",
        "distilgpt2",
        "facebook/blenderbot-400M-distill"
    ]
    
    print("\n🧪 Testing model availability via Inference API:")
    print("-" * 60)
    
    available_models = []
    for model in models_to_test:
        if test_model_availability(client, model):
            available_models.append(model)
    
    print(f"\n📊 Results:")
    print(f"✅ Available models: {len(available_models)}")
    print(f"❌ Unavailable models: {len(models_to_test) - len(available_models)}")
    
    if available_models:
        print(f"\n🎉 Available models for your account:")
        for model in available_models:
            print(f"  - {model}")
    else:
        print(f"\n⚠️ No models are available via Inference API for your account.")
        print("This is normal for free Hugging Face accounts.")
        print("Consider upgrading to a paid plan or using local models.")

def test_rag_pipeline():
    """Test the RAG pipeline with online API"""
    try:
        from model_llama4 import Llama4RAGChatbot
        
        print("\n🧪 Testing RAG Pipeline with Online API:")
        print("=" * 60)
        
        chatbot = Llama4RAGChatbot()
        
        # Test questions
        test_questions = [
            "What is artificial intelligence?",
            "Explain machine learning",
            "What are neural networks?"
        ]
        
        for question in test_questions:
            print(f"\n❓ Question: {question}")
            try:
                response = chatbot.generate_response(question)
                print(f"🤖 Answer: {response}")
            except Exception as e:
                print(f"❌ Error: {e}")
            print("-" * 50)
            
    except Exception as e:
        print(f"❌ RAG pipeline test failed: {e}")

if __name__ == "__main__":
    print("🚀 Hugging Face API and RAG Pipeline Test")
    print("=" * 60)
    
    # Test model availability
    test_available_models()
    
    # Test RAG pipeline
    test_rag_pipeline()
    
    print("\n✅ Testing complete!") 