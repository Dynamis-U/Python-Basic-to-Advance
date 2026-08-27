# modules = a file containing code you want to include in your program
#           use 'import to include a module (built-in or your own)'
#           useful to break up a large program resusable separate files

# print(help("modules")) #all modules 

# print(help("math")) # about all function and variable available in this module

# import math as m
# from math import e
# a, b, c, d, e = 1, 2, 3, 4, 5

# print(e ** a)  # it takes the new declared value of e not the imported one
# print(e ** b)
# print(e ** c)
# print(e ** d)
# print(e ** e)

# # to use imported one you can import it like this

# print(m.e ** e)
# print(m.e ** m.e)



# I have create a folder as module name example and im gonna import it and use its function

import example

# result = example.pi
# print(result)

# result = example.square(3)
# print(result)

# result = example.cube(3)
# print(result)

# result = example.circumfernce(3)
# print(result)

result = example.area(3)
print(result)