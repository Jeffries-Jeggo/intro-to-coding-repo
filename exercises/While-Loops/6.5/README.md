# Exercise 6.5: Break and Continue

## Objectives
Use 'break' to exit a loop early, 'continue' to skip iterations.

## Task
Use 'break' to exit a loop early.
Use 'continue' to skip the rest of the current iteration.

Examples:
# break
count = 0
while count < 10:
    if count == 5:
        break
    print(count)
    count = count + 1

# continue
count = 0
while count < 6:
    count = count + 1
    if count == 3:
        continue
    print(count)

Your Task:
1. Count from 0 to 10, but stop when count equals 7 (use break)
2. Count from 1 to 5, but skip 3 (use continue)
3. Count from 0 to 10, print only even numbers

## Starter Code
```python
# Write your code below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/6.5/test_6_5.py -v