try:
    with open('F:\\Games\\t.txt') as p:
        print(p.read())
except FileNotFoundError:
    print("File not found")
finally:
    print('-'*20)
    print('File Closed')

with open('pyt.txt', 'w') as p:
    pass