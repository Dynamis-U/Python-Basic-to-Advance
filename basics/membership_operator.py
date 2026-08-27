#Membership operators = used to test whether a value or variable is found in a secquence (string, list, tuple, set, or dictionary)
# (list , tuple, set behave similarily with membership operator)
# 1. in
# 2. not in

# word = "apple"

# letter = input("Guess a letter in the secret word: ")


# in operator 
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# # not in operator 
# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")


# set

# students = {"Spongebob", "Patrick", "Sandy"}

# student = input("Enter the name of the student: ")

# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")

# dictionary

# grades = {"Sandy": "A",
#           "Squidward": "B",
#           "Spongebob": "C",
#           "Patrick": "D"}

# student = input("Enter the name of a student:").capitalize()

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

# Email Validation

email = input("Enter the Valid EmailID:")

if "." in email and "@" in email:
    print(f"{email} is Vaild")
else:
    print(f"{email} is Invalid")



