while True:
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Floor division")
    print("7. Exponent")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "8":
        print("Calculator program has ended.")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        print("Result:", num1+num2)
    elif choice == "2":
        print("Result:", num1-num2)
    elif choice == "3":
        print("Result:", num1*num2)
    elif choice == "4":
        print("Result:", num1/num2)
    elif choice == "5":
        print("Result:", num1%num2)
    elif choice == "6":
        print("Result:", num1//num2)
    elif choice == "7":
        print("Result:", num1**num2)
    else:
        print("Invalid input. Try again.")
