#!/usr/bin/env python3.
import prompt
import random
from brain_games.cli import welcome_user


def progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    count = 1
    while count != 4:
        start = random.randint(1, 50)
        spis = [start]
        prog = random.randint(1, 10)
        index = random.randint(1, 9)
        while len(spis) <= 9:
            start += prog
            spis.append(start)
        znach = spis.pop(index)
        spis.insert(index, '..')
        print("Question:", *spis, sep=' ')
        answer = prompt.string("Your answer: ")
        if int(answer) == znach:
            print('Correct!')
            count += 1
            continue
        else:
            print(f"{answer} is wrong answer ;(."
                  f" Correct answer was {znach}. \n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    progression()
