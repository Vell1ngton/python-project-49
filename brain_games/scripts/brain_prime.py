#!/usr/bin/env python3.
import prompt
import random
from brain_games.PRIME_LOGIC import is_prime


def prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 1
    result = ''
    while count != 4:
        random_number = random.randint(1, 100)
        print(f'Question {random_number}')
        answer = prompt.string("Your answer: ")
        result = is_prime(random_number)
        if answer == result:
            print('Correct!')
            count += 1
            continue
        else:
            return (f"{answer} is wrong answer ;(."
                    f" Correct answer was {result} \n Let's try again, {name}")
    return f"Congratulations, {name}!"


if __name__ == '__main__':
    prime()
