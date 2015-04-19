import unittest

from hero import Hero
from spell import Spell
from weapon import Weapon


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.test_hero = Hero("Ivan", "Ricar", 80, 70, 2)

    def test_known_as(self):
        self.assertEqual("Ivan the Ricar", self.test_hero.known_as())

    def test_is_alive(self):
        self.assertTrue(self.test_hero.is_alive())

    def test_is_dead(self):
        self.test_hero.take_damage(85)
        self.assertFalse(self.test_hero.is_alive())

    def test_get_health(self):
        self.assertEqual(80, self.test_hero.get_health())

    def test_get_mana(self):
        self.assertEqual(70, self.test_hero.get_mana())

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

    def test_take_damage(self):
        self.test_hero.take_damage(35)
        self.assertEqual(45, self.test_hero.get_health())

    def test_take_more_damage_than_health(self):
        self.test_hero.take_damage(85)
        self.assertFalse(self.test_hero.is_alive())
        self.assertEqual(0, self.test_hero.get_health())

    def test_cannot_heal_dead_hero(self):
        self.test_hero.take_damage(80)
        self.assertFalse(self.test_hero.take_healing(5))

    def test_take_healing(self):
        self.test_hero.take_damage(60)
        self.test_hero.take_healing(35)
        self.assertEqual(55, self.test_hero.get_health())

    def test_take_healing_more_than_max_health(self):
        self.test_hero.take_damage(10)
        self.test_hero.take_healing(20)
        self.assertEqual(80, self.test_hero.get_health())

    def test_take_more_mana_than_max_mana(self):
        self.test_hero.set_mana(30)
        self.test_hero.take_mana(mana_points=50)
        self.assertEqual(70, self.test_hero.get_mana())

    def test_take_mana(self):
        self.test_hero.set_mana(40)
        self.test_hero.take_mana(mana_points=20)
        self.assertEqual(60, self.test_hero.get_mana())

    def test_attack_with_available_weapon(self):
        w = Weapon(name="The Axe of Destiny", damage=20)
        self.test_hero.equip(w)
        self.assertEqual(20, self.test_hero.attack('weapon'))

    def test_attack_with_weapon_without_weapon(self):
        self.assertEqual(0, self.test_hero.attack('weapon'))

    def test_attack_with_available_magic(self):
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        self.test_hero.learn(s)
        self.assertEqual(30, self.test_hero.attack('magic'))

    def test_attack_with_magic_without_magic(self):
        self.assertEqual(0, self.test_hero.attack('magic'))


if __name__ == '__main__':
    unittest.main()
