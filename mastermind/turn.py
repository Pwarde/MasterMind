import re


class Turn:
    def __init__(self, settings, code):
        super().__init__()
        self.secret_code = code
        self.colors = int(settings['colors'])

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


class Checks:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def evaluate_turn(self, guess, code):
        reduced_code, reduced_guess, correct_places = self.correct_place(guess, code)
        wrong_places = self.wrong_place(reduced_guess, reduced_code)
        return correct_places, wrong_places

    def correct_place(self, guess, code):
        combined = list(zip(guess, code))

        reduced = [i for i in combined if i[0] != i[1]]
        if not reduced:
            return [], [], len(code)
        else:
            reduced_guess, reduced_code = zip(*reduced)
            correct_places = len(guess) - len(reduced_guess)

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
