try:
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))

    print("what kind of operation do you want to perform.\n Press + for addition\n Presss - for subtraction\n Press * for multiplication\n Press / for division")

    o = input("Enter operation: ")

    match o:
        case '+' :
            print(f"The result is: {a + b}")
        case '-' :
            print(f"The result is: {a - b}")
        case '*' :
            print(f"The result is: {a * b}")
        case '/' :
            if b != 0:
                print(f"The result is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case default :
            print("Invalid operation selected.")

except Exception as e :
    print("Invalid input. Please enter numeric values.")
    exit()
 