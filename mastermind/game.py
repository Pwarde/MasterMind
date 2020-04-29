from random import randint
from turn import Turn
from settings import Settings
from database import DataBase


class Game:
    # def __init__(self, settings):

    def new_game(self):
        query = f"INSERT into           \
                    games (             \
                        'secret_code',  \
                        'status',       \
                        'max_turns',    \
                        'code_length',  \
                        'colors'        \
                    ) VALUE (           \
                        {secretCode},   \
                        {status},       \
                        {maxTurns},     \
                        {codeLength},   \
                        {colors}        \
                    )                   \
                "
        db = DataBase()
        connection = db.connect()
        db.execute(connection, query)

    def unpack_settings(self):
        settings = Settings.get_settings()
        secretCode = self.generate_code()
        maxTurns = 0
        codeLength = 0
        colors = 0
        status = 'in_progress'
        for setting in settings:
            if setting['name'] == 'maxTurns':
                maxTurns = setting['value']
            if setting['name'] == 'codeLength':
                codeLength = setting['value']
            if setting['name'] == 'colors':
                colors = setting['value']

    def generate_code(self):
        code = [randint(1, self.settings['colors']) for i in range(self.settings['codeLength'])]
        return code

    def resume_game(self):
        game_id = input("Please enter the ID of the game you want to resume:\n")

        self.game()

    def game(self):
        """import/get settings and game progress"""

    def do_turn(self):
        turn = Turn()
        outcome = turn.do_turn()
        return outcome

    def append_turn(self, lastTurn):
        self.turns.append(lastTurn)
