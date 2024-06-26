#!/usr/bin/env python3.
import prompt
import random
from brain_games.PRIME_LOGIC import is_prime
from brain_games.cli import welcome_user


def prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 1
    while count != 4:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string("Your answer: ")
        result = is_prime(random_number)
        if answer == result:
            print('Correct!')
            count += 1
            continue
        else:
            print(f"{answer} is wrong answer ;(."
                  f" Correct answer was {result}. \n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    prime()
