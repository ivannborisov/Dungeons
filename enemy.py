from hero_enemy_base import HeroEnemyBase


class Enemy(HeroEnemyBase):

    def __init__(self, health, mana, damage):

        super(Enemy, self).__init__(health, mana)

        self.__damage = damage  # kogato se naloji da slojim getter
