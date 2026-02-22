balance = 1000
ch = int(input("1.Check 2.Deposit 3.Withdraw: "))
if ch == 1:
    print(balance)
elif ch == 2:
    amt = int(input("Amount: "))
    balance = balance + amt
    print(balance)
elif ch == 3:
    amt = int(input("Amount: "))
    if amt <= balance:
        balance = balance - amt
        print(balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid")
