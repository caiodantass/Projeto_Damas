from constantes import *

def criando_tabuleiro():
    
    print()
    print("\033[7;40m𝙱𝙴𝙼 𝚅𝙸𝙽𝙳𝙾 𝙰𝙾 𝙹𝙾𝙶𝙾 𝙳𝙴 𝙳𝙰𝙼𝙰𝚂!\033[m")
    print()
    
    for l in range(8):
        lista = []
        for c in range(8):
            if (l+c) % 2 == 0:
                if l>=0 and l<=2:
                    lista.append('●')

                elif l >= 3 and l <=4:
                    lista.append(' ')

                elif l>=5 and l <=7:
                    lista.append('○')

                else:
                    lista.append(' ')
            else:
                lista.append(' ')
        matriz.append(lista)
    imprime_tabuleiro()

def imprime_tabuleiro():
    print("  0|1|2|3|4|5|6|7|")

    for x in range(len(matriz)):
        for l in range(len(matriz)):
            if l == 0:
                print(end='{}|{}|'.format(x,matriz[x][l]))
            else:
                print(matriz[x][l], end='|')
        print()