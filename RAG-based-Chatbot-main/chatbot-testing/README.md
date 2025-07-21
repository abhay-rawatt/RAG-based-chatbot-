# 🧪 Chatbot Testing Suite

This folder contains comprehensive testing and diagnostic tools for the RAG Chatbot project. Use these scripts to identify and resolve issues with the chatbot.

**Location**: This testing suite is now included within the main chatbot package for easy access and distribution.

## 📋 Test Scripts Overview

### 🔍 Core Testing Scripts

#### `simple_test.py`
- **Purpose**: Basic functionality test without TensorFlow dependencies
- **Tests**: Imports, file structure, knowledge base, model initialization
- **Usage**: `python simple_test.py`
- **Best for**: Quick system health check

#### `comprehensive_test.py`
- **Purpose**: Full system test with all dependencies
- **Tests**: All imports, model loading, API connectivity, GUI/CLI components
- **Usage**: `python comprehensive_test.py`
- **Best for**: Complete system validation

#### `test_online_api.py`
- **Purpose**: Test Hugging Face API connectivity and RAG pipeline
- **Tests**: Token validation, model availability, knowledge base retrieval
- **Usage**: `python test_online_api.py`
- **Best for**: API and RAG functionality verification

### 🔧 Diagnostic Scripts

#### `check_hf_account_status.py`
- **Purpose**: Verify Hugging Face account and token status
- **Tests**: Token validity, account permissions, API access
- **Usage**: `python check_hf_account_status.py`
- **Best for**: Token and account troubleshooting

#### `check_inference_api_models.py`
- **Purpose**: Test which models are available via Inference API
- **Tests**: Multiple model availability, API endpoints
- **Usage**: `python check_inference_api_models.py`
- **Best for**: Model availability diagnosis

#### `test_inference_api.py`
- **Purpose**: Basic Inference API connectivity test
- **Tests**: Simple API calls, response handling
- **Usage**: `python test_inference_api.py`
- **Best for**: API connectivity verification

#### `check_llama_inference_api.py`
- **Purpose**: Specific Llama model API testing
- **Tests**: Llama model availability, API responses
- **Usage**: `python check_llama_inference_api.py`
- **Best for**: Llama model troubleshooting

#### `check_llama_access.py`
- **Purpose**: Test Llama model access permissions
- **Tests**: Model access, token permissions, gated model access
- **Usage**: `python check_llama_access.py`
- **Best for**: Model access troubleshooting

### 🎯 Specific Component Tests

#### `test_llama4.py`
- **Purpose**: Test Llama-4-Maverick model specifically
- **Tests**: Model loading, inference, response generation
- **Usage**: `python test_llama4.py`
- **Best for**: Llama-4 model validation

#### `test_gui.py`
- **Purpose**: Test GUI components and Streamlit integration
- **Tests**: GUI imports, Streamlit functionality
- **Usage**: `python test_gui.py`
- **Best for**: GUI troubleshooting

#### `test_api.py`
- **Purpose**: Test API-based model functionality
- **Tests**: API model loading, response generation
- **Usage**: `python test_api.py`
- **Best for**: API model validation

#### `quick_test.py`
- **Purpose**: Quick system functionality test
- **Tests**: Basic imports, model initialization
- **Usage**: `python quick_test.py`
- **Best for**: Fast system check

#### `test_model.py`
- **Purpose**: Test local model functionality
- **Tests**: Local model loading, pipeline functionality
- **Usage**: `python test_model.py`
- **Best for**: Local model validation

#### `test_system.py`
- **Purpose**: Comprehensive system diagnostics
- **Tests**: All components, performance metrics
- **Usage**: `python test_system.py`
- **Best for**: Complete system analysis

#### `test.py`
- **Purpose**: Basic functionality test
- **Tests**: Core imports and basic functionality
- **Usage**: `python test.py`
- **Best for**: Simple validation

## 🚀 How to Use

### 1. Quick Health Check
```bash
cd chatbot-testing
python simple_test.py
```
This will give you a quick overview of system health.

### 2. Complete System Test
```bash
cd chatbot-testing
python comprehensive_test.py
```
This will test all components and provide detailed results.

### 3. API Connectivity Test
```bash
cd chatbot-testing
python test_online_api.py
```
This will test your Hugging Face token and API connectivity.

### 4. Specific Issue Diagnosis

#### Token Issues
```bash
cd chatbot-testing
python check_hf_account_status.py
```

#### Model Availability Issues
```bash
cd chatbot-testing
python check_inference_api_models.py
```

#### GUI Issues
```bash
cd chatbot-testing
python test_gui.py
```

#### Audio Issues
```bash
cd chatbot-testing
python test_system.py
```

## 📊 Understanding Test Results

### ✅ Success Indicators
- All imports successful
- Model initialization completed
- Knowledge base loaded
- GUI/CLI components working
- API connectivity established

### ❌ Common Issues and Solutions

#### Import Errors
- **Issue**: `ModuleNotFoundError`
- **Solution**: Install missing dependencies with `pip install -r requirements.txt`

#### Token Issues
- **Issue**: `Token validation failed: 401`
- **Solution**: Update your Hugging Face token using `python update_token.py`

#### API Issues
- **Issue**: `Model is NOT available via Inference API`
- **Solution**: This is normal for free accounts. The system will use fallback responses.

#### Audio Issues
- **Issue**: `No module named 'sounddevice'`
- **Solution**: Install audio dependencies with `pip install sounddevice pyaudio`

## 🔧 Troubleshooting Workflow

### Step 1: Basic Check
```bash
cd chatbot-testing
python simple_test.py
```

### Step 2: If Issues Found
```bash
cd chatbot-testing
python comprehensive_test.py
```

### Step 3: Specific Diagnosis
Based on the error, run the appropriate diagnostic script:
- Token issues → `check_hf_account_status.py`
- API issues → `test_online_api.py`
- GUI issues → `test_gui.py`
- Model issues → `test_llama4.py`

### Step 4: Fix and Retest
After making fixes, run the tests again to verify resolution.

## 📈 Performance Testing

### Memory Usage
- Monitor RAM usage during model loading
- Check for memory leaks during extended use

### Response Time
- Test response generation speed
- Monitor API call latency

### Audio Performance
- Test speech-to-text accuracy
- Verify text-to-speech quality

## 🛠️ Custom Testing

You can create custom test scripts by following the pattern of existing tests:

```python
def test_custom_functionality():
    """Test specific functionality"""
    try:
        # Your test code here
        print("✅ Test passed")
    except Exception as e:
        print(f"❌ Test failed: {e}")
```

## 📝 Reporting Issues

When reporting issues, include:
1. The test script that failed
2. The complete error message
3. Your system specifications
4. The steps to reproduce the issue

## 🎯 Best Practices

1. **Run tests in order**: Start with `simple_test.py`, then move to more comprehensive tests
2. **Check logs**: Look for detailed error messages in test output
3. **Isolate issues**: Use specific diagnostic scripts for targeted troubleshooting
4. **Document changes**: Keep track of any fixes you make
5. **Retest**: Always run tests again after making changes

---

**Happy Testing! 🧪✨** 