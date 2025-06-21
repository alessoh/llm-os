import openai
import numpy as np
from typing import List, Dict, Any
import json
import os
from datetime import datetime
import config

# Initialize OpenAI client
client = openai.OpenAI(api_key=config.OPENAI_API_KEY)

def get_embedding(text: str) -> List[float]:
    """Get embedding for a text string."""
    try:
        response = client.embeddings.create(
            model=config.EMBEDDING_MODEL,
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"Error getting embedding: {e}")
        return []

def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    a_np = np.array(a)
    b_np = np.array(b)
    return np.dot(a_np, b_np) / (np.linalg.norm(a_np) * np.linalg.norm(b_np))

def save_json(data: Dict[str, Any], filepath: str):
    """Save data to JSON file."""
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, default=str)

def load_json(filepath: str) -> Dict[str, Any]:
    """Load data from JSON file."""
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}

def timestamp() -> str:
    """Get current timestamp string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_agent_response(agent_name: str, response: str) -> str:
    """Format agent response with color and name."""
    return f"{config.COLOR_AGENT}[{agent_name}]{config.COLOR_RESET} {response}"

def format_system_message(message: str) -> str:
    """Format system message with color."""
    return f"{config.COLOR_SYSTEM}[System]{config.COLOR_RESET} {message}"

def format_error(error: str) -> str:
    """Format error message with color."""
    return f"{config.COLOR_ERROR}[Error]{config.COLOR_RESET} {error}"