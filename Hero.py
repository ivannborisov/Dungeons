class Hero:

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.__name = name
        self.__title = title
        self.__health = health
        self.__mana = mana
        self.__mana_regeneration_rate = mana_regeneration_rate
        self.__spell = None

    def known_as(self):
        return "{} the {}".format(self.__name, self.__title)

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def can_cast(self):
        if(self.__spell is not None or self.__mana < self.__spell.mana_cost):
            return False
        else:
            return True

#     def use_spell(self, spell):
#         if self.can_cast()
#             return True
#         else:
#             raise
