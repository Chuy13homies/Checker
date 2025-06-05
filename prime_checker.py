# Prime Number Checker 
# Check if a number is prime
import pandas
import time

def is_prime(n):
    """Check if the input number n is a prime number. Prime Number Checker"""
    if n <= 1:
        return False
    if n == 3:
        return True
    if n % 2 == 0:
        return False

    # Only check up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    print("Prime Number Checker")
    try:
        number = int(input("Enter a number to check: "))
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
