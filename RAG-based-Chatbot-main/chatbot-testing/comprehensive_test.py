#!/usr/bin/env python3
"""
Comprehensive Test Script for RAG Chatbot Project
Tests all components and reports any issues found.
"""

import os
import sys
import importlib
import traceback
from typing import List, Dict, Any

def test_imports():
    """Test all critical imports"""
    print("🔍 Testing imports...")
    
    imports_to_test = [
        ('streamlit', 'st'),
        ('transformers', 'transformers'),
        ('torch', 'torch'),
        ('sentence_transformers', 'sentence_transformers'),
        ('faiss', 'faiss'),
        ('numpy', 'np'),
        ('pandas', 'pd'),
        ('huggingface_hub', 'huggingface_hub'),
        ('requests', 'requests'),
        ('datetime', 'datetime'),
        ('threading', 'threading'),
        ('time', 'time'),
        ('os', 'os'),
        ('sys', 'sys'),
        ('typing', 'typing'),
        ('traceback', 'traceback')
    ]
    
    failed_imports = []
    
    for module_name, import_name in imports_to_test:
        try:
            importlib.import_module(module_name)
            print(f"✅ {module_name}")
        except ImportError as e:
            print(f"❌ {module_name}: {e}")
            failed_imports.append(module_name)
    
    return failed_imports

def test_audio_imports():
    """Test audio-related imports"""
    print("\n🔊 Testing audio imports...")
    
    audio_imports = [
        ('speechrecognition', 'speech_recognition'),
        ('pyttsx3', 'pyttsx3'),
        ('sounddevice', 'sounddevice'),
        ('pyaudio', 'pyaudio')
    ]
    
    failed_audio_imports = []
    
    for pkg_name, import_name in audio_imports:
        try:
            importlib.import_module(import_name)
            print(f"✅ {pkg_name}")
        except ImportError as e:
            print(f"❌ {pkg_name}: {e}")
            failed_audio_imports.append(pkg_name)
    
    return failed_audio_imports

def test_project_files():
    """Test project file syntax and imports"""
    print("\n📁 Testing project files...")
    
    project_files = [
        'model_llama4.py',
        'GUI.py',
        'cli.py',
        'main.py',
        'test_online_api.py',
        'update_token.py',
        'audio_processor.py',
        'audio_processor_simple.py'
    ]
    
    failed_files = []
    
    for file_name in project_files:
        if os.path.exists(file_name):
            try:
                # Try to import the module
                module_name = file_name.replace('.py', '')
                importlib.import_module(module_name)
                print(f"✅ {file_name}")
            except Exception as e:
                print(f"❌ {file_name}: {e}")
                failed_files.append(file_name)
        else:
            print(f"⚠️ {file_name}: File not found")
            failed_files.append(file_name)
    
    return failed_files

