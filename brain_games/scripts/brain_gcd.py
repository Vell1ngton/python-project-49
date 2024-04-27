#!/usr/bin/env python3.
import prompt
import random
from brain_games.cli import welcome_user

# flake8: noqa: C901


def gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 1
    while count != 4:
        spis = []
        random_number1 = random.randint(0, 100)
        random_number2 = random.randint(0, 100)
        if random_number1 > random_number2:
            for i in range(1, int(random_number1 / 2) + 1):
                if random_number1 % i == 0 and random_number2 % i == 0:
                    spis.append(i)
                    continue
        else:
            for i in range(1, int(random_number2 / 2) + 1):
                if random_number1 % i == 0 and random_number2 % i == 0:
                    spis.append(i)
                    continue
        if len(spis) > 1:
            result = max(spis)
            print(f'Question: {random_number1} {random_number2}')
            answer = prompt.string("Your answer: ")
            if int(answer) == result:
                print('Correct!')
                count += 1
                continue
            else:
                print(f"{answer} is wrong answer ;(."
                        f" Correct answer was {result}. \n"
                        f"Let's try again, {name}!")
                break
        else:
            continue
    else:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    gcd()
