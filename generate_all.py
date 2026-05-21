#!/usr/bin/env python3
"""Generate all 40 exercises for intro-to-coding-repo"""
import os

base = "/home/ubuntu/intro-to-coding-repo"

LESSONS = [
    {
        "num": "1",
        "name": "Functions-and-Arithmetic-Operators",
        "display_name": "Functions and Arithmetic Operators",
        "exercises": [
            {
                "id": "1.1", "title": "Calling Built-in Functions",
                "objectives": "Learn to call Python's built-in functions like print(), max(), and min().",
                "task": """In this exercise you'll practice calling Python's built-in functions.

Functions are like machines - you put something in, and they give something out.
The general pattern is: function_name(argument)

Try these:
1. print("Hello")  - print outputs text to the screen
2. max(1, 5, 3)    - max finds the largest number
3. min(10, 2, 8)   - min finds the smallest number
4. abs(-7)         - abs gives the absolute value

Your Task:
Write print() statements to:
- Print any string you like
- Find the max of 4, 12, 7, 3
- Find the min of 20, 5, 18, 9
- Find the absolute value of -15""",
                "starter": "# Write your print statements below\n\n",
                "solution": 'print("Hello World")\nprint(max(4, 12, 7, 3))\nprint(min(20, 5, 18, 9))\nprint(abs(-15))\n',
            },
            {
                "id": "1.2", "title": "Arithmetic Operators",
                "objectives": "Use Python's arithmetic operators: +, -, *, /, **, %",
                "task": """Python supports all the standard math operators:
- +  addition
- -  subtraction
- *  multiplication
- /  division
- ** power (exponent)
- %  modulo (remainder)

Example:
print(5 + 3)   # prints 8
print(10 - 4)  # prints 6
print(3 * 7)   # prints 21
print(20 / 4)  # prints 5.0
print(2 ** 4)  # prints 16
print(17 % 5)  # prints 2

Your Task:
Write print() statements to calculate:
1. 8 + 2
2. 10 - 3
3. 4 * 7
4. 100 / 5
5. 2 to the power of 8
6. Remainder when 100 divided by 7""",
                "starter": "# Write your print statements below\n\n# 1.\n# 2.\n# 3.\n# 4.\n# 5.\n# 6.\n",
                "solution": "print(8 + 2)\nprint(10 - 3)\nprint(4 * 7)\nprint(100 / 5)\nprint(2 ** 8)\nprint(100 % 7)\n",
            },
            {
                "id": "1.3", "title": "Function Arguments",
                "objectives": "Understand that functions can take multiple arguments of different types.",
                "task": """Functions can take multiple arguments, and different functions accept different numbers.

Examples:
- print("hi")           - takes 1 argument
- max(1, 2, 3)          - takes 3 arguments
- min(10, 2, 8, 3)      - takes 4 arguments
- int(9.8)              - converts to integer
- float(25)             - converts to float

Your Task:
1. Convert the float 9.8 to an integer using int()
2. Convert the integer 25 to a float using float()
3. Find the max of 4, 12, 7, 3, 5
4. Find the min of 20, 5, 18, 9, 3
5. Convert the string "42" to an integer using int()""",
                "starter": "# Write your code below\n\n",
                "solution": 'print(int(9.8))\nprint(float(25))\nprint(max(4, 12, 7, 3, 5))\nprint(min(20, 5, 18, 9, 3))\nprint(int("42"))\n',
            },
            {
                "id": "1.4", "title": "Order of Operations",
                "objectives": "Understand that Python follows standard order of operations (PEMDAS).",
                "task": """Python follows standard math order of operations:
P - Parentheses first
E - Exponents (power)
M/D - Multiply/Divide left to right
A/S - Add/Subtract left to right

When functions are involved, work from the inside out.

Example:
max(5 + 3, 10 - 2) = max(8, 8) = 8

Your Task - calculate and print:
1. max(4 + 1, 6 - 1)
2. min(10 + 2, 15 - 3)
3. abs(5 - 20)
4. int(7.5 + 2.3)
5. max(3 * 2, 20 / 2)
6. min(10 * 2, 50 / 2)""",
                "starter": "# Write your print statements below\n\n",
                "solution": "print(max(4 + 1, 6 - 1))\nprint(min(10 + 2, 15 - 3))\nprint(abs(5 - 20))\nprint(int(7.5 + 2.3))\nprint(max(3 * 2, 20 / 2))\nprint(min(10 * 2, 50 / 2))\n",
            },
            {
                "id": "1.5", "title": "Practice with Functions",
                "objectives": "Put together everything you've learned in this lesson.",
                "task": """Put together calling functions, arithmetic, and order of operations.

Challenge 1: Find the average of 10, 20, and 30
Hint: average = sum / count

Challenge 2: Find the smallest value after adding 5 to each of these: 8, 3, 15, 1

Challenge 3: Convert the result of 25 / 4 to an integer

Challenge 4: Find the max of (3 + 4) and (5 * 2)

Challenge 5: Use abs() to find the difference between 10 and 50""",
                "starter": "# Write your print statements below\n\n",
                "solution": "print((10 + 20 + 30) / 3)\nprint(min(8+5, 3+5, 15+5, 1+5))\nprint(int(25 / 4))\nprint(max(3 + 4, 5 * 2))\nprint(abs(10 - 50))\n",
            },
        ],
    },
    {
        "num": "2",
        "name": "Variables-and-Assignment",
        "display_name": "Variables and Assignment",
        "exercises": [
            {
                "id": "2.1", "title": "Creating Variables",
                "objectives": "Learn to create variables and assign values to them.",
                "task": """Variables store values for later use. Use the assignment operator (=) to create a variable.

Example:
age = 27
name = "Mika"
temperature = 31.5

Your Task:
Create the following variables:
1. age = 27
2. temperature = 31.5
3. name = "YourName" (use your actual name)
4. cash = 1050
5. is_student = True

Then print each variable.""",
                "starter": "# Create your variables below\n\n",
                "solution": 'age = 27\ntemperature = 31.5\nname = "Mika"\ncash = 1050\nis_student = True\n\nprint(age)\nprint(temperature)\nprint(name)\nprint(cash)\nprint(is_student)\n',
            },
            {
                "id": "2.2", "title": "Variable Types",
                "objectives": "Understand the four basic variable types: int, float, str, bool.",
                "task": """Python has four basic variable types:
- int    (whole numbers): age = 27
- float  (decimals): price = 19.99
- str    (text): name = "Mika"
- bool   (True/False): is_valid = True

Python assigns the type automatically.

Your Task:
Create one variable of each type:
1. An int called 'count' with value 42
2. A float called 'temperature' with value 36.6
3. A str called 'city' with value "Taipei"
4. A bool called 'is_raining' with value False

Print all four.""",
                "starter": "# Create your variables below\n\n",
                "solution": 'count = 42\ntemperature = 36.6\ncity = "Taipei"\nis_raining = False\n\nprint(count)\nprint(temperature)\nprint(city)\nprint(is_raining)\n',
            },
            {
                "id": "2.3", "title": "Variable Naming Rules",
                "objectives": "Learn valid variable naming conventions in Python.",
                "task": """Variable names must follow these rules:
- Start with a letter or underscore (not a number)
- Can contain letters, numbers, and underscores
- Cannot be a Python keyword

Valid: time, x, first_name, _lastname, counter1, my_var2
Invalid: 2temp, my-var, counter!, #name

Your Task:
1. Create a variable 'year' with value 2024
2. Create a variable 'student_name' with value "YourName"
3. Create a variable starting with underscore called '_secret' with value 42
Print all three.""",
                "starter": "# Create your variables below\n\n",
                "solution": 'year = 2024\nstudent_name = "Mika"\n_secret = 42\n\nprint(year)\nprint(student_name)\nprint(_secret)\n',
            },
            {
                "id": "2.4", "title": "Updating Variables",
                "objectives": "Learn how to update variable values, including using the old value.",
                "task": """You can change a variable's value by assigning a new one.
You can also use the variable's old value to compute the new one.

Example:
score = 0
score = 50        # replaces 0 with 50
score = score + 10 # adds 10 to the old value

Your Task:
1. Create a variable 'points' starting at 0
2. Add 25 to it
3. Add another 30
4. Print the final value

Challenge: Start with x = 5, then double it three times.""",
                "starter": "# Write your code below\n\n",
                "solution": "points = 0\npoints = points + 25\npoints = points + 30\nprint(points)\n\nx = 5\nx = x * 2\nprint(x)\nx = x * 2\nprint(x)\nx = x * 2\nprint(x)\n",
            },
            {
                "id": "2.5", "title": "Type Conversion",
                "objectives": "Use int(), float(), and str() to convert between types.",
                "task": """Use int(), float(), and str() to convert between types.

Examples:
num_str = "42"
num_int = int(num_str)    # "42" -> 42
pi = 3.14159
print(int(pi))            # 3.14159 -> 3 (loses decimal!)
age = 25
print("I am " + str(age))  # must convert to str for concatenation

Your Task:
1. Convert the string "100" to an int and add 50
2. Convert 2.9 to an int
3. Convert the number 99 to a string and concatenate with " is almost 100" """,
                "starter": "# Write your code below\n\n",
                "solution": 'result1 = int("100") + 50\nprint(result1)\n\nresult2 = int(2.9)\nprint(result2)\n\nresult3 = str(99) + " is almost 100"\nprint(result3)\n',
            },
        ],
    },
    {
        "num": "3",
        "name": "Creating-Functions",
        "display_name": "Creating Functions",
        "exercises": [
            {
                "id": "3.1", "title": "Defining a Simple Function",
                "objectives": "Learn to create your own function using the def keyword.",
                "task": """Use 'def' to create your own functions. Don't forget the colon.
The code inside a function must be indented.

Example:
def greeting():
    print("Hello there!")

greeting()  # Call the function

Your Task:
1. Create a function called 'farewell' that prints "Goodbye!"
2. Call your function
3. Create a function called 'hello' that prints "Hello World!"
4. Call it""",
                "starter": "# Define your functions below\n\n",
                "solution": 'def farewell():\n    print("Goodbye!")\n\nfarewell()\n\ndef hello():\n    print("Hello World!")\n\nhello()\n',
            },
            {
                "id": "3.2", "title": "Functions with Parameters",
                "objectives": "Learn to pass data into functions using parameters.",
                "task": """Put variable names inside the parentheses when defining a function.
These are called parameters. When you call the function, you pass values called arguments.

Example:
def greet(name):    # 'name' is a parameter
    print("Hello " + name)

greet("Mika")        # "Mika" is an argument

Your Task:
1. Write a function 'triple' that takes a number and prints it multiplied by 3
2. Test it with triple(4), triple(10), triple(-5)
3. Write a function 'greet_person' that takes a name and prints "Welcome, [name]!" """,
                "starter": "# Write your functions below\n\n",
                "solution": 'def triple(number):\n    print(number * 3)\n\ntriple(4)\ntriple(10)\ntriple(-5)\n\ndef greet_person(name):\n    print("Welcome, " + name + "!")\n\ngreet_person("Mika")\n',
            },
            {
                "id": "3.3", "title": "Returning Values",
                "objectives": "Use the 'return' keyword to send values back from functions.",
                "task": """Use 'return' to send a value back from a function.
Without return, a function returns None.

Example:
def add(a, b):
    return a + b

result = add(5, 3)   # result = 8

Your Task:
1. Write a function 'square' that takes a number and returns it squared
2. Test: result = square(5); print(result)  # should be 25
3. Write a function 'add_three' that takes three numbers and returns their sum
4. Test: print(add_three(10, 20, 30))  # should be 60""",
                "starter": "# Write your functions below\n\n",
                "solution": "def square(number):\n    return number * number\n\nresult = square(5)\nprint(result)\n\ndef add_three(a, b, c):\n    return a + b + c\n\nprint(add_three(10, 20, 30))\n",
            },
            {
                "id": "3.4", "title": "Multiple Parameters",
                "objectives": "Create functions that take multiple parameters.",
                "task": """Functions can have multiple parameters. Order matters.

Example:
def introduce(first_name, last_name):
    print(first_name + " " + last_name)

Your Task:
1. Write a function 'subtract' that takes two numbers and returns first minus second
2. Test: result = subtract(10, 3); print(result)  # 7
3. Write a function 'rectangle_area' that takes width and height and returns width * height
4. Test: print(rectangle_area(5, 3))  # 15
5. Write a function 'full_greeting' that takes first and last name, returns "Hello [first] [last]!" """,
                "starter": "# Write your functions below\n\n",
                "solution": 'def subtract(a, b):\n    return a - b\n\nresult = subtract(10, 3)\nprint(result)\n\ndef rectangle_area(width, height):\n    return width * height\n\nprint(rectangle_area(5, 3))\n\ndef full_greeting(first, last):\n    return "Hello " + first + " " + last + "!"\n\nprint(full_greeting("Mika", "Tanaka"))\n',
            },
            {
                "id": "3.5", "title": "Combining Functions",
                "objectives": "Call functions inside other functions, or use return values as arguments.",
                "task": """You can call functions inside other functions, or use return values as arguments.

Example:
def add_and_double(a, b):
    total = a + b
    return total * 2

result = double(add_three(1, 2, 3))

Your Task:
1. Write a function 'is_larger' that takes two numbers and returns True if first is bigger
2. Test: print(is_larger(10, 5))  # True
3. Test: print(is_larger(3, 8))   # False
4. Write a function 'average' that takes three numbers and returns their average
5. Test: print(average(10, 20, 30))  # 20.0""",
                "starter": "# Write your functions below\n\n",
                "solution": "def is_larger(a, b):\n    return a > b\n\nprint(is_larger(10, 5))\nprint(is_larger(3, 8))\n\ndef average(a, b, c):\n    return (a + b + c) / 3\n\nprint(average(10, 20, 30))\n",
            },
        ],
    },
    {
        "num": "4",
        "name": "Booleans-and-Conditionals",
        "display_name": "Booleans and Conditionals",
        "exercises": [
            {
                "id": "4.1", "title": "Boolean Values",
                "objectives": "Understand that Boolean variables can only be True or False.",
                "task": """Boolean variables can only be True or False.
They often come from comparisons like 5 < 10.

Examples:
is_adult = True
is_weekend = False
print(5 < 10)      # prints True
print(10 == 10)    # prints True

Your Task:
1. Create a variable 'is_sunny' set to True and print it
2. Create a variable 'is_hot' set to temperature > 30 where temperature = 35. Print it.
3. Check if 100 is greater than 50. Store in 'check' and print it.
4. Check if 7 * 3 equals 21.""",
                "starter": "# Write your code below\n\n",
                "solution": "is_sunny = True\nprint(is_sunny)\n\ntemperature = 35\nis_hot = temperature > 30\nprint(is_hot)\n\ncheck = 100 > 50\nprint(check)\n\nresult = 7 * 3 == 21\nprint(result)\n",
            },
            {
                "id": "4.2", "title": "Comparison Operators",
                "objectives": "Learn the comparison operators: ==, !=, <, <=, >, >=",
                "task": """Comparison operators:
- ==  equal
- !=  not equal
- <   less than
- <=  less than or equal
- >   greater than
- >=  greater than or equal

IMPORTANT: = is assignment, == is comparison!

Your Task:
1. Print whether 7 * 3 equals 21
2. Print whether 10 / 2 does NOT equal 5
3. Print whether 2**10 is greater than 100
4. Print whether 100 % 7 equals 2
5. Create variables a=10, b=5, then print whether a > b""",
                "starter": "# Write your print statements below\n\n",
                "solution": "print(7 * 3 == 21)\nprint(10 / 2 != 5)\nprint(2**10 > 100)\nprint(100 % 7 == 2)\n\na = 10\nb = 5\nprint(a > b)\n",
            },
            {
                "id": "4.3", "title": "If Statements",
                "objectives": "Learn to use 'if' to run code only when a condition is True.",
                "task": """Use 'if' to run code only when a condition is True.
The code inside 'if' must be indented.

Example:
age = 25
if age > 18:
    print("You are an adult")

Your Task:
1. Create a variable 'score' with value 75
2. Write an if statement that prints "Pass!" if score >= 50
3. Create a variable 'temperature' with value 30
4. Write an if statement that prints "Hot!" if temperature > 25""",
                "starter": "# Write your code below\n\n",
                "solution": "score = 75\nif score >= 50:\n    print(\"Pass!\")\n\ntemperature = 30\nif temperature > 25:\n    print(\"Hot!\")\n",
            },
            {
                "id": "4.4", "title": "If-Else Statements",
                "objectives": "Use 'else' to specify what happens when the 'if' condition is False.",
                "task": """Use 'else' to specify what happens when the 'if' condition is False.
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
6. Test: print(is_even(7))  # Odd""",
                "starter": "# Write your functions below\n\n",
                "solution": "def check_pass(score):\n    if score >= 50:\n        return \"Pass\"\n    else:\n        return \"Fail\"\n\nprint(check_pass(75))\nprint(check_pass(30))\n\ndef is_even(num):\n    if num % 2 == 0:\n        return \"Even\"\n    else:\n        return \"Odd\"\n\nprint(is_even(4))\nprint(is_even(7))\n",
            },
            {
                "id": "4.5", "title": "If-Elif-Else Chains",
                "objectives": "Use 'elif' for multiple conditions checked in order.",
                "task": """Use 'elif' for multiple conditions. Python checks them in order.
Only the first True branch runs.

Example:
def get_grade(score):
    if score >= 90:
        return \"A\"
    elif score >= 80:
        return \"B\"
    elif score >= 70:
        return \"C\"
    else:
        return \"F\"

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
4. Test with 15, 10, 3""",
                "starter": "# Write your functions below\n\n",
                "solution": "def temperature_message(degrees):\n    if degrees < 10:\n        return \"Cold\"\n    elif degrees <= 25:\n        return \"Nice\"\n    else:\n        return \"Hot\"\n\nprint(temperature_message(5))\nprint(temperature_message(18))\nprint(temperature_message(30))\n\ndef size_of_number(num):\n    if num > 10:\n        return \"Big\"\n    elif num == 10:\n        return \"Medium\"\n    else:\n        return \"Small\"\n\nprint(size_of_number(15))\nprint(size_of_number(10))\nprint(size_of_number(3))\n",
            },
        ],
    },
    {
        "num": "5",
        "name": "Modular-Thinking-and-Libraries",
        "display_name": "Modular Thinking and Libraries",
        "exercises": [
            {
                "id": "5.1", "title": "Importing Modules",
                "objectives": "Learn to import and use Python library modules.",
                "task": """Use 'import' to bring library modules into your code.
Then use the module name followed by a dot to access its functions.

Example:
import math
print(math.sqrt(64))     # 8.0
print(math.floor(3.7))   # 3
print(math.ceil(3.2))    # 4

Your Task:
1. Import the math module
2. Use math.sqrt(144) and print the result
3. Use math.floor(9.9) and print the result
4. Use math.ceil(2.1) and print the result
5. Use math.pow(2, 8) to calculate 2 to the power of 8""",
                "starter": "# Write your code below\n\n",
                "solution": "import math\n\nprint(math.sqrt(144))\nprint(math.floor(9.9))\nprint(math.ceil(2.1))\nprint(math.pow(2, 8))\n",
            },
            {
                "id": "5.2", "title": "The Random Module",
                "objectives": "Use the random module to generate random numbers.",
                "task": """The random module lets you generate random numbers.

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
5. Simulate a coin flip: random.randint(0, 1) where 0=Heads, 1=Tails""",
                "starter": "# Write your code below\n\n",
                "solution": 'import random\n\nprint(random.randint(1, 100))\nprint(random.choice(["Rock", "Paper", "Scissors"]))\nprint(random.random())\n\ncoin = random.randint(0, 1)\nif coin == 0:\n    print("Heads")\nelse:\n    print("Tails")\n',
            },
            {
                "id": "5.3", "title": "Using Multiple Modules",
                "objectives": "Learn to import and use more than one module.",
                "task": """You can import more than one module. Each keeps its functions separate.

Examples:
import math
import random

print(math.sqrt(16))
print(random.randint(1, 10))

Your Task:
1. Import both math and random
2. Use math.floor() and random.random() together
3. Generate a random integer from 1-6, then use math.sqrt() on it""",
                "starter": "# Write your code below\n\n",
                "solution": "import math\nimport random\n\nprint(math.floor(random.random() * 10))\n\ndice = random.randint(1, 6)\nprint(math.sqrt(dice))\n",
            },
            {
                "id": "5.4", "title": "Creating Your Own Module",
                "objectives": "Learn that a module is just a Python file, and create your own.",
                "task": """A module is just a Python file. Creating your own module is easy!

Step 1: Create a file called 'operations.py' with:
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

Step 2: In this file (student.py), write:
import operations
result = operations.add(5, 3)
print(result)
result = operations.multiply(4, 7)
print(result)

Your Task:
1. Create the operations.py file with add and multiply functions
2. Import it in this file and test both functions""",
                "starter": "# Create operations.py first!\n\nimport operations\n\nprint(operations.add(5, 3))\nprint(operations.multiply(4, 7))\n",
                "solution": "# operations.py should contain:\ndef add(a, b):\n    return a + b\n\ndef multiply(a, b):\n    return a * b\n\n# student.py should contain:\nimport operations\nprint(operations.add(5, 3))\nprint(operations.multiply(4, 7))\n",
            },
            {
                "id": "5.5", "title": "Using Your Module in a Program",
                "objectives": "Build a simple program using your own module.",
                "task": """Now that you have a module, let's use it to build something!

Your module 'operations.py' should already have:
- add(a, b)
- multiply(a, b)

Your Task:
1. Use multiply() to calculate the area of a rectangle (width=8, height=5)
2. Print "Area: [result]"
3. Use add() and multiply() together to calculate the perimeter
4. Add a new function to operations.py: def square(n): return n * n
5. Import and test it here: print(operations.square(7))""",
                "starter": "# Write your code below\n\n",
                "solution": "import operations\n\narea = operations.multiply(8, 5)\nprint(\"Area: \" + str(area))\n\nperimeter = operations.add(operations.multiply(2, 8), operations.multiply(2, 5))\nprint(\"Perimeter: \" + str(perimeter))\n\nprint(operations.square(7))\n",
            },
        ],
    },
    {
        "num": "6",
        "name": "While-Loops",
        "display_name": "While Loops",
        "exercises": [
            {
                "id": "6.1", "title": "Basic While Loops",
                "objectives": "Learn to use while loops to repeat code.",
                "task": """A while loop repeats as long as its condition is True.
Be careful - an infinite loop never ends!

Example:
count = 0
while count < 5:
    print(count)
    count = count + 1

Output: 0, 1, 2, 3, 4

Your Task:
1. Write a while loop that prints numbers 0, 1, 2, 3, 4
2. Write a while loop that prints numbers 1 to 5
3. Write a while loop that prints "Hello" 3 times
4. CHALLENGE: Count down from 5 to 1, then print "Blast off!\"""",
                "starter": "# Write your while loops below\n\n",
                "solution": "count = 0\nwhile count < 5:\n    print(count)\n    count = count + 1\n\ncount = 1\nwhile count <= 5:\n    print(count)\n    count = count + 1\n\ncount = 0\nwhile count < 3:\n    print(\"Hello\")\n    count = count + 1\n\ncount = 5\nwhile count > 0:\n    print(count)\n    count = count - 1\nprint(\"Blast off!\")\n",
            },
            {
                "id": "6.2", "title": "While Loop Conditions",
                "objectives": "Use more complex conditions with and, or, not.",
                "task": """You can put more complex conditions in a while loop.

Examples:
while num > 0 and num % 3 != 0:
while count < 10 or found == False:

Your Task:
1. Start at 0, add 2 each time, stop when it reaches or exceeds 10
   (print: 0, 2, 4, 6, 8)
2. Start at 20, subtract 3 each time, stop when <= 0
   (print: 20, 17, 14, 11, 8, 5, 2)
3. Start at 1, double each time, stop when > 100""",
                "starter": "# Write your while loops below\n\n",
                "solution": "num = 0\nwhile num < 10:\n    print(num)\n    num = num + 2\n\nnum = 20\nwhile num > 0:\n    print(num)\n    num = num - 3\n\nnum = 1\nwhile num <= 100:\n    print(num)\n    num = num * 2\n",
            },
            {
                "id": "6.3", "title": "While Loops with If Inside",
                "objectives": "Combine while loops with if statements inside.",
                "task": """You can add if statements inside while loops.

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
3. Start at 10, divide by 2 each time until <= 1. Print each value.""",
                "starter": "# Write your code below\n\n",
                "solution": "count = 1\nwhile count <= 5:\n    if count > 3:\n        print(\"Big\")\n    else:\n        print(count)\n    count = count + 1\n\ncount = 0\nwhile count <= 10:\n    if count % 3 == 0:\n        print(\"Fizz\")\n    else:\n        print(count)\n    count = count + 1\n\nnum = 10\nwhile num > 1:\n    print(num)\n    num = num // 2\n",
            },
            {
                "id": "6.4", "title": "While Loops with Input",
                "objectives": "Use while loops to keep asking for input until valid data is entered.",
                "task": """While loops are useful for repeatedly asking for input until valid.

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
- Returns the valid answer""",
                "starter": "# Write your function below\n\n",
                "solution": 'def get_yes_or_no():\n    answer = input(\'Type "yes" or "no": \')\n    while answer != "yes" and answer != "no":\n        print("Invalid. Try again.")\n        answer = input(\'Type "yes" or "no": \')\n    return answer\n',
            },
            {
                "id": "6.5", "title": "Break and Continue",
                "objectives": "Use 'break' to exit a loop early, 'continue' to skip iterations.",
                "task": """Use 'break' to exit a loop early.
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
3. Count from 0 to 10, print only even numbers""",
                "starter": "# Write your code below\n\n",
                "solution": "count = 0\nwhile count <= 10:\n    if count == 7:\n        break\n    print(count)\n    count = count + 1\n\ncount = 0\nwhile count < 5:\n    count = count + 1\n    if count == 3:\n        continue\n    print(count)\n\ncount = 0\nwhile count <= 10:\n    count = count + 1\n    if count % 2 != 0:\n        continue\n    print(count)\n",
            },
        ],
    },
    {
        "num": "7",
        "name": "For-Loops",
        "display_name": "For Loops",
        "exercises": [
            {
                "id": "7.1", "title": "Basic For Loops with Range",
                "objectives": "Use 'for' with 'range(start, end)' when you know how many times to loop.",
                "task": """Use 'for' with 'range' when you know how many times to loop.
range(start, end) gives numbers from start to end-1.

Examples:
for count in range(0, 5):   # 0, 1, 2, 3, 4
    print(count)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

Your Task:
1. Use a for loop to print numbers 0 through 4
2. Use a for loop to print numbers 10 through 14
3. Use a for loop to print "Python" 3 times
4. Use a for loop to print the first 5 multiples of 2: 2, 4, 6, 8, 10""",
                "starter": "# Write your for loops below\n\n",
                "solution": "for i in range(0, 5):\n    print(i)\n\nfor i in range(10, 15):\n    print(i)\n\nfor i in range(3):\n    print(\"Python\")\n\nfor i in range(1, 6):\n    print(i * 2)\n",
            },
            {
                "id": "7.2", "title": "For Loops with Lists",
                "objectives": "Use a for loop to iterate over items in a list.",
                "task": """Use a for loop to go through each item in a list.

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
3. Use range and len to print index and value of ['A', 'B', 'C', 'D'].""",
                "starter": "# Write your code below\n\n",
                "solution": "animals = ['cat', 'dog', 'mouse', 'rabbit']\nfor animal in animals:\n    print(animal)\n\nnumbers = [2, 4, 6, 8, 10]\nfor num in numbers:\n    print(num * 3)\n\nletters = ['A', 'B', 'C', 'D']\nfor i in range(len(letters)):\n    print(str(i) + \": \" + letters[i])\n",
            },
            {
                "id": "7.3", "title": "For Loops with Conditionals",
                "objectives": "Add if statements inside for loops to filter or count.",
                "task": """Add if statements inside for loops to filter or count.

Example:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for num in numbers:
    if num > 5:
        count = count + 1

Your Task:
1. Given list [3, 7, 2, 8, 4, 9, 1, 5], find and print the largest number (don't use max()!)
2. Count how many even numbers are in the same list. Print the count.
3. Print only numbers > 4 from [1, 5, 3, 8, 2, 9, 4].""",
                "starter": "# Write your code below\n\n",
                "solution": "numbers = [3, 7, 2, 8, 4, 9, 1, 5]\nlargest = numbers[0]\nfor num in numbers:\n    if num > largest:\n        largest = num\nprint(largest)\n\neven_count = 0\nfor num in numbers:\n    if num % 2 == 0:\n        even_count = even_count + 1\nprint(even_count)\n\nfor num in [1, 5, 3, 8, 2, 9, 4]:\n    if num > 4:\n        print(num)\n",
            },
            {
                "id": "7.4", "title": "Accumulator Pattern",
                "objectives": "Use a variable outside the loop to accumulate a result.",
                "task": """Use a variable outside the loop to accumulate a result.

Example:
total = 0
for num in [1, 2, 3, 4, 5]:
    total = total + num
print("Sum: " + str(total))

Your Task:
1. Calculate the sum of [5, 10, 15, 20, 25]. Print the result.
2. Calculate the product (multiply) of [1, 2, 3, 4, 5]. Print the result.
3. Count how many items in [3, 7, 2, 8, 4, 9, 1, 5] are greater than 5. Print the count.
4. Calculate the average of [10, 20, 30, 40, 50].""",
                "starter": "# Write your code below\n\n",
                "solution": "total = 0\nfor num in [5, 10, 15, 20, 25]:\n    total = total + num\nprint(total)\n\nproduct = 1\nfor num in [1, 2, 3, 4, 5]:\n    product = product * num\nprint(product)\n\ncount = 0\nfor num in [3, 7, 2, 8, 4, 9, 1, 5]:\n    if num > 5:\n        count = count + 1\nprint(count)\n\ntotal = 0\nfor num in [10, 20, 30, 40, 50]:\n    total = total + num\naverage = total / 5\nprint(average)\n",
            },
            {
                "id": "7.5", "title": "Nested For Loops",
                "objectives": "Put one for loop inside another.",
                "task": """Put one for loop inside another. The inner loop runs completely for each iteration of the outer loop.

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
   ***""",
                "starter": "# Write your code below\n\n",
                "solution": "for row in range(3):\n    for col in range(3):\n        print(str(col), end=\" \")\n    print()\n\nfor row in range(2):\n    for col in range(4):\n        print(str(row) + \"-\" + str(col), end=\" \")\n    print()\n\nfor row in range(1, 4):\n    stars = \"\"\n    for col in range(row):\n        stars = stars + \"*\"\n    print(stars)\n",
            },
        ],
    },
    {
        "num": "8",
        "name": "Strings",
        "display_name": "Strings",
        "exercises": [
            {
                "id": "8.1", "title": "String Basics",
                "objectives": "Learn that strings are sequences of characters enclosed in quotes.",
                "task": """Strings are sequences of characters enclosed in quotes.
You can use single or double quotes.

Examples:
name = "Mika"
greeting = 'Hello ' + name   # concatenation
line = "-" * 10              # multiplication (repeats)

Your Task:
1. Create a variable 'first_name' with your first name
2. Create a variable 'last_name' with your last name
3. Concatenate them with a space and print
4. Create a line of 20 equals signs and print it
5. Create 'Python' and print it 3 times using multiplication""",
                "starter": "# Write your code below\n\n",
                "solution": 'first_name = "Mika"\nlast_name = "Tanaka"\nfull_name = first_name + " " + last_name\nprint(full_name)\n\nline = "=" * 20\nprint(line)\n\nword = "Python"\nprint(word * 3)\n',
            },
            {
                "id": "8.2", "title": "String Methods",
                "objectives": "Learn to use string methods like .upper(), .lower(), .len(), .count(), .isdigit().",
                "task": """Strings have built-in methods you call with a dot.

Examples:
text = "Hello World"
print(text.upper())       # HELLO WORLD
print(text.count("l"))    # 3
print(len(text))          # 11
print("123".isdigit())    # True

Your Task:
1. Create 'Python Programming' and use .upper(). Print.
2. Use .count('m') on 'mammoth'. Print.
3. Create 'hello' and use .capitalize() to get 'Hello'. Print.
4. Use len() on "Computer Science". Print.
5. Check if "12345" is a digit. Print.""",
                "starter": "# Write your code below\n\n",
                "solution": 'print("Python Programming".upper())\nprint("mammoth".count("m"))\nprint("hello".capitalize())\nprint(len("Computer Science"))\nprint("12345".isdigit())\n',
            },
            {
                "id": "8.3", "title": "String Slicing",
                "objectives": "Access parts of a string using indices and slicing.",
                "task": """Access parts of a string using indices in square brackets.
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
4. Given 'Hello World', print 'World' using slicing.""",
                "starter": "# Write your code below\n\n",
                "solution": 'print("Computer"[:4])\nprint("Programming"[3:])\nprint("Python"[2])\nprint("Hello World"[6:])\n',
            },
            {
                "id": "8.4", "title": "String Immutability",
                "objectives": "Understand that strings cannot be changed after creation.",
                "task": """Strings cannot be changed after creation (immutable).
Any operation that seems to modify actually creates a new string.

Example:
name = "Mika"
# name[0] = "m"  # This would cause an error!
name = name.lower()  # Creates new string

Your Task:
1. Start with 'ABC' and use .lower() to get 'abc'. Print.
2. Start with 'Hi' and concatenate to get 'Hi There!'. Print.
3. Start with 'Python' and use slicing + concatenation to get 'python'.
4. Create your name, convert to uppercase, then back to lowercase.""",
                "starter": "# Write your code below\n\n",
                "solution": 'print("ABC".lower())\n\ngreeting = "Hi"\ngreeting += " There!\"\nprint(greeting)\n\nword = "Python"\nword = word[0].lower() + word[1:]\nprint(word)\n\nname = "Mika"\nname = name.upper()\nprint(name)\nname = name.lower()\nprint(name)\n',
            },
            {
                "id": "8.5", "title": "String Practice",
                "objectives": "Put together string methods, slicing, and concatenation.",
                "task": """Practice combining string methods, slicing, and concatenation.

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
4. CHALLENGE: Given 'ABC123DEF', extract just the numeric part using slicing.""",
                "starter": "# Write your code below\n\n",
                "solution": 'email = "student@school.com"\nat_index = email.find("@")\nprint(email[:at_index])\n\nfilename = "test.txt"\nprint(filename.endswith(".py"))\n\ntext = "Hello World"\ntext = text.replace("World", "Python")\nprint(text)\n\ncode = "ABC123DEF"\nstart = end = 0\nfor i in range(len(code)):\n    if code[i].isdigit():\n        if start == 0:\n            start = i\n    elif start > 0:\n        end = i\n        break\nprint(code[start:end])\n',
            },
        ],
    },
]


