x = input("Credit Card Number: ")
x = x.replace("-",'')
x = x.replace(" ", '')

so = 0
xe = x[::-2]


for i in range(len(xe)):
    so += int(xe[i])

xo = x[-2::-2]

se = 0

for k in range(len(xo)):
    t = int(xo[k])*2
    if t >= 10:
        t1 = t % 10
        t2 = int(t/10)
        t = t1 + t2
        se += t

    elif t < 10:
        se += t

n = so + se

if n % 10 == 0:
    print("VALID")
else:
    print("INVALID")