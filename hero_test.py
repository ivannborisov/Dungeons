import unittest

from hero import Hero


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.test_hero = Hero("Ivan", "Ricar", 80, 70, 2)

    def test_known_as(self):
        self.assertEqual("Ivan the Ricar", self.test_hero.known_as())

if __name__ == '__main__':
    unittest.main()
