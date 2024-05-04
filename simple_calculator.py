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

