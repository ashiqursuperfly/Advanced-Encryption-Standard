from encryption import encrypt16


def append_to_file(content: str, filename: str = "encrypted"):
    file = open(filename, "a")
    file.write(content)
    file.close()


def encrypt_file(filename: str, key: str):
    file = open(filename, 'r')

    for line in file:
        while len(line) != 0:
            to_encrypt = line[0:16]
            line = line[16:]
            print(to_encrypt)
            append_to_file(encrypt16(key=key, plaintext=to_encrypt) + '\n')


if __name__ == "__main__":
    encrypt_file('input.txt', "Thats My Kung Fu Dasdas dasdas")
