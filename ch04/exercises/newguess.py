import random

value = random.randint(1,1001)
guess = 0
valguess = 0
while guess != value:
    guess = int(input("Guess which number from 1-1000: "))
    print(guess)
    valguess = valguess +1
    
    if value > guess:
        print("TOO LOW")
    elif value == guess:
        print("CORRECT!")
        break
    else:
        print("TOO HIGH")

print("The answer was:", value)
print("You took", valguess, "tries")