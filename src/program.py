import argparse
import re
import sys

import enigma


def parse_rotor_argument(expr):
    m = re.match(r'([a-z]+)\s+([a-z])$', expr, re.IGNORECASE)

    if not m:
        raise Exception('Invalid rotor configuration: ' + expr)

    rotor_name = m.group(1).upper()
    rotor_state = m.group(2).upper()

    if rotor_name == 'I':
        return enigma.Rotor.Rotor_I(rotor_state)

    if rotor_name == 'II':
        return enigma.Rotor.Rotor_II(rotor_state)

    if rotor_name == 'III':
        return enigma.Rotor.Rotor_III(rotor_state)

    raise Exception('Unknown rotor: ' + rotor_name)


def parse_reflector_argument(expr: str):
    name = expr.upper()

    if name == 'A':
        return enigma.Reflector.Ukw_A()

    if name == 'B':
        return enigma.Reflector.Ukw_B()

    if name == 'C':
        return enigma.Reflector.Ukw_C()

    raise Exception('Unknown reflector: ' + name)


def parse_plugboard_argument(expr_list):
    connections = []

    for expr in expr_list:
        m = re.match(r'(a-z)(a-z)$', expr, re.IGNORECASE)

        if not m:
            raise Exception('Invalid plugboard connection: ' + expr)

        a = m.group(1).upper()
        b = m.group(2).upper()

        connections.append((a, b))

    return enigma.Plugboard(connections)


def build_enigma_from_args():
    parser = argparse.ArgumentParser(
        prog='Enigma Cipher',
        description='Encrypt text with this Enigma I implementation')

    parser.add_argument(
        '--plugboard',
        required=False,
        action='append',
        default=[],
        help='Plugboard connection: [pair of connected letters]')

    parser.add_argument(
        '--reflector',
        required=True,
        help='Reflector name: [name]')

    parser.add_argument(
        '--rotor1',
        required=True,
        help='Rotor configuration: [name] [top letter]')

    parser.add_argument(
        '--rotor2',
        required=True,
        help='Rotor configuration: [name] [top letter]')

    parser.add_argument(
        '--rotor3',
        required=True,
        help='Rotor configuration: [name] [top letter]')

    args = parser.parse_args()

    return enigma.EnigmaMachine(
        plugboard=parse_plugboard_argument(args.plugboard),
        reflector=parse_reflector_argument(args.reflector),
        rotor1=parse_rotor_argument(args.rotor1),
        rotor2=parse_rotor_argument(args.rotor2),
        rotor3=parse_rotor_argument(args.rotor3))


def read_from_stdin():
    while True:
        plaintext = sys.stdin.read(5)

        if not plaintext:
            return

        yield plaintext.upper().strip()


def main():
    enigma_machine = build_enigma_from_args()

    for plaintext_chunk in read_from_stdin():
        ciphertext = enigma_machine.encrypt(plaintext_chunk)
        print(ciphertext, end='')

    print()


if __name__ == '__main__':
    main()
