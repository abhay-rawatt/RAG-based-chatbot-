# 🚀 RAG Chatbot Installation Guide

## Quick Start

### Option 1: Automated Setup (Recommended)
```bash
cd RAG
python setup.py
```

### Option 2: Manual Setup
```bash
cd RAG
pip install -r requirements_alternative.txt
python quick_test.py
```

## 📋 System Requirements

### Minimum Requirements
- **Python**: 3.8 or higher
- **RAM**: 8GB (16GB recommended)
- **Storage**: 10GB free space
- **OS**: Windows 10/11, macOS, or Linux

### Recommended Requirements
- **RAM**: 32GB for optimal performance
- **GPU**: CUDA-compatible GPU (optional)
- **Storage**: SSD for faster I/O

## 🔧 Installation Steps

### Step 1: Clone/Download the Project
```bash
# If you have the files already, navigate to the RAG folder
cd RAG
```

### Step 2: Install Dependencies

#### Option A: Basic Installation (Recommended for first-time users)
```bash
pip install -r requirements_alternative.txt
```

#### Option B: Full Installation (Includes speech-to-text)
```bash
pip install -r requirements.txt
```

**Note**: Option B requires Microsoft Visual C++ Build Tools on Windows for PyAudio.

### Step 3: Verify Installation
```bash
python quick_test.py
```

### Step 4: Launch the Chatbot
```bash
# Web GUI (Recommended)
python main.py --gui

# Command Line Interface
python main.py --cli

# Interactive Menu
python main.py
```

## 🎯 Features

### ✅ Working Features
- **RAG System**: Retrieval-Augmented Generation
- **Text-to-Speech**: Audio responses
- **Web GUI**: Modern Streamlit interface
- **CLI**: Command-line interface
- **Knowledge Base**: Custom text file support
- **Real-time Updates**: Dynamic knowledge base

### ⚠️ Optional Features
- **Speech-to-Text**: Requires PyAudio installation
- **Continuous Listening**: Requires PyAudio

## 🔧 Troubleshooting

### Common Issues

#### 1. PyAudio Installation Fails
**Error**: `Microsoft Visual C++ 14.0 or greater is required`

**Solution**:
```bash
# Install Visual C++ Build Tools
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

# Then install PyAudio
pip install pyaudio
```

#### 2. Model Loading Takes Too Long
**Solution**:
- Ensure stable internet connection
- First download may take 5-10 minutes
- Subsequent runs will be faster

#### 3. Memory Issues
**Error**: `CUDA out of memory` or slow performance

**Solution**:
- Close other applications
- Use CPU-only mode (already configured)
- Reduce model quantization in `model.py`

#### 4. Dependencies Missing
**Error**: `ModuleNotFoundError`

**Solution**:
```bash
pip install -r requirements_alternative.txt
```

### Performance Optimization

#### For Large Knowledge Bases
- Increase chunk size in `model.py`
- Use SSD storage
- Consider GPU acceleration

#### For Audio Processing
- Use noise-canceling microphone
- Adjust speech rate settings
- Optimize timeout settings

## 📁 Project Structure

```
RAG/
├── main.py                    # Main launcher
├── model.py                   # Core RAG model
├── GUI.py                     # Streamlit web interface
├── cli.py                     # Command line interface
├── audio_processor.py         # Full audio support
├── audio_processor_simple.py  # Basic audio support
├── knowledge.txt              # Knowledge base
├── requirements.txt           # Full dependencies
├── requirements_alternative.txt # Basic dependencies
├── setup.py                   # Automated setup
├── quick_test.py             # Quick system test
├── test_system.py            # Comprehensive test
└── README.md                 # Detailed documentation
```

## 🎮 Usage Examples

### Web GUI
1. Launch: `python main.py --gui`
2. Open browser: http://localhost:8501
3. Type questions in the chat interface
4. Toggle audio mode for voice responses

### Command Line
1. Launch: `python main.py --cli`
2. Type questions directly
3. Use `/help` for commands
4. Use `/audio` for voice mode

### Knowledge Base Management
1. Edit `knowledge.txt` directly
2. Use GUI sidebar option
3. Use CLI `/update` command

## 🔒 Security & Privacy

- **Local Processing**: All data processed locally
- **No External Storage**: No data sent to servers
- **Custom Knowledge**: Your knowledge base stays private
- **Audio Privacy**: Voice processing done locally

## 📞 Support

### Getting Help
1. Check the troubleshooting section
2. Review error messages carefully
3. Test with simple questions first
4. Check system requirements
5. Verify all dependencies are installed

### Common Commands
```bash
# Test system
python quick_test.py

# Launch GUI
python main.py --gui

# Launch CLI
python main.py --cli

# Run setup
python setup.py

# Check dependencies
python main.py --check-deps
```

## 🎉 Success Indicators

You'll know everything is working when:
- ✅ `python quick_test.py` passes all tests
- ✅ Web GUI opens in browser
- ✅ Text-to-speech works
- ✅ Chatbot responds to questions
- ✅ Knowledge base loads correctly

## 🚀 Next Steps

After successful installation:
1. **Customize Knowledge Base**: Edit `knowledge.txt`
2. **Adjust Settings**: Modify `model.py` parameters
3. **Add Audio**: Install PyAudio for speech-to-text
4. **Scale Up**: Add more knowledge content
5. **Integrate**: Use in your own applications

---

**Happy Chatting! 🤖✨**