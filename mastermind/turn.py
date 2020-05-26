import re
import json


class Turn:
    def __init__(self, game, turns):
        super().__init__()
        self.secret_code = game['secret_code']
        self.colors = int(game['colors'])
        self.turns = turns

    def do_turn(self, *args, **kwargs):
        guess = self.input_code(message='message')
        if guess == self.secret_code:
            return 'win'
        elif self.verify_guess(guess, self.turns):
            return guess
        else:
            return self.do_turn()

    def input_code(self, *args, **kwargs):
        message = kwargs.get('message') or "Please input a numerical code seperated with spaces"
        user_input = input(message)

        pattern = '\\d+'
        code = re.findall(pattern, user_input)
        return [int(i) for i in code]

    def verify_guess(self, guess, turns):
        if not self.correct_length(guess):
            print('Invalid length')
            return False
        if not self.in_bounds(guess):
            print(f'Please use only numbers 1-{self.colors}')
            return False
        if not self.not_duplicate(guess, turns):
            print('Duplicate guess, please try again!')
            return False
        return True

    def correct_length(self, guess):
        print(self.secret_code)
        return len(guess) == len(self.secret_code)

    def in_bounds(self, guess):
        in_bounds = True
        for value in guess:
            if not 0 < value <= self.colors:
                in_bounds = False
                break
        return in_bounds

    def not_duplicate(self, guess, turns):
        for turn in turns:
            if guess == turn:
                return False
        return True


class Display:
    def __init__(self, guess, code):
        self.guess = guess
        self.code = code
        print(type(guess))
        print(type(code))

    def evaluate_turn(self):
        reduced_code, reduced_guess, correct_places = self.correct_place()
        wrong_places = self.wrong_place(reduced_guess, reduced_code)
        self.display(correct_places, wrong_places)
        return correct_places, wrong_places

    def correct_place(self):
        combined = list(zip(self.guess, self.code))

        reduced = [i for i in combined if i[0] != i[1]]
        if not reduced:
            return [], [], len(self.code)
        else:
            reduced_guess, reduced_code = zip(*reduced)
            correct_places = len(self.guess) - len(reduced_guess)
            return reduced_code, reduced_guess, correct_places

    def wrong_place(self, reduced_guess, reduced_code):
        reduced_code = list(reduced_code)
        wrong_places = 0
        for i in reduced_guess:
            try:
                idx = reduced_code.index(i)
                reduced_code.pop(idx)
                wrong_places += 1
            except ValueError:
                None
        return wrong_places

    def display(self, correct_places, wrong_places):
        print(f'correct: {correct_places}, wrong placement: {wrong_places}')
