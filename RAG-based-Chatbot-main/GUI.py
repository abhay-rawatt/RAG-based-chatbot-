import streamlit as st
import threading
import time
import os
from datetime import datetime
from model_llama4 import Llama4RAGChatbot
try:
    from audio_processor import AudioProcessor
    AUDIO_AVAILABLE = True
except ImportError:
    from audio_processor_simple import SimpleAudioProcessor as AudioProcessor
    AUDIO_AVAILABLE = False

class ChatbotGUI:
    def __init__(self):
        """Initialize the chatbot GUI"""
        self.chatbot = None
        self.audio_processor = None
        self.chat_history = []
        self.is_audio_mode = False
        self.is_listening = False
        
        # Initialize session state
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        if 'is_audio_mode' not in st.session_state:
            st.session_state.is_audio_mode = False
        if 'is_listening' not in st.session_state:
            st.session_state.is_listening = False
        
    def setup_page(self):
        """Setup the Streamlit page configuration"""
        st.set_page_config(
            page_title="RAG Chatbot - Llama-4-Maverick",
            page_icon="🤖",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Custom CSS for better styling
        st.markdown("""
        <style>
        .main-header {
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
            color: #1f77b4;
            margin-bottom: 2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .sub-header {
            font-size: 1.5rem;
            text-align: center;
            color: #666;
            margin-bottom: 2rem;
        }
        .chat-message {
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .user-message {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin-left: 2rem;
        }
        .bot-message {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            margin-right: 2rem;
        }
        .status-indicator {
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: bold;
            text-align: center;
            margin: 1rem 0;
        }
        .status-active {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
        }
        .status-inactive {
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            color: white;
        }
        .stButton > button {
            border-radius: 20px;
            font-weight: bold;
            padding: 0.5rem 2rem;
            border: none;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        .sidebar .sidebar-content {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        </style>
        """, unsafe_allow_html=True)
    
    def initialize_models(self):
        """Initialize the chatbot and audio processor"""
        try:
            with st.spinner("🔄 Initializing models (Llama-4-Maverick)..."):
                self.chatbot = Llama4RAGChatbot()
                self.audio_processor = AudioProcessor()
                st.success("✅ Models initialized successfully!")
                return True
        except Exception as e:
            st.error(f"❌ Failed to initialize models: {e}")
            return False
    
    def display_header(self):
        """Display the main header"""
        st.markdown('<h1 class="main-header">🤖 RAG Chatbot</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Powered by Llama-4-Maverick-17B-128E-Instruct</p>', unsafe_allow_html=True)
    
    def display_sidebar(self):
        """Display the sidebar with controls"""
        with st.sidebar:
            st.markdown("## ⚙️ Settings")
            
            # Audio mode toggle
            if AUDIO_AVAILABLE:
                audio_mode = st.toggle("🎤 Audio Mode", value=st.session_state.is_audio_mode)
                if audio_mode != st.session_state.is_audio_mode:
                    st.session_state.is_audio_mode = audio_mode
                    st.rerun()
                
                if st.session_state.is_audio_mode:
                    st.info("🎤 Audio mode is active. You can speak to the chatbot!")
            else:
                st.warning("⚠️ Full audio support not available. Text-to-speech only.")
                st.info("💡 Install PyAudio for speech-to-text: pip install pyaudio")
                
                # Audio controls
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("🎤 Start Listening", key="start_listen"):
                        self.start_audio_listening()
                
                with col2:
                    if st.button("⏹️ Stop Listening", key="stop_listen"):
                        self.stop_audio_listening()
                
                # Audio settings
                st.markdown("### 🔊 Audio Settings")
                speech_rate = st.slider("Speech Rate (WPM)", 50, 300, 150)
                volume = st.slider("Volume", 0.0, 1.0, 0.9)
                
                if st.button("Apply Audio Settings"):
                    if self.audio_processor:
                        self.audio_processor.change_speech_rate(speech_rate)
                        self.audio_processor.change_volume(volume)
                        st.success("✅ Audio settings applied!")
            
            # Chat controls
            st.markdown("### 💬 Chat Controls")
            
            if st.button("🗑️ Clear Chat History"):
                st.session_state.chat_history = []
                st.rerun()
            
            if st.button("📚 Update Knowledge Base"):
                self.show_knowledge_update()
            
            # Model info
            st.markdown("### ℹ️ Model Information")
            st.info("""
            **Model:** Llama-4-Maverick-17B-128E-Instruct
            **Type:** RAG (Retrieval-Augmented Generation)
            **Knowledge Base:** Custom text file
            **Audio Support:** Speech-to-Text & Text-to-Speech
            **Mode:** Local Model with Pipeline
            """)
    
    def display_chat_interface(self):
        """Display the main chat interface"""
        # Chat container
        chat_container = st.container()
        
        with chat_container:
            # Display chat history
            for message in st.session_state.chat_history:
                if message["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>👤 You:</strong> {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message bot-message">
                        <strong>🤖 Assistant:</strong> {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
            
            # Status indicators
            if st.session_state.is_audio_mode:
                if st.session_state.is_listening:
                    st.markdown('<div class="status-indicator status-active">🎤 Listening...</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="status-indicator status-inactive">⏸️ Not Listening</div>', unsafe_allow_html=True)
            
            # Input area
            if not st.session_state.is_audio_mode:
                # Text input
                user_input = st.text_input("💬 Ask me anything:", key="user_input", placeholder="Type your question here...")
                
                col1, col2 = st.columns([1, 4])
                with col1:
                    if st.button("🚀 Send", key="send_text"):
                        if user_input.strip():
                            self.process_text_input(user_input)
                
                with col2:
                    if st.button("🎤 Switch to Audio", key="switch_audio"):
                        st.session_state.is_audio_mode = True
                        st.rerun()
            else:
                # Audio input
                st.markdown("### 🎤 Voice Input")
                col1, col2, col3 = st.columns([1, 1, 2])
                
                with col1:
                    if st.button("🎤 Listen", key="listen_once"):
                        self.listen_once()
                
                with col2:
                    if st.button("📝 Switch to Text", key="switch_text"):
                        st.session_state.is_audio_mode = False
                        st.rerun()
    
    def process_text_input(self, user_input: str):
        """Process text input and generate response"""
        if not self.chatbot:
            st.error("❌ Chatbot not initialized!")
            return
        
        # Add user message to history
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now()
        })
        
        # Generate response
        with st.spinner("🤖 Thinking..."):
            try:
                response = self.chatbot.generate_response(user_input)
                
                # Add bot response to history
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response,
                    "timestamp": datetime.now()
                })
                
                # Speak response if in audio mode
                if st.session_state.is_audio_mode and self.audio_processor:
                    self.audio_processor.text_to_speech(response, block=False)
                
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error generating response: {e}")
    
    def listen_once(self):
        """Listen for a single voice input"""
        if not self.audio_processor:
            st.error("❌ Audio processor not initialized!")
            return
        
        with st.spinner("🎤 Listening..."):
            text = self.audio_processor.speech_to_text(timeout=10)
            
            if text:
                st.session_state.user_input = text
                self.process_text_input(text)
            else:
                st.warning("⚠️ No speech detected or could not understand audio")
    
    def start_audio_listening(self):
        """Start continuous audio listening"""
        if not self.audio_processor:
            st.error("❌ Audio processor not initialized!")
            return
        
        st.session_state.is_listening = True
        
        def audio_callback(text):
            if text:
                self.process_text_input(text)
        
        # Start continuous listening in background
        self.audio_processor.start_continuous_listening(audio_callback)
        st.success("✅ Started listening for voice input!")
    
    def stop_audio_listening(self):
        """Stop continuous audio listening"""
        if self.audio_processor:
            self.audio_processor.stop_continuous_listening()
            st.session_state.is_listening = False
            st.success("✅ Stopped listening!")
    
    def show_knowledge_update(self):
        """Show knowledge base update interface"""
        st.markdown("### 📚 Update Knowledge Base")
        
        new_content = st.text_area(
            "Add new content to knowledge base:",
            height=200,
            placeholder="Enter new information here..."
        )
        
        if st.button("💾 Save to Knowledge Base"):
            if new_content.strip():
                try:
                    self.chatbot.update_knowledge_base(new_content)
                    st.success("✅ Knowledge base updated successfully!")
                except Exception as e:
                    st.error(f"❌ Failed to update knowledge base: {e}")
            else:
                st.warning("⚠️ Please enter some content")
    
    def run(self):
        """Run the main GUI application"""
        self.setup_page()
        self.display_header()
        
        # Initialize models if not already done
        if not self.chatbot:
            if not self.initialize_models():
                st.error("❌ Failed to initialize models. Please check your setup.")
                return
        
        # Display sidebar and main interface
        self.display_sidebar()
        self.display_chat_interface()

def main():
    """Main function to run the GUI"""
    try:
        gui = ChatbotGUI()
        gui.run()
    except Exception as e:
        st.error(f"❌ Application error: {e}")
        st.exception(e)

if __name__ == "__main__":
    main() 