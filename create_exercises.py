#!/usr/bin/env python3
import os

base = "/home/ubuntu/intro-to-coding-repo"

exercises = {
    "1.1": {
        "title": "Calling Built-in Functions",
        "objectives": "Learn to call Python's built-in functions like print(), max(), and min(). Understand that functions take inputs (arguments) and produce outputs.",
        "task": """In this exercise you'll practice calling Python's built-in functions.

Functions are like machines - you put something in, and they give something out.
The general pattern is: function_name(argument)

Try these:
1. print("Hello")  - print outputs text to the screen
2. max(1, 5, 3)    - max finds the largest number
3. min(10, 2, 8)   - min finds the smallest number
4. abs(-7)         - abs gives the absolute value

Your Task:
Write print() statements to:
- Print any string you like
- Find the max of 4, 12, 7, 3
- Find the min of 20, 5, 18, 9
- Find the absolute value of -15
""",
        "starter": "# Starter code for 1.1\n# Write your print statements below\n\n",
        "solution": '# Solution for 1.1\nprint("Hello World")\nprint(max(4, 12, 7, 3))\nprint(min(20, 5, 18, 9))\nprint(abs(-15))\n',
        "test_type": "assertion",
    },
    "1.2": {
        "title": "Arithmetic Operators",
        "objectives": "Use Python's arithmetic operators: +, -, *, /, **, %",
        "task": """Python supports all the standard math operators:
- +  addition
- -  subtraction
- *  multiplication
- /  division
- ** power (exponent)
- %  modulo (remainder)

Example:
print(5 + 3)   # prints 8
print(10 - 4)  # prints 6
print(3 * 7)   # prints 21
print(20 / 4)  # prints 5.0
print(2 ** 4)  # prints 16 (2 to the power of 4)
print(17 % 5)  # prints 2 (remainder when 17 divided by 5)

Your Task:
Write print() statements to calculate:
1. 8 + 2
2. 10 - 3
3. 4 * 7
4. 100 / 5
5. 2 to the power of 8
6. Remainder when 100 divided by 7
""",
        "starter": "# Starter code for 1.2\n# Write your print statements below\n\n# 1.\n# 2.\n# 3.\n# 4.\n# 5.\n# 6.\n",
        "solution": "# Solution for 1.2\nprint(8 + 2)\nprint(10 - 3)\nprint(4 * 7)\nprint(100 / 5)\nprint(2 ** 8)\nprint(100 % 7)\n",
        "test_type": "output",
    },
    "1.3": {
        "title": "Function Arguments",
        "objectives": "Understand that functions can take multiple arguments of different types.",
        "task": """Functions can take multiple arguments, and different functions accept different numbers.

Examples:
- print("hi")           - takes 1 argument
- max(1, 2, 3)          - takes 3 arguments
- min(10, 2, 8, 3)      - takes 4 arguments
- int(9.8)              - converts to integer
- float(25)             - converts to float

Your Task:
Write code to:
1. Convert the float 9.8 to an integer using int()
2. Convert the integer 25 to a float using float()
3. Find the max of 4, 12, 7, 3, 5
4. Find the min of 20, 5, 18, 9, 3
5. Convert the string "42" to an integer using int()
""",
        "starter": "# Starter code for 1.3\n# Write your code below\n\n",
        "solution": "# Solution for 1.3\nprint(int(9.8))\nprint(float(25))\nprint(max(4, 12, 7, 3, 5))\nprint(min(20, 5, 18, 9, 3))\nprint(int(\"42\"))\n",
        "test_type": "assertion",
    },
    "1.4": {
        "title": "Order of Operations",
        "objectives": "Understand that Python follows standard order of operations (PEMDAS).",
        "task": """Python follows standard math order of operations:
P - Parentheses first
E - Exponents (power)
M/D - Multiply/Divide left to right
A/S - Add/Subtract left to right

When functions are involved, work from the inside out.

Example:
max(5 + 3, 10 - 2) = max(8, 8) = 8

Your Task - calculate and print:
1. max(4 + 1, 6 - 1)
2. min(10 + 2, 15 - 3)
3. abs(5 - 20)
4. int(7.5 + 2.3)
5. max(3 * 2, 20 / 2)
6. min(10 * 2, 50 / 2)
""",
        "starter": "# Starter code for 1.4\n# Write your print statements below\n\n",
        "solution": "# Solution for 1.4\nprint(max(4 + 1, 6 - 1))\nprint(min(10 + 2, 15 - 3))\nprint(abs(5 - 20))\nprint(int(7.5 + 2.3))\nprint(max(3 * 2, 20 / 2))\nprint(min(10 * 2, 50 / 2))\n",
        "test_type": "output",
    },
    "1.5": {
        "title": "Practice with Functions",
        "objectives": "Put together everything you've learned in this lesson.",
        "task": """Put together calling functions, arithmetic, and order of operations.

Challenge 1: Find the average of 10, 20, and 30
Hint: average = sum / count

Challenge 2: Find the smallest value after adding 5 to each of these: 8, 3, 15, 1
Hint: min(8+5, 3+5, 15+5, 1+5)

Challenge 3: Convert the result of 25 / 4 to an integer

Challenge 4: Find the max of (3 + 4) and (5 * 2)

Challenge 5: Use abs() to find the difference between 10 and 50 (should be positive)
""",
        "starter": "# Starter code for 1.5\n# Write your print statements below\n\n",
        "solution": "# Solution for 1.5\n# Challenge 1: average of 10, 20, 30\nprint((10 + 20 + 30) / 3)\n\n# Challenge 2: min of (8+5), (3+5), (15+5), (1+5)\nprint(min(8+5, 3+5, 15+5, 1+5))\n\n# Challenge 3: convert 25/4 to integer\nprint(int(25 / 4))\n\n# Challenge 4: max of (3+4) and (5*2)\nprint(max(3 + 4, 5 * 2))\n\n# Challenge 5: absolute difference\nprint(abs(10 - 50))\n",
        "test_type": "assertion",
    },
}

def slug(ex_id):
    return ex_id.replace(".", "_")

for ex_id, data in exercises.items():
    lesson = ex_id.split(".")[0]
    path = f"{base}/exercises/1-Functions-and-Arithmetic/{ex_id}"
    
    os.makedirs(path, exist_ok=True)
    os.makedirs(f"{base}/teacher/markscheme/{ex_id}", exist_ok=True)
    os.makedirs(f"{base}/tests/{ex_id}", exist_ok=True)
    
    # README
    readme = f"""# Exercise {ex_id}: {data['title']}

## Objectives
{data['objectives']}

## Task
{data['task']}

## Starter Code (in student.py)
{data['starter']}
"""
    with open(f"{path}/README.md", "w") as f:
        f.write(readme)
    
    # Student starter
    with open(f"{path}/student.py", "w") as f:
        f.write(data['starter'])
    
    # Teacher solution
    with open(f"{base}/teacher/markscheme/{ex_id}/solution.py", "w") as f:
        f.write(data['solution'])
    
    # Test file
    if data["test_type"] == "output":
        test = f'''import pytest
from io import StringIO
import sys

def test_ex_{slug(ex_id)}():
    # For output-based exercises, capture stdout
    # Run the student code and check output
    # This is a placeholder - update with specific test
    pass
'''
    else:
        test = f'''import pytest

def test_ex_{slug(ex_id)}():
    # For assertion-based exercises
    # Import student's code and check outputs
    pass
'''
    
    with open(f"{base}/tests/{ex_id}/test_{slug(ex_id)}.py", "w") as f:
        f.write(test)

print("Lesson 1 created successfully!")
print("Exercises:", list(exercises.keys()))