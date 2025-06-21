#!/usr/bin/env python3
"""
Test script to verify LLM OS setup
Run this to check if everything is installed correctly
"""

import sys
import os

print("=" * 60)
print("LLM OS Setup Verification")
print("=" * 60)
print()

# Check Python version
print(f"✓ Python version: {sys.version.split()[0]}")
if sys.version_info < (3, 9):
    print("✗ ERROR: Python 3.9 or higher required")
    sys.exit(1)

# Check required packages
packages_status = []

def check_package(package_name, import_name=None):
    if import_name is None:
        import_name = package_name
    try:
        module = __import__(import_name)
        version = getattr(module, '__version__', 'installed')
        packages_status.append((package_name, True, version))
        print(f"✓ {package_name}: {version}")
    except ImportError:
        packages_status.append((package_name, False, 'NOT INSTALLED'))
        print(f"✗ {package_name}: NOT INSTALLED")

print("\nChecking required packages...")
check_package('openai')
check_package('numpy')
check_package('scikit-learn', 'sklearn')
check_package('python-dateutil', 'dateutil')
check_package('psutil')
check_package('colorama')

# Check optional packages
print("\nChecking optional packages...")
check_package('python-dotenv', 'dotenv')

# Check OpenAI API key
print("\nChecking OpenAI API key...")
api_key = os.getenv('OPENAI_API_KEY')
if api_key:
    print(f"✓ OpenAI API key set ({len(api_key)} characters)")
    if not api_key.startswith('sk-'):
        print("⚠ WARNING: API key should start with 'sk-'")
else:
    print("✗ OpenAI API key NOT set")

# Test OpenAI connection if possible
if api_key and all(status[1] for status in packages_status if status[0] == 'openai'):
    print("\nTesting OpenAI API connection...")
    try:
        import openai
        client = openai.OpenAI(api_key=api_key)
        models = client.models.list()
        print("✓ Successfully connected to OpenAI API")
        
        # Test a simple completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'test successful'"}],
            max_tokens=10
        )
        print(f"✓ API test response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"✗ Failed to connect to OpenAI API: {str(e)}")

# Check project files
print("\nChecking project files...")
required_files = [
    'llm_os.py',
    'agents.py',
    'config.py',
    'utils.py',
    'semantic_storage.py',
    'resource_manager.py',
    'requirements.txt'
]

for file in required_files:
    if os.path.exists(file):
        print(f"✓ {file}")
    else:
        print(f"✗ {file} NOT FOUND")

# Summary
print("\n" + "=" * 60)
failed_packages = [p for p in packages_status if not p[1]]
if failed_packages:
    print("Setup INCOMPLETE. Please install missing packages:")
    print("Run: pip install -r requirements.txt")
elif not api_key:
    print("Setup INCOMPLETE. Please set your OpenAI API key:")
    print("Run: set OPENAI_API_KEY=your-api-key-here")
else:
    print("✓ Setup appears to be complete!")
    print("You can now run: python llm_os.py")

print("=" * 60)