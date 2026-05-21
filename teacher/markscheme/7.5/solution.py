for row in range(3):
    for col in range(3):
        print(str(col), end=" ")
    print()

for row in range(2):
    for col in range(4):
        print(str(row) + "-" + str(col), end=" ")
    print()

for row in range(1, 4):
    stars = ""
    for col in range(row):
        stars = stars + "*"
    print(stars)
