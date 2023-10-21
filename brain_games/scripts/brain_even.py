#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.cli import welcome_user


def main():

    count = 0
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while count < 3:
        random_number = randint(1, 100)
        print('Question: ' + str(random_number))
        answer = prompt.string("Your answer: ")
        if random_number % 2 == 0 and answer == 'yes':
            print("Correct!")
        elif random_number % 2 == 1 and answer == 'no':
            print("Correct!")
        elif random_number % 2 == 0 and answer == 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'. \nLet's try again, {name}!")
            break
        elif random_number % 2 == 1 and answer == 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {name}!")
            break
        else:
            print(f"It's a wrong answer :(")
            break
        count += 1
        if count > 2:
            print(f'Congratulations, {name}')
        

if __name__ == '__main__':
    main()