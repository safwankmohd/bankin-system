import re

class User_Account:   #database of user account
    accounts = {"manu":{'username':'manu','password':'manu123','balance':6000}}

class BankingSystem:
    def __init__(self):
        self.balance = 0
        self.username = None
        self.password = None

        print("Welcome To Online Banking.....\n"
              "Press 1 to login to account.\n"
              "Press 2 for create a new account.\n"
              "Press 3 for exit.")
        n1 = int(input('Enter your choice: '))

        if n1 == 1:
            self.login()
        elif n1 == 2:
            self.create_account()
            self.login()
        elif n1 == 3:
            print("Thank you for using our banking system.....")
            exit()
        else:
            print("ERROR.. Enter the correct Option")
            self.__init__()

    def login(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your Password: ")

        if self.username in User_Account.accounts and User_Account.accounts[self.username]["password"] == self.password:
            print("Login successful.")
            self.balance = User_Account.accounts[self.username]["balance"]
            self.banking_interface()
        else:
            print("Incorrect username or password. Try again...!!")
            self.__init__()

    def banking_interface(self):
        print(f"HELLO {self.username} WELCOME TO NET BANKING...\n"
              f"Press 1 for Deposit\n"
              f"Press 2 for Withdraw\n"
              f"Press 3 for Balance\n"
              f"Press 4 for Exit")
        n2 = int(input('Enter your choice: '))
        if n2 == 1:
            self.deposit()
        elif n2 == 2:
            self.withdraw()
        elif n2 == 3:
            self.balance_info()
        elif n2 == 4:
            print("Thank you for using our banking system.....")
            exit()
        else:
            print('Please enter a valid number...')
            self.banking_interface()

    def deposit(self):
        deposit_amount = float(input("Enter the amount to deposit: "))
        if deposit_amount > 0:
            self.balance += deposit_amount
            User_Account.accounts[self.username]["balance"] = self.balance
            print(f"Deposited Rs.{deposit_amount}. New balance: Rs.{self.balance}")
        else:
            print("Invalid deposit amount.")
        self.banking_interface()

    def withdraw(self):
        withdrawal_amount = float(input("Enter the amount to withdraw: "))
        if 0 < withdrawal_amount <= self.balance:
            self.balance -= withdrawal_amount
            User_Account.accounts[self.username]["balance"] = self.balance
            print(f"Withdrawn Rs.{withdrawal_amount}. New balance: Rs.{self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
        self.banking_interface()

    def balance_info(self):
        print(f"Current balance is Rs.{self.balance}")
        self.banking_interface()

    def create_account(self):
        print("REGISTRATION")
        user_name = input("Enter username: ")
        email = input("Enter email id: ")
        phone_number = input("Enter phone number: ")
        password = input("Enter the password: ")
        confirm_password = input("Confirm password: ")

        rule1 = '^[A-Za-z\s]+'
        match1 = re.fullmatch(rule1, user_name)
        if not match1:
            print("Please enter a valid username")
            return self.create_account()

        rule2 = "([a-z][0-9_.-]+|[a-z_.-]+|[0-9]+[a-z_.-]+)@gmail.com"
        match2 = re.fullmatch(rule2, email)
        if not match2:
            print("Please enter a valid email")
            return self.create_account()

        rule3 = "[0-9]{10}"
        match3 = re.fullmatch(rule3, phone_number)
        if not match3:
            print("Please enter a valid phone number")
            return self.create_account()

        rule4 = "[A-Za-z0-9._\-]{8,12}"
        match4 = re.fullmatch(rule4, password)
        if not match4:
            print('Please enter a valid password')
            return self.create_account()

        rule5 = "[A-Za-z0-9._\-]{8,12}"
        match5 = re.fullmatch(rule5, confirm_password)
        if not match5:
            print('Please enter a valid password')
            return self.create_account()

        if password == confirm_password:
            User_Account.accounts[user_name] = {
                "password": password,
                "balance": 0
            }
            print("Registration success")
            print("Re-login to your account")
        else:
            print("Registration failed")
            print("Enter the correct password")
            self.create_account()

# Create an instance of the BankingSystem class
bank = BankingSystem()

# Initialize the program
bank.__init__()

# Display the initial balance
bank.balance_info()
