## File: config.py

```python
# Configuration settings for LLM OS

import os

# OpenAI settings
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL_NAME = "gpt-3.5-turbo"
EMBEDDING_MODEL = "text-embedding-ada-002"

# System settings
MAX_CONTEXT_LENGTH = 4000
MAX_CONVERSATION_HISTORY = 10
STORAGE_PATH = "./llm_os_storage"
EMBEDDINGS_CACHE = "./embeddings_cache.json"

# Agent settings
AGENT_TEMPERATURE = 0.7
SYSTEM_TEMPERATURE = 0.3

# Resource monitoring
RESOURCE_CHECK_INTERVAL = 5  # seconds
PREDICTION_WINDOW = 60  # seconds

# Colors for terminal
from colorama import Fore, Style
COLOR_SYSTEM = Fore.CYAN
COLOR_USER = Fore.GREEN
COLOR_AGENT = Fore.YELLOW
COLOR_ERROR = Fore.RED
COLOR_RESET = Style.RESET_ALL