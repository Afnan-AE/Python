import os
import shutil

p = 'p.txt'
p1 = 'folder'
p2 = 'folderWfile'

try:
    os.remove(p)
    os.rmdir(p1)
    shutil.rmtree(p2)

except FileNotFoundError:
    print("FILE WAS NOT FOUND")
except PermissionError:
    print("PERMISSION DENIED")
except OSError:
    print("OS ERROR OCCURED")

else:
    print(f"{p} is deleted.\n{p1} is deleted.\n{p2} is deleted")

