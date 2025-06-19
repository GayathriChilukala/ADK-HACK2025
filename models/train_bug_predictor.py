# models/train_bug_predictor.py
from google.cloud import aiplatform
import pandas as pd

def train_bug_prediction_model():
    """Train ML model on Vertex AI"""
    
    # Initialize Vertex AI
    aiplatform.init(project="your-project", location="us-central1")
    
    # Prepare training data
    dataset = prepare_bug_dataset()
    
    # Create AutoML training job
    job = aiplatform.AutoMLTabularTrainingJob(
        display_name="bug-prediction-model",
        optimization_prediction_type="classification",
        optimization_objective="minimize-log-loss",
    )
    
    # Train model
    model = job.run(
        dataset=dataset,
        target_column="has_bug",
        training_fraction_split=0.8,
        validation_fraction_split=0.1,
        test_fraction_split=0.1,
    )
    
    return model