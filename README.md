
Consider GPU acceleration
For Audio Processing
Use noise-canceling microphone
Adjust speech rate settings
Optimize timeout settings
🧪 Testing
Quick Test
python main.py --test
Comprehensive Testing
Navigate to the chatbot-testing folder for advanced diagnostic tools:

simple_test.py - Basic functionality test
comprehensive_test.py - Full system test
test_online_api.py - API connectivity test
Various other diagnostic scripts
cd chatbot-testing
python simple_test.py  # Quick health check
python comprehensive_test.py  # Full system test
🔒 Security & Privacy
Local Processing: All data processed locally
No External Storage: No data sent to external servers
Custom Knowledge: Your knowledge base stays private
Audio Privacy: Voice processing done locally
📊 Performance Metrics
Model Loading: ~2-5 minutes (first time)
Response Generation: 2-10 seconds per query
Audio Processing: Real-time
Knowledge Base Updates: Instant
Memory Usage: 8-16GB RAM
🤝 Contributing
Fork the repository
Create a feature branch
Make your changes
Test thoroughly
Submit a pull request
📄 License
This project uses the Llama 4 Community License. See the HuggingFace model page for details.

🙏 Acknowledgments
Meta AI for Llama-4-Maverick model
HuggingFace for model hosting and transformers library
Streamlit for the web interface framework
Sentence Transformers for embedding capabilities
FAISS for efficient similarity search
📞 Support
For issues and questions:

Check the troubleshooting section
Review error messages carefully
Test with simple questions first
Check system requirements
Verify all dependencies are installed
Happy Chatting! 🤖✨

IMPORTANT:

For security, no Hugging Face token is included in this repository.
You must run python update_token.py to set your own token before using the chatbot or running any tests.
Do NOT hardcode your token in any file. The update_token.py script will safely insert it where needed.
