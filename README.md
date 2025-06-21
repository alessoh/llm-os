# llm-os
LLM Operating System
# README.md

```markdown
# LLM OS - AI-Native Operating System Demo

A demonstration of an AI-native operating system that uses natural language as its primary interface, implementing core concepts like semantic storage, multi-agent architecture, and context-aware assistance.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installing Anaconda](#installing-anaconda)
- [Setting Up the Environment](#setting-up-the-environment)
- [Getting OpenAI API Key](#getting-openai-api-key)
- [Downloading LLM OS](#downloading-llm-os)
- [Running LLM OS](#running-llm-os)
- [Usage Guide](#usage-guide)
- [File Structure](#file-structure)
- [Troubleshooting](#troubleshooting)

## Overview

LLM OS is a proof-of-concept implementation showing how future operating systems might work when AI is deeply integrated into every aspect of computing. Instead of clicking through menus or typing commands, you interact using natural language.

## Features

- **Natural Language Interface**: Communicate with your computer like you would with a human assistant
- **Semantic File System**: Files are stored and retrieved based on meaning, not just names
- **Multi-Agent Architecture**: Specialized AI agents handle different types of tasks
- **Context-Aware Assistance**: The system remembers your conversation and preferences
- **Predictive Resource Management**: Monitors and predicts system resource usage
- **Learning System**: Remembers your preferences and improves over time

## System Requirements

### Hardware
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 1GB free space (includes Conda installation)
- **Processor**: Any modern CPU (64-bit required)
- **Internet**: Required for downloading packages and API calls

### Software
- **Operating System**: Windows 10 or Windows 11 (64-bit)
- **Anaconda/Miniconda**: Will be installed (instructions below)
- **OpenAI API Key**: Required (instructions below)

## Installing Anaconda

### Step 1: Download Anaconda

1. Open your web browser and go to: https://www.anaconda.com/download
2. Click the **Download** button for Windows
3. Save the installer (it will be named something like `Anaconda3-2024.02-1-Windows-x86_64.exe`)

### Step 2: Install Anaconda

1. **Run the installer** by double-clicking the downloaded file
2. Click **Next** on the welcome screen
3. Click **I Agree** to accept the license
4. Select **Just Me (recommended)** and click **Next**
5. Choose installation location (default is fine) and click **Next**
6. **IMPORTANT**: Check both boxes:
   - ✓ Add Anaconda3 to my PATH environment variable
   - ✓ Register Anaconda3 as my default Python
7. Click **Install** (this takes 5-10 minutes)
8. Click **Next** when installation completes
9. Click **Finish**

### Step 3: Verify Anaconda Installation

1. Press `Windows Key + R`
2. Type `cmd` and press Enter
3. In the black command window, type:
   ```cmd
   conda --version
   ```
4. You should see something like: `conda 24.1.2`
5. If you see an error, restart your computer and try again

## Setting Up the Environment

### Step 1: Open Anaconda Prompt

1. Click the **Start Menu**
2. Type `Anaconda Prompt`
3. Click on **Anaconda Prompt (Anaconda3)**
4. A black window will open with text like:
   ```
   (base) C:\Users\YourName>
   ```

### Step 2: Create LLM OS Environment

In the Anaconda Prompt, type these commands one by one:

```cmd
# Create a new environment named 'llmos' with Python 3.9
conda create -n llmos python=3.9 -y

