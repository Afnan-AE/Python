cn = "1234-5678-9012-4567"

print(cn[4])
print(cn[:4])
print(cn[5:])
print(cn[-5])
print(cn[4::5])

#exercise

n = input("Card Number: ")
print(f"Card Number: XXXX-XXXX-XXXX-{n[-4:]}")
print(f"Inverse Card Number: {n[::-1]}")