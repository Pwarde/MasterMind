import json
from random import randint
from game.turn import Turn
from data.settings import Settings
from data.database import DataBase
from data.queries import game_queries, turn_queries


class Game:
    # def __init__(self, settings):

    def new(self):
        settings = Settings.get_settings()
        max_turns = settings['max_turns']['value']
        code_length = settings['code_length']['value']
        colors = settings['colors']['value']
        status = 1
        secret_code = self.generate_code(code_length, colors)

        with DataBase() as db:
            query = game_queries.get('new_game').format(secret_code, status, max_turns, code_length, colors)
            return db.execute(query)

    def generate_code(self, code_length, colors):
        return [randint(1, colors) for i in range(code_length)]

    def resume(self):
        return input("Please enter the ID of the game you want to resume:\n")

    def fetch_game(self, game_id):
        game_metrics = None
        with DataBase() as db:
            query = game_queries.get('get_game').format(game_id)
            game_metrics = db.read(query)
        variables = ['id', 'secret_code', 'status', 'max_turns', 'code_length', 'colors']
        return {i: j for i, j in zip(variables, game_metrics[0])}

    def fetch_turns(self, game_id):
        with DataBase() as db:
            query = turn_queries.get('get_turns').format(game_id)
            return db.read(query)

    def start(self, game_id):
        game = self.fetch_game(game_id)
        turns = self.fetch_turns(game_id)
        game['secret_code'] = json.loads(game['secret_code'])
        for i in range(1, game["max_turns"]):
            turn = [game_id, i]
            # new = [*self.do_turn(game, turns)]
            turn += [*self.do_turn(game, turns)]
            if self.get_win(game["code_length"], turn[3]):
                status = 'won'
                self.set_status(game_id, 'won')
                return print('you win!')
            else:
                self.append_turn(turns, turn)
                # self.display(turn, game)
        return print('lost')

    def do_turn(self, game, turns):
        turn = Turn(game, turns)
        return turn.do_turn()

    def append_turn(self, turns, turn):
        with DataBase() as db:
            query = turn_queries.get('insert').format(*turn)
            return db.execute(query)
        turns.append(turn)
        print(turns)

    def display(self, turn, game):
        display = Display(turn, game['secret_code'])
        print('display')
        display.evaluate_turn()

    def get_win(self, code_length, correct_positions):
        if code_length == correct_positions:
            return True

    def set_status(self, game_id, status):
        with DataBase() as db:
            query = game_queries.get('update_status').format(status, game_id)
            return db.execute(query)


if __name__ == '__main__':
    game = Game()
    game.resume()
