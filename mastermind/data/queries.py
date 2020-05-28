game_queries = {
    "new_game": "INSERT into          \
                    games (              \
                        secret_code,     \
                        status,          \
                        max_turns,       \
                        code_length,     \
                        colors           \
                    ) VALUE (            \
                        '{}', '{}', '{}', '{}', '{}' \
                    )\
                ",
    "update_status": "UPDATE games SET status = '{}' WHERE games.id={}",
    "get_game": "SELECT id, secret_code, status, max_turns, code_length, colors FROM games WHERE id = {}"
}

turn_queries = {
    "insert":   "INSERT INTO turns (              \
                    game_id,                     \
                    turn_no,                     \
                    guess,                       \
                    correct,                     \
                    wrong_place                  \
                ) VALUE (                        \
                    '{}', '{}', '{}', '{}', '{}' \
                )",
    "get_turns": "SELECT * FROM turns WHERE game_id = {} ORDER BY turn_no asc"
}