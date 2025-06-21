import openai
from typing import Dict, Any, List, Optional
import json
import config
import utils
from semantic_storage import SemanticFileSystem
from resource_manager import PredictiveResourceManager

class BaseAgent:
    """Base class for all agents."""
    
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
    
    def think(self, prompt: str, context: str = "") -> str:
        """Use LLM to process request."""
        messages = [
            {"role": "system", "content": self.role},
        ]
        
        if context:
            messages.append({"role": "system", "content": f"Context: {context}"})
        
        messages.append({"role": "user", "content": prompt})
        
        try:
            response = self.client.chat.completions.create(
                model=config.MODEL_NAME,
                messages=messages,
                temperature=config.AGENT_TEMPERATURE,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error in {self.name}: {str(e)}"

class FileManagementAgent(BaseAgent):
    """Agent for file and document management."""
    
    def __init__(self, file_system: SemanticFileSystem):
        super().__init__(
            name="FileManager",
            role="You are a file management assistant. Help users create, find, and organize documents. Be concise and helpful."
        )
        self.fs = file_system
    
    def process_command(self, command: str, context: str = "") -> str:
        """Process file-related commands."""
        # Determine action
        action_prompt = f"""
        Analyze this command and respond with ONLY one of these actions:
        - CREATE: if user wants to create a new document
        - SEARCH: if user wants to find documents
        - LIST: if user wants to see recent documents
        - ORGANIZE: if user wants help organizing
        
        Command: {command}
        
        Action:"""
        
        action = self.think(action_prompt).strip().upper()
        
        if "CREATE" in action:
            return self._create_document(command, context)
        elif "SEARCH" in action:
            return self._search_documents(command)
        elif "LIST" in action:
            return self._list_recent()
        else:
            return self._provide_organization_advice(command)
    
    def _create_document(self, command: str, context: str) -> str:
        """Create a new document."""
        content_prompt = f"""
        Based on this request, generate appropriate document content:
        Request: {command}
        
        Generate the content:"""
        
        content = self.think(content_prompt, context)
        file_id = self.fs.create_file(content, command)
        
        return f"Created document {file_id} with content:\n\n{content[:200]}..."
    
    def _search_documents(self, command: str) -> str:
        """Search for documents."""
        results = self.fs.search(command)
        
        if not results:
            return "No documents found matching your query."
        
        response = "Found these relevant documents:\n"
        for i, result in enumerate(results, 1):
            response += f"\n{i}. {result['id']} (similarity: {result['similarity']:.2f})"
            response += f"\n   Created: {result['created']}"
            response += f"\n   Preview: {result['content'][:100]}...\n"
        
        return response
    
    def _list_recent(self) -> str:
        """List recent documents."""
        recent = self.fs.get_recent_files()
        
        if not recent:
            return "No recent documents found."
        
        response = "Recent documents:\n"
        for doc in recent:
            response += f"\n- {doc['id']} (accessed {doc.get('access_count', 0)} times)"
            response += f"\n  Created: {doc['created']}"
            response += f"\n  Preview: {doc['content'][:100]}...\n"
        
        return response
    
    def _provide_organization_advice(self, command: str) -> str:
        """Provide organization advice."""
        return self.think(f"Provide brief advice for: {command}")

class SystemAnalysisAgent(BaseAgent):
    """Agent for system analysis and resource management."""
    
    def __init__(self, resource_manager: PredictiveResourceManager):
        super().__init__(
            name="SystemAnalyst",
            role="You are a system analysis assistant. Help users understand resource usage, patterns, and optimize performance."
        )
        self.rm = resource_manager
    
    def process_command(self, command: str) -> str:
        """Process system analysis commands."""
        self.rm.update()
        
        # Get current stats
        stats = self.rm.get_current_stats()
        anomalies = self.rm.detect_anomalies()
        
        # Analyze with LLM
        analysis_prompt = f"""
        Analyze this system state and user request:
        
        Request: {command}
        
        System State:
        - CPU: {stats['cpu']['current']:.1f}% (predicted: {stats['cpu']['predicted_30s']:.1f}%)
        - Memory: {stats['memory']['current']:.1f}% (predicted: {stats['memory']['predicted_30s']:.1f}%)
        - Disk: {stats['disk']['used_percent']:.1f}% used
        
        Top Processes:
        {json.dumps(stats['top_processes'], indent=2)}
        
        Anomalies: {', '.join(anomalies) if anomalies else 'None'}
        
        Provide helpful analysis and recommendations:"""
        
        return self.think(analysis_prompt)

class PersonalAssistant(BaseAgent):
    """Main personal assistant agent."""
    
    def __init__(self):
        super().__init__(
            name="Assistant",
            role="""You are a helpful AI assistant that's part of an AI-native operating system. 
            You help users with various tasks, remember their preferences, and coordinate with other agents.
            Be friendly, concise, and proactive in offering help."""
        )
        self.memory = {}
    
    def remember(self, key: str, value: Any):
        """Remember user preference or information."""
        self.memory[key] = {
            'value': value,
            'time': utils.timestamp()
        }
    
    def recall(self, key: str) -> Optional[Any]:
        """Recall remembered information."""
        if key in self.memory:
            return self.memory[key]['value']
        return None
    
    def process_general(self, command: str, context: str = "") -> str:
        """Process general commands and questions."""
        # Check if this is a memory command
        if "remember" in command.lower():
            return self._handle_memory(command)
        
        # General assistance
        memory_context = f"User preferences: {json.dumps(self.memory)}" if self.memory else ""
        full_context = f"{context}\n{memory_context}" if memory_context else context
        
        return self.think(command, full_context)
    
    def _handle_memory(self, command: str) -> str:
        """Handle memory-related commands."""
        memory_prompt = f"""
        Extract what the user wants to remember from this command:
        "{command}"
        
        Respond with ONLY a JSON object in this format:
        {{"key": "preference_name", "value": "what_to_remember"}}
        
        If you can't extract clear information, respond with {{"error": "unclear"}}.
        """
        
        response = self.think(memory_prompt)
        
        try:
            data = json.loads(response)
            if "error" not in data:
                self.remember(data["key"], data["value"])
                return f"I'll remember that your {data['key']} is {data['value']}"
            else:
                return "I'm not sure what you want me to remember. Can you be more specific?"
        except:
            return "I had trouble understanding what to remember. Please try again."

class AgentCoordinator:
    """Coordinates multiple agents."""
    
    def __init__(self):
        self.fs = SemanticFileSystem()
        self.rm = PredictiveResourceManager()
        
        self.file_agent = FileManagementAgent(self.fs)
        self.system_agent = SystemAnalysisAgent(self.rm)
        self.assistant = PersonalAssistant()
    
    def route_command(self, command: str, context: str = "") -> tuple[str, str]:
        """Route command to appropriate agent."""
        routing_prompt = f"""
        Classify this command into ONE category:
        - FILE: for document/file operations
        - SYSTEM: for resource/performance analysis  
        - GENERAL: for general assistance
        
        Command: {command}
        
        Category:"""
        
        response = self.assistant.think(routing_prompt)
        category = response.strip().upper()
        
        if "FILE" in category:
            agent_response = self.file_agent.process_command(command, context)
            return ("FileManager", agent_response)
        elif "SYSTEM" in category:
            agent_response = self.system_agent.process_command(command)
            return ("SystemAnalyst", agent_response)
        else:
            agent_response = self.assistant.process_general(command, context)
            return ("Assistant", agent_response)