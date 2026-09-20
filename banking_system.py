def show_menu():
    print('=' * 5 + " Banking System " + '=' * 5)
    print()
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Transfer Money")
    print("6. Transaction History")
    print("7. Delete Account")
    print("8. Exit")

    try:
        choice = int(input("Enter a the operation you want to perform: "))
        if 0 < choice <= 8:
            return choice 
        else:
            print("Enter the choice that is in range (1 - 8)")
    except ValueError:
        print("Invalid choice input! try again")

#Bank class
class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_holder, balance):
        account = self.find_account(account_number)
        if account is None:
            new_account = Account(account_number, account_holder, balance)
            self.accounts.append(new_account)
            print("Account is created")
        else:
            print("Account number already exists. Try with different number.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account_number == account.account_number:
                return account
        return None

    def view_account(self, account_number):
        account = self.find_account(account_number)
        if account is not None:
            print(f"Account no: {account.account_number}")
            print(f"Account holder: {account.account_holder}")
            print(f"Account balance: ₹{account.balance}")
        else:
            print("Account not found.")
            return

    def delete_account(self, account_number):
        account = self.find_account(account_number)
        if account is not None:
            self.accounts.remove(account)
            print("Account has been successfully deleted.")
        else:
            print("Account not found.")
            return



#Account class
class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []
    def deposit(self):
        while True:
            try:
                amount = float(input("Enter the amount you want to deposit:₹ "))
                if amount > 0:  
                    self.balance+= amount
                    self.add_transaction(f"Deposit ₹+{amount}")
                    print("Amount added successfully")
                    return self.balance
                else:
                    print("Amount must be greater than zero.")
            except ValueError:
                print("Invalid input!. Try again.")

    def withdraw(self):
        while True:
            try:
                amount = float(input("Enter the amount you want to withdraw:₹"))
                if amount > 0:
                    if amount <= self.balance:
                        self.balance-= amount
                        self.add_transaction(f"Withdrawn ₹-{amount}")
                        print("Withdraw successfull")
                        print(f"Remaning balance is:₹{self.balance}")
                        return
                    else:
                        print("Balance is not sufficent enough in the account")
                else:
                    print("Amount must be greater than zero")
            except ValueError:
                print("Invalid input!. Try again.")

    def transfer(self, another_account):
        while True:
            try:
                amount = float(input("Enter the amount to transfer:₹ "))
                if amount > 0 and amount <= self.balance:
                    self.balance-= amount
                    another_account.balance+= amount
                    self.add_transaction(f"Transfer: ₹-{amount} to {another_account.account_number}")
                    another_account.add_transaction(f"Transfer ₹+{amount} from {self.account_number}")

                    print(f"Transfer successful. Your remaining balance: ₹{self.balance}")
                    return self.balance
                elif amount > self.balance:
                    print(f"Balance is insufficent. enter amount till your balance {self.balance}")
                else:
                    print("Amount must be greater than zero")
            except ValueError:
                print("Invalid input!, try again")

    def add_transaction(self, transactions):
        self.transactions.append(transactions)

    def view_transactions(self):
        print('=' * 5 + " Transaction History " + '=' * 5)
        for idx, trans in enumerate(self.transactions, start = 1):
            print(f"{idx}. {trans}")



bank = Bank()
while True:
    choice = show_menu()
    if choice == 1:
        while True:
            try:
                account_number = int(input("Enter your account number: "))
                account_holder = input("Enter your name: ").strip()
                balance = 0
                bank.create_account(account_number, account_holder, balance)
                break
            except ValueError:
                print("Invalid input for account no. Try again")

    elif choice == 2:
        while True:
            try:
                account_number = int(input("Enter your account number: "))
                bank.view_account(account_number)
                break
            except ValueError:
                print("Invalid input for account no. Try again")
    elif choice == 3:
        while True:
            try:
                account_number = int(input("Enter your account number: "))
                account = bank.find_account(account_number)
                if account is not None:
                    account.deposit()
                    break
                else:
                    print("Account not found")
                    break
            except ValueError:
                print("Invalid input for account no. Try again")
    elif choice == 4:
        while True:
            try:
                account_number = int(input("Enter your account number: "))
                account = bank.find_account(account_number)
                if account is not None:
                    account.withdraw()
                    break
                else:
                    print("Account not found")
                    break
            except ValueError:
                print("Invalid input for account no. Try again")
    elif choice == 5:
        while True:
            try:
                account_number = int(input("Enter your account number: "))
                account_1 = bank.find_account(account_number)
                another_account_number = int(input("Enter the account number you want to transfer money to: "))
                account_2 = bank.find_account(another_account_number)
                if account_1 is not account_2:
                    if account_1 is not None and account_2 is not None :
                        account_1.transfer(account_2)
                        break
                    else:
                        print("Account not found")
                        break
                else:
                    print("!!! User account and reciver account cannot be the same. !!!")
            except ValueError:
                print("Invalid input for account no. Try again")
    elif choice == 6:
        while True:
                try:
                    account_number = int(input("Enter your account number: "))
                    account = bank.find_account(account_number)
                    if account is not None:
                        account.view_transactions()
                        break
                    else:
                        print("Account not found")
                        break
                except ValueError:
                    print("Invalid input for account no. Try again")
    elif choice == 7:
         while True:
            try:
                account_number = int(input("Enter your account number: "))
                bank.delete_account(account_number)
                break
            except ValueError:
                print("Invalid input for account no. Try again")
    elif choice == 8:
        print("Thank you")
        break

    else:
        continue