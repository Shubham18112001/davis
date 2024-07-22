# Prompt the user to input an integer and raise a ValueError if the input is not a valid integer
def input_integer():
    try:
        user_input = int(input("Please enter an integer: "))
        print(f"You entered: {user_input}")
    except ValueError:
        print("Error: That was not a valid integer.")

input_integer()
