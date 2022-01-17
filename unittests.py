import unittest
from TeamRandomizer import *


class TestingTeamRandomizer(unittest.TestCase):
    """Class responsible for running assertions to test TeamRandomizer classes to ensure they work as intended."""

    def test_1_Person(self):
        """Testing Person class specifically get_name method."""

        person_1 = Person("John")

        self.assertEqual(person_1.get_name(), "John")

    def test_2_Player(self):
        """
        Testing Player class and ensuring methods are inhirted correctly from Person class.
        Testing get_rank and set_rank methods.
        """

        player_1 = Player("John", 5)

        self.assertEqual(player_1.get_name(), "John")
        self.assertEqual(player_1.get_rank(), 5)
        self.assertEqual(player_1.set_rank(3), None)    # Result is None because method doesn't return anything


if __name__ == '__main__':
    unittest.main()
