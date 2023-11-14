import random
import operator

RULE = 'What is the result of the expression?'


def get_correct_args():
    number_1 = random.randint(1, 25)
    number_2 = random.randint(1, 25)
    operations = ['+', '-', '*']
    random_operation = random.choice(operations)
    calculate = f'{number_1} {random_operation} {number_2}'
    correct_answer = str(calc_expression(number_1, number_2, random_operation))
    return calculate, correct_answer


def calc_expression(number_1, number_2, random_operation):
    get_operator = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    op = get_operator[random_operation]
    elem = op(number_1, number_2)
    return elem
