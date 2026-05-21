# Exercise 5.4: Creating Your Own Module

## Objectives
Learn that a module is just a Python file, and create your own.

## Task
A module is just a Python file. Creating your own module is easy!

Step 1: Create a file called 'operations.py' with:
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

Step 2: In this file (student.py), write:
import operations
result = operations.add(5, 3)
print(result)
result = operations.multiply(4, 7)
print(result)

Your Task:
1. Create the operations.py file with add and multiply functions
2. Import it in this file and test both functions

## Starter Code
```python
# Create operations.py first!

import operations

print(operations.add(5, 3))
print(operations.multiply(4, 7))

```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/5.4/test_5_4.py -v