# Activate the environment
conda activate llmos
```

After activation, your prompt should change to:
```
(llmos) C:\Users\YourName>
```

### Step 3: Install Git (If Not Already Installed)

Check if Git is installed:
```cmd
git --version
```

If you see an error, install Git:
1. Download Git from: https://git-scm.com/download/win
2. Run the installer using default settings
3. Restart Anaconda Prompt after installation

## Getting OpenAI API Key

### Step 1: Create OpenAI Account

1. Open your browser and go to: https://platform.openai.com/
2. Click **Sign up** (or **Log in** if you have an account)
3. Complete the registration process

### Step 2: Get Your API Key

1. Once logged in, click your profile icon (top right)
2. Click **View API keys**
3. Click **Create new secret key**
4. Give it a name (e.g., "LLM OS Demo")
5. Click **Create secret key**
6. **IMPORTANT**: Copy the key immediately (starts with `sk-`)
7. Save it in Notepad temporarily - you'll need it soon!

### Step 3: Add Credits (If Needed)

1. Click **Settings** → **Billing**
2. Add a payment method
3. Add at least $5 in credits (should last for hundreds of interactions)

## Downloading LLM OS

### Option 1: Using Git (Recommended)

In Anaconda Prompt (with llmos environment active):

```cmd
# Navigate to your Documents folder
cd %USERPROFILE%\Documents

# Clone the repository
git clone https://github.com/alessoh/llm-os.git

# Enter the project folder
cd llm-os
```

### Option 2: Download ZIP

1. Open your browser and go to: https://github.com/alessoh/llm-os
2. Click the green **Code** button
3. Click **Download ZIP**
4. Save to your Downloads folder
5. Extract the ZIP file:
   - Right-click the downloaded file
   - Click **Extract All...**
   - Choose `%USERPROFILE%\Documents` as destination
   - Click **Extract**
6. Rename the extracted folder from `llm-os-main` to `llm-os`

In Anaconda Prompt:
```cmd
# Navigate to the project folder
cd %USERPROFILE%\Documents\llm-os
```

### Step 3: Install Required Packages

Still in Anaconda Prompt (with llmos environment active):

```cmd
# Install all required packages
pip install -r requirements.txt
```

This will install:
- openai==1.3.0
- numpy==1.24.3
- scikit-learn==1.3.0
- python-dateutil==2.8.2
- psutil==5.9.5
- colorama==0.4.6

## Running LLM OS

### Step 1: Set OpenAI API Key

In the Anaconda Prompt, set your API key:

```cmd
# Replace sk-your-key-here with your actual key
set OPENAI_API_KEY=sk-your-key-here
```

To set it permanently (recommended):

```cmd
# This sets it for all future sessions
setx OPENAI_API_KEY "sk-your-key-here"
```

### Step 2: Start LLM OS

Make sure you're in the project folder and conda environment is active:

```cmd
# Your prompt should show (llmos) C:\Users\YourName\Documents\llm-os>
# If not in the right place:
cd %USERPROFILE%\Documents\llm-os

# If environment not active:
conda activate llmos

# Start the program
python llm_os.py
```

### Step 3: Success!

You should see:

```
============================================================
   LLM OS - AI-Native Operating System Demo
============================================================
[System] Initializing LLM OS...
[System] LLM OS initialized successfully!
[System] Type 'help' for available commands or just chat naturally.

You>
```

## Usage Guide

### Basic Interaction

Type naturally! Examples:

```
You> Create a document about space exploration
You> Find all documents about science
You> What's using my computer's memory?
You> Remember that I'm learning Python
You> Help me organize my files
```

### Special Commands

- `help` - Show available commands
- `exit` or `quit` - Exit the program

### Example Session

```
You> Create a note about my project ideas

[FileManager] Created document file_20240120_143022 with content:

# Project Ideas

Here are some innovative project concepts to explore:

1. **Smart Home Automation**
   - Voice-controlled lighting system
   - Automated temperature management...

You> What's my CPU usage?

[SystemAnalyst] Current system analysis:

CPU Usage: 15.2% (Predicted in 30s: 17.8%)
Memory Usage: 42.3% (6.8 GB available)

Top Process: chrome.exe using 8.5% CPU

Your system is running smoothly with plenty of resources available.

You> Remember I prefer markdown format for docs

[Assistant] I'll remember that your preference is markdown format for docs

You> exit

