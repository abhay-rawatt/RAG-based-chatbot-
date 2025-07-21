#!/usr/bin/env python3
"""
RAG Chatbot - Llama-4-Maverick-17B-128E-Instruct
Main launcher script

This script provides a menu to choose between different interfaces:
1. Streamlit GUI (recommended)
2. Command Line Interface
3. Quick Test
4. Exit
"""

import os
import sys
import subprocess
import argparse

def print_banner():
    """Print the application banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                    🤖 RAG CHATBOT                            ║
║         Powered by Llama-4-Maverick-17B-128E-Instruct        ║
║                                                              ║
║  Features:                                                   ║
║  • Retrieval-Augmented Generation (RAG)                      ║
║  • Speech-to-Text & Text-to-Speech                           ║
║  • Modern Web GUI & Command Line Interface                   ║
║  • Custom Knowledge Base Support                             ║
║  • Real-time Audio Processing                                ║
║  • Advanced Image-Text-to-Text Capabilities                  ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        ('streamlit', 'streamlit'),
        ('transformers', 'transformers'),
        ('torch', 'torch'),
        ('sentence-transformers', 'sentence_transformers'),
        ('faiss-cpu', 'faiss'),  # Check import faiss
        ('speechrecognition', 'speech_recognition'),
        ('pyttsx3', 'pyttsx3'),
        ('sounddevice', 'sounddevice'),
        ('numpy', 'numpy'),
        ('pandas', 'pandas')
    ]
    
    missing_packages = []
    
    for pkg_name, import_name in required_packages:
        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(pkg_name)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Install missing packages with:")
        print("   pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed!")
    return True

def run_streamlit_gui():
    """Run the Streamlit GUI"""
    print("🚀 Starting Streamlit GUI...")
    print("📱 The web interface will open in your browser.")
    print("🔄 If it doesn't open automatically, go to: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the server")
    
    try:
        # Run streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "GUI.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 GUI stopped by user")
    except Exception as e:
        print(f"❌ Failed to start GUI: {e}")

def run_cli():
    """Run the Command Line Interface"""
    print("💻 Starting Command Line Interface...")
    print("💡 Type /help for available commands")
    print("⏹️  Press Ctrl+C to exit")
    
    try:
        from cli import main as cli_main
        cli_main()
    except KeyboardInterrupt:
        print("\n👋 CLI stopped by user")
    except Exception as e:
        print(f"❌ Failed to start CLI: {e}")

def run_quick_test():
    """Run a quick test of the chatbot"""
    print("🧪 Running quick test...")
    
    try:
        from model_llama4 import Llama4RAGChatbot
        chatbot = Llama4RAGChatbot()
        response = chatbot.generate_response("What is artificial intelligence?")
        print(f"✅ Test successful! Response: {response[:100]}...")
    except Exception as e:
        print(f"❌ Test failed: {e}")

def show_menu():
    """Show the main menu"""
    print("\n📋 Choose an option:")
    print("1. 🖥️  Launch Web GUI (Streamlit)")
    print("2. 💻 Launch Command Line Interface")
    print("3. 🧪 Run Quick Test")
    print("4. 📚 Update Knowledge Base")
    print("5. ⚙️  Check Dependencies")
    print("6. ❓ Help")
    print("0. 🚪 Exit")
    
    while True:
        try:
            choice = input("\n🎯 Enter your choice (0-6): ").strip()
            
            if choice == "1":
                run_streamlit_gui()
                break
            elif choice == "2":
                run_cli()
                break
            elif choice == "3":
                run_quick_test()
                break
            elif choice == "4":
                update_knowledge_base()
                break
            elif choice == "5":
                check_dependencies()
                break
            elif choice == "6":
                show_help()
                break
            elif choice == "0":
                print("👋 Goodbye!")
                sys.exit(0)
            else:
                print("❌ Invalid choice. Please enter a number between 0-6.")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            sys.exit(0)

def update_knowledge_base():
    """Update the knowledge base"""
    print("📚 Knowledge Base Update")
    print("=" * 50)
    
    knowledge_file = "knowledge.txt"
    
    if not os.path.exists(knowledge_file):
        print(f"❌ Knowledge file '{knowledge_file}' not found!")
        return
    
    print(f"📖 Current knowledge base: {knowledge_file}")
    print("Enter new content to add (type 'END' on a new line to finish):")
    print("=" * 50)
    
    lines = []
    try:
        while True:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
    except KeyboardInterrupt:
        print("\n❌ Update cancelled")
        return
    
    if lines:
        new_content = '\n'.join(lines)
        try:
            with open(knowledge_file, 'a', encoding='utf-8') as f:
                f.write(f"\n\n{new_content}")
            print("✅ Knowledge base updated successfully!")
            print("🔄 Restart the chatbot to load the new content.")
        except Exception as e:
            print(f"❌ Failed to update knowledge base: {e}")
    else:
        print("⚠️ No content provided")

def show_help():
    """Show help information"""
    help_text = """
🤖 RAG Chatbot Help

📋 Available Options:
1. Web GUI (Streamlit) - Modern web interface with audio support
2. Command Line Interface - Text-based interface for terminal users
3. Quick Test - Test the chatbot with sample questions
4. Update Knowledge Base - Add new information to the knowledge base
5. Check Dependencies - Verify all required packages are installed
6. Help - Show this help message
0. Exit - Close the application

🎤 Audio Features:
• Speech-to-Text: Speak your questions
• Text-to-Speech: Hear the chatbot's responses
• Adjustable speech rate and volume
• Continuous listening mode

📚 Knowledge Base:
• Custom text file (knowledge.txt)
• Automatic chunking and embedding
• Real-time updates
• RAG-based responses

⚙️ Technical Details:
• Model: Llama-4-Maverick-17B-128E-Instruct
• Embeddings: Sentence Transformers
• Vector Database: FAISS
• Audio: Speech Recognition + pyttsx3

🔧 Troubleshooting:
• Ensure all dependencies are installed
• Check microphone permissions for audio
• Verify HuggingFace token is valid
• Ensure sufficient RAM for model loading

📞 Support:
• Check the README.md for detailed setup instructions
• Review error messages for specific issues
• Test with simple questions first
    """
    print(help_text)

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='RAG Chatbot Launcher')
    parser.add_argument('--gui', action='store_true', help='Launch GUI directly')
    parser.add_argument('--cli', action='store_true', help='Launch CLI directly')
    parser.add_argument('--test', action='store_true', help='Run quick test')
    parser.add_argument('--check-deps', action='store_true', help='Check dependencies')
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # Check dependencies first
    if not check_dependencies():
        print("\n❌ Please install missing dependencies before continuing.")
        return
    
    # Handle direct launch options
    if args.gui:
        run_streamlit_gui()
    elif args.cli:
        run_cli()
    elif args.test:
        run_quick_test()
    elif args.check_deps:
        check_dependencies()
    else:
        # Show interactive menu
        show_menu()

if __name__ == "__main__":
    main() 
