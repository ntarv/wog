
import CurrencyRouletteGame
import GuessGame
import MemoryGame
from score import add_score


def welcome():
    name = input("What is you name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can play of three games.\n\n")
    return name


def load_game():
    print("Please choose a game to play:\n"
          "1. Memory Game - numbers will appear for 0.7 second and you have to guess it\n"
          "2. Guess Game - guess a number\n"
          "3. Currency Roulette - try and guess the value of USD in ILS")

    while True:
        try:
            choose = int(input("Please insert a number between 1 - 3: "))
            while 3 < choose or choose < 1:
                choose = int(input("Please insert a number between 1 - 3: "))
            difficulty = int(input('Please choose game difficulty from 1 to 5:'))
            while 5 < difficulty or difficulty < 1:
                difficulty = int(input("Please insert a number between 1 - 5: "))
        except ValueError:
            print("Error: Enter just numbers please !!!")
            continue
        if choose == 1:
            MemoryGame.generate_sequence(difficulty)
            if bool(GuessGame) is True:
                add_score(difficulty)
        if choose == 2:
            GuessGame.generate_number(difficulty)
            if bool(MemoryGame) is True:
                add_score(difficulty)
        if choose == 3:
            CurrencyRouletteGame.get_money_interval(difficulty)
            if bool(CurrencyRouletteGame) is True:
                add_score(difficulty)
        return difficulty, choose




welcome()
load_game()
load_game()
load_game()
