#!/usr/bin/env python3.
import prompt
import random


def progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
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
        print(f"Question: {spis}")
        answer = prompt.string("Your answer: ")
        if int(answer) == znach:
            print('Correct!')
            count += 1
            continue
        else:
            return f"{answer} is wrong answer ;(. Correct answer was {znach} \n Let's try again, {name}"
    return f"Congratulations, {name}!"


if __name__ == '__main__':
    progression()
