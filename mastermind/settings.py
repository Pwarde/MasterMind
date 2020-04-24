import json


class Settings:
    def show_menu(self):
        try:
            current_settings = self.get_settings()
            print('The current game settings are:\n')
            for idx, setting in enumerate(current_settings):
                print(f"{int(idx)+1}. {setting['description']}: {setting['value']}")
            self.set_settings(current_settings)
        except TypeError:
            print("Please make sure there is a valid settings file!")
            return None
        return current_settings

    def get_settings(self):
        try:
            with open("settings.json", "r") as read_file:
                data = json.load(read_file)
                print(data)
                return data
        except:
            print("No settings file present")
            return None

    def set_settings(self, current_settings):
        setting_idx = input('Please type the number of the setting to change. Type M to go back to main menu: \n')
        if setting_idx == 'M':
            return None
        else:
            setting_idx = int(setting_idx) - 1
            setting_dict = current_settings[setting_idx]

            try:
                value = input(setting_dict['new_value_text'])
            except KeyError:
                value = input(setting_dict['description'])

            current_settings[setting_idx][value] = value
            print('aaa')

            with open("settings.json", "w") as write_file:
                json.dumps(current_settings, write_file)
            return current_settings


