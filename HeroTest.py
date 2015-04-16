import unittest

from Hero import Hero
from spell import Spell


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.test_hero = Hero("Ivan", "Ricar", 100, 100, 2)

    def test_known_as(self):
        self.assertEqual("Ivan the Ricar", self.test_hero.known_as())

    def test_is_alive(self):
        self.assertTrue(self.test_hero.is_alive())

    def test_get_health(self):
        self.assertEqual(100, self.test_hero.get_health())

    def test_get_mana(self):
        self.assertEqual(100, self.test_hero.get_mana())

    def test_can_cast_without_spell(self):
        self.assertFalse(self.test_hero.can_cast())

    def test_can_cast_with_affordable_spell(self):
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        self.test_hero.learn(s)
        self.assertTrue(self.test_hero.can_cast())

    def test_can_cast_with_unaffordable_spell(self):
        s = Spell(name="Fireball", damage=30, mana_cost=150, cast_range=2)
        self.test_hero.learn(s)
        self.assertFalse(self.test_hero.can_cast())


if __name__ == '__main__':
    unittest.main()
