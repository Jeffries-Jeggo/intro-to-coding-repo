# Exercise 8.3: String Slicing

## Objectives
Access parts of a string using indices and slicing.

## Task
Access parts of a string using indices in square brackets.
Index 0 is the first character. Slicing [start:stop] gets characters from start to stop-1.

Example:
text = "Hello"
# H e l l o
# 0 1 2 3 4

print(text[0])      # H
print(text[1:4])    # ell
print(text[:3])     # Hel
print(text[2:])     # llo

Your Task:
1. Given 'Computer', print the first 4 characters.
2. Given 'Programming', print characters from index 3 to the end.
3. Given 'Python', print the middle character (index 2).
4. Given 'Hello World', print 'World' using slicing.

## Starter Code
```python
# Write your code below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/8.3/test_8_3.py -v