import sys
import subprocess
from pathlib import Path

def main():
    if len(sys.argv) < 2 or not sys.argv[1]:
        print("No active file detected. Click instide a student.py file")
        return
    
    active_file = Path(sys.argv[1])

    if "exercises" not in active_file.parts:
        print("Navigate to a student.py file inside the exercises folders")
        return
    
    exercise_id = active_file.parent.name
    test_filename = f"test_{exercise_id.replace(',','_')}.py"

    test_file_suffix = exercise_id.replace('.', '_')
    test_path = Path("tests") / exercise_id / f"test_{test_file_suffix}.py"

    if not test_path.exists():
        print(f"Expected test file missing at : {test_path}")
        return
    
    print(f"Running tests for Exercise {exercise_id}... \n")

    result = subprocess.run(['pytest', '-v', str(test_path)])

    sys.exit(result.returncode)

if __name__ == '__main__':
    main()