import unittest

from Hero import Hero


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.test_hero = Hero("Ivan", "Ricar", 100, 100, 2)

    def test_known_as(self):
        self.assertEqual("Ivan the Ricar", self.test_hero.known_as())

    def test_get_health(self):
        self.assertEqual(100, self.test_hero.get_health())

    def test_get_mana(self):
        self.assertEqual(100, self.test_hero.get_mana())

    def test_can_cast(self):
        pass

if __name__ == '__main__':
    unittest.main()
