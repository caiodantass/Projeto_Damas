import constantes


def criando_tabuleiro():
    """Gera o trabuleiro de inicío do jogo
    """
    
    print()
    print("\033[7;40m𝙱𝙴𝙼 𝚅𝙸𝙽𝙳𝙾 𝙰𝙾 𝙹𝙾𝙶𝙾 𝙳𝙴 𝙳𝙰𝙼𝙰𝚂!\033[m")
    print()
    
    for l in range(8):
        lista = []
        for c in range(8):
            if (l+c) % 2 == 0:
                if l>=0 and l<=2:
                    lista.append(constantes.brancas)

                elif l >= 3 and l <=4:
                    lista.append(constantes.vazio)

                elif l>=5 and l <=7:
                    lista.append(constantes.pretas)

                else:
                    lista.append(constantes.vazio)
            else:
                lista.append(constantes.vazio)
        constantes.matriz.append(lista)

def imprime_tabuleiro():
    """Imprime o tabuleiro
    """
    
    print("  0|1|2|3|4|5|6|7|")

    for x in range(len(constantes.matriz)):
        for l in range(len(constantes.matriz)):
            if l == 0:
                print(end='{}|{}|'.format(x, constantes.matriz[x][l]))
            else:
                print(constantes.matriz[x][l], end='|')
        print()
