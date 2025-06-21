#!/usr/bin/env python3
"""
LLM OS - A Simple AI-Native Operating System Demo
"""

import os
import sys
import time
from datetime import datetime
from typing import List, Dict, Any
import json
import openai

import config
import utils
from agents import AgentCoordinator
from semantic_storage import SemanticFileSystem
from resource_manager import PredictiveResourceManager

class LLMOS:
    """Main LLM Operating System class."""
    
    def __init__(self):
        print(utils.format_system_message("Initializing LLM OS..."))
        
        # Check API key
        if not config.OPENAI_API_KEY:
            print(utils.format_error("OpenAI API key not found! Set OPENAI_API_KEY environment variable."))
            sys.exit(1)
        
        # Test API connection
        print(utils.format_system_message("Testing OpenAI API connection..."))
        try:
            test_client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
            # Simple test to verify API key works
            models = test_client.models.list()
            print(utils.format_system_message("API connection successful!"))
        except openai.AuthenticationError:
            print(utils.format_error("Invalid OpenAI API key! Please check your API key."))
            sys.exit(1)
        except openai.APIConnectionError:
            print(utils.format_error("Failed to connect to OpenAI API. Check your internet connection."))
            sys.exit(1)
        except Exception as e:
            print(utils.format_error(f"Unexpected error connecting to OpenAI API: {str(e)}"))
            sys.exit(1)
        
        # Initialize components
        try:
            self.coordinator = AgentCoordinator()
            self.conversation_history = []
            self.context = {
                'session_start': utils.timestamp(),
                'user_profile': {}
            }
        except Exception as e:
            print(utils.format_error(f"Failed to initialize components: {str(e)}"))
            sys.exit(1)
        
        print(utils.format_system_message("LLM OS initialized successfully!"))
        print(utils.format_system_message("Type 'help' for available commands or just chat naturally."))
        print()
    
    def run(self):
        """Main interaction loop."""
        while True:
            try:
                # Get user input
                user_input = input(f"{config.COLOR_USER}You>{config.COLOR_RESET} ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['exit', 'quit', 'shutdown']:
                    self.shutdown()
                    break
                
                # Check for help
                if user_input.lower() == 'help':
                    self.show_help()
                    continue
                
                # Process command
                self.process_command(user_input)
                
            except KeyboardInterrupt:
                print("\n")
                self.shutdown()
                break
            except Exception as e:
                print(utils.format_error(f"Unexpected error: {str(e)}"))
    
    def process_command(self, command: str):
        """Process a user command."""
        try:
            # Add to history
            self.conversation_history.append({
                'role': 'user',
                'content': command,
                'timestamp': utils.timestamp()
            })
            
            # Build context
            context = self._build_context()
            
            # Route to appropriate agent
            agent_name, response = self.coordinator.route_command(command, context)
            
            # Display response
            print(utils.format_agent_response(agent_name, response))
            print()
            
            # Add to history
            self.conversation_history.append({
                'role': 'assistant',
                'agent': agent_name,
                'content': response,
                'timestamp': utils.timestamp()
            })
            
            # Trim history if too long
            if len(self.conversation_history) > config.MAX_CONVERSATION_HISTORY * 2:
                self.conversation_history = self.conversation_history[-config.MAX_CONVERSATION_HISTORY:]
                
        except openai.RateLimitError:
            print(utils.format_error("Rate limit reached. Please wait a moment and try again."))
        except openai.APIError as e:
            print(utils.format_error(f"OpenAI API error: {str(e)}"))
        except Exception as e:
            print(utils.format_error(f"Error processing command: {str(e)}"))
    
    def _build_context(self) -> str:
        """Build context from conversation history."""
        recent_history = self.conversation_history[-config.MAX_CONVERSATION_HISTORY:]
        
        context_parts = []
        
        # Add recent conversation
        if recent_history:
            conv = []
            for entry in recent_history:
                role = entry['role']
                content = entry['content']
                conv.append(f"{role}: {content}")
            
            context_parts.append("Recent conversation:\n" + "\n".join(conv))
        
        # Add system context
        context_parts.append(f"Current time: {utils.timestamp()}")
        context_parts.append(f"Session duration: {self._get_session_duration()}")
        
        return "\n\n".join(context_parts)
    
    def _get_session_duration(self) -> str:
        """Get session duration as string."""
        start = datetime.strptime(self.context['session_start'], "%Y-%m-%d %H:%M:%S")
        duration = datetime.now() - start
        
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60
        
        if hours > 0:
            return f"{hours}h {minutes}m"
        else:
            return f"{minutes}m"
    
    def show_help(self):
        """Show help information."""
        help_text = """
Available commands and examples:

FILE OPERATIONS:
- "Create a document about [topic]"
- "Find all documents related to [topic]"
- "Show me recent documents"
- "Help me organize my files"

SYSTEM ANALYSIS:
- "What's using the most resources?"
- "Analyze my system performance"
- "Show me resource usage patterns"
- "What processes are running?"

GENERAL ASSISTANCE:
- "Remember that I prefer [preference]"
- "What do you remember about me?"
- "Help me with [task]"
- Any general question or request

SYSTEM COMMANDS:
- help - Show this help message
- exit/quit/shutdown - Exit the LLM OS

You can also just chat naturally - the system will understand and route your request appropriately!
"""
        print(utils.format_system_message(help_text))
    
    def shutdown(self):
        """Shutdown the OS."""
        print(utils.format_system_message("Shutting down LLM OS..."))
        
        try:
            # Save conversation history
            history_file = os.path.join(config.STORAGE_PATH, "conversation_history.json")
            utils.save_json({
                'history': self.conversation_history,
                'context': self.context
            }, history_file)
            print(utils.format_system_message("Conversation history saved."))
        except Exception as e:
            print(utils.format_error(f"Failed to save history: {str(e)}"))
        
        print(utils.format_system_message("Goodbye!"))

def main():
    """Main entry point."""
    print(config.COLOR_SYSTEM)
    print("=" * 60)
    print("   LLM OS - AI-Native Operating System Demo")
    print("=" * 60)
    print(config.COLOR_RESET)
    
    # Create and run OS
    os_instance = LLMOS()
    os_instance.run()

if __name__ == "__main__":
    main()