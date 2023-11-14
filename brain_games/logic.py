import prompt

ROUNDS = 3


def launch_game(game):
    name = greeting()
    print(game.RULE)
    count = 0
    while count < ROUNDS:
        question, correct_answer = game.get_correct_args()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!!!"
            )
            return 
    print(f'Congratulations, {name}!')


def greeting():

    name = prompt.string('Welcome to the Brain Games! \nMay I have your name? ')
    print(f'Hello, {name}!')
    return name
