# Exercise 7.5: Nested For Loops

## Objectives
Put one for loop inside another.

## Task
Put one for loop inside another. The inner loop runs completely for each iteration of the outer loop.

Example:
for i in range(3):    # outer loop: 0, 1, 2
    for j in range(2):  # inner loop: 0, 1
        print("i=" + str(i) + ", j=" + str(j))

Your Task:
1. Print a 3x3 grid (numbers 0-2 for both rows and columns), each row on a separate line.
2. Print a 2x4 grid where each cell shows "row-col".
3. CHALLENGE: Print a triangle:
   *
   **
   ***

## Starter Code
```python
# Write your code below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/7.5/test_7_5.py -v