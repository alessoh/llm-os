import psutil
import time
from collections import deque
from typing import Dict, List, Any
import numpy as np
from datetime import datetime, timedelta
import utils

class PredictiveResourceManager:
    """Manages and predicts system resource usage."""
    
    def __init__(self):
        self.history = {
            'cpu': deque(maxlen=100),
            'memory': deque(maxlen=100),
            'disk_io': deque(maxlen=100)
        }
        self.patterns = {}
        self.last_check = time.time()
    
    def update(self):
        """Update resource measurements."""
        current_time = time.time()
        
        # Collect metrics
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory()
        disk_io = psutil.disk_io_counters()
        
        # Store measurements
        self.history['cpu'].append({
            'time': current_time,
            'value': cpu_percent
        })
        self.history['memory'].append({
            'time': current_time,
            'value': memory.percent
        })
        self.history['disk_io'].append({
            'time': current_time,
            'read': disk_io.read_bytes,
            'write': disk_io.write_bytes
        })
        
        self.last_check = current_time
    
    def predict_usage(self, resource: str, seconds_ahead: int = 30) -> float:
        """Predict resource usage in the future."""
        if resource not in self.history or len(self.history[resource]) < 5:
            return 0.0
        
        # Simple linear prediction
        recent = list(self.history[resource])[-10:]
        if resource == 'disk_io':
            values = [(r['read'] + r['write']) / 1024 / 1024 for r in recent]
        else:
            values = [r['value'] for r in recent]
        
        if len(values) < 2:
            return values[-1] if values else 0.0
        
        # Calculate trend
        x = np.arange(len(values))
        y = np.array(values)
        
        # Simple linear regression
        A = np.vstack([x, np.ones(len(x))]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        
        # Predict
        future_x = len(values) + (seconds_ahead / 5)  # Assuming 5-second intervals
        prediction = m * future_x + c
        
        # Bound prediction
        return max(0, min(100, prediction))
    
    def get_current_stats(self) -> Dict[str, Any]:
        """Get current resource statistics."""
        cpu = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        # Get top processes
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                pinfo = proc.info
                if pinfo['cpu_percent'] > 1 or pinfo['memory_percent'] > 1:
                    processes.append(pinfo)
            except:
                pass
        
        processes.sort(key=lambda x: x['cpu_percent'] + x['memory_percent'], reverse=True)
        
        return {
            'cpu': {
                'current': cpu,
                'predicted_30s': self.predict_usage('cpu', 30),
                'cores': psutil.cpu_count()
            },
            'memory': {
                'current': memory.percent,
                'predicted_30s': self.predict_usage('memory', 30),
                'available_gb': memory.available / (1024**3),
                'total_gb': memory.total / (1024**3)
            },
            'disk': {
                'used_percent': disk.percent,
                'free_gb': disk.free / (1024**3)
            },
            'top_processes': processes[:5]
        }
    
    def detect_anomalies(self) -> List[str]:
        """Detect resource usage anomalies."""
        anomalies = []
        
        stats = self.get_current_stats()
        
        # High CPU usage
        if stats['cpu']['current'] > 80:
            anomalies.append(f"High CPU usage: {stats['cpu']['current']:.1f}%")
        
        # High memory usage
        if stats['memory']['current'] > 85:
            anomalies.append(f"High memory usage: {stats['memory']['current']:.1f}%")
        
        # Predict future issues
        if stats['cpu']['predicted_30s'] > 90:
            anomalies.append("CPU usage likely to spike in next 30 seconds")
        
        if stats['memory']['predicted_30s'] > 90:
            anomalies.append("Memory usage likely to spike in next 30 seconds")
        
        return anomalies