for x in range(1, 10):
    print(x, end = "")  #to print every x in same line use end = ""

# for newline end = "\n"

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end = "")
    print()

