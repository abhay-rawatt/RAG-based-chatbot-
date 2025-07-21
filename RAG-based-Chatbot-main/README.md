# 🤖 RAG Chatbot - Llama-4-Maverick

A powerful **Retrieval-Augmented Generation (RAG)** chatbot powered by Meta's **Llama-4-Maverick-17B-128E-Instruct** model with speech-to-text and text-to-speech capabilities.

## 🌟 Features

- **🤖 Advanced RAG System**: Retrieval-Augmented Generation for accurate, context-aware responses
- **🎤 Audio Support**: Speech-to-Text and Text-to-Speech capabilities
- **🖥️ Modern Web GUI**: Beautiful Streamlit interface with real-time chat
- **💻 Command Line Interface**: Lightweight CLI for terminal users
- **📚 Custom Knowledge Base**: Easy-to-update text-based knowledge system
- **⚡ Optimized Performance**: Efficient chunking and embedding for large knowledge bases
- **🎯 Context-Aware**: Responses based strictly on your knowledge base
- **🔄 Real-time Updates**: Dynamic knowledge base updates without restart
- **🌐 Online API Integration**: Uses Hugging Face Inference API with robust fallback

## 📋 Requirements

### System Requirements
- **Python**: 3.8 or higher
- **RAM**: 8GB (16GB recommended)
- **Storage**: 10GB free space
- **OS**: Windows 10/11, macOS, or Linux

### Recommended Requirements
- **RAM**: 32GB for optimal performance
- **GPU**: CUDA-compatible GPU (optional)
- **Storage**: SSD for faster I/O

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Hugging Face Token

**IMPORTANT**: You need a valid Hugging Face token with appropriate permissions.

1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Create a new token with these permissions:
   - ✅ Read
   - ✅ Write (if you want to upload models)
   - ✅ Inference API (if available for your account)

3. Update the token in the code:
   - Open `model_llama4.py`
   - Find line 12: `hf_token: str = "YOUR_TOKEN_HERE"`
   - Replace `YOUR_TOKEN_HERE` with your actual token

**Or use the token updater:**
```bash
python update_token.py
```

### 3. Run the Application

```bash
# Launch the main menu
python main.py

# Or launch directly:
python main.py --gui    # Launch web GUI
python main.py --cli    # Launch command line interface
python main.py --test   # Run quick test
```

## 🎯 Usage Guide

### Web GUI (Recommended)

1. **Launch the GUI:**
   ```bash
   python main.py --gui
   ```

2. **Features:**
   - 💬 Text chat with real-time responses
   - 🎤 Audio mode for voice input/output
   - 📚 Knowledge base management
   - ⚙️ Audio settings (speech rate, volume)
   - 🗑️ Chat history management

3. **Audio Mode:**
   - Toggle audio mode in the sidebar
   - Click "Start Listening" for continuous voice input
   - Adjust speech rate and volume settings
   - Responses are automatically spoken in audio mode

### Command Line Interface

1. **Launch the CLI:**
   ```bash
   python main.py --cli
   ```

2. **Available Commands:**
   - `/help` - Show help information
   - `/audio` - Toggle audio mode
   - `/text` - Switch to text-only mode
   - `/clear` - Clear chat history
   - `/update` - Update knowledge base
   - `/status` - Show current status
   - `/quit` - Exit the chatbot

### Knowledge Base Management

1. **Update Knowledge Base:**
   - Use the GUI sidebar option
   - Or use CLI: `/update`
   - Or edit `knowledge.txt` directly

2. **Knowledge Base Format:**
   - Plain text file (`knowledge.txt`)
   - Automatic chunking and embedding
   - Supports large documents
   - Real-time updates

## 🔧 Configuration Options

You can customize the chatbot by modifying these parameters in `model_llama4.py`:

```python
chatbot = Llama4RAGChatbot(
    model_name="meta-llama/Llama-4-Maverick-17B-128E-Instruct",  # Model to use
    hf_token="your_token_here",                                    # Your HF token
    knowledge_file="knowledge.txt",                                # Knowledge base file
    chunk_size=512,                                               # Text chunk size
    chunk_overlap=50,                                             # Overlap between chunks
    top_k=3                                                       # Number of relevant chunks
)
```

