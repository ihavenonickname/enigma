ALPHABET_SIZE = 26
UPPERCASE_A_POS_ASCII = 65


def char_to_idx(c: str):
    return ord(c) - UPPERCASE_A_POS_ASCII


def string_to_idx(s: str):
    return [char_to_idx(c) for c in s]


def idx_to_char(i: int):
    return chr(UPPERCASE_A_POS_ASCII + i)
