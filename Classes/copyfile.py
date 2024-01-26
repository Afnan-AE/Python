#copyfile() =  copies contents of a file
#copy() =      copyfile() + permission mode + destination can be a directory
#copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile('pyt.txt', 'pytcopy.txt')
with open('pytcopy.txt', 'a') as p:
    p.write('\nThis is copy of the previous one')