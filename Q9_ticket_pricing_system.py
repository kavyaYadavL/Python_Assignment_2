try:
    age = int(input("Enter age: "))
    day = input("Enter day of week: ")
    tickets = int(input("Enter number of tickets: "))

    if age < 3:
        base_price = 0
    elif age <= 12:
        base_price = 150
    elif age <= 59:
        base_price = 300
    else:
        base_price = 200

    total_price = base_price * tickets

    if day.lower() in ["friday", "saturday", "sunday"]:
        discount = total_price * 0.20
    else:
        discount = 0
    final_price = total_price - discount
    print("\n--- BILL DETAILS ---")
    print("Base price:", base_price)
    print("Total before discount:", total_price)
    print("Discount:", discount)
    print("Final amount:", final_price)

except:
    print("Invalid input. Please try again.")
