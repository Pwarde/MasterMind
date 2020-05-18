from random import randint
from turn import Turn
from settings import Settings
from database import DataBase


class Game:
    # def __init__(self, settings):

    def new(self):
        settings = Settings.get_settings()
        max_turns = settings['maxTurns']['value']
        code_length = settings['codeLength']['value']
        colors = settings['colors']['value']
        status = 1

        secret_code = self.generate_code(code_length, colors)

        query = f"INSERT into          \
                    games (            \
                        secret_code,   \
                        status,        \
                        max_turns,     \
                        code_length,   \
                        colors         \
                    ) VALUE (          \
                        '{secret_code}',\
                        '{status}',    \
                        '{max_turns}',  \
                        '{code_length}',\
                        '{colors}'     \
                    )                  \
                "

        with DataBase() as db:
            return db.execute(query)

    def generate_code(self, code_length, colors):
        return [randint(1, colors) for i in range(code_length)]

    def resume(self):
        game_id = input("Please enter the ID of the game you want to resume:\n")
        settings = self.fetch_game(game_id)
        self.turns = self.fetch_turns(game_id)
        self.game(settings)

    def fetch_game(self, game_id):
        get_game = f"SELECT secret_code, status, max_turns, code_length, colors FROM games WHERE id = {game_id}"

        game_metrics = None
        with DataBase() as db:
            game_metrics = db.read(get_game)

        variables = ['secret_code', 'status', 'max_turns', 'code_length', 'colors']
        return {i: j for i, j in zip(variables, game_metrics[0])}

    def fetch_turns(self, game_id):
        get_turns = f"SELECT FROM turns WHERE game_id = {game_id} ORDER BY turn_no asc"

        with DataBase() as db:
            return db.read(get_turns)

    def game(self, settings):
        """import/get settings and game progress"""

    def do_turn(self):
        turn = Turn()
        return turn.do_turn()

    def append_turn(self, lastTurn):
        self.turns.append(lastTurn)


if __name__ == '__main__':
    game = Game()
    game.resume()
