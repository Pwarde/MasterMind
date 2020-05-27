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
        return self.set_settings(current_settings, lookup)

    @staticmethod
    def get_settings():
        try:
            with open("settings.json", "r") as read_file:
                return json.load(read_file)
        except FileNotFoundError:
            print("No settings file present, please make sure settings.json is present")

    def change(self, setting, value):
        text = value.get('new_value_text') or value.get('description')
        try:
            value['value'] = int(input(text))
            return value
        except ValueError:
            print("incorrect value please try again.")
        else:
            print("Incorrect input, please try again")

    def set(self, settings):
        try:
            with open("settings.json", "w") as write_file:
                json.dump(settings, write_file, indent=2)
        except ValueError:
            print("Incorrect input, please make sure settings are valid.")
