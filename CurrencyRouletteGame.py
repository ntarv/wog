from currency_converter import CurrencyConverter
import random


def get_money_interval(difficulty):
    t = CurrencyConverter()
    usd = int(random.randint(1, difficulty))
    print(usd, "$")
    con = t.convert(usd, 'USD', 'ILS')
    print(con)
    low = int(con - (5 - difficulty))
    high = int(con + (5 - difficulty))

    guess = int(input(f"Guess how much of {usd}$ in ILS: "))
    if low <= guess <= high:
        print("True")
    else:
        print("False")






