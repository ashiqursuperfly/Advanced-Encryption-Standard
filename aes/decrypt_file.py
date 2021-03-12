from decryption import decrypt16


def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')


def append_to_file(content: str, filename: str = "out/decrypted"):
    file = open(filename, "ab")
    file.write(bytearray(bitstring_to_bytes(content)))
    file.close()


def decrypt_file(filename: str, key: str):
    file = open(filename, 'r')

    for line in file:
        to_decrypt = line[0: len(line)-1]
        append_to_file(decrypt16(key=key, ciphertext=to_decrypt))


if __name__ == "__main__":
    decrypt_file('out/encrypted', "Thats My Kung Fu Dasdas dasdas")
