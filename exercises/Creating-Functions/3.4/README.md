# Exercise 3.4: Multiple Parameters

## Objectives
Create functions that take multiple parameters.

## Task
Functions can have multiple parameters. Order matters.

Example:
def introduce(first_name, last_name):
    print(first_name + " " + last_name)

Your Task:
1. Write a function 'subtract' that takes two numbers and returns first minus second
2. Test: result = subtract(10, 3); print(result)  # 7
3. Write a function 'rectangle_area' that takes width and height and returns width * height
4. Test: print(rectangle_area(5, 3))  # 15
5. Write a function 'full_greeting' that takes first and last name, returns "Hello [first] [last]!" 

## Starter Code
```python
# Write your functions below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/3.4/test_3_4.py -v