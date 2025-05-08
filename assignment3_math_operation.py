import math

def calculate_math_operations():
    # Input validation with while loop
    while True:
        try:
            num = float(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Calculate square root (only for non-negative numbers)
    if num >= 0:
        sqrt_result = math.sqrt(num)
        print(f"Square root of {num}: {sqrt_result:.1f}")
    else:
        print(f"Square root not calculated (number {num} is negative).")

    # Calculate natural logarithm (only for positive numbers)
    if num > 0:
        log_result = math.log(num)
        print(f"Natural logarithm of {num}: {log_result:.10f}")
    else:
        print(f"Natural logarithm not calculated (number {num} is not positive).")

    # Calculate sine (in radians)
    sine_result = math.sin(num)
    print(f"Sine of {num} radians: {sine_result:.10f}")

# Run the program
calculate_math_operations()