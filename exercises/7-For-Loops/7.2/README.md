# Exercise 7.2: For Loops with Lists

## Objectives
Use a for loop to iterate over items in a list.

## Task
Use a for loop to go through each item in a list.

Examples:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    print(str(i) + ": " + str(numbers[i]))

Your Task:
1. Create a list ['cat', 'dog', 'mouse', 'rabbit']. Print each item.
2. Create a list [2, 4, 6, 8, 10]. Print each item multiplied by 3.
3. Use range and len to print index and value of ['A', 'B', 'C', 'D'].

## Starter Code
```python
# Write your code below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/7.2/test_7_2.py -v