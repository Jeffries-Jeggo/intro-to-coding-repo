# Exercise 4.5: If-Elif-Else Chains

## Objectives
Use 'elif' for multiple conditions checked in order.

## Task
Use 'elif' for multiple conditions. Python checks them in order.
Only the first True branch runs.

Example:
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

Your Task:
1. Write a function 'temperature_message' that takes degrees:
   - Returns "Cold" if < 10
   - Returns "Nice" if 10-25
   - Returns "Hot" if > 25
2. Test with 5, 18, 30
3. Write a function 'size_of_number' that takes a number and returns:
   - "Big" if > 10
   - "Medium" if == 10
   - "Small" if < 10
4. Test with 15, 10, 3

## Starter Code
```python
# Write your functions below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/4.5/test_4_5.py -v