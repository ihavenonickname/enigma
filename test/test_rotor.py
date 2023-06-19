from unittest import TestCase
from string import ascii_uppercase

from src.enigma.rotor import Rotor
from src.enigma.helper import string_to_idx, char_to_idx

class TestRotor(TestCase):
    def test_cornell_suggestions(self):
        # https://www.cs.cornell.edu/courses/cs3110/2018sp/a1/a1.html

        # Example 1
        rotor = Rotor.Rotor_I(char_to_idx('A'))
        expected = 4
        actual = rotor.right_to_left(0)
        self.assertEqual(expected, actual)

        # Example 2
        rotor = Rotor.Rotor_I(char_to_idx('B'))
        expected = 10
        actual = rotor.right_to_left(0)
        self.assertEqual(expected, actual)

        # Example 3
        rotor = Rotor.Rotor_I(char_to_idx('A'))
        expected = 20
        actual = rotor.left_to_right(0)
        self.assertEqual(expected, actual)

        # Example 4
        rotor = Rotor.Rotor_I(char_to_idx('B'))
        expected = 22
        actual = rotor.left_to_right(0)
        self.assertEqual(expected, actual)


# w2 = Rotor.Rotor_I(char_to_idx('B'))
# print(w2.right_to_left(0))

# w3 = Rotor.Rotor_I(char_to_idx('A'))
# print(w3.left_to_right(0))

# w4 = Rotor.Rotor_I(char_to_idx('B'))
# print(w4.left_to_right(0))

# w5 = Rotor.Rotor_III(char_to_idx('O'))
# print(w5.right_to_left(14))

# w6 = Rotor.Rotor_I(char_to_idx('F'))
# print(w6.left_to_right(10))
