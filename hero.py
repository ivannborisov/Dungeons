from hero_enemy_base import HeroEnemyBase


class Hero(HeroEnemyBase):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):

        super(Hero, self).__init__(health, mana, 0, 0)

        if not isinstance(name, str) or not isinstance(title, str) or not\
                isinstance(mana_regeneration_rate, int):
            raise TypeError

        self.__name = name
        self.__title = title
        self.__mana_regeneration_rate = mana_regeneration_rate  # kogato se naloji da slojim getter

    def known_as(self):
        return "{} the {}".format(self.__name, self.__title)

    def get_name(self):
        return self.__name
