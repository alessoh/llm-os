# Configuration settings for LLM OS

import os
from pathlib import Path

# Try to load from .env file if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, will use environment variables only

# OpenAI settings
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL_NAME = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')  # Can be overridden
EMBEDDING_MODEL = os.getenv('OPENAI_EMBEDDING_MODEL', 'text-embedding-ada-002')

# Alternative models you can use:
# MODEL_NAME = "gpt-3.5-turbo-0125"  # Latest GPT-3.5
# MODEL_NAME = "gpt-4o-mini"  # More capable, similar cost
# MODEL_NAME = "gpt-4-turbo-preview"  # Most capable

# System settings
MAX_CONTEXT_LENGTH = 4000
MAX_CONVERSATION_HISTORY = 10

# Storage paths - use absolute paths to avoid issues
BASE_DIR = Path(__file__).parent.absolute()
STORAGE_PATH = os.path.join(BASE_DIR, "llm_os_storage")
EMBEDDINGS_CACHE = os.path.join(STORAGE_PATH, "embeddings_cache.json")

# Agent settings
AGENT_TEMPERATURE = 0.7
SYSTEM_TEMPERATURE = 0.3

# Resource monitoring
RESOURCE_CHECK_INTERVAL = 5  # seconds
PREDICTION_WINDOW = 60  # seconds

# Colors for terminal
try:
    from colorama import Fore, Style, init
    init()  # Initialize colorama for Windows
    COLOR_SYSTEM = Fore.CYAN
    COLOR_USER = Fore.GREEN
    COLOR_AGENT = Fore.YELLOW
    COLOR_ERROR = Fore.RED
    COLOR_RESET = Style.RESET_ALL
except ImportError:
    # Fallback if colorama not installed
    COLOR_SYSTEM = ""
    COLOR_USER = ""
    COLOR_AGENT = ""
    COLOR_ERROR = ""
    COLOR_RESET = ""