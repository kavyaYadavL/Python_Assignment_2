try:
    total_bill = float(input("Enter total bill: "))
    people = int(input("Number of people: "))
    tax_percent = float(input("Tax percentage: "))
    tip_percent = float(input("Tip percentage: "))

    tax_amount = (tax_percent / 100) * total_bill
    after_tax = total_bill + tax_amount
    tip_amount = (tip_percent / 100) * after_tax
    final_total = after_tax + tip_amount
    per_person = final_total / people

    print("\n=== BILL BREAKDOWN ===")
    print("Subtotal:", total_bill)
    print("Tax:", tax_amount)
    print("After tax:", after_tax)
    print("Tip:", tip_amount)
    print("Total:", final_total)
    print("Per person:", per_person)

except:
    print("Invalid input. Please enter correct values.")
