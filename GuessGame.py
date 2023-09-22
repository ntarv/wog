from random import randint


def generate_number(difficulty):
    generate = randint(1, difficulty)

    print(f"Lets go! You have {difficulty -1} attempts")

    for play in range(1, difficulty):
        get_guess_from_user = int(input("Write number: "))

        if get_guess_from_user > generate:
            print("To much!")
        elif get_guess_from_user < generate:
            return
        else:
            print(f"You WIN for in {play} attempt")
            break
        print(f"You used {play} attempt")
    else:
        print(f"You waste all attempts. The number was {generate}")
