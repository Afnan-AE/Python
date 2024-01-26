import random

l, h = 1, 10
n = random.randint(l, h)

no = random.random()

print(n)
print(no)

ch = [1, 2, 3, 4]
chs = random.choice(ch)

print(chs)
random.shuffle(ch)

print(ch)

#number guessing game

low = 1
high = 20

n1 = random.randint(low, high)
gu = 0

while True:
    g = int(input("Enter a guess: "))
    gu += 1

    if g < n1:
        print("Too low")
    elif g > n1:
        print("Too high")
    else:
        print(f"{g} is the correct number")
        break

print(f"You needed {gu} guesses to pass this round.")
