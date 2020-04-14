from game import Game
from turn import Turn

settings = {
    'codeLength': 4,
    'colors': 6,
    'maxTurns': 4,
}
game = Game(settings)
game.secretCode = game.generate_code()


def do_turn(game, *args, **kwargs):
    turn = Turn(game.settings, game.secretCode)
    message = kwargs.get('message')
    guess = turn.input_code(message=message)
    return guess if turn.verify_guess(guess, game.turns) else do_turn(game, message='again')


for i in range(game.settings['maxTurns']):
    guess = do_turn(game)
    game.turns.append(guess)


print(game.turns)


# print(turn.verify_guess(guess, game.turns))
