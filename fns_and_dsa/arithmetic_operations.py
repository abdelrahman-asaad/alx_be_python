def perform_operation(num1 ,num2 ,operation):
    print("Arithmetic operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    if operation == "add" :
        print(num1 + num2)
    elif operation == "subtract" :
        print(num1 - num2)
    elif operation == "divide" :
        if num2 != 0 :
            print(num1 / num2)
        else :
            print("can't divide by zero ")
    elif operation == "miltiply" :
        print(num1 * num2)
    else :
        input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()                       