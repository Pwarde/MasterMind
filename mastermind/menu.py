from settings import Settings
from game import Game


class Menu:
    def __init__(self, options):
        # self.show_menu()
        self.options = options
        self.back = 'b'

    def show_menu(self):
        lookup = {}
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
            lookup[str(idx)] = option
        return lookup

    def input_menu(self, lookup):
        message = "give number:\n"
        return input(message)

    def evaluate_input(self, choice, lookup):
        print(self.back.capitalize())
        if choice in lookup:
            print('select option')
        elif choice == self.back or choice == self.back.capitalize():
            print('exit menu or quit game\n')
        else:
            print('Invalid')


if __name__ == '__main__':
    options = {"a": ['a', 'b'], 'b':'b', 'c':'d'}
    menu = Menu(options)
    lookup = menu.show_menu()
    print(lookup)
    choice = menu.input_menu(lookup)
    menu.evaluate_input(choice, lookup)
    # print(type(choice))
