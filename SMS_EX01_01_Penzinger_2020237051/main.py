import ex_1_1
import ex_1_2


if __name__ == '__main__':
    # EX 1.1
    # filename = "Chiffre.txt"
    # read_file(filename)

    # EX 1.2
    play_fair_matrix = ex_1_2.create_playfair_matrix('PASSWORD')

    print(play_fair_matrix)
    print(ex_1_2.encrypt('SECURE MESSAGE', play_fair_matrix))
    print(ex_1_2.decrypt('OBRYDRTDBSWSKD', play_fair_matrix))
