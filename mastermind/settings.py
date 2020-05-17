import json


class Settings:
    def show_menu(self):
        current_settings = self.get_settings()
        if not current_settings:
            return None
        try:
            print('The current game settings are:\n')
            lookup = {}
            for idx, setting in enumerate(current_settings, 1):
                lookup[idx] = setting
                print(f"{idx}. {current_settings[setting]['description']}: {current_settings[setting]['value']}")
        except TypeError:
            print("Please make sure there is a valid settings file!")
            return None
        close_settings = self.set_settings(current_settings, lookup)
        return close_settings

    @staticmethod
    def get_settings():
        try:
            with open("settings.json", "r") as read_file:
                data = json.load(read_file)
                # misschien is het handig om hier een structured dict te returnen. dat werkt denk ik een stuk fijner met je settings uitlezen.
                # je zou natuurlijk ook van je settings file zelf al een structured dict kunnen maken en die gewoon importen.
                # de python ConfigParser is ook leuk om naar te kijken, maar ondersteunt alleen strings (je moet dus zelf typecasten):
                # https://docs.python.org/3/library/configparser.html
                return data
        except FileNotFoundError:
            print("No settings file present, please make sure settings.json is present")

    def set_settings(self, current_settings, lookup):
        idx = input('\nPlease type the number of the setting to change. Type M to go back to main menu: \n')
        if idx == 'M':
            return True
        elif(idx.isdigit() and 0 < int(idx) <= len(current_settings)):
            idx = int(idx)
            setting = current_settings[lookup[idx]]
            text = setting.get('new_value_text') or setting.get('description')
            try:
                setting['value'] = int(input(text))
                with open("settings.json", "w") as write_file:
                    json.dump(current_settings, write_file, indent=2)

            except ValueError:
                print("incorrect value please try again.")
            return False
        else:
            print("Incorrect input, please try again")
            return False
