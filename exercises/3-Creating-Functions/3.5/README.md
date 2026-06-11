# Exercise 3.5: Combining Functions

## Objectives
Call functions inside other functions, or use return values as arguments.

## Task
You can call functions inside other functions, or use return values as arguments.

Example:
def add_and_double(a, b):
    total = a + b
    return total * 2

result = double(add_three(1, 2, 3))

Your Task:
1. Write a function 'is_larger' that takes two numbers and returns True if first is bigger
2. Test: print(is_larger(10, 5))  # True
3. Test: print(is_larger(3, 8))   # False
4. Write a function 'average' that takes three numbers and returns their average
5. Test: print(average(10, 20, 30))  # 20.0

## Starter Code
```python
# Write your functions below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/3.5/test_3_5.py -v