from .helper import ALPHABET_SIZE, char_to_idx


class Plugboard():
    def __init__(self, *, config: list[tuple[int, int]] | list[tuple[str, str]]):
        self._memo = list(range(ALPHABET_SIZE))

        for a, b in config:
            if isinstance(a, str) and isinstance(b, str):
                a = char_to_idx(a)
                b = char_to_idx(b)

            self._memo[a] = b
            self._memo[b] = a

    def __getitem__(self, i: int) -> int:
        return self._memo[i]
