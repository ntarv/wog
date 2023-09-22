import random
import time
from os import system, name


def generate_sequence(difficult):

    rand_list = []

    for i in range(0, difficult):
        rand_list.append(random.randint(1, difficult))
    print(rand_list)
    if name == 'nt':
        system('cls')
    else:
        system('clear')

    time.sleep(0.7)
    for i in range(0, 100):
        print('')

    for i in range(0, difficult):
        print("Enter number you remember in turn")
        guess = int(input())
        if guess == rand_list[i]:
            print("Good")
        else:
            print("Bad")




