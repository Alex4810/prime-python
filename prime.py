#imports the ability to use math functions
import math

#initializes prime boolean is true
prime = True

#creates new number from user input
number = int(input("Please enter a number: "))
#2 is the only even prime number
if number == 2:
    prime = True
#0 and 1 are too small to be prime
elif number == 1:
    prime = False
elif number ==0:
    prime = False
else:
#checks to see if the number is divisible by all numbers from 2 till the square root of the number
#if none of them, then the number is prime.
    for x in range(2, int(math.sqrt(number)) + 1):
        if number % x == 0:
            prime = False
            break  # Exit the loop as soon as a divisor is found
#prints the final result to the user
if prime:
#if the number is prime
    print("Prime")
else:
#if the number is not prime
    print("Not prime")
