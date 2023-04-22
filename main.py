import random

random_numbers = random.randint(1, 100)
a = int(input("Guess a number between 1 and 100: "))
counter = 0

while a != random_numbers:
    if a < random_numbers:
        print("The guessing number is bigger")
    elif a > random_numbers:
        print("The guessing number is smaller")
    counter += 1
    a = int(input("Guess a number between 1 and 100: "))

counter += 1
print("You guessed the number!")
print("It took you " + str(counter) + " tries to guess the number.")
