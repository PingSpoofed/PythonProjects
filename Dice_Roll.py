import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount < 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main():
    while True:
        try:
            user_input: str = input("How many rolls would you like: ")

            if user_input.lower() == "exit":
                print("thanks for playing")
                break

            print(*roll_dice(int(user_input)), sep=', ')
            print("Total value of: ",sum(roll_dice(int(user_input))))
        except ValueError:
            print("Please enter a valid number")

if __name__ == '__main__':
    main()
