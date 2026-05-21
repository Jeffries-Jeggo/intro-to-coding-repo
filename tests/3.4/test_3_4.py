import pytest
import os

def test_3_4_exists():
    """Test that student.py exists"""
    path = "exercises/3-Creating-Functions/3.4/student.py"
    assert os.path.exists(path), "student.py not found"

def test_3_4_syntax():
    """Test that student.py has valid Python syntax"""
    path = "exercises/3-Creating-Functions/3.4/student.py"
    with open(path) as f:
        code = f.read()
    compile(code, "<student.py>", "exec")

def test_3_4_runs():
    """Test that student.py can execute without error"""
    path = "exercises/3-Creating-Functions/3.4/student.py"
    with open(path) as f:
        code = f.read()
    try:
        exec(code, {"__name__": "__main__"})
    except Exception as e:
        pytest.fail("Error running student.py: " + str(e))
