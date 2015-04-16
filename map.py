from random import randint  # za zar4eto posle


class Map:

    def __init__(self, file_name):
        f = open(file_name)
        self.txt_map = f.read().split('\n')
        for index in range(0, len(self.txt_map)):
            self.txt_map[index] = list(self.txt_map[index])
        self.hero_row = None
        self.hero_column = None

    def print_map(self):
        for element in self.txt_map:
            for a in element:
                print(a, end='')
            print()

    def spawn(self):
        for row in range(0, len(self.txt_map)):
            for column in range(0, len(self.txt_map[row])):
                if self.txt_map[row][column] == 'S':
                    self.hero_row = row
                    self.hero_column = column
                    self.txt_map[row][column] = 'H'

                    return True
        return False

    def move_hero(self, direction):
        pass
