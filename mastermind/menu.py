from settings import Settings
from game import Game

class Menu:
    def __init__(self):
        self.show_menu()

    def show_menu(self):
        print('menu')
        choice = input('number')
        if choice == "1":
            self.new_game()
        elif choice == "2":
            self.resume_game()
        elif choice == "3":
            self.open_settings()
        else:
            return None

    def open_settings(self):
        settings = Settings()
        close_settings = settings.show_menu()
        print(close_settings)
        self.show_menu() if close_settings else self.open_settings()

    def new_game(self):
        game = Game()
        game.new_game()

    def resume_game(self):
        game = Game()
        game.resume_game()
