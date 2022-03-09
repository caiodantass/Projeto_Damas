from tabuleiro import *
from constantes import *

def movimentacao(l_o, c_o, l_d, c_d, x):
    # Condições para movimentações não possiveis
    if l_d > 7 or c_d > 7:
        print('\033[31mMovimentação inválida, a peça está fora do tabuleiro!\033[0;0m')
        return False
    
    if l_o == l_d:
        print('\033[31mMovimentação inválida, a peça só pode mover para a diagonal!\033[0;0m')
        return False
    
    if c_o == c_d:
        print('\033[31mMovimentação inválida, a peça só pode mover para a diagonal!\033[0;0m')
        return False
    
    if x == "p":
        # Para as peças pretas
        if matriz[l_d][c_d] != ' ':
                print('\033[31mMovimentação inválida, já existe uma peça nessa posição!\033[0;0m')
                return False
        if ((( c_o < 7 and matriz[l_o - 1][c_o + 1] == '●') or (c_o > 0 and matriz[l_o - 1][c_o - 1] == '●'))):
            if ((l_d != l_o - 2 or c_d != c_o - 2) and (l_d != l_o - 2 or c_d != c_o + 2)):
                print('\033[31mMovimentação além do permitido!\033[0;0m')
                return False
            captura(l_o, c_o, l_d, c_d, x)
        else:
            if ((l_d != l_o - 1 or c_d != c_o - 1) and (l_d != l_o - 1 or c_d != c_o + 1)):
                print('\033[31mMovimentação além do permitido!\033[0;0m')
                return False
            
            else:
                matriz[l_d][c_d] = '○'
            matriz[l_o][c_o] = " "
        

    if x == "b":
        # Para as peças brancas
        if matriz[l_d][c_d] != ' ':
                print('\033[31mMovimentação inválida, já existe uma peça nessa posição!\033[0;0m')
                return False
        if (((c_o < 7 and matriz[l_o + 1][c_o + 1] == '○') or (c_o > 0 and matriz[l_o + 1][c_o - 1] == '○'))):
            if ((l_d != l_o + 2 or c_d != c_o - 2) and (l_d != l_o + 2 or c_d != c_o + 2)):
                print("\033[31mMovimentação além do permitido!\033[0;0m")
                return False
            captura(l_o, c_o, l_d, c_d, x)
        else:
            if ((l_d != l_o + 1 or c_d != c_o - 1) and (l_d != l_o + 1 or c_d != c_o + 1)):
                print("\033[31mMovimentação além do permitido!\033[0;0m")
                return False
            else:
                matriz[l_d][c_d] = '●'
            matriz[l_o][c_o] = " "
    return True

def captura(l_o, c_o, l_d, c_d, x):
    # Captura das peças
    global quant_pecas_j1, quant_pecas_j2
    
    # Peças pretas
    if x == "p":
        #direita
        if matriz[l_d + 1][c_d - 1]  == '●':
            quant_pecas_j2 -= 1
            matriz[l_d][c_d] = '○'
            matriz[l_d + 1][c_d - 1]  = ' '
            matriz[l_o][c_o] = ' '
        
        #esquerda
        elif matriz[l_d + 1][c_d + 1]  == '●':
            quant_pecas_j2 -= 1
            matriz[l_d][c_d] = '○'
            matriz[l_d + 1][c_d + 1]  = ' '
            matriz[l_o][c_o] = ' '
    
    #Peças brancas
    if x == "b":
        #direita
        if matriz[l_d - 1][c_d - 1]  == '○':
            quant_pecas_j1 -= 1
            matriz[l_d][c_d] = '●'
            matriz[l_d - 1][c_d - 1]  = ' '
            matriz[l_o][c_o] = ' '
        
        #esquerda
        elif matriz[l_d - 1][c_d + 1]  == '○':
            quant_pecas_j1 -= 1
            matriz[l_d][c_d] = '●'
            matriz[l_d - 1][c_d + 1]  = ' '
            matriz[l_o][c_o] = ' '