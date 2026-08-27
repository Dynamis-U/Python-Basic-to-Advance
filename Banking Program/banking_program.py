# Python Banking Program

def deposit(balance):
    print("******************************")
    amount = float(input("Enter an amount to be deposited: "))
    print("******************************")
    if amount > 0:
        print("*****************************")
        print(f"Deposit of amount {amount:.2f} is successful")
        print("*****************************")
        return amount
    elif amount <= 0:
        print("*****************************")
        print("This is not a valid amount")
        print("*****************************")
        return 0

def withdraw(balance):
    print("*******************************")
    amount = float(input("Enter the amount to be withdrawn: "))
    print("*******************************")
    if amount < balance and amount > 0:
        print("*****************************")
        print(f"Withdrawal of amount {amount:.2f} is successful")
        print("*****************************")
        return amount
    elif amount > balance:
        print("*****************************")
        print("Amount is out of balance")
        print("*****************************")
        return 0

def show_Balance(balance):
    print("*******************************")
    print(f"Your available balance is : {balance:.2f}")
    print("*******************************")


def main():
    is_running = True
    balance = 0
    while is_running:
        print("*****************************")
        print("       Banking Program       ")
        print("*****************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*****************************")

        choice = input("Enter your choice (1-4):")

        if choice == '1':
            show_Balance(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid choice")

    print("*****************************")
    print("Thank you! Have a nice day!")
    print("*****************************")

if __name__ == '__main__':
    main()