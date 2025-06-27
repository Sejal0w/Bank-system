bank_accounts = {}

def create_account():
    name = input("Enter your name: ")
    acc_no = input("Enter account number: ")
    if acc_no in bank_accounts:
        print("Account already exists.")
    else:
        bank_accounts[acc_no] = {'name': name, 'balance': 0}
        print("Account created successfully.")

def deposit():
    acc_no = input("Enter account number: ")
    if acc_no in bank_accounts:
        amount = float(input("Enter amount to deposit: "))
        bank_accounts[acc_no]['balance'] += amount
        print(f"Deposited ₹{amount}. New balance: ₹{bank_accounts[acc_no]['balance']}")
    else:
        print("Account not found.")
def withdraw():
    acc_no = input("Enter account number: ")
    if acc_no in bank_accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= bank_accounts[acc_no]['balance']:
            bank_accounts[acc_no]['balance'] -= amount
            print(f"Withdrawn ₹{amount}. New balance: ₹{bank_accounts[acc_no]['balance']}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

def view_balance():
    acc_no = input("Enter account number: ")
    if acc_no in bank_accounts:
        print(f"Name: {bank_accounts[acc_no]['name']}")
        print(f"Balance: ₹{bank_accounts[acc_no]['balance']}")
    else:
        print("Account not found.")
def main():
    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            view_balance()
        elif choice == '5':
            print("Thank you for using our bank system!")
            break
        else:
            print("Invalid choice. Try again.")

main()



