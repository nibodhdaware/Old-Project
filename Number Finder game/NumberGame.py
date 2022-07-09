import random

secret_number = random.randint(1, 10)
GuessCount = 0
GuessLimit = 3

while GuessCount < GuessLimit:
    guess = int(input("Guess a Number: "))
    GuessCount += 1
    if guess == secret_number:
        print("Congratulations! You guessed the number right")
        break

else:
    print("You tried your best but you have no chances left")
    


