from random import randint

guesses = []
low_num, higher_num = 1, 1000
random_number: int = randint(low_num, higher_num)

print(f"Guess the number in the range of {low_num} and {higher_num}")

while True:
    try:
        user_guess: int = int(input('Guess: '))
        guesses.append([user_guess])
    except ValueError as e:
        print("Please enter a valid number")
        continue
    if len(guesses) != 3:
        if user_guess > random_number:
            print("The number is lower")
        elif user_guess < random_number:
            print("The number is higher")
        elif len(guesses) == 3:
            break
        else:
            print("you guessed it")
            break
    else:
        print("You guessed 3 times and its game over")
        print(f"These wore youre guesses {guesses}")
        break
