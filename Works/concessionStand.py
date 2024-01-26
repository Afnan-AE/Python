it = {'popcorn': 3.99,
      'Soda': 1.99,
      'Burger': 3.99,
      'Chicken Pops(CP)': 4.99,
      'wedges': 3.99 }

a = it.items()

for k,v in a:
    print(f"{k}: ${v}")
print('-'*24)

con = True
f = []
t = 0
while con:
    an = input("Select an item(q to quit): ")
    if an == 'q':
        c = False
        break
    else:
        f.append(an)
        t += float(it.get(an))


print(f"{' YOUR ORDER ':-^24}")
for i in f:
    print(i, end=" ")
print()

print(f"Total is ${t}")
