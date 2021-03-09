from BitVector import *

def get_round_constant(round: int):
    
    RC = {
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

    return RC[round]


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

def sbox(hexstr: str, x: str, y: str):
    
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

# TODO: change func name
def shiftrow(hexstring: str):

    if len(hexstring) == 8:
        res = hexstring[2] + hexstring[3] + hexstring[4] + hexstring[5] + hexstring[6] + hexstring[7] + hexstring[0] + hexstring[1]
        return res
    else:
        res = hexstring[0] + hexstring[1] + hexstring[10] + hexstring[11] + hexstring[20] + hexstring[21] + hexstring[30] + hexstring[31]
        res += hexstring[8] + hexstring[9] + hexstring[18] + hexstring[19] + hexstring[28] + hexstring[29] + hexstring[6] + hexstring[7]
        res += hexstring[16] + hexstring[17] + hexstring[26] + hexstring[27] + hexstring[4] + hexstring[5] + hexstring[14] + hexstring[15]
        res += hexstring[24] + hexstring[25] + hexstring[2] + hexstring[3] + hexstring[12] + hexstring[13] + hexstring[22] + hexstring[23]
        return res

def xor(op1hexstr: str, op2hexstr: str):
    
    op1 = BitVector(hexstring=op1hexstr)
    op2 = BitVector(hexstring=op2hexstr)
    res = op1^op2
    
    return res.get_bitvector_in_hex()

def g(w3: str, round: int):
    g_w3 = str(w3)

    # circular byte shift
    g_w3 = shiftrow(g_w3)
    
    # byte substitution
    g_w3 = sub_byte(g_w3)

    # add round constant
    g_w3 = xor(g_w3, get_round_constant(round))

    return g_w3

def generate_round_key(keyhexstr: str, round: int):
    
    # one word == one byte == one ascii character
    w0 = keyhexstr[0:8]
    w1 = keyhexstr[8:16]
    w2 = keyhexstr[16:24]
    w3 = keyhexstr[24:32]
    
    g_w3 = g(w3, round)

    w4 = xor(w0, g_w3)
    w5 = xor(w1, w4)
    w6 = xor(w2, w5)
    w7 = xor(w3, w6)
    
    # 4 words form 1 round key
    return (w4 + w5 + w6 + w7)
    
def mult(bv1: BitVector, bv2: BitVector):
    modulus = BitVector(bitstring='100011011')
    return bv1.gf_multiply_modular(bv2, modulus, 8)

def gps(hexstring: str, idx: int):
    _x =  BitVector(hexstring=hexstring[idx*2 : idx*2 + 2])
    # print(_x.get_bitvector_in_hex())
    return _x

MixCol = BitVector(hexstring="02010103030201010103020101010302").get_bitvector_in_hex()

def get_mix_columned_col(colno: int, hexstr1: str, hexstr2: str):
    _0 = mult(gps(hexstr1, 0), gps(hexstr2, colno * 4)) ^ mult(gps(hexstr1, 4), gps(hexstr2, colno * 4 + 1)) ^mult(gps(hexstr1, 8), gps(hexstr2, colno * 4 + 2)) ^ mult(gps(hexstr1, 12), gps(hexstr2, colno * 4 + 3))
    # print(_0.get_bitvector_in_hex())
    _1 = mult(gps(hexstr1, 1), gps(hexstr2, colno * 4)) ^ mult(gps(hexstr1, 5), gps(hexstr2, colno * 4 + 1)) ^mult(gps(hexstr1, 9), gps(hexstr2, colno * 4 + 2)) ^ mult(gps(hexstr1, 13), gps(hexstr2, colno * 4 + 3))
    # print(_1.get_bitvector_in_hex())
    _2 = mult(gps(hexstr1, 2), gps(hexstr2, colno * 4)) ^ mult(gps(hexstr1, 6), gps(hexstr2, colno * 4 + 1)) ^mult(gps(hexstr1, 10), gps(hexstr2, colno * 4 + 2)) ^ mult(gps(hexstr1, 14), gps(hexstr2, colno * 4 + 3))
    # print(_2.get_bitvector_in_hex())
    _3 = mult(gps(hexstr1, 3), gps(hexstr2, colno * 4)) ^ mult(gps(hexstr1, 7), gps(hexstr2, colno * 4 + 1)) ^mult(gps(hexstr1, 11), gps(hexstr2, colno * 4 + 2)) ^ mult(gps(hexstr1, 15), gps(hexstr2, colno * 4 + 3))
    # print(_3.get_bitvector_in_hex())

    return (_0.get_bitvector_in_hex() + _1.get_bitvector_in_hex() + _2.get_bitvector_in_hex() + _3.get_bitvector_in_hex())


def encryption_round_zero(statematrixstring: str, roundkeys: list):
    return xor(statematrixstring, roundkeys[0])

def encryption_round_one_to_nine(statematrixstring: str, roundkeys: list):

    for round in range(1, 10):

        statematrixstring = sub_byte(statematrixstring)

        statematrixstring = shiftrow(statematrixstring)

        statematrixstring = get_mix_columned_col(0, MixCol, statematrixstring) + get_mix_columned_col(1, MixCol, statematrixstring) + get_mix_columned_col(2, MixCol, statematrixstring) + get_mix_columned_col(3, MixCol, statematrixstring)

        # print("statematrix mxcol", statematrixstring)

        statematrixstring = xor(statematrixstring, roundkeys[round])


    return statematrixstring
    

def encryption_round_ten(statematrixstring: str, roundkeys: list):
    statematrixstring = sub_byte(statematrixstring)

    statematrixstring = shiftrow(statematrixstring)

    # print("statematrix mxcol", statematrixstring)

    statematrixstring = xor(statematrixstring, roundkeys[10])

    return statematrixstring


def encrypt16(key: str, plaintext: str):

    if len(key) != 16 and len(plaintext) != 16:
        raise Exception("Length of key / plaintext segment must be 16") 
    
    key = BitVector(textstring=key)
    plaintext = BitVector(textstring=plaintext)

    statematrixstring = plaintext.get_bitvector_in_hex()
        
    roundkeys = list()
    roundkey = key.get_bitvector_in_hex()
    roundkeys.append(roundkey)
    
    for i in range(1, 11):
        roundkey = generate_round_key(roundkey, i)
        print(i, ':', roundkey)
        roundkeys.append(roundkey)

    statematrixstring = encryption_round_zero(statematrixstring, roundkeys)
    
    statematrixstring = encryption_round_one_to_nine(statematrixstring, roundkeys)
    
    statematrixstring = encryption_round_ten(statematrixstring, roundkeys)

    print("encrypted hash", statematrixstring)

def main():
    encrypt16("Thats my Kung Fu", "Two One Nine Two")

main()            