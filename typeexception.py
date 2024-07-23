def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)  
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    try:
        num1 = get_number_input("Enter the first number: ")
        num2 = get_number_input("Enter the second number: ")
        print(f"The numbers you entered are {num1} and {num2}.")
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
