#!/usr/bin/env python3.

import random
import prompt

def is_even():
    print('Welcome to the Brain Games!')
    prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    count = 1
    while count != 4:
        random_number = random.randint(0,100)
        print(f'Question {random_number}')
        answer = prompt.string("Your answer: ")
        if random_number % 2 != 0 and answer == 'no' or random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
            count += 1
            continue
        else:
            if random_number % 2 != 0 and answer == 'yes':
                return "'yes' is wrong answer ;(. Correct answer was 'no'\n Let's try again, Bill"
            if random_number % 2 == 0 and answer == 'no':
                return "'no' is wrong answer ;(. Correct answer was 'yes'\n Let's try again, Bill"
    return "Congratulations, Bill!"


if __name__ == 'main':
    is_even()