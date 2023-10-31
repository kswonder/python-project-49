from brain_games import cli
import prompt

ROUNDS = 3


def launch_game(game):
    name = cli.welcome_user()
    print(game.RULE)
    count = 0
    while count < ROUNDS:
        question, correct_answer = game.get_correct_answer()
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
            return 0
    print(f'Congratulations, {name}!')
