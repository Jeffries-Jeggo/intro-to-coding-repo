# Exercise 4.4: If-Else Statements

## Objectives
Use 'else' to specify what happens when the 'if' condition is False.

## Task
Use 'else' to specify what happens when the 'if' condition is False.
Only one branch runs.

Example:
age = 15
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")

Your Task:
1. Write a function 'check_pass' that takes a score and returns "Pass" if >= 50, "Fail" otherwise
2. Test: print(check_pass(75))  # Pass
3. Test: print(check_pass(30))  # Fail
4. Write a function 'is_even' that takes a number and returns "Even" if divisible by 2, "Odd" otherwise
5. Test: print(is_even(4))  # Even
6. Test: print(is_even(7))  # Odd

## Starter Code
```python
# Write your functions below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/4.4/test_4_4.py -v