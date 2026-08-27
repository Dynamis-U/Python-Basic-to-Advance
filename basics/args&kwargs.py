# *args     = allows you to pass multiple non-key arguments
#  **kwargs = allows you to pass multiple keyword - arguments
#             *unpacking operator
#             1. positional 2. default 3. keyword 4. ARBITRARY


# 1) POSITIONAL ARGUMENT:

# def add(x , y):
#     return x + y

# print(add(1,3))

# using * for any number of argument

# def add(*args):
#     sum = 0
#     for arg in args:
#         sum += arg
#     return sum

# print(add(1,3,4,2))

# KEYWORD ARGUMENT:

# def print_address(**kwargs):
#     for key, value in  kwargs.items():
#         print(f"{key} : {value}")

# print_address(street = "123 Fake St.",
#               apt = "100",
#               city = "Detroit",
#               state = "MI",
#               zip = "54321")

# *args and **kwargs together

def shipping_label(*args, **kwargs):  # always *args will be before **kwargs
    for arg in args:
        print(arg, end = " ")
    print()

    if 'apt' in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif 'pobox' in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")

    print(f"{kwargs.get('city')} {kwargs.get('State')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
                   street = "123 Fake St.",
                   apt = "#89",
                   pobox = "PO box #1001",
                   city = "Detroit",
                   State = "Dallas",
                   zip = "73822")