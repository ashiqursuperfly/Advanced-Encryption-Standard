from decryption import decrypt16


def append_to_file(content: str, filename: str = "decrypted"):
    file = open(filename, "a")
    file.write(content)
    file.close()


def decrypt_file(filename: str, key: str):
    file = open(filename, 'r')

    for line in file:
        to_decrypt = line[0: len(line)-1]
        append_to_file(decrypt16(key=key, ciphertext=to_decrypt))


if __name__ == "__main__":
    decrypt_file('encrypted', "Thats My Kung Fu Dasdas dasdas")
