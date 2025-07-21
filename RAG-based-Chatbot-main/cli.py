import argparse
import sys
import os
from model import RAGChatbot
from audio_processor import AudioProcessor

class ChatbotCLI:
    def __init__(self):
        """Initialize the CLI chatbot"""
        self.chatbot = None
        self.audio_processor = None
        self.is_audio_mode = False
        
    def initialize(self):
        """Initialize the chatbot and audio processor"""
        try:
            print("🔄 Initializing RAG Chatbot (Llama-4-Maverick)...")
            from model_llama4 import Llama4RAGChatbot
            self.chatbot = Llama4RAGChatbot()
            self.audio_processor = AudioProcessor()
            print("✅ Initialization complete!")
            return True
        except Exception as e:
            print(f"❌ Initialization failed: {e}")
            return False
    
    def display_help(self):
        """Display help information"""
        print("""
🤖 RAG Chatbot CLI - Powered by Llama-4-Maverick

Commands:
  /help          - Show this help message
  /audio         - Toggle audio mode (speech input/output)
  /text          - Switch to text-only mode
  /clear         - Clear chat history
  /quit          - Exit the chatbot
  /update        - Update knowledge base
  /status        - Show current status

Usage:
  - Type your questions directly for text input
  - Use /audio to enable voice input/output
  - Use /help for more commands
        """)
    
    def display_status(self):
        """Display current status"""
        print(f"""
📊 Current Status:
  Audio Mode: {'🎤 Enabled' if self.is_audio_mode else '📝 Disabled'}
  Chatbot: {'✅ Ready' if self.chatbot else '❌ Not Ready'}
  Audio Processor: {'✅ Ready' if self.audio_processor else '❌ Not Ready'}
        """)
    
    def toggle_audio_mode(self):
        """Toggle audio mode"""
        self.is_audio_mode = not self.is_audio_mode
        mode = "🎤 Audio Mode" if self.is_audio_mode else "📝 Text Mode"
        print(f"✅ Switched to {mode}")
    
    def process_text_input(self, user_input: str):
        """Process text input and generate response"""
        if not self.chatbot:
            print("❌ Chatbot not initialized!")
            return
        
        try:
            print("🤖 Thinking...")
            response = self.chatbot.generate_response(user_input)
            
            print(f"\n🤖 Assistant: {response}\n")
            
            # Speak response if in audio mode
            if self.is_audio_mode and self.audio_processor:
                self.audio_processor.text_to_speech(response)
            
        except Exception as e:
            print(f"❌ Error generating response: {e}")
    
    def process_audio_input(self):
        """Process audio input"""
        if not self.audio_processor:
            print("❌ Audio processor not initialized!")
            return
        
        print("🎤 Listening... (speak now)")
        text = self.audio_processor.speech_to_text(timeout=10)
        
        if text:
            print(f"👤 You said: {text}")
            self.process_text_input(text)
        else:
            print("⚠️ No speech detected or could not understand audio")
    
    def update_knowledge_base(self):
        """Update the knowledge base"""
        if not self.chatbot:
            print("❌ Chatbot not initialized!")
            return
        
        print("📚 Knowledge Base Update")
        print("Enter new content (type 'END' on a new line to finish):")
        
        lines = []
        while True:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        
        if lines:
            new_content = '\n'.join(lines)
            try:
                self.chatbot.update_knowledge_base(new_content)
                print("✅ Knowledge base updated successfully!")
            except Exception as e:
                print(f"❌ Failed to update knowledge base: {e}")
        else:
            print("⚠️ No content provided")
    
    def run(self):
        """Run the CLI chatbot"""
        if not self.initialize():
            return
        
        print("""
🤖 Welcome to RAG Chatbot!
Type /help for available commands.
Type /quit to exit.
        """)
        
        while True:
            try:
                if self.is_audio_mode:
                    # Audio mode
                    print("\n🎤 Audio Mode - Press Enter to speak, or type a command:")
                    user_input = input().strip()
                    
                    if user_input.startswith('/'):
                        # Process command
                        self.process_command(user_input)
                    else:
                        # Listen for speech
                        self.process_audio_input()
                else:
                    # Text mode
                    user_input = input("\n💬 You: ").strip()
                    
                    if user_input.startswith('/'):
                        # Process command
                        self.process_command(user_input)
                    elif user_input:
                        # Process text input
                        self.process_text_input(user_input)
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except EOFError:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    def process_command(self, command: str):
        """Process CLI commands"""
        cmd = command.lower().strip()
        
        if cmd == '/help':
            self.display_help()
        elif cmd == '/audio':
            self.toggle_audio_mode()
        elif cmd == '/text':
            self.is_audio_mode = False
            print("✅ Switched to Text Mode")
        elif cmd == '/clear':
            print("🗑️ Chat history cleared")
        elif cmd == '/quit':
            print("👋 Goodbye!")
            sys.exit(0)
        elif cmd == '/update':
            self.update_knowledge_base()
        elif cmd == '/status':
            self.display_status()
        else:
            print(f"❓ Unknown command: {command}")
            print("Type /help for available commands")

def main():
    """Main function"""
    # Check if called directly or imported
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='RAG Chatbot CLI')
        parser.add_argument('--audio', action='store_true', help='Start in audio mode')
        parser.add_argument('--test', action='store_true', help='Run quick test')
        
        args = parser.parse_args()
        
        cli = ChatbotCLI()
        
        if args.test:
            # Run quick test
            print("🧪 Running quick test...")
            if cli.initialize():
                test_questions = [
                    "What is artificial intelligence?",
                    "Explain machine learning",
                    "What are neural networks?"
                ]
                
                for question in test_questions:
                    print(f"\n❓ Question: {question}")
                    cli.process_text_input(question)
                    print("-" * 50)
        else:
            # Run normal CLI
            if args.audio:
                cli.is_audio_mode = True
            cli.run()
    else:
        # Called from main.py - just run the CLI
        cli = ChatbotCLI()
        cli.run()

if __name__ == "__main__":
    main() 