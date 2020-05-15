import mysql.connector
from mysql.connector import Error
# from contextlib import ContextDecorator


class DataBase:
    def __init__(self, *args):
        self.host = 'localhost'
        self.database = 'mastermind'
        self.user = 'mysql'
        self.password = 'mysql'

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(host=self.host,
                                                      database=self.database,
                                                      user=self.user,
                                                      password=self.password)
            print(f"Connected to DB {self.database}")
            self.cursor = self.connection.cursor()
            return self
        except Error as e:
            print(e)

    def __exit__(self, *args, **kwargs):
        self.cursor.close()
        self.connection.close()

    def execute(self, query, *args, **kwargs):
        print(*args)
        print(**kwargs)
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("query executed")
            return self.cursor.lastrowid
        except Error as e:
            print(e)

    # def read(self, query):
    #     result = None
    #     try:
    #         cursor.execute(query)
    #         result = cursor.fetchall()
    #         return result
    #     except Error as e:
    #         print(e)


games_table_query = """
CREATE TABLE IF NOT EXISTS games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    secret_code JSON,
    status ENUM('in_progress', 'won', 'lost'),
    max_turns INT,
    code_length INT,
    colors INT
    ) ENGINE = InnoDB;
"""

turns_table_query = """
CREATE TABLE IF NOT EXISTS turns (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    turn_no INT NOT NULL,
    guess JSON NOT NULL,
    correct INT(2),
    wrong_place INT,
    FOREIGN KEY fk_game_id (game_id) REFERENCES games (id)
    ) ENGINE = InnoDB;
"""

create_games = """
INSERT INTO
    `games` (`secret_code`)
VALUES
    ('[2, 4, 5, 1]'),
    ('[5, 2, 1, 4]')
"""

create_turns = """
INSERT INTO
    `turns` (`game_id`, `guess`)
VALUES
    ('1', '[2, 5, 1, 3]'),
    ('1', '[5, 1, 3, 2]'),
    ('1', '[1, 1, 3, 4]'),
    ('2', '[2, 1, 1, 3]'),
    ('2', '[2, 3, 1, 3]'),
    ('2', '[2, 2, 1, 3]')
"""

get_games = """
SELECT secret_code FROM games
"""

get_turns = """
SELECT
    games.secret_code,
    turns.guess
FROM
    turns
    INNER JOIN games ON games.id = turns.game_id
WHERE
    games.id = 1
"""


# db = DataBase()
# connection = db.connect()

# db.execute(connection, games_table_query)
# db.execute(connection, turns_table_query)
# db.execute(connection, create_games)
# db.execute(connection, create_turns)
# games = db.read(connection, get_games)
# turns = db.read(connection, get_turns)

# print(turns)
# code = json.loads(games[0][0])
# print(code)
# print(type(code))
# for num in code:
#     print(num)
