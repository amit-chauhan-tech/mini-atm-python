account = {
    "name": "AMIT CHAUHAN",
    "balance": 500001,
    "pin": "9199",
    "type": "salry account"
}

print("=== MINI ATM ===")

pin = input("Enter your pin: ")

if pin == account["pin"]:

    while True:
        print("\n**** ATM MENU ****")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Account Details")
        print("5. EXIT")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("YOUR BALANCE IS:", account["balance"])

        elif choice == "2":
            amount = int(input("Enter your amount: "))

            if amount > 0:
                account["balance"] = account["balance"] + amount
                print("Money deposited successfully")
                print("NEW BALANCE:", account["balance"])
            else:
                print("Invalid amount")

        elif choice == "3":
            amount = int(input("Enter your amount: "))

            if amount <= 0:
                print("Invalid amount")

            elif amount > account["balance"]:
                print("Insufficient balance")

            else:
                account["balance"] = account["balance"] - amount
                print("COLLECT YOUR CASH")
                print("NEW BALANCE:", account["balance"])

        elif choice == "4":
            print("\nACCOUNT NAME:", account["name"])
            print("ACCOUNT BALANCE:", account["balance"])
            print("ACCOUNT TYPE:", account["type"])

        elif choice == "5":
            print("THANK YOU")
            break

        else:
            print("Invalid choice")

else:
    print("Invalid PIN")
    print("Access denied")

 
