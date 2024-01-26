w = float(input("Weight: "))
u = input('Unit(kg / L): ')

if u == 'kg':print(f"Weight is {round(w*2.205, 3)} lbs")
elif u == 'L': print(f"Weight is {round(w/2.205, 3)} kgs")
else: print(f"Invalid unit({u})")