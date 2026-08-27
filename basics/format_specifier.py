price1 = 2.12343
price2 = -38433.2422245
price3 = 1230330.43439

# print(f"Price1 is ${price1: .2f}") #.2f for precision specifier
# print(f"Price2 is ${price2: .2f}") #additional 0 added if .3f used at last
# print(f"Price3 is ${price3: .2f}")

# + used for sign specifier
# , used for comma at thousands
# < used for left justified
# > used for right justified

# print(f"Price1 is ${price1:+}") #.2f for precision specifier
# print(f"Price2 is ${price2:+}") #additional 0 added if .3f used at last
# print(f"Price3 is ${price3:+}")

# print(f"Price1 is ${price1:+,}") #.2f for precision specifier
# print(f"Price2 is ${price2:+,}") #additional 0 added if .3f used at last
# print(f"Price3 is ${price3:+,}")

# print(f"Price1 is ${price1:+,.2f}") #.2f for precision specifier
# print(f"Price2 is ${price2:+,.2f}") #additional 0 added if .3f used at last
# print(f"Price3 is ${price3:+,.2f}")

# print(f"Price1 is ${price1:10}") #.2f for precision specifier
# print(f"Price2 is ${price2:10}") #additional 0 added if .3f used at last
# print(f"Price3 is ${price3:10}")

#in price1:10 now each space have 10 values for the output

#if price1:010 now each number is 0 is padded 

# print(f"Price1 is ${price1:010}") #.2f for precision specifier
# print(f"Price2 is ${price2:010}") #additional 0 added if .3f used at last
# print(f"Price3 is ${price3:010}")

# print(f"Price1 is ${price1:>10}") #.2f for precision specifier
# print(f"Price2 is ${price2:>10}") #additional 0 added if .3f used at last
# print(f"Price3 is ${price3:>10}")

# print(f"Price1 is ${price1:<10}") #.2f for precision specifier
# print(f"Price2 is ${price2:<10}") #additional 0 added if .3f used at last
# print(f"Price3 is ${price3:<10}")

# now for center justified use ^ symbol

print(f"Price1 is ${price1:^10}") #.2f for precision specifier
print(f"Price2 is ${price2:^10}") #additional 0 added if .3f used at last
print(f"Price3 is ${price3:^10}")













