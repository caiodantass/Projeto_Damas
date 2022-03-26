import constantes
import banco_de_dados
from movimentacao import *

def verifica_entrada(entrada):
    """Verifica se a entrada está correta.

    Args:
        entrada (list): Lista com as informações de entrada.

    Returns:
       bool: Retorna um bool referente a validação de entrada.
    """
    
    if len(entrada) != 2:
        print('\033[31mValor de entrada incorreto. Digite dois valores entre 0 e 7!\033[0;0m')
        return False
    return True

def verifica_empate():
    """Verificação do empate de jogo
    """
    
    # Quantidade de jogadas consecutivas com movimentação da dama e sem captura e sem movimentação de peças normais
    if constantes.quant_jogadas_con_j1 >= 20:
        return True

    # Quantidade de jogadas consecutivas com movimentação da dama e sem captura e sem movimentação de peças normais
    if constantes.quant_jogadas_con_j2 >= 20:
        return True
    
    return False

def verifica_matriz():
    """Verificação de peças a serem capturadas no tabuleiro
    """
    for l in range(8):
        for c in range(8):
            
            vazio = constantes.matriz[l][c] != constantes.vazio
            
            cond_preta = constantes.matriz[l][c] == constantes.pretas
            cond_dama_preta = constantes.matriz[l][c] == constantes.dama_preta
            
            cond_branca = constantes.matriz[l][c] == constantes.brancas
            cond_dama_branca = constantes.matriz[l][c] == constantes.dama_branca
            
            if (vazio and cond_preta):                
                verifica_diagonais(l, c, constantes.brancas, constantes.obrigatorio_branca)
                verifica_diagonais(l, c, constantes.dama_branca, constantes.obrigatorio_branca)
            
            if (vazio and cond_dama_preta):
                verifica_diagonais_dama(l, c, constantes.brancas, constantes.obrigatorio_preta, constantes.dama_preta, True)
                verifica_diagonais_dama(l, c, constantes.dama_branca, constantes.obrigatorio_preta, constantes.dama_preta, True)

            if (vazio and cond_branca):
                verifica_diagonais(l, c, constantes.pretas, constantes.obrigatorio_preta)
                verifica_diagonais(l, c, constantes.dama_preta, constantes.obrigatorio_preta)

            if  (vazio and cond_dama_branca):
                verifica_diagonais_dama(l, c, constantes.pretas, constantes.obrigatorio_branca, constantes.dama_branca, True)
                verifica_diagonais_dama(l, c, constantes.dama_preta, constantes.obrigatorio_branca, constantes.dama_branca, True)

def jogador_nome(n):
    """Verifica o nome de cada jogador

    Args:
        entrada (string): Nome que os jogadores vão colocar.

    Returns:
       string: Nome do jogador 
    """
    return constantes.J1 if n == 1 else constantes.J2


def jogador_peca(n):
    return constantes.pretas if n == 1 else constantes.brancas


def alterna_jogador():
    """Alterna a vez do jogador
    """
    # Passa a vez pro jogador 2 (caso tenha sido a vez do jogador 1)
    if constantes.jogador_atual == 1:
        constantes.jogador_atual = 2

    # ou, passa a vez pro jogador 1 (caso tenha sido a vez do jogador 2)
    elif constantes.jogador_atual == 2:
        constantes.jogador_atual = 1


def imprime_pos_jogada():
    """Informações após a jogada de cada participante.
    """
    print()
    print(f'\033[1mQuantidade de peças do Jogador 1 ("{constantes.pretas}"): {constantes.quant_pecas_j1}\033[0;0m')
    print(f'\033[1mQuantidade de peças do Jogador 2 ("{constantes.brancas}"): {constantes.quant_pecas_j2}\033[0;0m')
    print()
    imprime_tabuleiro()


def start():
    """Verificações das condições de inicío.
    """
    continuar = False
    if banco_de_dados.verifica_memory_card():
        try:
            continuar = int(input("Foram detectados dados no memory card, deseja retornar onde parou? [1: sim | 0: não]: "))
            if continuar != 0 and continuar != 1:
                raise Exception()
        except:
            print("\033[31mValor inválido! Digite 0 ou 1!\033[0;0m")
            return start()
    if continuar:
        banco_de_dados.loadgame()
    else:
        print()
        constantes.J1 = input(f'Jogador 1 (peças "{constantes.pretas}"), digite seu nome: ')
        constantes.J2 = input(f'Jogador 2 (peças "{constantes.brancas}"), digite seu nome: ')
        constantes.jogador_atual = 1
        criando_tabuleiro()

start()

# Execução do programa
while True:
    # Condição de fim de jogo
    if constantes.quant_pecas_j1 == 0 or constantes.quant_pecas_j2 == 0:
        if constantes.quant_pecas_j1 == 0:
            print("\033[32m{} GANHOU A PARTIDA!\033[0;0m".format(constantes.J1))
        if constantes.quant_pecas_j2 == 0:
            print("\033[32m{} GANHOU A PARTIDA!\033[0;0m".format(constantes.J2))
        break
    
    if verifica_empate():
        print("\033[33mPARTIDA EMPATADA!\033[0;0m")
        break

    imprime_pos_jogada()
    
    verifica_matriz()

    print()
    print(f"\033[34mVez do Jogador {constantes.jogador_atual} ('{jogador_peca(constantes.jogador_atual)}')\033[0;0m")

    # Posição e movimentação do jogador
    try:
        posicao_l_c = list(map(int, input(f"\nJogador {constantes.jogador_atual} "
                                        f"('{jogador_nome(constantes.jogador_atual)}'),"
                                        f" escolha a posição da peça - (Linha,Coluna): ").split()))
    except:
        print('\033[31mValor de entrada incorreto. Digite dois valores entre 0 e 7!\033[0;0m')
        continue
    
    if not verifica_entrada(posicao_l_c):
        continue
    
    if (posicao_l_c[0] > 7 or posicao_l_c[0] < 0) or (posicao_l_c[1] > 7 or posicao_l_c[1] < 0):
        print('\033[31mMovimentação inválida, a peça está fora do tabuleiro!\033[0;0m')
        continue
    
    if constantes.matriz[posicao_l_c[0]][posicao_l_c[1]] == constantes.vazio:
        print('\033[31mPosição inválida, não existe peça nessa posição!\033[0;0m')
        continue
    
    try:
        posicao_l_c_d = list(map(int, input(f"Jogador {constantes.jogador_atual} "
                                            f"('{jogador_nome(constantes.jogador_atual)}'),"
                                            f"escolha a movimentação da peça - (Linha,Coluna): ").split()))
    except:
        print()
        print('\033[31mValor de entrada incorreto. Digite dois valores entre 0 e 7!\033[0;0m')
        continue
        
    if not verifica_entrada(posicao_l_c_d):
        continue
    
    if (posicao_l_c_d[0] > 7 or posicao_l_c_d[0] < 0) or (posicao_l_c_d[1] > 7 or posicao_l_c_d[1] < 0):
        print('\033[31mMovimentação inválida, a peça está fora do tabuleiro!\033[0;0m')
        continue
    
    print()
    passa_vez = movimentacao(posicao_l_c[0], posicao_l_c[1], posicao_l_c_d[0], posicao_l_c_d[1], constantes.jogador_atual)
    
    # Se a movimentação terminou com sucesso ou o jogador não deve fazer mais nenhum movimento:
    if passa_vez:
        alterna_jogador()
        
    
    banco_de_dados.savegame()