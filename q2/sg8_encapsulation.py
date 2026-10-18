class BankAccount:
    # creates account number and balance
    def __init__(self, account_number, balance):
        self.__account_Number = account_number  # Stores account number
        self.__balance = balance  # Stores initial balance

    # updates balance if it is not negative
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance  # Updates the balance
        else:
            print("The balance must be not be a negative number.") # Warns user that balance shouldn't be negative

    # gets account number
    @property
    def account_number(self):
        return self.__account_Number

    # gets balance
    @property
    def balance(self):
        return self.__balance


# main function
def main():
    # creates object
    a1 = BankAccount(12345, 1000)

    # displays all account details
    print("Account 1")
    print("Account Number:", a1.account_Number)
    print(f"Balance: {a1.balance:.2f}")

    # updates balance to negative number
    print("\nUpdate balance to -100")
    a1.set_balance(-100)

    # displays account details again
    print("Account Number:", a1.account_number)
    print(f"Balance: {a1.balance:.2f}")


# calls main function
main()
