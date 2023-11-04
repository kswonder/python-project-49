from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_correct_answer():
    x = randint(1, 100)
    correct_answer = is_prime(x)
    if correct_answer:
        return x, 'yes'
    else:
        return x, 'no'


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
