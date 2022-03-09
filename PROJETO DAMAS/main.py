from constantes import *
from tabuleiro import *
from movimentacao import *

print()
J1 = input('Jogador 1 (peças "○"), digite seu nome:')
J2 = input('Jogador 2 (peças "●"), digite seu nome:')

criando_tabuleiro()
while True:
    # Condição de fim de jogo
    if quant_pecas_j1 == 0 or quant_pecas_j2 == 0:
        if quant_pecas_j1 != 0:
            print("{} ganhou a partida".format(J1))
        if quant_pecas_j2 != 0:
            print("{} ganhou a partida".format(J2))
        break
   
    ress = False
    
    print()
    print('\033[34mVez do Jogador 1\033[0;0m')
    
    while True:
        # Posição e movimentação do jogador 1
        posicao_l_c = list(map(int, input("\nJogador 1, escolha a posição da peça - (Linha,Coluna):").split()))

        if matriz[posicao_l_c[0]][posicao_l_c[1]] == ' ':
            print('\033[31mPosição inválida, não existe peça nessa posição!\033[0;0m')
        else:
            posicao_l_c_d = list(map(int, input("Jogador 1, escolha a movimentação da peça - (Linha,Coluna):").split()))
            print()
            ress = movimentacao(posicao_l_c[0], posicao_l_c[1], posicao_l_c_d[0], posicao_l_c_d[1], "p")
        if ress == True:
            break
    
    print(f"\033[1mQuantidade de peças do Jogador 1: {quant_pecas_j1}\033[0;0m")
    print(f"\033[1mQuantidade de peças do Jogador 2: {quant_pecas_j2}\033[0;0m")
    print()
    imprime_tabuleiro()
    
    ress = False
    
    print()
    print('\033[34mVez do Jogador 2\033[0;0m')

    while True:
        # Posição e movimentação do jogador 2
        posicao_l_c = list(map(int, input("\nJogador 2, escolha a posição da peça - (Linha,Coluna):").split()))

        if matriz[posicao_l_c[0]][posicao_l_c[1]] == ' ':
            print('\033[31mPosição inválida, não existe peça nessa posição!\033[0;0m')
        else:
            posicao_l_c_d = list(map(int, input("Jogador 2, escolha a movimentação da peça - (Linha,Coluna):").split()))
            print()
            ress = movimentacao(posicao_l_c[0], posicao_l_c[1], posicao_l_c_d[0], posicao_l_c_d[1], "b")
        if ress == True:
            break        
    
    print(f"\033[1mQuantidade de peças do Jogador 1: {quant_pecas_j1}\033[0;0m")
    print(f"\033[1mQuantidade de peças do Jogador 2: {quant_pecas_j2}\033[0;0m")
    print()
    imprime_tabuleiro()
