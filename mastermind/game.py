from random import randint


class Game:
    def __init__(self, settings):
        self.settings = settings
        self.turns = []
        self.secretCode = self.generate_code()
        print(self.secretCode)

    def generate_code(self):
        code = [randint(1, self.settings['colors']) for i in range(self.settings['codeLength'])]
        return code

    def append_turn(self, lastTurn):
        self.turns.append(lastTurn)
