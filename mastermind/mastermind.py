from menu import Menu
from game import Game


def main():
    def new_game():
        game = Game()
        game.new()
        print('p.')

    def resume_game():
        game = Game()
        game.resume()

    options = {"New Game": "new_game()", "Resume game": "resume_game()"}

    menu = Menu(options)
    action = menu.menu()
    while action:
        exec(action)
        action = menu.menu()


if __name__ == '__main__':
    main()


# def do_turn(game, *args, **kwargs):
#     turn = Turn(game.settings, game.secretCode)
#     message = kwargs.get('message')
#     guess = turn.input_code(message=message)
#     return guess if turn.verify_guess(guess, game.turns) else do_turn(game, message='again')


# for i in range(game.settings['maxTurns']):
#     message = 'Please enter your next guess: '
#     guess = do_turn(game) if i == 0 else do_turn(game, message=message)
#     game.turns.append(guess)
#     checks = Checks()
#     correctPlaces, wrongPlaces = checks.evaluate_turn(guess, game.secretCode)
#     if correctPlaces == game.settings['codeLength']:
#         print(f'You guessed correctly. The code is {game.secretCode} \nIt took you {len(game.turns)} turn(s) to guess right!')
#         break
#     else:
#         print(f'correct: {correctPlaces}, wrong placement: {wrongPlaces}')
# print('game is over')
