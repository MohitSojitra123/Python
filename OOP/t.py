# Function to perform the selected arithmetic operation on variable arguments
def arithmetic_operation(operation, *args):
    if not args:
        return "No numbers provided"
    
    result = args[0]
    if operation == '1':  # Addition
        for num in args[1:]:
            result += num
    elif operation == '2':  # Subtraction
        for num in args[1:]:
            result -= num
    elif operation == '3':  # Multiplication
        for num in args[1:]:
            result *= num
    elif operation == '4':  # Division
        for num in args[1:]:
            if num == 0:
                return "Error: Division by zero"
            result /= num
    else:
        return "Invalid operation"
    
    return result

# Function to display the menu and get user choice
def get_user_choice():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter choice (1/2/3/4): ")
    return choice

# Function to get a specific number of inputs from the user
def get_numbers():
    numbers = []
    count = input("How many numbers do you want to input? ")
    try:
        count = int(count)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_numbers()
    
    for _ in range(count):
        num = input("Enter a number: ")
        try:
            numbers.append(float(num))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return get_numbers()
    
    return numbers

def main():
    operation = get_user_choice()

    numbers = get_numbers()

    result = arithmetic_operation(operation, *numbers)


    print("Result:", result)


main()