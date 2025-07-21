import os
import numpy as np
import faiss
from typing import List, Dict, Any
from huggingface_hub import InferenceClient, login
from sentence_transformers import SentenceTransformer

class Llama4RAGChatbot:
    def __init__(self, model_name: str = "meta-llama/Llama-4-Maverick-17B-128E-Instruct", 
                 hf_token: str = "YOUR_HF_TOKEN_HERE",  # <-- Set by running update_token.py. Do NOT hardcode your token here!
                 knowledge_file: str = "knowledge.txt",
                 chunk_size: int = 512,
                 chunk_overlap: int = 50,
                 top_k: int = 3):
        """
        Initialize the RAG Chatbot with Llama-4-Maverick model
        
        Args:
            model_name: HuggingFace model name
            hf_token: HuggingFace API token
            knowledge_file: Path to knowledge base file
            chunk_size: Size of text chunks for embedding
            chunk_overlap: Overlap between chunks
            top_k: Number of top relevant chunks to retrieve
        """
        self.model_name = model_name
        self.hf_token = hf_token
        self.knowledge_file = knowledge_file
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.top_k = top_k
        
        # Initialize components
        self._login_hf()
        self._load_inference_client()
        self._load_knowledge_base()
        self._create_embeddings()
        
    def _login_hf(self):
        """Login to Hugging Face"""
        try:
            login(token=self.hf_token)
            print("✅ Successfully logged in to HuggingFace")
        except Exception as e:
            print(f"❌ Failed to login to HuggingFace: {e}")
            raise
    
    def _load_inference_client(self):
        """Load the InferenceClient for online API calls"""
        try:
            print(f"🔄 Setting up InferenceClient for {self.model_name}...")
            self.client = InferenceClient(token=self.hf_token)
            print("✅ InferenceClient ready")
            
            # Load sentence transformer for embeddings
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
            print("✅ All models loaded successfully")
            
        except Exception as e:
            print(f"❌ Failed to set up InferenceClient: {e}")
            raise
    
    def _load_knowledge_base(self):
        """Load and chunk the knowledge base"""
        try:
            print("📚 Loading knowledge base...")
            
            if not os.path.exists(self.knowledge_file):
                raise FileNotFoundError(f"Knowledge file {self.knowledge_file} not found")
            
            with open(self.knowledge_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Split content into paragraphs
            paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
            
            # Create chunks with overlap
            self.chunks = []
            for paragraph in paragraphs:
                if len(paragraph) <= self.chunk_size:
                    self.chunks.append(paragraph)
                else:
                    # Split long paragraphs into chunks
                    words = paragraph.split()
                    for i in range(0, len(words), self.chunk_size - self.chunk_overlap):
                        chunk = ' '.join(words[i:i + self.chunk_size])
                        if chunk.strip():
                            self.chunks.append(chunk)
            
            print(f"✅ Knowledge base loaded: {len(self.chunks)} chunks created")
            
        except Exception as e:
            print(f"❌ Failed to load knowledge base: {e}")
            raise
    
    def _create_embeddings(self):
        """Create embeddings for knowledge chunks"""
        try:
            print("🔍 Creating embeddings...")
            
            # Generate embeddings for all chunks
            embeddings = self.embedding_model.encode(self.chunks, show_progress_bar=True)
            
            # Create FAISS index for efficient similarity search
            dimension = embeddings.shape[1]
            self.index = faiss.IndexFlatIP(dimension)  # Inner Product for cosine similarity
            
            # Normalize embeddings for cosine similarity
            faiss.normalize_L2(embeddings)
            self.index.add(embeddings.astype('float32'))
            
            print(f"✅ Embeddings created: {len(self.chunks)} chunks indexed")
            
        except Exception as e:
            print(f"❌ Failed to create embeddings: {e}")
            raise
    
    def _retrieve_relevant_chunks(self, query: str) -> List[str]:
        """Retrieve most relevant chunks for a given query"""
        try:
            # Generate query embedding
            query_embedding = self.embedding_model.encode([query])
            faiss.normalize_L2(query_embedding)
            
            # Search for similar chunks
            scores, indices = self.index.search(query_embedding.astype('float32'), self.top_k)
            
            # Return relevant chunks
            relevant_chunks = [self.chunks[i] for i in indices[0]]
            return relevant_chunks
            
        except Exception as e:
            print(f"❌ Failed to retrieve chunks: {e}")
            return []
    
    def _generate_with_inference_api(self, prompt: str) -> str:
        """Generate response using Inference API"""
        try:
            print("🌐 Using Hugging Face Inference API...")
            response = self.client.text_generation(
                model=self.model_name,
                prompt=prompt,
                max_new_tokens=200,
                temperature=0.7,
            )
            return response
        except Exception as e:
            print(f"❌ Inference API generation failed: {e}")
            return self._generate_simple_response(prompt)
    
    def _generate_simple_response(self, prompt: str) -> str:
        """Generate a simple response based on context without model"""
        try:
            # Extract the question from the prompt
            if "Question:" in prompt:
                question = prompt.split("Question:")[-1].split("Answer:")[0].strip()
            else:
                question = prompt
            
            # Extract context from the prompt
            if "Context:" in prompt:
                context = prompt.split("Context:")[-1].split("Question:")[0].strip()
            else:
                context = ""
            
            # Simple response generation based on context
            if context:
                # Find the most relevant sentence from context
                sentences = context.split('.')
                relevant_sentences = []
                
                # Look for sentences that contain keywords from the question
                question_words = question.lower().split()
                for sentence in sentences:
                    sentence_lower = sentence.lower()
                    if any(word in sentence_lower for word in question_words if len(word) > 3):
                        relevant_sentences.append(sentence.strip())
                
                if relevant_sentences:
                    return f"Based on the information available: {relevant_sentences[0]}."
                else:
                    return "I don't have specific information about that in my knowledge base, but I can help you with other topics."
            else:
                return "I don't have information about that in my knowledge base. Please ask me about topics covered in my knowledge base."
                
        except Exception as e:
            return f"I apologize, but I encountered an error while processing your request: {str(e)}"
    
    def generate_response(self, query: str) -> str:
        """Generate a response using RAG with Llama-4-Maverick"""
        try:
            # Retrieve relevant chunks
            relevant_chunks = self._retrieve_relevant_chunks(query)
            context = "\n\n".join(relevant_chunks)
            
            # Create prompt for the model
            prompt = f"Answer the following question using ONLY the provided context. If the answer is not in the context, say 'I don't have information about that in my knowledge base.'\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
            
            # Generate response using appropriate method
            response = self._generate_with_inference_api(prompt)
            
            return response
            
        except Exception as e:
            print(f"❌ Failed to generate response: {e}")
            return f"I apologize, but I encountered an error while processing your request: {str(e)}"
    
    def get_chat_history(self) -> List[Dict[str, str]]:
        """Get chat history (placeholder for future implementation)"""
        return []
    
    def clear_chat_history(self):
        """Clear chat history (placeholder for future implementation)"""
        pass
    
    def update_knowledge_base(self, new_content: str):
        """Update the knowledge base with new content"""
        try:
            # Append new content to knowledge file
            with open(self.knowledge_file, 'a', encoding='utf-8') as f:
                f.write(f"\n\n{new_content}")
            
            # Reload knowledge base and recreate embeddings
            self._load_knowledge_base()
            self._create_embeddings()
            
            print("✅ Knowledge base updated successfully")
            
        except Exception as e:
            print(f"❌ Failed to update knowledge base: {e}")
            raise

# Test function
def test_llama4_rag_chatbot():
    """Test the Llama-4-Maverick RAG chatbot"""
    try:
        chatbot = Llama4RAGChatbot()
        
        # Test questions
        test_questions = [
            "What is artificial intelligence?",
            "Explain machine learning",
            "What are neural networks?"
        ]
        
        print("\n🧪 Testing Llama-4-Maverick RAG Chatbot (Online API):")
        print("=" * 50)
        
        for question in test_questions:
            print(f"\n❓ Question: {question}")
            response = chatbot.generate_response(question)
            print(f"🤖 Answer: {response}")
            print("-" * 50)
            
    except Exception as e:
        print(f"❌ Test failed: {e}")

if __name__ == "__main__":
    test_llama4_rag_chatbot() 