import os
import json
from typing import List, Dict, Any, Optional
from datetime import datetime
import utils
import config

class SemanticFileSystem:
    """A simple semantic file system using embeddings."""
    
    def __init__(self):
        self.storage_path = config.STORAGE_PATH
        self.metadata_file = os.path.join(self.storage_path, "metadata.json")
        self.embeddings_file = os.path.join(self.storage_path, "embeddings.json")
        self._ensure_storage()
        self.metadata = self._load_metadata()
        self.embeddings = self._load_embeddings()
    
    def _ensure_storage(self):
        """Ensure storage directory exists."""
        os.makedirs(self.storage_path, exist_ok=True)
    
    def _load_metadata(self) -> Dict[str, Any]:
        """Load file metadata."""
        return utils.load_json(self.metadata_file)
    
    def _load_embeddings(self) -> Dict[str, List[float]]:
        """Load file embeddings."""
        return utils.load_json(self.embeddings_file)
    
    def _save_metadata(self):
        """Save file metadata."""
        utils.save_json(self.metadata, self.metadata_file)
    
    def _save_embeddings(self):
        """Save file embeddings."""
        utils.save_json(self.embeddings, self.embeddings_file)
    
    def create_file(self, content: str, context: str = "") -> str:
        """Create a new file with semantic understanding."""
        file_id = f"file_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Generate embedding from content and context
        full_text = f"{context}\n\n{content}" if context else content
        embedding = utils.get_embedding(full_text)
        
        # Store metadata
        self.metadata[file_id] = {
            "id": file_id,
            "content": content,
            "context": context,
            "created": utils.timestamp(),
            "modified": utils.timestamp(),
            "access_count": 0,
            "tags": self._extract_tags(content)
        }
        
        # Store embedding
        self.embeddings[file_id] = embedding
        
        # Save to disk
        self._save_metadata()
        self._save_embeddings()
        
        return file_id
    
    def _extract_tags(self, content: str) -> List[str]:
        """Extract semantic tags from content."""
        # Simple tag extraction - in a real system, this would use NLP
        words = content.lower().split()
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
        tags = [w for w in words if len(w) > 4 and w not in common_words]
        return list(set(tags))[:5]
    
    def search(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Search files using semantic similarity."""
        if not self.embeddings:
            return []
        
        # Get query embedding
        query_embedding = utils.get_embedding(query)
        if not query_embedding:
            return []
        
        # Calculate similarities
        similarities = []
        for file_id, file_embedding in self.embeddings.items():
            similarity = utils.cosine_similarity(query_embedding, file_embedding)
            similarities.append((file_id, similarity))
        
        # Sort by similarity
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Return top results
        results = []
        for file_id, similarity in similarities[:limit]:
            if file_id in self.metadata:
                result = self.metadata[file_id].copy()
                result['similarity'] = similarity
                results.append(result)
        
        return results
    
    def get_file(self, file_id: str) -> Optional[Dict[str, Any]]:
        """Get file by ID."""
        if file_id in self.metadata:
            # Update access count
            self.metadata[file_id]['access_count'] += 1
            self.metadata[file_id]['last_accessed'] = utils.timestamp()
            self._save_metadata()
            return self.metadata[file_id]
        return None
    
    def get_recent_files(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get recently accessed files."""
        files = list(self.metadata.values())
        files.sort(key=lambda x: x.get('last_accessed', x['created']), reverse=True)
        return files[:limit]