## 📁 Project Structure

```
RAG bases chatbot/
├── main.py                    # Main launcher script
├── model_llama4.py           # Core RAG chatbot implementation
├── GUI.py                     # Streamlit web interface
├── cli.py                     # Command line interface
├── audio_processor.py         # Full audio support
├── audio_processor_simple.py  # Basic audio support
├── knowledge.txt              # Knowledge base file
├── requirements.txt           # Python dependencies
├── update_token.py           # Token management utility
├── README.md                 # This file
├── INSTALLATION_GUIDE.md     # Detailed installation guide
└── chatbot-testing/          # Testing and diagnostic tools
    ├── README.md             # Testing guide
    ├── simple_test.py        # Basic functionality test
    ├── comprehensive_test.py # Full system test
    ├── test_online_api.py    # API connectivity test
    ├── check_hf_account_status.py # Token validation
    ├── check_inference_api_models.py # Model availability
    ├── test_inference_api.py # Basic API test
    └── check_llama_inference_api.py # Llama model test
```

## 🔧 Troubleshooting

### Common Issues

#### 1. Token Issues
**Error**: `Token validation failed: 401`

**Solution**:
1. Check if your token is valid at https://huggingface.co/settings/tokens
2. Ensure the token has the correct permissions
3. Update the token using `python update_token.py`
4. Run diagnostic test: `cd chatbot-testing && python check_hf_account_status.py`

#### 2. Model Availability Issues
**Error**: `Model is NOT available via Inference API`

**Solution**:
- Free Hugging Face accounts have limited access to Inference API
- The system will use fallback responses from your knowledge base
- Consider upgrading to a paid plan for API access
- Run diagnostic test: `cd chatbot-testing && python test_online_api.py`

#### 3. Audio Issues
**Error**: `ModuleNotFoundError: No module named 'sounddevice'`

**Solution**:
```bash
pip install sounddevice pyaudio
```
Run diagnostic test: `cd chatbot-testing && python test_system.py`

#### 4. Dependencies Missing
**Error**: `ModuleNotFoundError`

**Solution**:
```bash
pip install -r requirements.txt
```
Run diagnostic test: `cd chatbot-testing && python comprehensive_test.py`

### Performance Optimization

#### For Large Knowledge Bases
- Increase chunk size in `model_llama4.py`
- Use SSD storage
- Consider GPU acceleration

#### For Audio Processing
- Use noise-canceling microphone
- Adjust speech rate settings
- Optimize timeout settings

## 🧪 Testing

### Quick Test
```bash
python main.py --test
```

### Comprehensive Testing
Navigate to the `chatbot-testing` folder for advanced diagnostic tools:
- `simple_test.py` - Basic functionality test
- `comprehensive_test.py` - Full system test
- `test_online_api.py` - API connectivity test
- Various other diagnostic scripts

```bash
cd chatbot-testing
python simple_test.py  # Quick health check
python comprehensive_test.py  # Full system test
```

## 🔒 Security & Privacy

- **Local Processing**: All data processed locally
- **No External Storage**: No data sent to external servers
- **Custom Knowledge**: Your knowledge base stays private
- **Audio Privacy**: Voice processing done locally

## 📊 Performance Metrics

- **Model Loading**: ~2-5 minutes (first time)
- **Response Generation**: 2-10 seconds per query
- **Audio Processing**: Real-time
- **Knowledge Base Updates**: Instant
- **Memory Usage**: 8-16GB RAM

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project uses the Llama 4 Community License. See the [HuggingFace model page](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) for details.

## 🙏 Acknowledgments

- **Meta AI** for Llama-4-Maverick model
- **HuggingFace** for model hosting and transformers library
- **Streamlit** for the web interface framework
- **Sentence Transformers** for embedding capabilities
- **FAISS** for efficient similarity search

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review error messages carefully
3. Test with simple questions first
4. Check system requirements
5. Verify all dependencies are installed

---

**Happy Chatting! 🤖✨**

> **IMPORTANT:**
> - For security, no Hugging Face token is included in this repository.
> - You must run `python update_token.py` to set your own token before using the chatbot or running any tests.
> - Do NOT hardcode your token in any file. The update_token.py script will safely insert it where needed.
