o = input("Operator(* + / -): ")

n = float(input("Number 1: "))
m = float(input("Number 2: "))

if o == "+": print(f"Answer: {round(n+m), 3}")
elif o == "-": print(f"Answer: {round(n-m) ,3}")
elif o == "*": print(f"Answer: {round(n*m), 3}")
elif o == "/": print(f"Answer: {round(n/m), 3}")
else: print("Invalid operator, operation terminated.")