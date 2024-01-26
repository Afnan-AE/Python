h = 0
y = "Gitoditrium"

for i in range(len(y)):
    print(i, end='')
print()
for j in y:
    print(j, end='')

for x in range(0,11):
    if x == 3:
        continue
    elif h >= 50:
        break
    h += x

    
print()
print(h)