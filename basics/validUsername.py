#validate user input excercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("spaces is not allowed")
elif not username.isalpha():
    print("digits are not allowed")
else:
    print(f"Welcome {username}")