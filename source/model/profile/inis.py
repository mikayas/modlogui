import configparser as cfparser


class Ini:
    '''ini file management and changes'''

    def __init__(self, file):
        self.config = cfparser.ConfigParser(allow_no_value=True)
        self.file = file
        self.config.read(self.file)

    def set_value(self, section, key):
        return self.config[section][key]

    def change_value(self, section, key, value):
        self.config.set(section, key, value)
        with open(self.file, 'w') as file:
            self.config.write(file)

