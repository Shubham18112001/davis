# Prompt the user to input two numbers and raise a TypeError exception if the inputs are not numerical
def input_two_numbers():
    try:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
        print(f"The numbers you entered are: {num1} and {num2}")
    except ValueError:
        print("Error: Both inputs must be numerical.")

# Usage
input_two_numbers()
