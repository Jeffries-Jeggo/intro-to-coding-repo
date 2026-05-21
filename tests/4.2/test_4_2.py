import pytest
import os

def test_4_2_exists():
    """Test that student.py exists"""
    path = "exercises/4-Booleans-and-Conditionals/4.2/student.py"
    assert os.path.exists(path), "student.py not found"

def test_4_2_syntax():
    """Test that student.py has valid Python syntax"""
    path = "exercises/4-Booleans-and-Conditionals/4.2/student.py"
    with open(path) as f:
        code = f.read()
    compile(code, "<student.py>", "exec")

def test_4_2_runs():
    """Test that student.py can execute without error"""
    path = "exercises/4-Booleans-and-Conditionals/4.2/student.py"
    with open(path) as f:
        code = f.read()
    try:
        exec(code, {"__name__": "__main__"})
    except Exception as e:
        pytest.fail("Error running student.py: " + str(e))
