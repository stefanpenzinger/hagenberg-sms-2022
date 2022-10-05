_PLAYFAIR_LEN = 5


def create_playfair_matrix(key: str):
    used_chars = []

    for char in key:
        if char == 'J':
            char = 'I'
        if char not in used_chars:
            used_chars.append(char)

    for char in range(65, 91):
        char = chr(char)

        if char == 'J':
            char = 'I'
        if char not in used_chars:
            used_chars.append(char)

    playfair_matrix = [[0 for x in range(_PLAYFAIR_LEN)] for y in range(_PLAYFAIR_LEN)]
    i = 0
    j = 0

    for char in used_chars:
        if i < 5:
            playfair_matrix[j][i] = char
            i = i + 1

        if i == 5:
            i = 0
            j = j + 1

            if j == 5:
                break

    return playfair_matrix


def encrypt(message: str, playfair_matrix: list):
    message = message.upper().replace('J', 'I').replace(' ', '')

    for char in message:
        if 65 > ord(char) > 90:
            message.replace(char, '')

    encrypted_message = ''

    pair = [None] * 2
    tmp = None
    count = 0
    i = 0

    if len(message) % 2 == 1:
        message = message + 'X'

    while i < len(message):
        if tmp is not None:
            pair[0] = tmp
            tmp = None
            pair[1] = message[i]

            i = i + 1
            count = 2

        if count < 2:
            pair[count] = message[i]

            i = i + 1
            count = count + 1

        if count == 2:
            if pair[0] == pair[1]:
                tmp = pair[1]
                pair[1] = 'X'

            index1 = __index_2d(matrix=playfair_matrix, value=pair[0])
            index2 = __index_2d(matrix=playfair_matrix, value=pair[1])

            # Characters in the same row
            if index1[0] == index2[0]:
                if index1[1] == 4:
                    pair[0] = playfair_matrix[index1[0]][0]  # 1, 4
                else:
                    pair[0] = playfair_matrix[index1[0]][index1[1] + 1]  # 1, x

                if index2[1] == 4:
                    pair[1] = playfair_matrix[index2[0]][0]
                else:
                    pair[1] = playfair_matrix[index2[0]][index2[1] + 1]
            # Characters in the same column
            elif index1[1] == index2[1]:
                if index1[0] == 4:
                    pair[0] = playfair_matrix[0][index1[1]]  # 4, 1
                else:
                    pair[0] = playfair_matrix[index1[0] + 1][index1[1]]  # x, 1

                if index2[0] == 4:
                    pair[1] = playfair_matrix[0][index2[1]]
                else:
                    pair[1] = playfair_matrix[index2[0] + 1][index2[1]]
            # Otherwise
            else:
                pair[0] = playfair_matrix[index1[0]][index2[1]]
                pair[1] = playfair_matrix[index2[0]][index1[1]]

            encrypted_message = encrypted_message + pair[0] + pair[1]
            count = 0

    return encrypted_message


def decrypt(encrypted_message: str, playfair_matrix: list):
    encrypted_message = encrypted_message.replace(' ', '').upper().replace('J', 'I')
    decrypted_message = ''
    pair = [None] * 2
    i = 0

    if len(encrypted_message) % 2 == 1:
        exit('ERROR - Message was not encrypted with playfair')

    while i < len(encrypted_message):
        index1 = __index_2d(matrix=playfair_matrix, value=encrypted_message[i])
        index2 = __index_2d(matrix=playfair_matrix, value=encrypted_message[i + 1])

        # Characters in the same row
        if index1[0] == index2[0]:
            if index1[1] == 0:
                pair[0] = playfair_matrix[index1[0]][4]  # 1, 4
            else:
                pair[0] = playfair_matrix[index1[0]][index1[1] - 1]  # 1, x

            if index2[1] == 4:
                pair[1] = playfair_matrix[index2[0]][4]
            else:
                pair[1] = playfair_matrix[index2[0]][index2[1] - 1]
        # Characters in the same column
        elif index1[1] == index2[1]:
            if index1[0] == 0:
                pair[0] = playfair_matrix[4][index1[1]]  # 4, 1
            else:
                pair[0] = playfair_matrix[index1[0] - 1][index1[1]]  # x, 1

            if index2[0] == 4:
                pair[1] = playfair_matrix[4][index2[1]]
            else:
                pair[1] = playfair_matrix[index2[0] - 1][index2[1]]
        # Otherwise
        else:
            pair[0] = playfair_matrix[index1[0]][index2[1]]
            pair[1] = playfair_matrix[index2[0]][index1[1]]

        decrypted_message = decrypted_message + pair[0] + pair[1]
        i = i + 2

    return decrypted_message.replace('X', '')


def __index_2d(matrix, value):
    for i, x in enumerate(matrix):
        if value in x:
            return i, x.index(value)
