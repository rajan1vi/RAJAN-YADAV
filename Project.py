import random
import sys
class ATM():
    def __init__(self,name,account_number,balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def account_details(self):
        print("\n---------ACCOUNT DETAIL-----------")
        print(f"Account Holder : {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available Balance: Rs.{self.balance}\n")

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Rs.", self.balance)
        print()

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient balance")
            print(f"Your balance is Rs.{self.balance} only")
            print("try with lesser amount than balance")
        else:
            self.balance = self.balance - self.amount
            print(f"Rs.{amount} withdrawal successful!")
            print("Current account balance: Rs.", self.balance)
            print()

    def check_balance(self):
        print("Available balance: Rs.",self.balance)
        print()

    def transaction(self):
        print("""
             TRANSACTION
        ***************************
              Menu:
              1.Account Detail
              2.Check Balance
              3.Deposit
              4.Withdraw
              5.Exit
        ****************************
          """)
        while True:
            try:
                option = int(input("Enter 1,2,3,4 or 5:"))
            except:
                print("Error: Enter 1,2,3,4, or 5 only! \n")
                continue
            else:
                if option == 1:
                    atm.account_details()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Rs.): "))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Rs.): "))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt...........
            *********************************************************
                Transaction is now complete.
                Transaction number: {random.randint(10000 , 10000000)}
                Account holder: {self.name.upper()}
                Account number: {self.account_number}
                Available balance: Rs.{self.balance}
                
                Thanks for choosing us as your bank
            ***********************************************************    
                """)
                    sys.exit()
print("******** WELCOME TO UNION BANK OF INDIA*********")
print("_____________________________________________________________________________________\n")
print("--------------ACCOUNT CREATION------------------")
name = input("Enter your name: ")
account_number = int(input("Enter your account number: "))
print("Congratulations! Account created successfully ")

atm = ATM(name, account_number)
while True:
    trans=input("Do you want to ant transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
        --------------------------------------------------------------
        | THANKS FOR CHOOSING US AS YOUR BANK |
        | VISIT US AGAIN! |
        --------------------------------------------------------------
            """)
        break
    else:
        print("Wrong command!      Enter 'y' for yes and 'n' for NO.\n"  )






