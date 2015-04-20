from random import randint  # za zar4eto posle
from enemy import Enemy


class Map:

    def __init__(self, file_name):
        f = open(file_name)
        self.txt_map = f.read().split('\n')
        for index in range(0, len(self.txt_map)):
            self.txt_map[index] = list(self.txt_map[index])
        self.hero_row = None
        self.hero_column = None
        self.spawn_positions = []
        self.enemies = []

    def print_map(self):
        for element in self.txt_map:
            for a in element:
                print(a, end = '')
            print()

    def spawn(self):
        spawn = 0
        num_enemies = 0
        for row in range(0, len(self.txt_map)):
            for column in range(0, len(self.txt_map[row])):
                if self.txt_map[row][column] == 'S':
                    spawn += 1
                    if spawn == 1:
                        self.hero_row = row
                        self.hero_column = column
                        self.txt_map[row][column] = 'H'
                    else:
                        self.spawn_positions.append([row, column])
                if self.txt_map[row][column] == 'E':
                    self.enemies.append(Enemy(100, 100, 5, row, column))
                    num_enemies += 1

        if spawn is not 0:
            return True
        return False

    def move_hero(self, position):
        h_r = self.hero_row
        h_c = self.hero_column

        if position == 'left':
            if self.txt_map[h_r][h_c-1] == '#':
                return False
            else:
                self.hero_column -= 1
                self.txt_map[h_r][h_c] = '.'
                self.map_element(self.txt_map[h_r][h_c-1])
                self.txt_map[h_r][h_c-1] = 'H'
                return True

        if position == 'right':
            if self.txt_map[h_r][h_c+1] == '#':
                return False
            else:
                self.hero_column += 1
                self.txt_map[h_r][h_c] = '.'
                self.map_element(self.txt_map[h_r][h_c+1])
                self.txt_map[h_r][h_c+1] = 'H'
                return True

        if position == 'up':
            if self.txt_map[h_r-1][h_c] == '#':
                return False
            else:
                self.hero_column -= 1
                self.txt_map[h_r][h_c] = '.'
                self.map_element(self.txt_map[h_r-1][h_c])
                self.txt_map[h_r-1][h_c] = 'H'
                return True

        if position == 'down':
            if self.txt_map[h_r+1][h_c] == '#':
                return False
            else:
                self.hero_row += 1
                self.txt_map[h_r][h_c] = '.'
                self.map_element(self.txt_map[h_r+1][h_c])
                self.txt_map[h_r+1][h_c] = 'H'
                return True

    def map_element(self, element):
        h_r = self.hero_row
        h_c = self.hero_column
        print(element)

    def hero_attack(self, direction, by=None):
        directions = {'up': -1, 'down': 1, 'left': -1, 'right': 1}
        attack_range = 2
        is_start_fight = False
        i = 1
        if by is None:
            while i <= attack_range:
                pos = directions[direction] * i
                if direction == 'left' or direction == 'right':
                    if self.txt_map[self.hero_row][self.hero_column+pos] == 'E':
                        is_start_fight = True
                        break

                if direction == 'up' or direction == 'down':
                    if self.txt_map[self.hero_row+pos][self.hero_column] == 'E':
                        is_start_fight = True
                        break
                i += 1

        if is_start_fight:
            print('Fight started')
        else:
            print('Nothing in casting range {}'.format(attack_range))


map = Map('level1.txt')
map.spawn()
# map.hero_attack(direction='right')
print(map.enemies)
print(map.enemies[0].row)
print(map.enemies[0].column)
