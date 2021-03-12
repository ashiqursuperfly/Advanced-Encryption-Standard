from aesutil import *
from BitVector import *


def encryption_round_zero(state_matrix_str: str, round_keys: list):
    return xor(state_matrix_str, round_keys[0])


def encryption_round_one_to_nine(state_matrix_str: str, round_keys: list):
    for rk_no in range(1, 10):
        state_matrix_str = sub_byte(state_matrix_str)
        state_matrix_str = circular_byte_shift(state_matrix_str)
        state_matrix_str = get_mix_columned_col(0, state_matrix_str) + get_mix_columned_col(1, state_matrix_str) + get_mix_columned_col(2, state_matrix_str) + get_mix_columned_col(3, state_matrix_str)
        state_matrix_str = xor(state_matrix_str, round_keys[rk_no])

    return state_matrix_str


def encryption_round_ten(state_matrix_str: str, round_keys: list):
    state_matrix_str = sub_byte(state_matrix_str)
    state_matrix_str = circular_byte_shift(state_matrix_str)
    state_matrix_str = xor(state_matrix_str, round_keys[10])

    return state_matrix_str


def encrypt16(key: str, bitstring: str = None, hexstring: str = None, textstring: str = None):

    key = key.rjust(16, '0')
    key = key[0:16]

    if len(key) != 16:
        raise Exception("Length of key / bitstring segment must be 16")

    key = BitVector(textstring=key)

    if bitstring is not None:
        to_encrypt = BitVector(bitstring=bitstring)
    elif hexstring is not None:
        to_encrypt = BitVector(hexstring=hexstring)
        print(hexstring)
    else:
        to_encrypt = BitVector(textstring=textstring)

    state_matrix_str = to_encrypt.get_bitvector_in_hex()

    round_keys = list()
    round_key = key.get_bitvector_in_hex()
    round_keys.append(round_key)

    for i in range(1, 11):
        round_key = generate_round_key(round_key, i)
        # print(i, ':', round_key)
        round_keys.append(round_key)

    state_matrix_str = encryption_round_zero(state_matrix_str, round_keys)
    state_matrix_str = encryption_round_one_to_nine(state_matrix_str, round_keys)
    state_matrix_str = encryption_round_ten(state_matrix_str, round_keys)

    print("encrypted: ", state_matrix_str)

    return state_matrix_str


def main():
    encrypt16("Thats my Kung Fu hahagg", textstring="Two One Nine Two")


if __name__ == '__main__':
    main()
