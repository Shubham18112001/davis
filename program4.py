def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in %): "))
time = float(input("Enter the time period (in years): "))

interest = calculate_simple_interest(principal, rate, time)

print(f"The simple interest is: {interest}")
