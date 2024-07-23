def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"The result of dividing {numerator} by {denominator} is {result}.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage
numerator = int(input("enter numerator value : "))
denominator = int(input("enter denominator value : "))

divide_numbers(numerator, denominator)
