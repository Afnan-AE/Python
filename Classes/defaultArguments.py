import time

def ti(e, s=0):
    for i in range(s, e+1):
        print(i)
        time.sleep(1)
    print("Done")


ti(10,5)