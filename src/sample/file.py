import os

class File:
    def read(self, file):
        with open(file, 'r') as file:
            return file.readline()

    def write(self, file, text):
        with open(file, 'w') as file:
            file.write(text)

    def delete(self, file):
        if os.path.exists(file):
            os.remove('path')
        else:
            raise Exception('No such file!')