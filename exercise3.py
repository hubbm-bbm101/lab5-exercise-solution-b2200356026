import random

random_number = random.randint(1, 50)
while True:
    guess = int(input("Guess the number:"))
    if guess < random_number:
        print("Increase your number:")
    elif guess > random_number:
        print("Decrease your number:")
    else:
        print("You found it wonderful")
        break
