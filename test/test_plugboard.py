
from unittest import TestCase

from src.enigma.plugboard import Plugboard


class TestPlugboard(TestCase):
    def test_empty(self):
        # Arrrange
        plugboard = Plugboard(config=[])
        expected1 = 0
        expected2 = 10
        expected3 = 25

        # Act
        actual1 = plugboard[expected1]
        actual2 = plugboard[expected2]
        actual3 = plugboard[expected3]

        # Assert
        self.assertEqual(expected1, actual1)
        self.assertEqual(expected2, actual2)
        self.assertEqual(expected3, actual3)

    def test_right_to_left(self):
        # Arrrange
        plugboard = Plugboard(config=[(0, 1)])

        # Act
        actual = plugboard[0]

        # Assert
        self.assertEqual(1, actual)

    def test_left_to_right(self):
        # Arrrange
        plugboard = Plugboard(config=[(0, 1)])

        # Act
        actual = plugboard[1]

        # Assert
        self.assertEqual(0, actual)
