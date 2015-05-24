from random import randint  # za zar4eto posle
from enemy import Enemy
from hero import Hero
from spell import Spell
from weapon import Weapon


class Map:

    def __init__(self, file_name):
        f = open(file_name)
        self.txt_map = f.read().split('\n')
        for index in range(0, len(self.txt_map)):
            self.txt_map[index] = list(self.txt_map[index])
        self.spawn_positions = []
        self.enemies = []
        self.hero = None
        f.close()

    def print_map(self):
        for element in self.txt_map:
            for a in element:
                print(a, end='')
            print()

    def spawn(self, hero):

        self.hero = hero

        spawn = 0
        num_enemies = 0
        for row in range(0, len(self.txt_map)):
            for column in range(0, len(self.txt_map[row])):
                if self.txt_map[row][column] == 'S':
                    spawn += 1
                    if spawn == 1:
                        self.hero.row = row
                        self.hero.column = column
                        self.txt_map[row][column] = 'H'
                    else:
                        self.spawn_positions.append([row, column])
                if self.txt_map[row][column] == 'E':
                    self.enemies.append(Enemy(100, 100, 20, row, column))
                    num_enemies += 1

        if spawn is not 0:
            return True

        print('Game Over!')
        return False

    def move_hero(self, position):
        h_r = self.hero.row
        h_c = self.hero.column

        if position == 'left':
            if self.txt_map[h_r][h_c - 1] == '#':
                return False
            else:
                self.hero.column -= 1
                self.txt_map[h_r][h_c] = '.'
                self.map_element(self.txt_map[h_r][h_c - 1])
                self.txt_map[h_r][h_c - 1] = 'H'
                return True

        if position == 'right':
            if self.txt_map[h_r][h_c + 1] == '#':
                return False
            else:
                self.hero.column += 1
                self.txt_map[h_r][h_c] = '.'
                self.map_element(self.txt_map[h_r][h_c + 1])
                self.txt_map[h_r][h_c + 1] = 'H'
                return True

        if position == 'up':
            if self.txt_map[h_r-1][h_c] == '#':
                return False
            else:
                self.hero.column -= 1
                self.txt_map[h_r][h_c] = '.'
                self.map_element(self.txt_map[h_r-1][h_c])
                self.txt_map[h_r-1][h_c] = 'H'
                return True

        if position == 'down':
            if self.txt_map[h_r+1][h_c] == '#':
                return False
            else:
                self.hero.row += 1
                self.txt_map[h_r][h_c] = '.'
                self.map_element(self.txt_map[h_r+1][h_c])
                self.txt_map[h_r+1][h_c] = 'H'
                return True

    def map_element(self, element):
        h_r = self.hero.row
        h_c = self.hero.column
        # print(element)

    def hero_attack(self, direction, by=None):
        directions = {'up': -1, 'down': 1, 'left': -1, 'right': 1}
        attack_range = 2
        is_start_fight = False
        i = 1
        if by == "Weapon":
            attack_range = 1

        if by == "Spell":
            attack_range = self.hero.get_spell().get_cast_range()

        while i <= attack_range:
            pos = directions[direction] * i
            if direction == 'left' or direction == 'right':
                if self.txt_map[self.hero.row][self.hero.column+pos] == 'E':
                    is_start_fight = True
                    enemy = self.find_enemy(self.hero.row, self.hero.column+pos)
                    break

            if direction == 'up' or direction == 'down':
                if self.txt_map[self.hero.row+pos][self.hero.column] == 'E':
                    is_start_fight = True
                    enemy = self.find_enemy(self.hero.row+pos, self.hero.column)
                    break
            i += 1

        if is_start_fight:
            print('Fight started')
            self.fight(enemy, attack_range, direction, by)
        else:
            print('Nothing in casting range {}'.format(attack_range))

    def fight(self, enemy, attack_range, direction, att_by):
        if enemy is None:
            raise Exception("There is problem with Enemy")

        # att_range = 2
        if att_by == "Weapon":
            dmg_by_spell = self.hero.attack(by="weapon")
        else:
            dmg_by_spell = self.hero.attack(by="spell")
        dmg_by_wep = self.hero.attack(by="weapon")

        while attack_range is not 0:
            if not enemy.is_alive():
                break
            enemy.take_damage(dmg_by_spell)
            print("{} make {} dmg to enemy".format(self.hero.get_name(), dmg_by_spell))
            self.move_hero(direction)
            attack_range -= 1

        if not self.hero.is_alive():
            print("Hero is death")
            self.hero_is_death()
        elif not enemy.is_alive():
            print("Enemy is death")

        else:

            while self.hero.is_alive() and enemy.is_alive():

                enemy.take_damage(dmg_by_wep)
                print("{} make {} dmg to enemy".format(self.hero.get_name(), dmg_by_wep))
                if not enemy.is_alive():
                    break
                self.hero.take_damage(enemy.get_dmg())
                print("Enemy make {} dmg to {}".format(enemy.get_dmg(), self.hero.get_name()))
                if not self.hero.is_alive():
                    break

            if not self.hero.is_alive():
                print("Hero is death")
                self.hero_is_death()
            elif not enemy.is_alive():
                print("Enemy is death")

    def hero_is_death(self):
        row = self.hero.row
        col = self.hero.column

        self.txt_map[row][col] = 'E'

        if len(self.spawn_positions) > 0:

            print("\n Your hero was reborn! \n")

            pos = self.spawn_positions.pop(0)
            self.hero.full_health()
            self.hero.row = pos[0]
            self.hero.column = pos[1]
            self.txt_map[pos[0]][pos[1]] = 'H'
        else:
            print("\n\n GAME OVER!!!")

    def change_map(self, obj):
        if isinstance(obj, Enemy):
            row = obj.row
            col = obj.column

        self.txt_map[row][col] = '.'

    def find_enemy(self, en_row, en_col):
        for i in range(0, len(self.enemies)):
            if self.enemies[i].row == en_row and self.enemies[i].column == en_col:
                return self.enemies[i]
        return None


map = Map('level1.txt')

hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

s = Spell(name="Fireball", damage=10, mana_cost=50, cast_range=2)
hero.learn(s)
w = Weapon(name="The Axe of Destiny", damage=5)
hero.equip(w)

map.spawn(hero)
map.hero_attack(direction='right', by="Spell")

s = Spell(name="Fireball", damage=10, mana_cost=50, cast_range=2)
hero.learn(s)
w = Weapon(name="The Axe of Destiny", damage=10)
hero.equip(w)

map.hero_attack(direction='left')


map.print_map()
