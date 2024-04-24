#!/usr/bin/env python3.

import random
import prompt


def is_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    count = 1
    while count != 4:
        random_number = random.randint(0, 100)
        print(f'Question {random_number}')
        answer = prompt.string("Your answer: ")
        if random_number % 2 != 0 and answer == 'no' or random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
            count += 1
            continue
        else:
            if random_number % 2 != 0 and answer == 'yes':
                return f"{answer} is wrong answer ;(. Correct answer was 'no'\n Let's try again, {name}'"
            if random_number % 2 == 0 and answer == 'no':
                return f"{answer} is wrong answer ;(. Correct answer was 'yes'\n Let's try again, {name}'"
            if random_number % 2 != 0 and answer != 'yes' and answer != 'no':
                return f"{answer} is wrong answer ;(. Correct answer was 'no'\n Let's try again, {name}'"
            if random_number % 2 == 0 and answer != 'yes' and answer != 'no':
                return f"{answer} is wrong answer ;(. Correct answer was 'yes'\n Let's try again, {name}'"
    return f"Congratulations, {name}!"


if __name__ == '__main__':
    is_even()
