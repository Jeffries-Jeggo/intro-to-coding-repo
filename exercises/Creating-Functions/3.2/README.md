# Exercise 3.2: Functions with Parameters

## Objectives
Learn to pass data into functions using parameters.

## Task
Put variable names inside the parentheses when defining a function.
These are called parameters. When you call the function, you pass values called arguments.

Example:
def greet(name):    # 'name' is a parameter
    print("Hello " + name)

greet("Mika")        # "Mika" is an argument

Your Task:
1. Write a function 'triple' that takes a number and prints it multiplied by 3
2. Test it with triple(4), triple(10), triple(-5)
3. Write a function 'greet_person' that takes a name and prints "Welcome, [name]!" 

## Starter Code
```python
# Write your functions below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/3.2/test_3_2.py -v