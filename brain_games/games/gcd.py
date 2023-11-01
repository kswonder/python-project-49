import random

RULE = "Find the greatest common divisor of given numbers."


def get_correct_answer():
    num_1 = random.randrange(0, 31, 2)
    num_2 = random.randrange(30, 101, 10)
    question = f'{num_1} {num_2}'
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 = num_1 - num_2
        else:
            num_2 = num_2 - num_1
    return str(question), str(num_2)
