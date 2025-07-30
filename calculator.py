# Basic Calculator Program

# Get the first number from the user
num1_str = input("Enter the first number: ")
num1 = float(num1_str)  # Convert input to a floating-point number

# Get the second number from the user
num2_str = input("Enter the second number: ")
num2 = float(num2_str)  # Convert input to a floating-point number

# Get the desired operation from the user
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
    print(f"{num1_str} + {num2_str} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1_str} - {num2_str} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1_str} * {num2_str} = {result}")
elif operation == '/':
    # Handle division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1_str} / {num2_str} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
