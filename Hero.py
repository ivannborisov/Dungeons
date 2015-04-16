class Hero:

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        if not isinstance(name, str) or not isinstance(title, str) or not\
                isinstance(health, int) or not isinstance(mana, int) or not\
                isinstance(mana_regeneration_rate, int):
            raise TypeError
        self.__name = name
        self.__title = title
        self.__health = health
        self.__mana = mana
        self.__mana_regeneration_rate = mana_regeneration_rate
        self.__spell = None

    def known_as(self):
        return "{} the {}".format(self.__name, self.__title)

    def is_alive(self):
        return self.__health > 0

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

# set_mana only for tests
    def set_mana(self, mana):
        self.__mana = mana

    def can_cast(self):
        if self.__spell is None or self.__mana < self.__spell.mana_cost:
            return False
        else:
            return True

    def take_damage(self, damage):
        if(damage > self.__health):
            self.__health = 0
        else:
            self.__health -= damage

    def take_healing(self, healing_points):

        if self.__health == 0:
            return False

        self.__health += healing_points

        if(self.__health > 100):
            self.__health = 100
        return True

    def learn(self, spell):
        self.__spell = spell

    def take_mana(self, mana_points=False, potion=False):
        if mana_points is not False:
            self.__mana += mana_points
            if self.__mana > 100:
                self.__mana = 100
        if potion is not False:
            self.__mana += potion.vol
