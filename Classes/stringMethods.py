name = "gitOdiTrium"

print(len(name))
print(name.capitalize())
print(name.isupper())
print(name.islower())
print(name.find('i'))
print(name.rfind('i'))
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count('i'))
print(name.replace('i', 'o'))
#print(help(str))

#exercise

u = input("Username: ")

if len(u) > 12:
    print("Username has to be under 12 characters.")

elif not u.find(' ') == -1:
    print("Username cannot contain spaces.")

elif u.isalpha() == False:
    print("Username can't have numbers.")

else: print(f"Hello {u}")