def slug(ex_id):
    return ex_id.replace(".", "_")


def make_readme(ex_id, title, objectives, task, starter):
    lines = [
        "# Exercise " + ex_id + ": " + title,
        "",
        "## Objectives",
        objectives,
        "",
        "## Task",
        task,
        "",
        "## Starter Code",
        "```python",
        starter,
        "```",
        "",
        "## Running Your Code",
        "1. Write your code in student.py",
        "2. Run it with: python student.py",
        "3. Check your output",
        "",
        "## Tests",
        "Run: pytest tests/" + ex_id + "/test_" + slug(ex_id) + ".py -v",
    ]
    return "\n".join(lines)


def make_test(ex_id, lesson_num, lesson_name):
    s = slug(ex_id)
    content = (
        'import pytest\n'
        'import os\n'
        '\n'
        'def test_' + s + '_exists():\n'
        '    """Test that student.py exists"""\n'
        '    path = "exercises/' + lesson_num + '-' + lesson_name + '/' + ex_id + '/student.py"\n'
        '    assert os.path.exists(path), "student.py not found"\n'
        '\n'
        'def test_' + s + '_syntax():\n'
        '    """Test that student.py has valid Python syntax"""\n'
        '    path = "exercises/' + lesson_num + '-' + lesson_name + '/' + ex_id + '/student.py"\n'
        '    with open(path) as f:\n'
        '        code = f.read()\n'
        '    compile(code, "<student.py>", "exec")\n'
        '\n'
        'def test_' + s + '_runs():\n'
        '    """Test that student.py can execute without error"""\n'
        '    path = "exercises/' + lesson_num + '-' + lesson_name + '/' + ex_id + '/student.py"\n'
        '    with open(path) as f:\n'
        '        code = f.read()\n'
        '    try:\n'
        '        exec(code, {"__name__": "__main__"})\n'
        '    except Exception as e:\n'
        '        pytest.fail("Error running student.py: " + str(e))\n'
    )
    return content


