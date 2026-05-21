def temperature_message(degrees):
    if degrees < 10:
        return "Cold"
    elif degrees <= 25:
        return "Nice"
    else:
        return "Hot"

print(temperature_message(5))
print(temperature_message(18))
print(temperature_message(30))

def size_of_number(num):
    if num > 10:
        return "Big"
    elif num == 10:
        return "Medium"
    else:
        return "Small"

print(size_of_number(15))
print(size_of_number(10))
print(size_of_number(3))
