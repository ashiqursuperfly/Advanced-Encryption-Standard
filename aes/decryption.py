from aesutil import *
from BitVector import *


def decryption_round_zero(state_matrix_str: str, round_keys: list):
    return xor(state_matrix_str, round_keys[10])


def decryption_round_one_to_nine(state_matrix_str: str, round_keys: list):

    for rk_no in range(9, 0, -1):
        state_matrix_str = circular_byte_shift(state_matrix_str, inverse=True)
        state_matrix_str = sub_byte(state_matrix_str, inverse=True)
        state_matrix_str = xor(state_matrix_str, round_keys[rk_no])
        state_matrix_str = get_mix_columned_col(0, state_matrix_str, inverse=True) + get_mix_columned_col(1, state_matrix_str, inverse=True) + get_mix_columned_col(2, state_matrix_str, inverse=True) + get_mix_columned_col(3, state_matrix_str, inverse=True)

    return state_matrix_str


def decryption_round_ten(state_matrix_str: str, round_keys: list):

    state_matrix_str = circular_byte_shift(state_matrix_str, inverse=True)
    state_matrix_str = sub_byte(state_matrix_str, inverse=True)
    state_matrix_str = xor(state_matrix_str, round_keys[0])

    return state_matrix_str


def decrypt16(key: str, ciphertext: str):

    key = key.rjust(16)

    if len(key) != 16:
        raise Exception("Length of key must be 16")

    key = BitVector(textstring=key)
    ciphertext = BitVector(hexstring=ciphertext)

    state_matrix_str = ciphertext.get_bitvector_in_hex()

    round_keys = list()
    round_key = key.get_bitvector_in_hex()
    round_keys.append(round_key)

    for i in range(1, 11):
        round_key = generate_round_key(round_key, i)
        # print(i, ':', round_key)
        round_keys.append(round_key)

    state_matrix_str = decryption_round_zero(state_matrix_str, round_keys)
    state_matrix_str = decryption_round_one_to_nine(state_matrix_str, round_keys)
    state_matrix_str = decryption_round_ten(state_matrix_str, round_keys)
    print("decrypted text", BitVector(hexstring=state_matrix_str).get_bitvector_in_ascii())


def main():
    decrypt16("Thats my ", "d3ca1cc9976600146bf908afa1cc3b6d")


if __name__ == '__main__':
    main()
