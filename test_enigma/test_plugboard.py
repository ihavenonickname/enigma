
from unittest import TestCase

from src.enigma.plugboard import Plugboard

class TestPlugboard(TestCase):
    def test_empty(self):
        # Arrrange
        plugboard = Plugboard()
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

# plugboard = Plugboard([
#     # ('R', 'C'),
#     # ('A', 'B'),
# ])

# enigma = EnigmaMachine(
#     plugboard=plugboard,
#     rotor1=Rotor.Rotor_I(char_to_idx('X')),
#     rotor2=Rotor.Rotor_II(char_to_idx('P')),
#     rotor3=Rotor.Rotor_III(char_to_idx('N')))

# for i in range(5):
#     plaintext = 'AAAAA'
#     ciphertext = enigma.encrypt(plaintext)
#     print(ciphertext)



# w1 = Rotor.Rotor_I(char_to_idx('A'))
# print(w1.right_to_left(0))

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
