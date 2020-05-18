class Menu:
    def __init__(self, options):
        self.options = options
        self.back = 'b'

    def menu(self):
        lookup = self.show()
        value = self.input(lookup)
        outcome = self.evaluate(value, lookup)
        if outcome == 'exit':
            print('exit')
        elif outcome:
            return self.options[lookup[value]]
        else:
            self.menu()

    def show(self):
        lookup = {}
        for idx, option in enumerate(self.options, 1):
            print(f"{idx}. {option}")
            lookup[str(idx)] = option
        return lookup

    def input(self, lookup):
        message = "give number:\n"
        return input(message)

    def evaluate(self, choice, lookup):
        if choice in lookup:
            return True
        elif choice == self.back or choice == self.back.capitalize():
            return 'exit'
        else:
            return False
        # probeer ervoor te zorgen dat je functies maar 1 datatype returnen


if __name__ == '__main__':
    options = {"a": ['a', 'b'], 'b': 'b', 'c': 'd'}
    menu = Menu(options)
    lookup = menu.show()
    print(lookup)
    choice = menu.input(lookup)
    menu.evaluate(choice, lookup)
