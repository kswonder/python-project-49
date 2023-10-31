from random import randint

RULE = "What number is missing in the progression?"


def get_correct_answer():

    max_elem = 10
    first_elem = randint(1, 5)
    step_elem = randint(1, 5)

    progression = rand_progression(max_elem, first_elem, step_elem)
    char = '...'
    random_elem = randint(0, 9)
    correct_answer = progression[random_elem]
    progression[random_elem] = char

    question_str = ' '.join(map(str, progression))

    return question_str, str(correct_answer)


def rand_progression(max_elem, first_elem, step_elem):
    max_elem = 10
    first_elem = randint(1, 5)
    step_elem = randint(1, 5)
    return [first_elem + step_elem * item for item in range(max_elem)]
