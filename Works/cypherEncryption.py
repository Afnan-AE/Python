import random
import string

char = string.ascii_letters + string.digits + string.punctuation
chars = list(char)

key = chars.copy()

random.shuffle(key)

print(chars)
print(key)

m = input("Message: ")
et = ""
idn = 0
for i in m:
    idn = chars.index(i)
    et += key[idn]
print(f"Normal Message : {m}")
print(f"Encrypted Message: {et}")

et = input("Encrypted Message: ")
m = ""
for j in et:
    idn = key.index(j)
    m += chars[idn]

print(f"Encrypted Message: {et}")
print(f"Decrypted Message: {m}")