def test_knowledge_base():
    """Test knowledge base file"""
    print("\n📚 Testing knowledge base...")
    
    knowledge_file = "knowledge.txt"
    
    if not os.path.exists(knowledge_file):
        print(f"❌ Knowledge file '{knowledge_file}' not found!")
        return False
    
    try:
        with open(knowledge_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if len(content.strip()) == 0:
            print("⚠️ Knowledge file is empty")
            return False
        
        # Count paragraphs
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        print(f"✅ Knowledge base loaded: {len(paragraphs)} paragraphs")
        return True
        
    except Exception as e:
        print(f"❌ Error reading knowledge base: {e}")
        return False

def test_model_initialization():
    """Test model initialization"""
    print("\n🤖 Testing model initialization...")
    
    try:
        from model_llama4 import Llama4RAGChatbot
        
        # Test initialization
        chatbot = Llama4RAGChatbot()
        print("✅ Model initialization successful")
        
        # Test a simple query
        response = chatbot.generate_response("What is artificial intelligence?")
        if response:
            print("✅ Query processing successful")
            return True
        else:
            print("⚠️ Query processing returned empty response")
            return False
            
    except Exception as e:
        print(f"❌ Model initialization failed: {e}")
        traceback.print_exc()
        return False

def test_gui_components():
    """Test GUI components"""
    print("\n🖥️ Testing GUI components...")
    
    try:
        import streamlit as st
        print("✅ Streamlit import successful")
        
        # Test GUI class import
        from GUI import ChatbotGUI
        print("✅ GUI class import successful")
        
        return True
        
    except Exception as e:
        print(f"❌ GUI component test failed: {e}")
        return False

def test_cli_components():
    """Test CLI components"""
    print("\n💻 Testing CLI components...")
    
    try:
        from cli import main as cli_main
        print("✅ CLI import successful")
        return True
        
    except Exception as e:
        print(f"❌ CLI component test failed: {e}")
        return False

def test_audio_components():
    """Test audio components"""
    print("\n🎤 Testing audio components...")
    
    try:
        from audio_processor import AudioProcessor
        print("✅ Audio processor import successful")
        
        # Test simple audio processor
        from audio_processor_simple import SimpleAudioProcessor
        print("✅ Simple audio processor import successful")
        
        return True
        
    except Exception as e:
        print(f"❌ Audio component test failed: {e}")
        return False

def generate_report(failed_imports, failed_audio_imports, failed_files, 
                   knowledge_ok, model_ok, gui_ok, cli_ok, audio_ok):
    """Generate a comprehensive test report"""
    print("\n" + "="*60)
    print("📊 COMPREHENSIVE TEST REPORT")
    print("="*60)
    
    # Summary
    total_tests = 8
    passed_tests = sum([
        len(failed_imports) == 0,
        len(failed_audio_imports) == 0,
        len(failed_files) == 0,
        knowledge_ok,
        model_ok,
        gui_ok,
        cli_ok,
        audio_ok
    ])
    
    print(f"✅ Tests Passed: {passed_tests}/{total_tests}")
    print(f"❌ Tests Failed: {total_tests - passed_tests}/{total_tests}")
    
    # Detailed results
    if failed_imports:
        print(f"\n❌ Failed Core Imports ({len(failed_imports)}):")
        for imp in failed_imports:
            print(f"   - {imp}")
    
    if failed_audio_imports:
        print(f"\n❌ Failed Audio Imports ({len(failed_audio_imports)}):")
        for imp in failed_audio_imports:
            print(f"   - {imp}")
    
    if failed_files:
        print(f"\n❌ Failed Project Files ({len(failed_files)}):")
        for file in failed_files:
            print(f"   - {file}")
    
    if not knowledge_ok:
        print("\n❌ Knowledge Base: Failed")
    
    if not model_ok:
        print("\n❌ Model Initialization: Failed")
    
    if not gui_ok:
        print("\n❌ GUI Components: Failed")
    
    if not cli_ok:
        print("\n❌ CLI Components: Failed")
    
    if not audio_ok:
        print("\n❌ Audio Components: Failed")
    
    # Recommendations
    print("\n💡 Recommendations:")
    
    if failed_imports or failed_audio_imports:
        print("   - Install missing dependencies: pip install -r requirements.txt")
    
    if failed_files:
        print("   - Check file syntax and fix import errors")
    
    if not knowledge_ok:
        print("   - Create or fix knowledge.txt file")
    
    if not model_ok:
        print("   - Check Hugging Face token and model access")
    
    if not gui_ok:
        print("   - Install Streamlit: pip install streamlit")
    
    if not audio_ok:
        print("   - Install audio dependencies: pip install pyaudio sounddevice")
    
    if passed_tests == total_tests:
        print("\n🎉 All tests passed! Your project is ready to use.")
    else:
        print(f"\n⚠️ {total_tests - passed_tests} issues found. Please fix them before using the project.")

def main():
    """Run comprehensive tests"""
    print("🚀 Starting Comprehensive Project Test")
    print("="*60)
    
    # Run all tests
    failed_imports = test_imports()
    failed_audio_imports = test_audio_imports()
    failed_files = test_project_files()
    knowledge_ok = test_knowledge_base()
    model_ok = test_model_initialization()
    gui_ok = test_gui_components()
    cli_ok = test_cli_components()
    audio_ok = test_audio_components()
    
    # Generate report
    generate_report(failed_imports, failed_audio_imports, failed_files,
                   knowledge_ok, model_ok, gui_ok, cli_ok, audio_ok)

if __name__ == "__main__":
    main() 