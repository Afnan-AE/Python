try:
    x = float(input("Numerator: "))
    y = float(input("Denominator: "))
    r = x/y

except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Please use a number.")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(f"Result: {r:.2f}")
finally:
    print("Thanks")