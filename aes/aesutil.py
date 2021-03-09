from BitVector import *


def get_round_constant(round_no: int):
    rc = {
        1: '01000000',
        2: '02000000',
        3: '04000000',
        4: '08000000',
        5: '10000000',
        6: '20000000',
        7: '40000000',
        8: '80000000',
        9: '1b000000',
        10: '36000000'
    }

    return rc[round_no]


"""
    - Removes leading 0x from hex string.
    - returns a two char hex string (adds leading 0 to make single digit hex into double digit)
"""


def format_2_digit_hex(hexdigit):
    _ = hex(hexdigit)[2:]

    if len(_) != 2:
        return '0' + _
    else:
        return _


def sbox(hexstr: str, x: int, y: int):

    Sbox = [
        [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
        [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
        [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
        [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
        [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
        [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
        [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
        [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
        [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
        [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
        [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
        [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
        [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
        [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
        [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
        [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16],
    ]

    return format_2_digit_hex(Sbox[int(hexstr[x], 16)][int(hexstr[y], 16)])


def sub_byte(hexstr: str):
    res = str()

    for i in range(0, len(hexstr) - 1, 2):
        res += sbox(hexstr, i, i + 1)

    return res


def circular_byte_shift(hex_str: str):
    if len(hex_str) == 8:
        res = hex_str[2] + hex_str[3] + hex_str[4] + hex_str[5] + hex_str[6] + hex_str[7] + hex_str[0] + hex_str[1]
        return res
    else:
        res = hex_str[0] + hex_str[1] + hex_str[10] + hex_str[11] + hex_str[20] + hex_str[21] + hex_str[30] + hex_str[31]
        res += hex_str[8] + hex_str[9] + hex_str[18] + hex_str[19] + hex_str[28] + hex_str[29] + hex_str[6] + hex_str[7]
        res += hex_str[16] + hex_str[17] + hex_str[26] + hex_str[27] + hex_str[4] + hex_str[5] + hex_str[14] + hex_str[15]
        res += hex_str[24] + hex_str[25] + hex_str[2] + hex_str[3] + hex_str[12] + hex_str[13] + hex_str[22] + hex_str[23]
        return res


def xor(op1hexstr: str, op2hexstr: str):
    op1 = BitVector(hexstring=op1hexstr)
    op2 = BitVector(hexstring=op2hexstr)
    res = op1 ^ op2

    return res.get_bitvector_in_hex()


def g(w3: str, round_no: int):
    g_w3 = str(w3)

    # circular byte shift
    g_w3 = circular_byte_shift(g_w3)

    # byte substitution
    g_w3 = sub_byte(g_w3)

    # add round constant
    g_w3 = xor(g_w3, get_round_constant(round_no))

    return g_w3


def generate_round_key(key_hex_str: str, round_no: int):
    # one word == one byte == one ascii character
    w0 = key_hex_str[0:8]
    w1 = key_hex_str[8:16]
    w2 = key_hex_str[16:24]
    w3 = key_hex_str[24:32]

    g_w3 = g(w3, round_no)

    w4 = xor(w0, g_w3)
    w5 = xor(w1, w4)
    w6 = xor(w2, w5)
    w7 = xor(w3, w6)

    # 4 words form 1 round key
    return w4 + w5 + w6 + w7


def mult(bv1: BitVector, bv2: BitVector):
    modulus = BitVector(bitstring='100011011')
    return bv1.gf_multiply_modular(bv2, modulus, 8)


def hex_at(hexstr: str, idx: int):
    _x = BitVector(hexstring=hexstr[idx * 2: idx * 2 + 2])
    return _x


def get_mix_columned_col(colno: int, hex2: str, is_inverse: bool = False):
    mix_col = "02010103030201010103020101010302"
    inv_mix_col = "02010103030201010103020101010302"

    hex1 = mix_col if is_inverse else inv_mix_col

    _0 = mult(hex_at(hex1, 0), hex_at(hex2, colno * 4)) ^ mult(hex_at(hex1, 4), hex_at(hex2, colno * 4 + 1)) ^ mult(hex_at(hex1, 8), hex_at(hex2, colno * 4 + 2)) ^ mult(hex_at(hex1, 12), hex_at(hex2, colno * 4 + 3))
    # print(_0.get_bitvector_in_hex())
    _1 = mult(hex_at(hex1, 1), hex_at(hex2, colno * 4)) ^ mult(hex_at(hex1, 5), hex_at(hex2, colno * 4 + 1)) ^ mult(hex_at(hex1, 9), hex_at(hex2, colno * 4 + 2)) ^ mult(hex_at(hex1, 13), hex_at(hex2, colno * 4 + 3))
    # print(_1.get_bitvector_in_hex())
    _2 = mult(hex_at(hex1, 2), hex_at(hex2, colno * 4)) ^ mult(hex_at(hex1, 6), hex_at(hex2, colno * 4 + 1)) ^ mult(hex_at(hex1, 10), hex_at(hex2, colno * 4 + 2)) ^ mult(hex_at(hex1, 14), hex_at(hex2, colno * 4 + 3))
    # print(_2.get_bitvector_in_hex())
    _3 = mult(hex_at(hex1, 3), hex_at(hex2, colno * 4)) ^ mult(hex_at(hex1, 7), hex_at(hex2, colno * 4 + 1)) ^ mult(hex_at(hex1, 11), hex_at(hex2, colno * 4 + 2)) ^ mult(hex_at(hex1, 15), hex_at(hex2, colno * 4 + 3))
    # print(_3.get_bitvector_in_hex())

    return _0.get_bitvector_in_hex() + _1.get_bitvector_in_hex() + _2.get_bitvector_in_hex() + _3.get_bitvector_in_hex()
