# Exercise 6.4: While Loops with Input

## Objectives
Use while loops to keep asking for input until valid data is entered.

## Task
While loops are useful for repeatedly asking for input until valid.

Example:
def get_positive_number():
    num = int(input("Enter a positive number: "))
    while num <= 0:
        print("Not positive! Try again.")
        num = int(input("Enter a positive number: "))
    return num

Your Task:
Write a function 'get_yes_or_no' that:
- Asks the user to type "yes" or "no"
- Keeps asking until valid input
- Returns the valid answer

## Starter Code
```python
# Write your function below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/6.4/test_6_4.py -v