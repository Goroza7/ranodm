import random

number = random.randint(1, 100)
guesses = 0

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    guess = int(input("Your guess: "))
    guesses += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {guesses} tries!")
        break
