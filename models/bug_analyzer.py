# models/bug_analyzer.py
from google.cloud import bigquery
import pandas as pd

class BugPatternAnalyzer:
    def __init__(self):
        self.client = bigquery.Client()
        
    def analyze_historical_patterns(self, code_features):
        """Query BigQuery for similar bug patterns"""
        
        query = """
        SELECT 
            bug_type,
            code_pattern,
            frequency,
            severity_score,
            fix_success_rate
        FROM `your-project.bugs.historical_data`
        WHERE similarity_score(code_pattern, @code_features) > 0.8
        ORDER BY frequency DESC
        LIMIT 100
        """
        
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter(
                    "code_features", "STRING", str(code_features)
                )
            ]
        )
        
        results = self.client.query(query, job_config=job_config)
        return [dict(row) for row in results]