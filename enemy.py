class Enemy:

    def __init__(self, health, mana, damage):
        self.__health = health
        self.__mana = mana
        self.__damage = damage
        self.__spell = None

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

    def learn(self, spell):
        self.__spell = spell
