try:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    elif number == 0:
        print("0! = 1")
    else:
        factorial = 1
        steps = ""
        for i in range(number, 0, -1):
            factorial *= i
            steps += str(i)
            if i != 1:
                steps += " × "
        print(f"{number}! = {steps} = {factorial}")
except:
    print("Invalid input. Please enter a valid integer.")
