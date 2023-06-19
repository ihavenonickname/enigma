from unittest import TestCase
from string import ascii_uppercase

from src.enigma.reflector import Reflector
from src.enigma.helper import string_to_idx, char_to_idx


class TestReflector(TestCase):
    def test_identity(self):
        # Arrrange
        expected = string_to_idx(ascii_uppercase)
        actual = []
        reflector = Reflector(expected)

        # Act
        for c in ascii_uppercase:
            actual.append(reflector[char_to_idx(c)])

        # Assert
        self.assertEqual(expected, actual)

    def test_reversed(self):
        # Arrrange
        expected = string_to_idx('BA' + ascii_uppercase[2:])
        actual = []
        reflector = Reflector(expected)

        # Act
        for i in range(26):
            actual.append(reflector[i])

        # Assert
        self.assertEqual(expected, actual)
