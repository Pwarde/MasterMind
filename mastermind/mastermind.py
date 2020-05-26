from menu import Menu
from game import Game
from settings import Settings


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
        settings = Settings()
        options = settings.get_settings()
        menu = Menu(options)
        option, value = menu.menu()
        options[option] = settings.change(option, value)
        settings.set(options)

    options = {"New Game": "new_game()", "Resume game": "resume_game()", "Settings": "settings()"}

    menu = Menu(options)
    try:
        option, value = menu.menu()
        while value:
            exec(value)
            option, value = menu.menu()
    except TypeError:
        pass


if __name__ == '__main__':
    main()




# for i in range(game.settings['maxTurns']):
#     message = 'Please enter your next guess: '
#     guess = do_turn(game) if i == 0 else do_turn(game, message=message)
#     game.turns.append(guess)
#     checks = Checks()
# print('game is over')
