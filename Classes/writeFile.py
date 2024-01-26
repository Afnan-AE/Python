p = 'F:\\Games\\t.txt'

with open(p, 'w') as pa:
    pa.write('HI')

with open(p, 'r') as pa:
    print(pa.read())

with open('pyt.txt', 'w') as pa:
    pa.write("This file is just for test")

