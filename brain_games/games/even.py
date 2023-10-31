import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_correct_answer():
    random_number = random.randint(1, 100)
    answer = 'yes' if random_number % 2 == 0 else 'no'
    return random_number, answer
