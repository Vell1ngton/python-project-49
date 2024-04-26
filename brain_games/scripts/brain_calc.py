#!/usr/bin/env python3.
import prompt
import random
from brain_games.cli import welcome_user


def calc():
    name = welcome_user()
    print('What is the result of the expression?')
    count = 1
    result = 0
    while count != 4:
        sign = ["+", "-", "*"]
        random_number1 = random.randint(0, 20)
        random_number2 = random.randint(0, 20)
        random_sign = random.choice(sign)
        if random_sign == '+':
            result = random_number1 + random_number2
        elif random_sign == '-':
            result = random_number1 - random_number2
        elif random_sign == '*':
            result = random_number1 * random_number2
        print(f'Question: {random_number1} {random_sign} {random_number2}')
        answer = prompt.string("Your answer: ")
        if result == int(answer):
            print('Correct!')
            count += 1
            continue
        else:
            return (f"{answer} is wrong answer ;(."
                    f" Correct answer was {result}. \n"
                    f"Let's try again, {name}!")
    return f"Congratulations, {name}!"


if __name__ == '__main__':
    calc()
