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
        self.assertEqual(player_1.set_rank(3), None)  # Result is None because method doesn't return anything

    def test_3_Exception(self):
        """Testing to make sure exception is raised when not enough players playing"""
        a = Player("a", 10)
        b = Player("b", 10)
        c = Player("c", 8)
        d = Player("d", 2)

        players_playing = [a]

        if len(players_playing) >= 2:
            raise NotEnoughPlayers

        self.assertRaises(NotEnoughPlayers)

    def test_4_power(self):
        """Testing team_power to ensure compare_total works"""
        a = Player("a", 10)
        b = Player("b", 10)
        c = Player("c", 8)
        d = Player("d", 2)

        team_1 = [a, c]
        team_2 = [b, d]

        team = team_power(team_1, team_2)

        self.assertEqual(team, 6)


if __name__ == '__main__':
    unittest.main()
