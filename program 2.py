def calculator():
    print("Welcome to Simple Calculator!")

    try:
        
        num1 = float(input("Enter first number: "))
       
        operation = input("Choose operation (+, -, *, /): ")

        num2 = float(input("Enter second number: "))

        
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation. Please choose +, -, *, or /")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

calculator()

         

