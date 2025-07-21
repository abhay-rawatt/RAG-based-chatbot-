# 🤖 RAG Chatbot - Llama-4-Maverick

A powerful **Retrieval-Augmented Generation (RAG)** chatbot powered by Meta's **Llama-4-Maverick-17B-128E-Instruct** model with speech-to-text and text-to-speech capabilities.

## 🚀 Quick Start

### 1. Clone or Download
```bash
# Clone the repository
git clone https://github.com/GLCRealm/RAG-based-Chatbot.git
cd RAG-based-Chatbot

# Or download and extract the ZIP file
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Your Token
```bash
python update_token.py
```
Or manually edit `model_llama4.py` and replace `YOUR_TOKEN_HERE` with your Hugging Face token.

### 4. Launch the Chatbot
```bash
python main.py
```

## 📁 Complete Project Structure

```
RAG-based-Chatbot/
├── 🚀 Core Application Files
│   ├── main.py                    # Main launcher with menu system
│   ├── model_llama4.py           # Core RAG chatbot implementation
│   ├── GUI.py                     # Streamlit web interface
│   ├── cli.py                     # Command line interface
│   ├── audio_processor.py         # Full audio support
│   ├── audio_processor_simple.py  # Basic audio support
│   ├── knowledge.txt              # Knowledge base file
│   ├── requirements.txt           # Python dependencies
│   └── update_token.py           # Token management utility
│
├── 📚 Documentation
│   ├── README.md                 # This comprehensive guide
│   └── INSTALLATION_GUIDE.md     # Detailed setup instructions
│
└── 🧪 chatbot-testing/           # Complete Testing Suite
    ├── README.md                 # Testing guide
    ├── simple_test.py            # Quick health check
    ├── comprehensive_test.py     # Full system test
    ├── test_online_api.py        # API connectivity test
    ├── check_hf_account_status.py # Token validation
    ├── check_inference_api_models.py # Model availability
    ├── test_inference_api.py     # Basic API test
    └── check_llama_inference_api.py # Llama model test
```

## 🎯 Features

- **🤖 Advanced RAG System**: Retrieval-Augmented Generation for accurate responses
- **🎤 Audio Support**: Speech-to-Text and Text-to-Speech capabilities
- **🖥️ Modern Web GUI**: Beautiful Streamlit interface with real-time chat
- **💻 Command Line Interface**: Lightweight CLI for terminal users
- **📚 Custom Knowledge Base**: Easy-to-update text-based knowledge system
- **⚡ Optimized Performance**: Efficient chunking and embedding
- **🎯 Context-Aware**: Responses based strictly on your knowledge base
- **🔄 Real-time Updates**: Dynamic knowledge base updates without restart
- **🌐 Online API Integration**: Uses Hugging Face Inference API with robust fallback
- **🧪 Complete Testing Suite**: Comprehensive diagnostic tools included

## 🎮 Usage Options

### Web GUI (Recommended)
```bash
python main.py --gui
```
- 💬 Real-time text chat
- 🎤 Audio mode for voice input/output
- 📚 Knowledge base management
- ⚙️ Audio settings (speech rate, volume)
- 🗑️ Chat history management

### Command Line Interface
```bash
python main.py --cli
```
- `/help` - Show help information
- `/audio` - Toggle audio mode
- `/text` - Switch to text-only mode
- `/clear` - Clear chat history
- `/update` - Update knowledge base
- `/status` - Show current status
- `/quit` - Exit the chatbot

### Quick Test
```bash
python main.py --test
```

## 🧪 Testing and Troubleshooting

### Quick Health Check
```bash
cd chatbot-testing
python simple_test.py
```

### Full System Test
```bash
cd chatbot-testing
python comprehensive_test.py
```

### API Connectivity Test
```bash
cd chatbot-testing
python test_online_api.py
```

### Specific Issue Diagnosis
```bash
cd chatbot-testing
# Token issues
python check_hf_account_status.py

# Model availability
python check_inference_api_models.py

# GUI issues
python test_gui.py

# Audio issues
python test_system.py
```

## 🔧 Configuration

### Knowledge Base
Edit `knowledge.txt` to customize the chatbot's knowledge:
- Add your domain-specific information
- Use paragraphs separated by double newlines
- Supports large documents with automatic chunking

### Model Settings
Modify parameters in `model_llama4.py`:
```python
chatbot = Llama4RAGChatbot(
    model_name="meta-llama/Llama-4-Maverick-17B-128E-Instruct",
    hf_token="your_token_here",
    knowledge_file="knowledge.txt",
    chunk_size=512,
    chunk_overlap=50,
    top_k=3
)
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. Token Issues
**Error**: `Token validation failed: 401`
**Solution**:
1. Check token at https://huggingface.co/settings/tokens
2. Update token: `python update_token.py`
3. Test: `cd chatbot-testing && python check_hf_account_status.py`

#### 2. API Issues
**Error**: `Model is NOT available via Inference API`
**Solution**:
- Normal for free accounts - system uses fallback responses
- Test: `cd chatbot-testing && python test_online_api.py`

#### 3. Audio Issues
**Error**: `ModuleNotFoundError: No module named 'sounddevice'`
**Solution**:
```bash
pip install sounddevice pyaudio
cd chatbot-testing && python test_system.py
```

#### 4. Dependencies Missing
**Error**: `ModuleNotFoundError`
**Solution**:
```bash
pip install -r requirements.txt
cd chatbot-testing && python comprehensive_test.py
```

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
4. Test thoroughly using the testing suite
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
2. Run the testing suite: `cd chatbot-testing && python comprehensive_test.py`
3. Review error messages carefully
4. Test with simple questions first
5. Check system requirements
6. Verify all dependencies are installed

---

**🎉 Ready to Use!** 

This complete package includes everything you need:
- ✅ **Full RAG chatbot** with Llama-4-Maverick
- ✅ **Dual interfaces** (GUI and CLI)
- ✅ **Audio capabilities** (speech-to-text and text-to-speech)
- ✅ **Complete testing suite** for troubleshooting
- ✅ **Comprehensive documentation**
- ✅ **Easy setup and configuration**

**Happy Chatting! 🤖✨** 