# ATM Transaction Sequence Simulation

balance = 10000
withdrawal_limit = 5000

successful = 0
rejected = 0

n = int(input("Enter number of transactions: "))

for i in range(1, n + 1):

    print("\nTransaction", i)
    transaction = input("Enter transaction type (deposit/withdraw): ").lower()
    amount = float(input("Enter amount: "))

    if transaction == "deposit":

        if amount > 0:
            balance = balance + amount
            successful += 1
            print("Deposit successful.")
            print("Current Balance: ₹", balance)
        else:
            rejected += 1
            print("Invalid deposit. Transaction rejected.")

    elif transaction == "withdraw":

        if amount <= 0:
            rejected += 1
            print("Invalid withdrawal. Transaction rejected.")

        elif amount > withdrawal_limit:
            rejected += 1
            print("Withdrawal exceeds limit. Transaction rejected.")

        elif amount > balance:
            rejected += 1
            print("Insufficient balance. Transaction rejected.")

        else:
            balance = balance - amount
            successful += 1
            print("Withdrawal successful.")
            print("Current Balance: ₹", balance)

    else:
        rejected += 1
        print("Invalid transaction type. Transaction rejected.")

print("\n----- TRANSACTION SUMMARY -----")
print("Initial Balance: ₹10000")
print("Successful Transactions:", successful)
print("Rejected Transactions:", rejected)
print("Final Balance: ₹", balance)
