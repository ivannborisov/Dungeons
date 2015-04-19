import unittest

from enemy import Enemy
from spell import Spell


class HeroTest(unittest.TestCase):
    def setUp(self):
        self.test_enemy = Enemy(100, 100, 20)

    # def test_can_cast_without_spell(self):
    #     self.assertFalse(self.test_enemy.can_cast())

    # def test_can_cast_with_affordable_spell(self):
    #     s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
    #     self.test_enemy.learn(s)
    #     self.assertTrue(self.test_enemy.can_cast())

    # def test_can_cast_with_unaffordable_spell(self):
    #     s = Spell(name="Fireball", damage=30, mana_cost=150, cast_range=2)
    #     self.test_enemy.learn(s)
    #     self.assertFalse(self.test_enemy.can_cast())

if __name__ == '__main__':
    unittest.main()
