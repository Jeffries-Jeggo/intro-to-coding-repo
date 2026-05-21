# Exercise 8.4: String Immutability

## Objectives
Understand that strings cannot be changed after creation.

## Task
Strings cannot be changed after creation (immutable).
Any operation that seems to modify actually creates a new string.

Example:
name = "Mika"
# name[0] = "m"  # This would cause an error!
name = name.lower()  # Creates new string

Your Task:
1. Start with 'ABC' and use .lower() to get 'abc'. Print.
2. Start with 'Hi' and concatenate to get 'Hi There!'. Print.
3. Start with 'Python' and use slicing + concatenation to get 'python'.
4. Create your name, convert to uppercase, then back to lowercase.

## Starter Code
```python
# Write your code below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/8.4/test_8_4.py -v