import unittest
from mastermind.game import Game
from mastermind.turn import Turn


class CodeGenerator(unittest.TestCase):
    # def __init__(self, settings):
    settings = {
        'codeLength': 4,
        'colors': 6,
        'maxTurns': 4,
    }
    game = Game(settings)

    def test_length(self):
        game = Game(self.settings)
        game.settings['codeLength'] = 8
        self.assertEqual(len(self.game.generate_code()), 8)

        self.settings['codeLength'] = 0
        self.assertEqual(len(self.game.generate_code()), 0)

        game.settings['codeLength'] = 800
        self.assertEqual(len(game.generate_code()), 800)

    def test_colors(self):
        game = Game(self.settings)
        game.settings['colors'] = 1
        game.settings['codeLength'] = 5
        self.assertEqual(game.generate_code(), [1, 1, 1, 1, 1])

        game.colors = 5
        code = [6, 6, 6, 6, 6]
        for x in code:
            self.assertTrue(not x <= game.settings['colors'])
            self.assertTrue(x > 0)


class CodeEvaluation(unittest.TestCase):
    settings = {
        'codeLength': 4,
        'colors': 6,
        'maxTurns': 4,
    }
    code = [1, 3, 1, 5]
    turn = Turn(settings, code)

    def test_correct_places(self):
        guess = [2, 3, 4, 5]
        self.assertEqual(self.turn.correct_place(guess, self.code), ((1, 1), (2, 4)))

    def test_wrong_places(self):
        reducedGuess = (2, 3, 2, 6)
        reducedCode = (1, 2, 3, 5)
        self.assertEqual(self.turn.wrong_place(reducedGuess, reducedCode), 2)

if __name__ == '__main__':
    unittest.main()
