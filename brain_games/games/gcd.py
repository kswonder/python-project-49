import random

RULE = "Find the greatest common divisor of given numbers."


def get_correct_answer():
    a = random.randrange(0, 31, 2)
    b = random.randrange(30, 101, 10)
    question = f'{a} {b}'
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return str(question), str(b)
