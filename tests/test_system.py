# tests/test_system.py
def test_preemptive_debugging():
    # Test with known buggy code samples
    buggy_samples = [
        "null_pointer_example.py",
        "race_condition_example.java", 
        "memory_leak_example.c",
        "input_validation_example.js"
    ]
    
    for sample in buggy_samples:
        result = orchestrator.preemptive_debug(load_sample(sample))
        
        # Verify bugs were detected
        assert len(result["prevented_bugs"]) > 0
        
        # Verify fixes were applied
        assert result["patched_code"] != result["original_code"]
        
        # Verify patched code passes tests
        assert run_tests(result["patched_code"]) == "PASS"



        