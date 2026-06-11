# Exercise 8.5: String Practice

## Objectives
Put together string methods, slicing, and concatenation.

## Task
Practice combining string methods, slicing, and concatenation.

Examples:
email = "mika.tanaka@school.edu"
at_index = email.find("@")
name_part = email[:at_index]
print(name_part.capitalize())

filename = "homework.py"
print(filename.endswith(".py"))

sentence = "I like cats"
sentence = sentence.replace("cats", "dogs")

Your Task:
1. Given 'student@school.com', extract the part before '@' using find. Print.
2. Given 'test.txt', check if it ends with '.py'. Print True/False.
3. Given 'Hello World', replace 'World' with 'Python'. Print.
4. CHALLENGE: Given 'ABC123DEF', extract just the numeric part using slicing.

## Starter Code
```python
# Write your code below


```

## Running Your Code
1. Write your code in student.py
2. Run it with: python student.py
3. Check your output

## Tests
Run: pytest tests/8.5/test_8_5.py -v