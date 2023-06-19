from string import ascii_uppercase
from .helper import char_to_idx, idx_to_char
from .plugboard import Plugboard
from .rotor import Rotor
from .reflector import Reflector


class EnigmaMachine():
    def __init__(self, *,
                 plugboard: Plugboard,
                 reflector: Reflector,
                 rotor1: Rotor,
                 rotor2: Rotor,
                 rotor3: Rotor):

        self._plugboard = plugboard

        self._reflector = reflector

        self._rotor1 = rotor1
        self._rotor2 = rotor2
        self._rotor3 = rotor3

    def _turn_rotors(self):
        if self._rotor3.step():
            if self._rotor2.step():
                self._rotor1.step()

    def _encrypt(self, i: int) -> int:
        # print('input', idx_to_char(i), i)

        self._turn_rotors()

        i = self._plugboard[i]

        # print('plugboard', idx_to_char(i), i)

        i = self._rotor3.right_to_left(i)
        # print('rotor 3', idx_to_char(i), i)

        i = self._rotor2.right_to_left(i)
        # print('rotor 2', idx_to_char(i), i)

        i = self._rotor1.right_to_left(i)
        # print('rotor 1', idx_to_char(i), i)

        i = self._reflector[i]

        # print('reflector', idx_to_char(i), i)

        i = self._rotor1.left_to_right(i)
        # print('rotor 1', idx_to_char(i), i)

        i = self._rotor2.left_to_right(i)
        # print('rotor 2', idx_to_char(i), i)

        i = self._rotor3.left_to_right(i)
        # print('rotor 3', idx_to_char(i), i)

        i = self._plugboard[i]

        # print('plugboard', idx_to_char(i), i)

        return i

    def encrypt(self, text: str) -> str:
        ciphertext = ''

        for c in text:
            c = c.upper()
            if c not in ascii_uppercase:
                raise Exception('only ascii letters allowed')
            i = char_to_idx(c)
            j = self._encrypt(i)
            ciphertext += idx_to_char(j)

        return ciphertext
