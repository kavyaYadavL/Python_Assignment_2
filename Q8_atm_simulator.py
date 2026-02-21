balance = 10000
while True:
    print("\n1.Check  2.Deposit  3.Withdraw  4.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        print("Balance:", balance)
    elif ch == 2:
        balance += float(input("Deposit amount: "))
        print("Deposited")
    elif ch == 3:
        amt = float(input("Withdraw amount: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawn")
        else:
            print("Insufficient balance")
    elif ch == 4:
        break
    else:
        print("Invalid choice")
