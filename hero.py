class Hero():

    def __init__(self, name, title, health, mana, mana_regeneration_rate):

        if not isinstance(name, str) or not isinstance(title, str) or not\
                isinstance(health, int) or not isinstance(mana, int) or not\
                isinstance(mana_regeneration_rate, int):
            raise TypeError

        self.__name = name
        self.__title = title
        self.__health = health
        self.__max_health = health
        self.__mana = mana
        self.__max_mana = mana
        self.__mana_regeneration_rate = mana_regeneration_rate
        self.__spell = None
        self.__weapon = None

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
        if self.__spell is None or self.__mana < self.__spell.get_mana_cost():
            return False
        else:
            return True

    def take_damage(self, damage_points):
        if damage_points > self.__health:
            self.__health = 0
        else:
            self.__health -= damage_points

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False

        self.__health += healing_points

        if self.__health > self.__max_health:
            self.__health = self.__max_health

        return True

    def learn(self, spell):
        self.__spell = spell

    def equip(self, weapon):
        self.__weapon = weapon

    def take_mana(self, mana_points=False, potion=False):
        if mana_points is not False:
            self.__mana += mana_points
            if self.__mana > self.__max_mana:
                self.__mana = self.__max_mana
        if potion is not False:
            self.__mana += potion.vol  # 6te pi6em li class Potion?

    def attack(self, by):
        if by == 'weapon' and self.__weapon is not None:
            return self.__weapon.get_damage()
        elif by == 'magic' and self.can_cast():
            return self.__spell.get_damage()
        else:
            return 0
