# llm-os
LLM Operating System
# LLM OS - AI-Native Operating System 

## 🌟 Features story

- **Natural Language Interface**: Communicate with your computer using everyday language
- **Semantic File System**: Files are stored and retrieved based on meaning, not just names
- **Multi-Agent Architecture**: Specialized AI agents handle different types of tasks
- **Context-Aware Assistance**: The system remembers your conversation and preferences
- **Predictive Resource Management**: Monitors and predicts system resource usage
- **Learning System**: Remembers your preferences and improves over time

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [System Requirements](#-system-requirements)
- [Detailed Installation](#-detailed-installation)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)
- [Examples](#-examples)

## 🚀 Quick Start

For experienced users who want to get running quickly:

```bash
# Clone the repository
git clone https://github.com/alessoh/llm-os.git
cd llm-os

# Create conda environment
conda create -n llmos python=3.9 -y
conda activate llmos

# Quick fix option (no code changes needed)
pip install openai==0.28.1 numpy==1.24.3 scikit-learn==1.3.0 python-dateutil==2.8.2 psutil==5.9.5 colorama==0.4.6

# Set API key and run
set OPENAI_API_KEY=sk-your-key-here
python llm_os.py
```

## 💻 System Requirements

### Hardware
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 1GB free space
- **Processor**: Any modern 64-bit CPU
- **Internet**: Required for API calls

### Software
- **OS**: Windows 10/11 (64-bit)
- **Python**: 3.9+ (via Anaconda)
- **OpenAI API Key**: Required (see [Getting an API Key](#getting-openai-api-key))

## 📦 Detailed Installation

### Step 1: Install Anaconda

1. Download Anaconda from: https://www.anaconda.com/download
2. Run the installer with default settings
3. **Important**: Check "Add Anaconda3 to PATH" during installation
4. Verify installation:
   ```cmd
   conda --version
   ```

### Step 2: Get OpenAI API Key

1. Create account at: https://platform.openai.com/
2. Navigate to API keys: https://platform.openai.com/api-keys
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. Add credits to your account (Settings → Billing)

### Step 3: Download LLM OS

** Using Git**
```cmd
cd %USERPROFILE%\Documents
git clone https://github.com/alessoh/llm-os.git
cd llm-os
``

### Step 4: Set Up Environment

```cmd
# Open Anaconda Prompt and navigate to project
cd %USERPROFILE%\Documents\llm-os

# Create and activate conda environment
conda create -n llmos python=3.9 -y
conda activate llmos
```

### Step 5: Install Dependencies

```
pip install -r requirements.txt
```

### Step 6: Configure API Key

**Method 1: Environment Variable (Quick)**
```cmd
set OPENAI_API_KEY=sk-your-actual-key-here
```

**Method 2: .env File (Recommended)**
```cmd
# Create .env file from template
copy .env.example .env

# Edit .env file and add your key
notepad .env
```

### Step 7: Verify Setup

```cmd
# Run the verification script
python test_setup.py
```

You should see all green checkmarks (✓). If not, see [Troubleshooting](#-troubleshooting).

### Step 8: Run LLM OS

```cmd
python llm_os.py
```

## 📖 Usage Guide

### Basic Commands

Once running, you can interact naturally:

```
You> Create a document about machine learning basics
You> Find all my Python notes
You> What's using the most CPU right now?
You> Remember that I prefer markdown format
You> Help me organize my project files
```

### Special Commands

- `help` - Show available commands and examples
- `exit` or `quit` - Exit the program

### Example Session

```
============================================================
   LLM OS - AI-Native Operating System Demo
============================================================
[System] Initializing LLM OS...
[System] API connection successful!
[System] LLM OS initialized successfully!
[System] Type 'help' for available commands or just chat naturally.

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
[System] Conversation history saved.
[System] Goodbye!
```

## 📁 Project Structure

```
llm-os/
├── llm_os.py              # Main program entry point
├── agents.py              # AI agent implementations
├── semantic_storage.py    # Semantic file system
├── resource_manager.py    # System resource monitoring
├── config.py              # Configuration settings
├── utils.py               # Utility functions
├── requirements.txt       # Python dependencies
├── test_setup.py          # Setup verification script
├── auto_fix.py            # Automatic code fixer
├── .env.example           # Environment variable template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

### Generated Files

When you run LLM OS, it creates:
```
llm_os_storage/
├── metadata.json          # File metadata
├── embeddings.json        # Semantic embeddings
└── conversation_history.json  # Chat history
```

## 🔧 Troubleshooting

### Common Issues

#### "conda is not recognized"
- Use **Anaconda Prompt** not Command Prompt
- Restart computer after Anaconda installation
- Reinstall Anaconda with PATH option checked

#### "No module named 'openai'"
```cmd
conda activate llmos
pip install -r requirements.txt
```

#### "OpenAI API key not found!"
```cmd
# Check if key is set
echo %OPENAI_API_KEY%

# If blank, set it:
set OPENAI_API_KEY=sk-your-actual-key
```

#### API Error 401 (Unauthorized)
- Verify API key starts with `sk-`
- Check key validity at: https://platform.openai.com/api-keys
- Ensure you have credits in your account

#### API Error 429 (Rate Limit)
- Wait 60 seconds before retrying
- Check usage at: https://platform.openai.com/usage

#### "Python was not found"
```cmd
# Ensure conda environment is active
conda activate llmos
```

### Advanced Troubleshooting

Run the diagnostic script:
```cmd
python test_setup.py
```

This will check:
- ✓ Python version
- ✓ Required packages
- ✓ API key configuration
- ✓ OpenAI connection
- ✓ Project files

## 💡 Examples

### File Operations
- `"Create a Python script for data analysis"`
- `"Find all documents about neural networks"`
- `"Show me files I created yesterday"`
- `"Help me organize my research papers"`

### System Analysis
- `"What's my current memory usage?"`
- `"Which programs are using the most resources?"`
- `"Analyze my system performance"`
- `"Predict CPU usage for the next minute"`

### Personal Assistant
- `"Remember that I'm working on a web project"`
- `"What preferences have you learned about me?"`
- `"Summarize our conversation"`
- `"Help me plan my coding tasks"`

## 🛠️ Configuration

### Environment Variables

Create a `.env` file in the project root:
```env
# Required
OPENAI_API_KEY=sk-your-api-key-here

# Optional
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_EMBEDDING_MODEL=text-embedding-ada-002
```

### Available Models

Edit `config.py` to change models:
```python
# Default (fast and cheap)
MODEL_NAME = "gpt-3.5-turbo"

# Latest GPT-3.5
MODEL_NAME = "gpt-3.5-turbo-0125"

# More capable
MODEL_NAME = "gpt-4o-mini"

# Most capable
MODEL_NAME = "gpt-4-turbo-preview"
```

## 📊 Cost Estimation

- Each interaction: ~$0.002 (GPT-3.5-turbo)
- 100 interactions: ~$0.20
- 1000 interactions: ~$2.00

Monitor usage at: https://platform.openai.com/usage

## 🤝 Contributing

This is a demonstration project. Feel free to:
- Fork and experiment
- Submit issues for bugs
- Share your modifications
- Build upon the concepts

## ⚖️ License

This project is provided as-is for educational purposes. See the repository for license details.

## 🔍 Additional Resources

- **Repository**: https://github.com/alessoh/llm-os
- **OpenAI Docs**: https://platform.openai.com/docs
- **Anaconda Help**: https://docs.anaconda.com/
- **Python Tutorial**: https://docs.python.org/3/tutorial/

## ⚠️ Important Notes

- **Internet Required**: The system needs internet for API calls
- **Privacy**: Commands are processed by OpenAI's servers
- **Costs**: OpenAI API usage incurs charges
- **Educational**: This is a demonstration, not production software

---

**Tip**: Start with simple commands and explore gradually. The system understands natural language, so just describe what you want!

For issues or questions, check the [Troubleshooting](#-troubleshooting) section or visit the GitHub repository.