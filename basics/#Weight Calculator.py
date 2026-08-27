#Weight Calculator

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pound? (K or L):")
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs";
else:
    print("{unit} was not valid")

print(f"Your weight is: {weight} {unit}")
