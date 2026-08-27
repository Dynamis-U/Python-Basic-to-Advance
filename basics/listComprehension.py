#List comprehension = A consise way to create lists Python
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

triples = [y * 3 for y in range(1, 11)]

print(triples)

fruits = ["apple", "banana", "coconut", "orange"]

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

# if condition

numbers = [1, -2, 3, -5, -6, 7, 8]

positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if not num & 1]
odd_nums = [num for num in numbers if num & 1]

print(f"Positive numbers : {positive_nums}")
print(f"Negative numbers : {negative_nums}")
print(f"Even number : {even_nums}")
print(f"Odd numbers : {odd_nums}")


