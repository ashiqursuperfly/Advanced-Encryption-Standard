from encryption import encrypt16
from bitstring import ConstBitStream


def append_to_file(content: str, filename: str = "out/encrypted"):
    file = open(filename, "a")
    file.write(content)
    file.close()


def encrypt_file(filename: str, key: str):
    file = ConstBitStream(filename=filename)

    read_so_far = 0
    total = file.len

    while True:

        if total - read_so_far < 128:
            bits = file.read(total - read_so_far)
            read_so_far += (total - read_so_far)

            bits = str(bits.__str__())
            bits = bits.ljust(34, '0')

            append_to_file(encrypt16(key=key, hexstring=bits[2:]) + '\n')
            print('read', read_so_far, 'total', total)
            break

        bits = file.read(128)
        append_to_file(encrypt16(key=key, bitstring=bits) + '\n')
        read_so_far += 128
        print('read', read_so_far, 'total', total)

    # only text files
    # to_encrypt = str()
    # for char in line:
    #     to_encrypt += char
    #     if len(to_encrypt) == 16:
    #         append_to_file(encrypt16(key=key, plaintext=to_encrypt) + '\n')
    #         to_encrypt = ''
    #
    # if len(to_encrypt) > 0:
    #     append_to_file(encrypt16(key=key, plaintext=to_encrypt.ljust(16)) + '\n')


if __name__ == "__main__":
    encrypt_file('in/demo.jpg', "Thats My Kung Fu Dasdas dasdas")
