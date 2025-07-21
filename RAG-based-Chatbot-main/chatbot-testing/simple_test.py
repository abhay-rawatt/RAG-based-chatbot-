#!/usr/bin/env python3
"""
Simple Test Script for RAG Chatbot Project
Tests core functionality without TensorFlow dependencies.
"""

import os
import sys
import importlib

def test_basic_imports():
    """Test basic imports without TensorFlow"""
    print("🔍 Testing basic imports...")
    
    basic_imports = [
        ('os', 'os'),
        ('sys', 'sys'),
        ('datetime', 'datetime'),
        ('threading', 'threading'),
        ('time', 'time'),
        ('typing', 'typing'),
        ('json', 'json'),
        ('re', 're'),
        ('requests', 'requests'),
        ('numpy', 'np'),
        ('pandas', 'pd')
    ]
    
    failed_imports = []
    
    for module_name, import_name in basic_imports:
        try:
            importlib.import_module(module_name)
            print(f"✅ {module_name}")
        except ImportError as e:
            print(f"❌ {module_name}: {e}")
            failed_imports.append(module_name)
    
    return failed_imports

def test_ml_imports():
    """Test ML-related imports"""
    print("\n🤖 Testing ML imports...")
    
    ml_imports = [
        ('sentence_transformers', 'sentence_transformers'),
        ('faiss', 'faiss'),
        ('huggingface_hub', 'huggingface_hub')
    ]
    
    failed_imports = []
    
    for module_name, import_name in ml_imports:
        try:
            importlib.import_module(module_name)
            print(f"✅ {module_name}")
        except ImportError as e:
            print(f"❌ {module_name}: {e}")
            failed_imports.append(module_name)
    
    return failed_imports

def test_ui_imports():
    """Test UI-related imports"""
    print("\n🖥️ Testing UI imports...")
    
    ui_imports = [
        ('streamlit', 'streamlit')
    ]
    
    failed_imports = []
    
    for module_name, import_name in ui_imports:
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
        ('pyttsx3', 'pyttsx3'),
        ('sounddevice', 'sounddevice')
    ]
    
    failed_imports = []
    
    for module_name, import_name in audio_imports:
        try:
            importlib.import_module(module_name)
            print(f"✅ {module_name}")
        except ImportError as e:
            print(f"❌ {module_name}: {e}")
            failed_imports.append(module_name)
    
    return failed_imports

def test_project_files():
    """Test project file existence and basic syntax"""
    print("\n📁 Testing project files...")
    
    project_files = [
        'model_llama4.py',
        'GUI.py',
        'cli.py',
        'main.py',
        'test_online_api.py',
        'update_token.py',
        'audio_processor.py',
        'audio_processor_simple.py',
        'knowledge.txt',
        'requirements.txt',
        'README.md'
    ]
    
    missing_files = []
    
    for file_name in project_files:
        if os.path.exists(file_name):
            print(f"✅ {file_name}")
        else:
            print(f"❌ {file_name}: File not found")
            missing_files.append(file_name)
    
    return missing_files

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

def test_simple_model():
    """Test model without full initialization"""
    print("\n🤖 Testing model structure...")
    
    try:
        # Just test if we can import the class
        from model_llama4 import Llama4RAGChatbot
        print("✅ Model class import successful")
        return True
        
    except Exception as e:
        print(f"❌ Model import failed: {e}")
        return False

def test_gui_structure():
    """Test GUI structure"""
    print("\n🖥️ Testing GUI structure...")
    
    try:
        from GUI import ChatbotGUI
        print("✅ GUI class import successful")
        return True
        
    except Exception as e:
        print(f"❌ GUI import failed: {e}")
        return False

def test_cli_structure():
    """Test CLI structure"""
    print("\n💻 Testing CLI structure...")
    
    try:
        from cli import main as cli_main
        print("✅ CLI import successful")
        return True
        
    except Exception as e:
        print(f"❌ CLI import failed: {e}")
        return False

def generate_report(failed_basic, failed_ml, failed_ui, failed_audio, 
                   missing_files, knowledge_ok, model_ok, gui_ok, cli_ok):
    """Generate a test report"""
    print("\n" + "="*60)
    print("📊 SIMPLE TEST REPORT")
    print("="*60)
    
    # Summary
    total_tests = 9
    passed_tests = sum([
        len(failed_basic) == 0,
        len(failed_ml) == 0,
        len(failed_ui) == 0,
        len(failed_audio) == 0,
        len(missing_files) == 0,
        knowledge_ok,
        model_ok,
        gui_ok,
        cli_ok
    ])
    
    print(f"✅ Tests Passed: {passed_tests}/{total_tests}")
    print(f"❌ Tests Failed: {total_tests - passed_tests}/{total_tests}")
    
    # Detailed results
    if failed_basic:
        print(f"\n❌ Failed Basic Imports ({len(failed_basic)}):")
        for imp in failed_basic:
            print(f"   - {imp}")
    
    if failed_ml:
        print(f"\n❌ Failed ML Imports ({len(failed_ml)}):")
        for imp in failed_ml:
            print(f"   - {imp}")
    
    if failed_ui:
        print(f"\n❌ Failed UI Imports ({len(failed_ui)}):")
        for imp in failed_ui:
            print(f"   - {imp}")
    
    if failed_audio:
        print(f"\n❌ Failed Audio Imports ({len(failed_audio)}):")
        for imp in failed_audio:
            print(f"   - {imp}")
    
    if missing_files:
        print(f"\n❌ Missing Files ({len(missing_files)}):")
        for file in missing_files:
            print(f"   - {file}")
    
    if not knowledge_ok:
        print("\n❌ Knowledge Base: Failed")
    
    if not model_ok:
        print("\n❌ Model Structure: Failed")
    
    if not gui_ok:
        print("\n❌ GUI Structure: Failed")
    
    if not cli_ok:
        print("\n❌ CLI Structure: Failed")
    
    # Recommendations
    print("\n💡 Recommendations:")
    
    if failed_basic or failed_ml or failed_ui or failed_audio:
        print("   - Install missing dependencies: pip install -r requirements.txt")
    
    if missing_files:
        print("   - Check if all project files are present")
    
    if not knowledge_ok:
        print("   - Create or fix knowledge.txt file")
    
    if not model_ok:
        print("   - Check model_llama4.py syntax")
    
    if not gui_ok:
        print("   - Check GUI.py syntax")
    
    if not cli_ok:
        print("   - Check cli.py syntax")
    
    if passed_tests == total_tests:
        print("\n🎉 All basic tests passed! Core functionality is ready.")
    else:
        print(f"\n⚠️ {total_tests - passed_tests} issues found. Please fix them.")

def main():
    """Run simple tests"""
    print("🚀 Starting Simple Project Test")
    print("="*60)
    
    # Run all tests
    failed_basic = test_basic_imports()
    failed_ml = test_ml_imports()
    failed_ui = test_ui_imports()
    failed_audio = test_audio_imports()
    missing_files = test_project_files()
    knowledge_ok = test_knowledge_base()
    model_ok = test_simple_model()
    gui_ok = test_gui_structure()
    cli_ok = test_cli_structure()
    
    # Generate report
    generate_report(failed_basic, failed_ml, failed_ui, failed_audio,
                   missing_files, knowledge_ok, model_ok, gui_ok, cli_ok)

if __name__ == "__main__":
    main() 