[System] Shutting down LLM OS...
[System] Goodbye!
```

### Tips for Best Results

1. **Be specific**: "Create a document about Python functions" works better than "make a file"
2. **Use context**: The system remembers your conversation
3. **Experiment**: Try different ways of asking for things
4. **Check help**: Type `help` to see examples

## File Structure

The project contains these files:

```
llm-os/
│   llm_os.py              # Main program
│   agents.py              # AI agents
│   semantic_storage.py    # File system
│   resource_manager.py    # Resource monitor
│   config.py              # Settings
│   utils.py               # Utilities
│   requirements.txt       # Package list
│   README.md              # This file
│
└───llm_os_storage/        # Created automatically when you run
    │   metadata.json      # File information
    │   embeddings.json    # Semantic data
    └───conversation_history.json  # Chat history
```

## Troubleshooting

### Common Issues and Solutions

#### "conda is not recognized as a command"

1. Restart your computer
2. Use **Anaconda Prompt** not regular Command Prompt
3. If still not working, reinstall Anaconda with PATH option checked

#### "No module named 'openai'"

In Anaconda Prompt:
```cmd
conda activate llmos
pip install -r requirements.txt
```

#### "OpenAI API key not found!"

Check your API key:
```cmd
# Should display your key
echo %OPENAI_API_KEY%

# If blank, set it again:
set OPENAI_API_KEY=sk-your-actual-key
```

#### API Error 401 (Unauthorized)

- Your API key is invalid
- Make sure it starts with `sk-`
- Try creating a new key on OpenAI's website

#### API Error 429 (Rate Limit)

- You've made too many requests
- Wait 1 minute and try again
- Check your OpenAI account for usage limits

#### "Python was not found"

Make sure conda environment is active:
```cmd
conda activate llmos
```

#### Git Clone Fails

If Git clone doesn't work, use the ZIP download method instead.

### Testing Your Setup

Create a test file called `test.py` in the llm-os folder:

```python
print("Python is working!")

try:
    import openai
    print("✓ OpenAI installed")
except:
    print("✗ OpenAI NOT installed")

import os
key = os.getenv('OPENAI_API_KEY')
if key:
    print(f"✓ API key set ({len(key)} chars)")
else:
    print("✗ API key NOT set")
```

Run it:
```cmd
python test.py
```

All checks should show ✓

### Getting Help

If you're stuck:

1. **Check you're in the right folder**: 
   ```cmd
   cd
   ```
   Should show: `C:\Users\YourName\Documents\llm-os`

2. **Check environment is active**: 
   ```cmd
   conda info --envs
   ```
   Should show `llmos` with an asterisk (*)

3. **Check Python version**:
   ```cmd
   python --version
   ```
   Should show Python 3.9.x

4. **Check all packages are installed**:
   ```cmd
   pip list
   ```
   Should show openai, numpy, scikit-learn, etc.

### Updating LLM OS

To get the latest version:

```cmd
# Navigate to project folder
cd %USERPROFILE%\Documents\llm-os

# Pull latest changes
git pull
```

## Quick Start Checklist

- [ ] Anaconda installed
- [ ] Conda environment created (`llmos`)
- [ ] Environment activated
- [ ] Git installed (or used ZIP download)
- [ ] Repository cloned/downloaded to Documents folder
- [ ] Requirements installed via pip
- [ ] OpenAI account created
- [ ] API key obtained and has credits
- [ ] API key set in environment
- [ ] In llm-os directory in Anaconda Prompt
- [ ] Ready to run `python llm_os.py`!

## Final Notes

- **Repository**: https://github.com/alessoh/llm-os
- **Cost**: Each interaction costs about $0.002
- **Internet**: Required at all times
- **Privacy**: Your commands go to OpenAI's servers
- **Storage**: Files are stored locally in `llm_os_storage` folder
- **Updates**: Check the repository for updates and improvements

---

**Remember**: This is a demonstration of AI-native operating system concepts. Have fun exploring the future of computing! 🚀

For issues or questions, check the Troubleshooting section or visit the GitHub repository.
```

This updated README now references the GitHub repository for downloading the code, includes both Git and ZIP download options, and removes the uninstall section as requested. It maintains the detailed Windows/Conda focus while pointing users to the actual repository location.