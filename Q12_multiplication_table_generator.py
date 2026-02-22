try:
    number = int(input("Enter number: "))
    end_range = int(input("Enter range (end): "))

    print("\nMultiplication Table of", number)

    for i in range(1, end_range + 1):
        print(number, "x", i, "=", number * i)
except:
    print("Invalid input. Please enter valid numbers.")
