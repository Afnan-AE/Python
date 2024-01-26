u = input("Temperature in Celcius or Fahrenheit(C/F): ")
t = float(input("Temperature: "))

if u == 'C': print(f"Temperature in Fahrenheit is {round(((9*t/5)+32),3)} degrees")
elif u == 'F': print(f"Temperature in Celcius is {round(((5*((t-32)/9))),3)} degrees")
else: print("Invalid Input.")