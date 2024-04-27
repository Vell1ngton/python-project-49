#!/usr/bin/env python3.

import random
import prompt
from brain_games.cli import welcome_user

# flake8: noqa: C901


def is_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 1
    while count != 4:
        n = random.randint(0, 100)
        print(f'Question: {n}')
        answer = prompt.string("Your answer: ")
        if n % 2 != 0 and answer == 'no' or n % 2 == 0 and answer == 'yes':
            print('Correct!')
            count += 1
            continue
        else:
            if n % 2 != 0 and answer == 'yes':
                print(f"{answer} is wrong answer ;(."
                        f" Correct answer was 'no'.\n"
                        f"Let's try again, {name}!'")
                break
            if n % 2 == 0 and answer == 'no':
                print(f"{answer} is wrong answer ;(."
                        f" Correct answer was 'yes'.\n"
                        f"Let's try again, {name}!'")
                break
            if n % 2 != 0 and answer != 'yes' and answer != 'no':
                print(f"{answer} is wrong answer ;(."
                        f" Correct answer was 'no'.\n"
                        f"Let's try again, {name}!'")
                break
            if n % 2 == 0 and answer != 'yes' and answer != 'no':
                print(f"{answer} is wrong answer ;(."
                        f" Correct answer was 'yes'.\n"
                        f"Let's try again, {name}!'")
                break
    else:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    is_even()
