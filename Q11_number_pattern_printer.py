try:
    print("Choose Pattern (1-4):")
    choice = int(input("Enter choice: "))
    n = 5

    if choice == 1:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()

    elif choice == 2:
        for i in range(1, n + 1):
            print(str(i) * i)

    elif choice == 3:
        for i in range(n, 0, -1):
            for j in range(i, 0, -1):
                print(j, end="")
            print()

    elif choice == 4:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()

    else:
        print("Invalid choice")

except:
    print("Invalid input")
