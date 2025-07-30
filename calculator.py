# Ask user for input
num1 = float(input("Enter the first number: "))
op = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation based on the operation
if op == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif op == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif op == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif op == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose +, -, *, or /.")
