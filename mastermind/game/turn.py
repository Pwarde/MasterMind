import re


class Turn:
    def __init__(self, game, turns):
        self.secret_code = game['secret_code']
        self.colors = int(game['colors'])
        self.turns = turns

    def do_turn(self, *args, **kwargs):
        guess = self.input_code()
        print(guess)
        validations = self.validate_guess(guess, self.turns)
        for validation in validations:
            if validation['valid'] == False:
                print(validation['message'])
                return self.do_turn()
        return guess, self.evaluate_guess(guess)

    def input_code(self, *args, **kwargs):
        message = kwargs.get('message') or "Please input a numerical code seperated with spaces"
        user_input = input(message)

        pattern = '\\d+'
        code = re.findall(pattern, user_input)
        return [int(i) for i in code]

    def validate_guess(self, guess):
        """Call the Validation class and check that the guess input is valid"""
        print('validation reached')
        validation = Validation(guess, self.turns)
        return validation.validate()

    def evaluate_guess(self, guess):
        """Call Evaluation class and evaluate the guess"""
        evaluation = Evaluation(guess, self.secret_code)
        return evaluation.evaluate()


class Validation:
    def __init__(self, guess, turns):
        self.guess = guess
        self.turns = turns

    def validate(self):
        result = []
        result.append(self.correct_length())
        result.append(self.in_bounds())
        result.append(self.not_duplicate())
        return result

    def correct_length(self, guess):
        validity = {"name": "correct_length"}
        message = "Incorrect length, please make sure that your guess is x long"
        if len(guess) == len(self.secret_code):
            validity["valid"] = True
        else:
            validity["valid"] = False
            validity["message"] = message
        return validity

    def in_bounds(self, guess):
        validity = {"name": "in_bounds", "valid": True}
        message = "Incorrect value entered, please make sure all values are between 0 and x"
        for value in guess:
            if not 0 < value <= self.colors:
                validity["valid"] = False
                validity["message"] = message
                break
        return validity

    def not_duplicate(self, guess, turns):
        validity = {"name": "not_duplicate", "valid": True}
        message = "This guess has already been made, please think better about what you are doing..."
        for turn in turns:
            if guess == turn:
                validity["valid"] = False
                validity["message"] = message
        return validity


class Evaluation:
    def __init__(self, guess, code):
        self.guess = guess
        self.code = code
        self.reduced_guess, self.reduced_code = self.reduce_guess()

    def evaluate(self):
        return self.correct_place(), self.wrong_place()

    def reduce_guess(self):
        """Remove same values on the same index for 2 same length lists
           returns reduced lists.
        """
        combined = list(zip(self.guess, self.code))
        reduced = [i for i in combined if i[0] != i[1]]
        if not reduced:
            return [], []
        else:
            return zip(*reduced)

    def correct_place(self):
        correct_places = len(self.guess) - len(self.reduced_guess)
        return correct_places

    def wrong_place(self):
        reduced_code = list(self.reduced_code)
        wrong_places = 0
        for i in self.reduced_guess:
            try:
                idx = reduced_code.index(i)
                reduced_code.pop(idx)
                wrong_places += 1
            except ValueError:
                None
        return wrong_places
