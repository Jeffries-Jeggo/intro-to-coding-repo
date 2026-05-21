def check_pass(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"

print(check_pass(75))
print(check_pass(30))

def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(4))
print(is_even(7))
