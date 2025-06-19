# agents/base_agent.py
import asyncio
import json
from typing import Dict, List, Any
from datetime import datetime

class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        self.id = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
    async def send_message(self, to_agent: str, message: Dict):
        """Simulate agent communication"""
        print(f"[{self.name}] → [{to_agent}]: {json.dumps(message, indent=2)}")
        return message
        
    async def process_message(self, message: Dict) -> Dict:
        """Override in subclasses"""
        return {"status": "processed", "agent": self.name}