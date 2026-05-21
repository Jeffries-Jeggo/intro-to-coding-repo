email = "student@school.com"
at_index = email.find("@")
print(email[:at_index])

filename = "test.txt"
print(filename.endswith(".py"))

text = "Hello World"
text = text.replace("World", "Python")
print(text)

code = "ABC123DEF"
start = end = 0
for i in range(len(code)):
    if code[i].isdigit():
        if start == 0:
            start = i
    elif start > 0:
        end = i
        break
print(code[start:end])
