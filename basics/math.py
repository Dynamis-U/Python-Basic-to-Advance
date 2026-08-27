import math

#x = 3.14
#y = -4
#z = 5

#result = round(x)
#result = abs(y)
#result = pow(4, 3)
#result = max(x, y, z)
#result = min(x,y,z)

#print(result)

#x = 9.1

#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)


#print(result)

radius = float(input("Enter the radius of a circle: "))
circumference = 2*math.pi*radius
area = math.pi * pow(radius, 2)


print(f"The circumference is {round(circumference, 2)}cm" )
print(f"Area of the circle is : {area}cm^2")