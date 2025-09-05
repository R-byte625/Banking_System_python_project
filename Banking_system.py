import json
import os

DATA_FILE = "bank_data.json"

# Load existing accounts from file
def load_accounts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save accounts to file
def save_accounts(accounts):
    with open(DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

# Verify PIN before sensitive actions
def verify_pin(account):
    pin = input("Enter PIN: ")
    return pin == account["pin"]

# Create a new account
def create_account(accounts):
    acc_no = input("Enter new account number: ")
    if acc_no in accounts:
        print("Account already exists!")
        return
    name = input("Enter account holder name: ")
    pin = input("Set a 4-digit PIN: ")
    if not pin.isdigit() or len(pin) != 4:
        print("Invalid PIN! Must be 4 digits.")
        return
    accounts[acc_no] = {"name": name, "pin": pin, "balance": 0.0, "history": []}
    print(f" Account created for {name} with account number {acc_no}")
    save_accounts(accounts)

# Deposit money
def deposit(accounts):
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print(" Account not found!")
        return
    if not verify_pin(accounts[acc_no]):
        print("Incorrect PIN!")
        return
    amount = float(input("Enter amount to deposit: "))
    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["history"].append(f"Deposited ₹{amount}")
    print(f" Deposited ₹{amount}. New Balance: ₹{accounts[acc_no]['balance']}")
    save_accounts(accounts)

# Withdraw money
def withdraw(accounts):
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print(" Account not found!")
        return
    if not verify_pin(accounts[acc_no]):
        print(" Incorrect PIN!")
        return
    amount = float(input("Enter amount to withdraw: "))
    if amount > accounts[acc_no]["balance"]:
        print(" Insufficient balance!")
    else:
        accounts[acc_no]["balance"] -= amount
        accounts[acc_no]["history"].append(f"Withdrew ₹{amount}")
        print(f" Withdrawn ₹{amount}. New Balance: ₹{accounts[acc_no]['balance']}")
        save_accounts(accounts)

# Check balance
def check_balance(accounts):
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
    if not verify_pin(accounts[acc_no]):
        print(" Incorrect PIN!")
        return
    print(f"Account Holder: {accounts[acc_no]['name']}")
    print(f" Balance: ₹{accounts[acc_no]['balance']}")
    print(" Transaction History:")
    for txn in accounts[acc_no]["history"]:
        print(" -", txn)

# Main menu
def main():
    accounts = load_accounts()
    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            print("👋 Exiting... Thank you for using our Bank System!")
            break
        else:
            print("⚠ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
