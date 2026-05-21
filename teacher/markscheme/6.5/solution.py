count = 0
while count <= 10:
    if count == 7:
        break
    print(count)
    count = count + 1

count = 0
while count < 5:
    count = count + 1
    if count == 3:
        continue
    print(count)

count = 0
while count <= 10:
    count = count + 1
    if count % 2 != 0:
        continue
    print(count)
