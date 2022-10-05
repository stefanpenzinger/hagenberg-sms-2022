import io


def read_file(file_name: str):
    num_of_chars = {}
    file = io.open(file_name, mode="r", encoding="utf-8")

    chiffre: str = file.read()
    file = io.open("Chiffre.txt", mode="r", encoding="utf-8")

    while 1:
        char = file.read(1)
        if not char:
            break

        if ord(char) > 123 or ord(char) < 65:
            continue
        elif char not in num_of_chars.keys():
            num_of_chars[char] = 1
        else:
            num_of_chars[char] = num_of_chars[char] + 1

    file.close()

    print(chiffre)
    print(dict(sorted(num_of_chars.items(), key=lambda item: item[1], reverse=True)))

    plain = chiffre

    plain = plain.replace('W', 'h')
    plain = plain.replace('T', 'w')
    plain = plain.replace('Z', 't')
    plain = plain.replace('E', 'n')
    plain = plain.replace('Q', 'e')
    plain = plain.replace('R', 'b')
    plain = plain.replace('U', 'r')
    plain = plain.replace('S', 'u')
    plain = plain.replace('C', 's')
    plain = plain.replace('Y', 'm')
    plain = plain.replace('I', 'y')
    plain = plain.replace('D', 'i')
    plain = plain.replace('M', 'd')
    plain = plain.replace('O', 'c')
    plain = plain.replace('X', 'o')
    plain = plain.replace('F', 'a')
    plain = plain.replace('L', 'f')
    plain = plain.replace('J', 'l')
    plain = plain.replace('A', 'g')
    plain = plain.replace('G', 'p')
    plain = plain.replace('B', 'k')
    plain = plain.replace('N', 'q')
    plain = plain.replace('H', 'z')
    plain = plain.replace('V', 'v')

    print(plain)
