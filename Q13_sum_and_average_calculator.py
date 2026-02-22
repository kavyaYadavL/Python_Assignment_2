try:
    count = int(input("How many numbers?"))

    total = 0

    for i in range(1, count + 1):
        number = float(input(f"Enter number {i}: "))
        
        total += number

        if i == 1:
            maximum = number
            minimum = number
        else:
            if number > maximum:
                maximum = number
            if number < minimum:
                minimum = number

    average = total / count

    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)

except:
    print("Invalid input. Please enter valid numbers.")
