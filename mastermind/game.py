from random import randint
from turn import Turn
from settings import Settings
from database import DataBase


class Game:
    # def __init__(self, settings):

    def new_game(self):
        settings = Settings.get_settings()
        maxTurns = settings['maxTurns']['value']
        codeLength = settings['codeLength']['value']
        colors = settings['colors']['value']
        status = 1

        secretCode = self.generate_code(codeLength, colors)

        query = f"INSERT into          \
                    games (            \
                        secret_code,   \
                        status,        \
                        max_turns,     \
                        code_length,   \
                        colors         \
                    ) VALUE (          \
                        '{secretCode}',\
                        '{status}',    \
                        '{maxTurns}',  \
                        '{codeLength}',\
                        '{colors}'     \
                    )                  \
                "
        db = DataBase()
        connection = db.connect()
        db.execute(connection, query)

    # def unpack_settings(self):
    def generate_code(self, codeLength, colors):
        code = [randint(1, colors) for i in range(codeLength)]
        return code

    def resume_game(self):
        game_id = input("Please enter the ID of the game you want to resume:\n")
        query = f"SELECT secret_code, status, max_turns, code_length, colors FROM games WHERE id = {game_id}"
        db = DataBase()
        connection = db.connect()
        result = db.read(connection, query)
        print(result)
        variables = ['secretCode', 'status', 'maxTurns', 'codeLength', 'colors']
        settings = {i: j for i, j in zip(variables, result[0])}
        print(settings)
        # self.game()

    def game(self):
        """import/get settings and game progress"""

    def do_turn(self):
        turn = Turn()
        outcome = turn.do_turn()
        return outcome

    def append_turn(self, lastTurn):
        self.turns.append(lastTurn)
