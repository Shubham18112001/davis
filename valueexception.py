def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Example usage
user_integer = get_integer_input("Please enter an integer: ")
print(f"You entered: {user_integer}")
