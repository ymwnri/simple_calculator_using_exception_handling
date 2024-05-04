# Ask user to choose one operation from add, subtract, multiply, divide
# Ask for user input for two numbers
# Use exception handling to catch any errors
# Ask user if they want to continue
# If yes, repeat the process. If no, exit the program

try:
    # Loop to execute the program
    while True:
        
        # Ask user to choose an operation
        get_operation = input("Choose an operation: add, subtract, multiply, divide: ")

        # Check if the operation is valid using try
        if get_operation not in ['add', 'subtract', 'multiply', 'divide'].upper():
            print("Choose within the four operation. Please try again.")
            continue

        # Ask user for two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the operation
        if get_operation == 'add':
            print(f"Sum: {num1 + num2}")
        elif get_operation == 'subtract':
            print(f"Difference: {num1 - num2}")
        elif get_operation == 'multiply':
            print(f"Product: {num1 * num2}")
        elif get_operation == 'divide':
            print(f"Quotient: {num1 / num2}")

        # Ask user if they want to continue
        get_continue = input("Do you want to continue? (Y/N): ")

        if get_continue.lower() != 'Y':
            break