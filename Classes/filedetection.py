import os

p = "F:\\Games\\t"
p1 = "F:\\Games"
p2 = "F:\\Games\\t.txt"

if os.path.exists(p):
    print("This path exists")
    if os.path.isfile(p):
        print("This is a file")
    elif os.path.isdir(p):
        print("This is a directory")
else:
    print("this path does not exist")

if os.path.isfile(p2):
    print("This is a file")

if os.path.exists(p1):
    print(True)