# Generate all
for lesson in LESSONS:
    lesson_num = lesson["num"]
    lesson_name = lesson["name"]
    folder = base + "/exercises/" + lesson_name

    for ex in lesson["exercises"]:
        ex_id = ex["id"]
        ex_folder = folder + "/" + ex_id
        os.makedirs(ex_folder, exist_ok=True)
        os.makedirs(base + "/teacher/markscheme/" + ex_id, exist_ok=True)
        os.makedirs(base + "/tests/" + ex_id, exist_ok=True)

        # README
        readme_content = make_readme(ex_id, ex["title"], ex["objectives"], ex["task"], ex["starter"])
        with open(ex_folder + "/README.md", "w") as f:
            f.write(readme_content)

        # Student starter
        with open(ex_folder + "/student.py", "w") as f:
            f.write(ex["starter"])

        # Teacher solution
        with open(base + "/teacher/markscheme/" + ex_id + "/solution.py", "w") as f:
            f.write(ex["solution"])

        # Test
        test_content = make_test(ex_id, lesson_num, lesson_name)
        with open(base + "/tests/" + ex_id + "/test_" + slug(ex_id) + ".py", "w") as f:
            f.write(test_content)

    print("Lesson " + lesson_num + ": " + lesson["display_name"] + " (" + str(len(lesson["exercises"])) + " exercises)")

total = sum(len(l["exercises"]) for l in LESSONS)
print("\nTotal: " + str(len(LESSONS)) + " lessons, " + str(total) + " exercises created!")
print("Repo: " + base)