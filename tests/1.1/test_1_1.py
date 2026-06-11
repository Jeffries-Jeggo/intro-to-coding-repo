import pytest
import os
import importlib.util
from pathlib import Path

def test_1_1_exists():
    """Test that student.py exists"""
    path = "exercises/1-Functions-and-Arithmetic-Operators/1.1/student.py"
    assert os.path.exists(path), "student.py not found"

def test_1_1_syntax():
    """Test that student.py has valid Python syntax"""
    path = "exercises/1-Functions-and-Arithmetic-Operators/1.1/student.py"
    with open(path) as f:
        code = f.read()
    compile(code, "<student.py>", "exec")

def test_1_1_runs():
    """Test that student.py can execute without error"""
    path = "exercises/1-Functions-and-Arithmetic-Operators/1.1/student.py"
    with open(path) as f:
        code = f.read()
    try:
        exec(code, {"__name__": "__main__"})
    except Exception as e:
        pytest.fail("Error running student.py: " + str(e))

def test_student_output(capsys):
    # 1. Construct the absolute or relative path to the student file
    # This points to: exercises/1-Functions-and-Arithmetic-Operators/1.1/student.py
    student_file_path = Path("exercises/1-Functions-and-Arithmetic-Operators/1.1/student.py")
    
    # 2. Use importlib to load the module from its file path safely
    spec = importlib.util.spec_from_file_location("student_module", student_file_path)
    student_module = importlib.util.module_from_spec(spec)
    
    # 3. Execute the module (this triggers their print statements)
    spec.loader.exec_module(student_module)
    
    # 4. Capture and assert the stdout
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
