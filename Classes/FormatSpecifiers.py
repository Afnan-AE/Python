p1, p2, p3 = 49.99, -5998.456, 101.10

#decimel precision
print(f"Price of this game is {p1:.1f}")
print(f"Price of this game is {p2:.1f}")
print(f"Price of this game is {p3:.1f}")

#padding
print(f"{p1:10}")
print(f"{p2:010}")
print(f"{p3:10}")

#justify
print(f"{p1:<10}")
print(f"{p1:>10}")
print(f"{p3:^10}")

#ps&neg
print(f"{p1:+}")
print(f"{p2: }")
print(f"{p3: }")

#thousand sperator(comma)

p4,p5 = 1000.45, 2600.34

print(f"Nice {p4:,}")
print(f"Nice {p5:,}")

#mixing these

print(f"Price of this game: {p1:+.1f}")
print(f"Price of this game: {p4:+,.1f}")
print(f"You are in debt of: {p2:+,.1f}")