ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ROTOR_1_MAPPING = 'JGDQOXUSCAMIFRVTPNEWKBLZYH'
ROTOR_2_MAPPING = 'NTZPSFBOKMWRCJDIVLAEYUXHGQ'
ROTOR_3_MAPPING = 'JVIUBHTCDYAKEQZPOSGXNRMWFL'


def enigma(x: int, y: int, z: int, plug: str, plain: str):
    cipher = ''
    count = 0
    plain = plain.upper()

    plug_split = plug.split(',')
    alphabet = list(ALPHABET)

    for plug_arr in plug_split:
        plug_arr = plug_arr.split(':')
        char1 = plug_arr[0]
        char2 = plug_arr[1]
        index1 = alphabet.index(char1)
        index2 = alphabet.index(char2)
        alphabet[index1] = char2
        alphabet[index2] = char1

    alphabet = "".join(alphabet)

    new_rotor_1_map = ROTOR_1_MAPPING[len(ROTOR_1_MAPPING) - x:] + ROTOR_1_MAPPING[0:len(ROTOR_1_MAPPING) - x]
    print(new_rotor_1_map)
    new_rotor_2_map = ROTOR_2_MAPPING[len(ROTOR_2_MAPPING) - y:] + ROTOR_2_MAPPING[0:len(ROTOR_2_MAPPING) - y]
    print(new_rotor_2_map)
    new_rotor_3_map = ROTOR_3_MAPPING[len(ROTOR_3_MAPPING) - z:] + ROTOR_3_MAPPING[0:len(ROTOR_3_MAPPING) - z]
    print(new_rotor_3_map)

    for char in plain:
        if ord(char) < 65 or ord(char) > 90:
            cipher = cipher + char
            continue

        if count > 0 and count % 7 == 0:
            new_rotor_2_map = new_rotor_2_map[len(new_rotor_2_map) - 1:] + new_rotor_2_map[0:len(new_rotor_2_map) - 1]
        if count > 0 and count % 49 == 0:
            new_rotor_3_map = new_rotor_3_map[len(new_rotor_3_map) - 1:] + new_rotor_3_map[0:len(new_rotor_3_map) - 1]

        index = alphabet.index(char)
        r1_char_map = new_rotor_1_map[index]

        index = alphabet.index(r1_char_map)
        r2_char_map = new_rotor_2_map[index]

        index = alphabet.index(r2_char_map)
        r3_char_map = new_rotor_3_map[index]

        index = (index + 13) % 26
        r3_char_map = new_rotor_3_map[index]

        index = alphabet.index(r3_char_map)
        r2_char_map = new_rotor_2_map[index]

        index = alphabet.index(r2_char_map)
        r1_char_map = new_rotor_1_map[index]

        index = alphabet.index(r1_char_map)
        cipher = cipher + alphabet.__getitem__(index)

        count = count + 1
        new_rotor_1_map = new_rotor_1_map[len(new_rotor_1_map) - 1:] + new_rotor_1_map[0:len(new_rotor_1_map) - 1]

    return cipher
