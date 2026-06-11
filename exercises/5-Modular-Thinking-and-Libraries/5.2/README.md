# Exercise 5.2: The Random Module

## Objectives
Use the random module to generate random numbers.

## Task
The random module lets you generate random numbers.

Examples:
import random
random.randint(1, 6)          # random integer from 1 to 6 (dice roll)
random.choice(["A", "B", "C"]) # random item from a list
random.random()               # random float from 0 to 1

Your Task:
1. Import random
2. Generate a random number between 1 and 100
3. Pick a random item from ["Rock", "Paper", "Scissors"]
4. Generate a random float between 0 and 1
5. Simulate a coin flip: random.randint(0, 1) where 0=Heads, 1=Tails

## Starter Code
```python
# Write your code below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/5.2/test_5_2.py -v