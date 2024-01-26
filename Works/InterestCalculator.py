p = r = t = 0

p = float(input("Principal is positive. Principal Amount: "))
while p <= 0:
    p = float(input("Principal is positive. Principal Amount: "))

r = float(input("Rate is positive. Rate amount: "))
while r < 0:
    r = float(input("Rate is positive. Rate amount: "))

t = int(input("Enter years as a whole: "))
while t <= 0:
    t = int(input("Enter years as a whole: "))

y = p * (pow((1 + r/100), t))
print(f"Balance after {t} years is ${y:+,.2f}")