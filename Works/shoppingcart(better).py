t = 0
fl = []
c = True

while c == True:
    f = input(f"Enter a food to buy(q to quit): ")
    if f == 'q':
        c = False
        break
    else:
        fl.append(f)
        p = float(input(f"Enter the price of {f}: $"))
        t += p

print("-----YOUR CART-----")
for e in fl:
    print(e, end=" ")
print()
print(f"Your total is: ${t}")
