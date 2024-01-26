from OOP import ar

a1 = ar('UNO R3', 2023, 2)
a2 = ar('UNO R2', 2020, 1)


a2.color = 'BLACK' #class variable changed

print(f'Model:{a1.m} ({a1.y}) | Color: {a1.color} | Port: {a1.p}')
print(f'Model:{a2.m} ({a2.y}) | Color: {a2.color} | Port: {a2.p}')