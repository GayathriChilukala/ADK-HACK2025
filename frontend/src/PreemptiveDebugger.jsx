// frontend/src/PreemptiveDebugger.jsx
import React, { useState } from 'react';
import CodeEditor from './CodeEditor';
import TimelineView from './TimelineView';
import BugPrevention from './BugPrevention';

function PreemptiveDebugger() {
    const [code, setCode] = useState('');
    const [analysis, setAnalysis] = useState(null);
    const [isAnalyzing, setIsAnalyzing] = useState(false);
    
    const analyzeCode = async () => {
        setIsAnalyzing(true);
        
        const response = await fetch('/api/preemptive-debug', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code })
        });
        
        const result = await response.json();
        setAnalysis(result);
        setIsAnalyzing(false);
    };
    
    return (
        <div className="preemptive-debugger">
            <div className="code-section">
                <CodeEditor 
                    value={code} 
                    onChange={setCode}
                    onAnalyze={analyzeCode}
                    isAnalyzing={isAnalyzing}
                />
            </div>
            
            {analysis && (
                <div className="results-section">
                    <TimelineView timeline={analysis.timeline_analysis} />
                    <BugPrevention 
                        bugs={analysis.prevented_bugs}
                        fixes={analysis.applied_fixes}
                    />
                </div>
            )}
        </div>
    );
}

export default PreemptiveDebugger;