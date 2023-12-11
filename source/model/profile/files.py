import os


class Files:
    '''manage and show profile files'''

    def __init__(self, dir_name):
        self.dir = dir_name
        self.files = []

    def add(self, index_list, file_name):
        self.files.insert(index_list, file_name)

    def all(self):
        for file in os.listdir(self.dir):
            if os.path.isfile(os.path.join(self.dir, file)):
                self.files.append(file)
        return self.files

