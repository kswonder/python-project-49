from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_correct_answer():
    x = randint(1, 100)
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return x, 'no'
    return x, 'yes'
