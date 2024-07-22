# Handle a ZeroDivisionError exception when dividing a number by zero
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Usage
divide_numbers(10, 0)
