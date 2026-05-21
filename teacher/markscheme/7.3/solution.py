numbers = [3, 7, 2, 8, 4, 9, 1, 5]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)

even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1
print(even_count)

for num in [1, 5, 3, 8, 2, 9, 4]:
    if num > 4:
        print(num)
