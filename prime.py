import math
prime = None

number = int(input("Please enter a number: "))
if(input == 2 ):
    prime = True
elif(input == 1):
    prime = False
else:
    for x in range (0, math.sqrt(number)):
        if(number%x == 0):
            prime = False
    prime = True

if(prime == True):
    print("Prime")
else:
    print("Not prime")


