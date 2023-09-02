import math

prime = True  # Initialize prime as True

number = int(input("Please enter a number: "))

if number == 2:
    prime = True
elif number == 1:
    prime = False
else:
    for x in range(2, int(math.sqrt(number)) + 1):
        if number % x == 0:
            prime = False
            break  # Exit the loop as soon as a divisor is found

if prime:
    print("Prime")
else:
    print("Not prime")
