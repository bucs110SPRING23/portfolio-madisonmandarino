import random

value = random.randint(1,11)

for i in range(3):
    guess = int(input("Guess which number from 1-10: "))
    print(guess)
    if value > guess:
        print("TOO LOW")
    elif value == guess:
        print("CORRECT!")
        break
    else:
        print("TOO HIGH")
