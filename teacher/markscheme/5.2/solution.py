import random

print(random.randint(1, 100))
print(random.choice(["Rock", "Paper", "Scissors"]))
print(random.random())

coin = random.randint(0, 1)
if coin == 0:
    print("Heads")
else:
    print("Tails")
