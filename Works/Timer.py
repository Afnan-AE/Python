
import time

x = int(input("Seconds: "))

for x in range(x, 0, -1):
    time.sleep(1)
    s = x % 60
    m = int(x / 60) % 60
    h = int(x / 3600)
    print(f"{h:02}:{m:02}:{s:02}")

print("TIME'S UP!")