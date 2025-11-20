# Assignment question 4
inches = float(input("Enter measurement in inches: "))
feet = inches / 12
yards = inches / 36
centimeters = inches * 2.54
meters = inches / 39.37
print(f"{inches} inches is equal to:")
print(f"{feet:.2f} feet")
print(f"{yards:.2f} yards")
print(f"{centimeters:.2f} centimeters")
print(f"{meters:.2f} meters")
