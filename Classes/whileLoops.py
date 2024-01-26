n = input("Name: ")

while n == "":
    n = input("Name: ")

print(f"Welcome {n}.")

i = int(input("Number(1-10): "))

while i < 1 or i > 10:
    i = input("Number(1-10): ")

print(f"{i} is a good number.")

g = 10;

while not g == 0:
    print(g)
    g -= 1;

print("BOOM!")
