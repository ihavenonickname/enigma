from .helper import ALPHABET_SIZE, char_to_idx


class Rotor():
    def __init__(self, *, connections: list[int], notch: int, offset: int):
        self._notch = notch
        self._connections_right_to_left = connections
        self._connections_left_to_right = list(range(ALPHABET_SIZE))
        for i, conn in enumerate(connections):
            self._connections_left_to_right[conn] = i
        self.offset = offset

    def right_to_left(self, i: int) -> int:
        hit = (i + self.offset) % ALPHABET_SIZE

        j = self._connections_right_to_left[hit]

        return (j - self.offset) % ALPHABET_SIZE

    def left_to_right(self, i: int) -> int:
        hit = (i + self.offset) % ALPHABET_SIZE

        j = self._connections_left_to_right[hit]

        return (j - self.offset) % ALPHABET_SIZE

    def step(self) -> bool:
        self.offset = (self.offset + 1) % ALPHABET_SIZE
        return self.offset == self._notch

    @staticmethod
    def Rotor_I(offset: int | str):
        if isinstance(offset, str):
            offset = char_to_idx(offset)

        return Rotor(
            connections=list(map(char_to_idx, 'EKMFLGDQVZNTOWYHXUSPAIBRCJ')),
            notch=char_to_idx('R'),
            offset=offset)

    @staticmethod
    def Rotor_II(offset: int | str):
        if type(offset) == str:
            offset = char_to_idx(offset)

        return Rotor(
            connections=list(map(char_to_idx, 'AJDKSIRUXBLHWTMCQGZNPYFVOE')),
            notch=char_to_idx('F'),
            offset=offset)

    @staticmethod
    def Rotor_III(offset: int | str):
        if type(offset) == str:
            offset = char_to_idx(offset)

        return Rotor(
            connections=list(map(char_to_idx, 'BDFHJLCPRTXVZNYEIWGAKMUSQO')),
            notch=char_to_idx('W'),
            offset=offset)
