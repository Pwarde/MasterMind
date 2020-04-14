import re


class Turn:
    def __init__(self, settings, code):
        super().__init__()
        self.secretCode = code
        self.colors = int(settings['colors']) or 6  # TODO: Remove or
        print(self.secretCode)

    def input_code(self, *args, **kwargs):
        print(kwargs)
        message = kwargs.get('message') or "Please input a numerical code seperated with spaces"
        userInput = input(message)

        pattern = '\\d+'
        code = re.findall(pattern, userInput)
        code = [int(i) for i in code]
        return code

    def correct_length(self, guess):
        return True if len(guess) is len(self.secretCode) else False

    def in_bounds(self, guess):
        inBounds = True
        for value in guess:
            if not 0 < value <= self.colors:
                inBounds = False
                break
        return inBounds

    def not_duplicate(self, guess, turns):
        print(turns)
        for turn in turns:
            if guess == turn:
                return False
        return True

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

    # def evaluate_turn(self, guess, code):

    def correct_place(self, guess, code):
        combined = list(zip(guess, code))
        
        reduced = [i for i in combined if i[0] != i[1]]
        reducedGuess, reducedCode = zip(*reduced)

        return reducedCode, reducedGuess

    def wrong_place(self, reducedGuess, reducedCode):
        reducedCode = list(reducedCode)
        wrong_places = 0
        for i in reducedGuess:
            try:
                idx = reducedCode.index(i)
                reducedCode.pop(idx)
                wrong_places += 1
            except ValueError:
                None
        return wrong_places
