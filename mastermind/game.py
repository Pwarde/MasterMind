from random import randint
from turn import Turn
from settings import Settings
from database import DataBase


class Game:
    # def __init__(self, settings):

    def new(self):
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
        game_id = db.execute(connection, query)
        print(game_id)
        self.game(game_id)
        return game_id

    # def unpack_settings(self):
    def generate_code(self, codeLength, colors):
        code = [randint(1, colors) for i in range(codeLength)]
        return code

    def resume(self):
        game_id = input("Please enter the ID of the game you want to resume:\n")
        settings = self.fetch_game(game_id)
        turns = self.fetch_turns(game_id)
        game(settings, turns)

    def fetch_game(self, game_id):
        get_game = f"SELECT secret_code, status, max_turns, code_length, colors FROM games WHERE id = {game_id}"
        db = DataBase()
        connection = db.connect()
        game_metrics = db.read(connection, get_game)
        print(game_metrics)
        variables = ['secretCode', 'status', 'maxTurns', 'codeLength', 'colors']
        settings = {i: j for i, j in zip(variables, game_metrics[0])}
        return settings

    def fetch_turns(self, game_id):
        get_turns = f"SELECT FROM turns WHERE game_id = {game_id} ORDER BY turn_no asc"
        db = DataBase()
        connection = db.connect()
        turns = db.read(connection, get_turns)
        print(turns)
        return turns

    def game(self, id):
        """import/get settings and game progress"""

    def do_turn(self):
        turn = Turn()
        outcome = turn.do_turn()
        return outcome

    def append_turn(self, lastTurn):
        self.turns.append(lastTurn)


if __name__ == '__main__':
    game = Game()
    game.resume()
