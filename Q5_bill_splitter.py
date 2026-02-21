bill = float(input("Total bill: "))
people = int(input("Number of people: "))
tax = float(input("Tax %: "))
tip = float(input("Tip %: "))
tax_amt = bill * tax / 100
tip_amt = (bill + tax_amt) * tip / 100
total = bill + tax_amt + tip_amt
print("Total bill:", total)
print("Per person:", total / people)
