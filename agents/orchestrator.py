# agents/orchestrator.py
import asyncio
from agents.base_agent import BaseAgent
from agents.temporal_analyzer import TemporalAnalyzer
from agents.auto_healer import AutoHealer
from typing import Dict

class PreemptiveOrchestrator(BaseAgent):
    def __init__(self):
        super().__init__("orchestrator")
        self.temporal_analyzer = TemporalAnalyzer()
        self.auto_healer = AutoHealer()
        
    async def preemptive_debug(self, code: str) -> Dict:
        """Main orchestration workflow"""
        print(f"[{self.name}] Starting preemptive debugging process...")
        
        # Step 1: Analyze timeline
        timeline_result = await self.temporal_analyzer.analyze_code_timeline(code)
        
        # Step 2: Generate fixes
        healing_result = await self.auto_healer.generate_fixes(
            code, timeline_result['vulnerabilities']
        )
        
        # Step 3: Compile results
        result = {
            "original_code": code,
            "patched_code": healing_result['patched_code'],
            "timeline_analysis": timeline_result['timeline'],
            "vulnerabilities_detected": timeline_result['vulnerabilities'],
            "fixes_applied": healing_result['fixes'],
            "prevention_score": self._calculate_prevention_score(timeline_result, healing_result),
            "agent_interactions": [
                f"{self.name} → {self.temporal_analyzer.name}",
                f"{self.temporal_analyzer.name} → {self.auto_healer.name}",
                f"{self.auto_healer.name} → {self.name}"
            ]
        }
        
        print(f"[{self.name}] Preemptive debugging complete! Prevention score: {result['prevention_score']}")
        return result
    
    def _calculate_prevention_score(self, timeline_result: Dict, healing_result: Dict) -> float:
        """Calculate how much we improved the code"""
        vuln_count = len(timeline_result['vulnerabilities'])
        fix_count = healing_result['fix_count']
        
        if vuln_count == 0:
            return 1.0
            
        prevention_score = min(fix_count / vuln_count, 1.0) * timeline_result['confidence']
        return round(prevention_score, 2)