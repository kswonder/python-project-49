import random

RULE = "Find the greatest common divisor of given numbers."


def get_correct_args():
    number_1 = random.randrange(0, 31, 2)
    number_2 = random.randrange(30, 101, 10)
    question = f'{number_1} {number_2}'
    correct_answer = get_gcd(number_1, number_2)

    return str(question), str(correct_answer)


def get_gcd(num_1, num_2):
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 = num_1 - num_2
        else:
            num_2 = num_2 - num_1
    return num_2
