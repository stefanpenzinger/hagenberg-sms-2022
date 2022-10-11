import ex_1_1
import ex_1_2
import bonus


if __name__ == '__main__':
    print("EX 1.1")
    filename = "Chiffre.txt"
    ex_1_1.read_file(filename)

    print("\nEX 1.2")
    play_fair_matrix = ex_1_2.create_playfair_matrix('PASSWORD')

    print(play_fair_matrix)
    print(ex_1_2.encrypt('SECURE MESSAGE', play_fair_matrix))
    print(ex_1_2.decrypt('OBRYDRTDBSWSKD', play_fair_matrix))

    print("\nEX Bonus")
    print(bonus.enigma(0, 0, 0, "A:H,D:P,X:Y", 'HELLO WORLD'))
