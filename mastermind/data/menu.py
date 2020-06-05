class Menu:
    def __init__(self, options):
        self.options = options
        self.back = 'b'

    # Geen duidelijke benaming voor deze method
    def menu(self):
        lookup = self.show()
        value = self.input(lookup)
        outcome = self.evaluate(value, lookup)
        if outcome == 'exit':
            print('exit')
        elif outcome:
            return lookup[value], self.options[lookup[value]]
        else:
            self.menu()

    # Nu heb je niet alleen een show_menu method in de settings, maar ook in menu zelf.
    # Lijkt mij niet logisch.
    def show(self):
        lookup = {}
        for idx, option in enumerate(self.options, 1):
            key = self.options[option]
            text = (key['description'] if (type(key) == dict and key.get('description')) else option)
            print(f"{idx}. {text}")
            lookup[str(idx)] = option
        return lookup

    # parameter te veel? 
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


if __name__ == '__main__':
    # Ik zou deze options wat meer human readable te maken
    options = {"a": ['a', 'b'], 'b': 'b', 'c': 'd'}
    menu = Menu(options)
    lookup = menu.show()
    choice = menu.input(lookup)
    menu.evaluate(choice, lookup)
