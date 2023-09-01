def main():
    # Get the input number from the user
    input_number = get_and_set_input()

    # Check if the input number is negative
    if input_number < 0:
        input_number = abs(input_number)
        print(f"-{input_number} is a negative number. Proceeding calculation with {input_number}")
    # Check if the input number is 0 or 1
    elif input_number == 0 or input_number == 1:
        print(
            f"{input_number} is too small to be a prime number. Therefore, it is not prime.")
    # Calculate and check if the input number is prime
    else:
        if is_prime(input_number):
            print(f"{input_number} is prime.")
        else:
            print(f"{input_number} is not prime.")


def get_and_set_input():
    # Prompt the user for input and convert it to an integer
    input_str = input("Please input a number to calculate with:\n")
    input_number = int(input_str)
    return input_number


def is_prime(num):
    # Check if the number is 2 (a prime)
    if num == 2:
        return True
    # Check if the number is 1 (not a prime)
    elif num == 1:
        return False
    else:
        # Check for divisors up to the square root of the number
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


# Entry point of the program
if __name__ == "__main__":
    main()
