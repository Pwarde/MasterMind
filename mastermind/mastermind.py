from menu import Menu
from game import Game


def main():
    def new_game():
        game = Game()
        game_id = game.new()
        print(game.start(game_id))

    def resume_game():
        game = Game()
        game_id = game.resume()
        game.start(game_id)

    def settings():
        print('settings')

    options = {"New Game": "new_game()", "Resume game": "resume_game()"}

    menu = Menu(options)
    action = menu.menu()
    while action:
        exec(action)
        action = menu.menu()


if __name__ == '__main__':
    main()




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
