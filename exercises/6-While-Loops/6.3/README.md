# Exercise 6.3: While Loops with If Inside

## Objectives
Combine while loops with if statements inside.

## Task
You can add if statements inside while loops.

Example:
count = 1
while count <= 10:
    if count % 2 == 0:
        print(str(count) + " is even")
    else:
        print(str(count) + " is odd")
    count = count + 1

Your Task:
1. Count from 1 to 5. Print "Big" if > 3, otherwise print the number.
2. Count from 0 to 10. Print "Fizz" if divisible by 3, otherwise print the number.
3. Start at 10, divide by 2 each time until <= 1. Print each value.

## Starter Code
```python
# Write your code below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/6.3/test_6_3.py -v