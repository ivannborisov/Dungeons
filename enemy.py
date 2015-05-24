from hero_enemy_base import HeroEnemyBase


class Enemy(HeroEnemyBase):

    def __init__(self, health, mana, damage, row, column):

        super(Enemy, self).__init__(health, mana, row, column)

        self.__damage = damage  # kogato se naloji da slojim getter

    def change_enemy_pos(self, row, col):
        pass

    def get_dmg(self):
        return self.__damage
