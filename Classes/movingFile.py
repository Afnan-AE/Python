import os

s = 'pyt.txt'
so = 'pytcopy.txt'

d = "F:\\Games\\pyt.txt"
do = "F:\\Games\\pytcopy.txt"

try:
    if os.path.exists(d):
        print("There is already a file there.")
    else:
        os.replace(s, d)

    if os.path.exists(do):
        print("There is already a file there.")
    else:
        os.replace(so, do)
except FileNotFoundError:
    print("INVALID ATTEMPT")