from .helper import char_to_idx


class Reflector():
    def __init__(self, connections: list[int]):
        self._connections = connections

    def __getitem__(self, i: int) -> int:
        return self._connections[i]

    @staticmethod
    def Ukw_A():
        return Reflector(list(map(char_to_idx, 'EJMZALYXVBWFCRQUONTSPIKHGD')))

    @staticmethod
    def Ukw_B():
        return Reflector(list(map(char_to_idx, 'YRUHQSLDPXNGOKMIEBFZCWVJAT')))

    @staticmethod
    def Ukw_C():
        return Reflector(list(map(char_to_idx, 'FVPJIAOYEDRZXWGCTKUQSBNMHL')))
