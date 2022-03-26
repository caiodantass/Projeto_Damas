from tabuleiro import *
import constantes as const

def verifica_posicao(l, c):
    """Verificação de posição dentro do limite do tabuleiro
    
    Args:
        l (int): Linha da matriz
        c (int): Coluna da matriz
    
    Returns:
        bool: Retorna um bool representando o posicionamento dentro da matriz
    """
    try:
        if (l>=0 and l<=7) and (c>=0 and c<=7):
            return const.matriz[l][c]
        else:
            return False
    except:
        pass

def limites_diagonais(l, c):
    """ Análisa os limites diagonais (posição máxima que se
    pode chegar atrávez da diagonal a qual a peça está localizada)
    
    Args:
        l (int): Linha da peça a ser analizada
        c (int): Coluna da peça a ser analizada
        
    Returns:
        list: Retorna uma lista com 4 listas, onde cada uma refere-se
        a uma diagonal.
    """
    if l<=c and l+c<=7:
        direita_descendo = ((- (c - l) + 7), 7)
        direita_subindo = (0, (l + c))
        esquerda_descendo = ((l + c), 0)
        esquerda_subindo = (0, (c - l))
    
    if l>=c and l+c>=7:
        direita_descendo = (7, -(l - c) + 7)
        direita_subindo = ((l + c) - 7, 7)
        esquerda_descendo = (7, (l + c) - 7)
        esquerda_subindo = (l - c, 0)
    
    if l>=c and l+c<=7:
        direita_descendo = (7, -(l - c) + 7)
        direita_subindo = (0, l + c)
        esquerda_descendo = (l + c, 0)
        esquerda_subindo = (l - c, 0)
    
    if l<=c and l+c>=7:
        direita_descendo = (-(c - l) + 7, 7)
        direita_subindo = ((l + c) - 7, 7)
        esquerda_descendo = (7, (l + c) - 7)
        esquerda_subindo = (0, c - l)
    
    return direita_descendo, direita_subindo, esquerda_descendo, esquerda_subindo

def gera_posicoes(l_o, c_o):
    """Gera a lista de posições validas dentro dos limites diagonais.
    
    Args:
        l_o (int): Linha referente a peça a ser analizada
        c_o (int): Coluna referente a peça a ser analizada
        
    Returns:
        list: Lista de posições validas para a movimentação da dama.
    """
    
    pos_validas = []
    
    limites = limites_diagonais(l_o, c_o)

    direita_descendo = limites[0]
    direita_subindo = limites[1]
    esquerda_descendo = limites[2]
    esquerda_subindo = limites[3]
    

    l = l_o - 1
    c = c_o + 1
    while(l>=direita_subindo[0] and c<=direita_subindo[1]):
        pos_validas.append([l, c])
        l -= 1
        c += 1
            
    l = l_o - 1
    c = c_o - 1
    while(l>=esquerda_subindo[0] and c>=esquerda_subindo[1]):
        pos_validas.append([l, c])
        l -= 1
        c -= 1
        
    l = l_o + 1
    c = c_o + 1
    while(l<=direita_descendo[0] and c<=direita_descendo[1]):
        pos_validas.append([l, c])
        l += 1
        c += 1
        
    l = l_o + 1
    c = c_o - 1
    while(l<=esquerda_descendo[0] and c>=esquerda_descendo[1]):
        pos_validas.append([l, c])
        l += 1
        c -= 1
        
    return pos_validas

def peca_a_capturar(l_o, c_o, l_d, c_d, x):
    """Analiza a posição das peças a serem capituradas.
    
    Args:
        l_o (int): Linha referente a peça do jogador atual
        c_o (int): Coluna referente a peça do jogador atual
        l_d (int): Linha referente a posição de destino
        c_d (int): Coluna referente a posição de destino
        x (int): Número representando o jogadro atual
        
    Returns:
        list: lista de coordenadas da peça a capturar
    """
    coordenadas = []
    
    if l_d == l_o + 2:
        # capturando pra baixo
        coordenadas.append(l_d + 1 if x==2 else l_d - 1)  # adiciona a linha de baixo
    elif l_d == l_o - 2:
        # capturando pra cima
        coordenadas.append(l_d - 1 if x==2 else l_d + 1)  # adiciona a linha de cima

    if c_d == c_o + 2:
        # capturando pra direita
        coordenadas.append(c_d + 1 if x==2 else c_d - 1)  # adiciona a coluna da direita
    elif c_d == c_o - 2:
        # capturando pra esquerda
        coordenadas.append(c_d - 1 if x==2 else c_d + 1)  # adiciona a coluna da esquerda

    return coordenadas

def verifica_diagonais_dama(l, c, peca_alvo, lista, peca, pos_captura=False):
    """Verifica as diagonais da dama em busca de peça a capturar.
    
    Args:
        l (int): Linha da peça
        c (int): Coluna da peça
        peca_alvo: Tipo de peça a ser análizada
        lista: Lista de obrigatoriedade de peças
        peca: Tipo de peça do jogador
        pos_captura (bool, opicional): Análise da jogada após a captura de peça.
        
    Returns:
        bool: Retorna um booleano referente a existencia de novas peças a capturar
    """
    
    limites = limites_diagonais(l, c)

    direita_descendo = verificar_movimentacao_dama((l, c), limites[0], peca)
    direita_subindo = verificar_movimentacao_dama((l, c), limites[1], peca)
    esquerda_descendo = verificar_movimentacao_dama((l, c), limites[2], peca)
    esquerda_subindo = verificar_movimentacao_dama((l, c), limites[3], peca)

    # Verifica se tem peça a capturar na direita subindo
    if not direita_subindo[0] and direita_subindo[1] != False:
        pos = direita_subindo[1]
        if verifica_posicao(pos[2],pos[3]) == peca_alvo:
            if pos_captura and (verifica_posicao(pos[0], pos[1]) == const.vazio):
                lista.append([pos[2], pos[3]])
    
    # Verifica se tem peça a capturar na esquerda subindo
    if not esquerda_subindo[0] and esquerda_subindo[1] != False:
        pos = esquerda_subindo[1]
        if verifica_posicao(pos[2],pos[3]) == peca_alvo:
            if pos_captura and (verifica_posicao(pos[0], pos[1]) == const.vazio):
                lista.append([pos[2], pos[3]])
    
    # Verifica se tem peça a capturar na direita descendo
    if not direita_descendo[0] and direita_descendo[1] != False:
        pos = direita_descendo[1]
        if verifica_posicao(pos[2],pos[3]) == peca_alvo:
            if pos_captura and (verifica_posicao(pos[0], pos[1]) == const.vazio):
                lista.append([pos[2], pos[3]])
    
    # Verifica se tem peça a capturar na esquerda descendo
    if not esquerda_descendo[0] and esquerda_descendo[1] != False:
        pos = esquerda_descendo[1]
        if verifica_posicao(pos[2],pos[3]) == peca_alvo:
            if pos_captura and (verifica_posicao(pos[0], pos[1]) == const.vazio):
                lista.append([pos[2], pos[3]])
            
    return pos_captura and len(lista) > 0

def verifica_diagonais(l, c, peca_alvo, lista, pos_captura=False):
    """Verificação das diagonais referente a uma peça normal (não dama)
    
    Args:
        l (int): Linha da peça
        c (int): Coluna da peça
        peca_alvo: Tipo de a ser análizada
        lista: Lista de obrigatoriedade 
        pos_captura (bool, opicional): Análise da jogada após a captura de peça.
        
    Returns:
        bool: Retorna um booleano referente a existencia de novas peças a capturar
    """
        
    #Verificar as diagonais ao lado
    diagonal_superior_esquerda = verifica_posicao(l - 1, c - 1)
    diagonal_superior_direita = verifica_posicao(l - 1, c + 1)
    diagonal_inferior_direita = verifica_posicao(l + 1, c + 1)
    diagonal_inferior_esquerda = verifica_posicao(l + 1, c - 1)
    
    #Lista de posição da diagonal da 2º casa a frente
    diag_sup_esq_2 = [l - 2, c - 2]
    diag_sup_dir_2 = [l - 2, c + 2]
    diag_inf_dir_2 = [l + 2, c + 2]
    diag_inf_esq_2 = [l + 2, c - 2]
    
    #Lista das posições da diagonal da 1º casa a frente
    diag_sup_esq_1 = [l - 1, c - 1]
    diag_sup_dir_1 = [l - 1, c + 1]
    diag_inf_dir_1 = [l + 1, c + 1]
    diag_inf_esq_1 = [l + 1, c - 1]

    if diagonal_superior_direita == peca_alvo:
        if pos_captura and verifica_posicao(diag_sup_dir_2[0], diag_sup_dir_2[1]) == const.vazio:
            lista.append(diag_sup_dir_2)
        elif not pos_captura and diagonal_inferior_esquerda == const.vazio:
            lista.append(diag_inf_esq_1)
            
    if diagonal_superior_esquerda == peca_alvo:
        if pos_captura and verifica_posicao(diag_sup_esq_2[0], diag_sup_esq_2[1]) == const.vazio:
            lista.append(diag_sup_esq_2)
        elif not pos_captura and diagonal_inferior_direita == const.vazio:
            lista.append(diag_inf_dir_1)
            
    if diagonal_inferior_direita == peca_alvo:
        if pos_captura and verifica_posicao(diag_inf_dir_2[0], diag_inf_dir_2[1]) == const.vazio:
            lista.append(diag_inf_dir_2)
        elif not pos_captura and diagonal_superior_esquerda == const.vazio:
            lista.append(diag_sup_esq_1)
            
    if diagonal_inferior_esquerda == peca_alvo:
        if pos_captura and verifica_posicao(diag_inf_esq_2[0], diag_inf_esq_2[1]) == const.vazio:
            lista.append(diag_inf_esq_2)
        elif not pos_captura and diagonal_superior_direita == const.vazio:
            lista.append(diag_sup_dir_1)

    return pos_captura and len(lista) > 0


def captura(l_o, c_o, l_d, c_d, jogador):
    """Realiza a captura da peça de uma peça
    
    Args:
        l_o (int): Linha de origem da jogada
        c_o (int): Coluna de origem da jogada
        l_d (int): Linha de destino da jogada
        c_d (int): Coluna de destino da jogada
        jogador (int): Tipo do jogador
    """

    # Peças pretas
    if jogador == 1:
        
        peca_dir_frente = verifica_posicao(l_o - 1, c_o + 1)
        peca_esq_frente = verifica_posicao(l_o - 1, c_o - 1)
        peca_dir_traz = verifica_posicao(l_o + 1, c_o + 1)
        peca_esq_traz = verifica_posicao(l_o + 1, c_o - 1)
        
        # direita-frente
        if  (peca_dir_frente == const.brancas or peca_dir_frente == const.dama_branca) and (l_o-2 == l_d and c_o+2 == c_d):
            const.quant_pecas_j2 -= 1
            const.matriz[l_d][c_d] = const.pretas if l_d != 0 else const.dama_preta
            const.matriz[l_o - 1][c_o + 1] = const.vazio
            const.matriz[l_o][c_o] = const.vazio

        # esquerda-frente
        elif (peca_esq_frente == const.brancas or peca_esq_frente == const.dama_branca) and (l_o-2 == l_d and c_o-2 == c_d):
            const.quant_pecas_j2 -= 1
            const.matriz[l_d][c_d] = const.pretas if l_d != 0 else const.dama_preta
            const.matriz[l_o - 1][c_o - 1] = const.vazio
            const.matriz[l_o][c_o] = const.vazio
            
        # direta-traz
        elif (peca_dir_traz == const.brancas or peca_dir_traz == const.dama_branca) and (l_o+2 == l_d and c_o+2 == c_d):
            const.quant_pecas_j2 -= 1
            const.matriz[l_d][c_d] = const.pretas if l_d != 0 else const.dama_preta
            const.matriz[l_o + 1][c_o + 1] = const.vazio
            const.matriz[l_o][c_o] = const.vazio
            
        # esquerda-traz
        elif (peca_esq_traz == const.brancas or peca_esq_traz == const.dama_branca) and (l_o+2 == l_d and c_o-2 == c_d):
            const.quant_pecas_j2 -= 1
            const.matriz[l_d][c_d] = const.pretas if l_d != 0 else const.dama_preta
            const.matriz[l_o + 1][c_o - 1] = const.vazio
            const.matriz[l_o][c_o] = const.vazio

    # Peças brancas
    elif jogador == 2:
        
        peca_dir_traz = verifica_posicao(l_o - 1, c_o + 1)
        peca_esq_traz = verifica_posicao(l_o - 1, c_o - 1)
        peca_dir_frente = verifica_posicao(l_o + 1, c_o + 1)
        peca_esq_frente = verifica_posicao(l_o + 1, c_o - 1)
                
        # direita-traz
        if (peca_dir_traz == const.pretas or peca_dir_traz == const.dama_preta) and (l_o-2 == l_d and c_o+2 == c_d):
            const.quant_pecas_j1 -= 1
            const.matriz[l_d][c_d] = const.brancas if l_d != 7 else const.dama_branca
            const.matriz[l_o - 1][c_o + 1] = const.vazio
            const.matriz[l_o][c_o] = const.vazio

        # esquerda-traz
        elif (peca_esq_traz == const.pretas or peca_esq_traz == const.dama_preta) and (l_o-2 == l_d and c_o-2 == c_d):
            const.quant_pecas_j1 -= 1
            const.matriz[l_d][c_d] = const.brancas if l_d != 7 else const.dama_branca
            const.matriz[l_o - 1][c_o - 1] = const.vazio
            const.matriz[l_o][c_o] = const.vazio

        # direita-frente
        elif (peca_dir_frente == const.pretas or peca_dir_frente == const.dama_preta) and (l_o+2 == l_d and c_o+2 == c_d):
            const.quant_pecas_j1 -= 1
            const.matriz[l_d][c_d] = const.brancas if l_d != 7 else const.dama_branca
            const.matriz[l_o + 1][c_o + 1] = const.vazio
            const.matriz[l_o][c_o] = const.vazio

        # esquerda-frente
        elif (peca_esq_frente == const.pretas or peca_esq_frente == const.dama_preta) and (l_o+2 == l_d and c_o-2 == c_d):
            const.quant_pecas_j1 -= 1
            const.matriz[l_d][c_d] = const.brancas if l_d != 7 else const.dama_branca
            const.matriz[l_o + 1][c_o - 1] = const.vazio
            const.matriz[l_o][c_o] = const.vazio

def verificar_movimentacao_dama(origem, destino, peca):
    """Validação da movimentação da dama (verifica a existencia de peças
    dentro da diagonal)
    
    Args:
        origem (list): Lista com as posições de origem da dama
        destino (list): Lista com as posições de destino da dama
        peca (int): Tipo de peça
        
    Returns:
        list: Lista com dois booleanos falsos representando uma jogada
            invalida (há peças no caminho e são aliadas).
        list: Lista com dois booleanos (verdadeiro e falso) representando
            uma jogada livre (não há peças no caminho).
        list: Lista com um booleano e uma lista de valores representando
            uma possivel captura (há peças no caminho e é inimiga).
    """
    
    direita_subindo =   origem[0] > destino[0] and origem[1] < destino[1]
    esquerda_subindo =  origem[0] > destino[0] and origem[1] > destino[1]
    direita_descendo =  origem[0] < destino[0] and origem[1] < destino[1]
    esquerda_descendo = origem[0] < destino[0] and origem[1] > destino[1]
    
    #
    
    
    if direita_subindo:
        l = origem[0] - 1
        c = origem[1] + 1
        while(l>=destino[0] and c<=destino[1]):
            if const.matriz[l][c] != const.vazio:
                if peca == 1 and (const.matriz[l][c] == const.pretas or const.matriz[l][c] == const.dama_preta):
                    return [False, False]
                elif peca == 2 and (const.matriz[l][c] == const.brancas or const.matriz[l][c] == const.dama_branca):
                    return [False, False]
                else:
                    return [False, (l-1, c+1, l, c)] #Diz que a movimentação não pode ocorrer, e diz a posição da peça
            l -= 1
            c += 1
            
    if esquerda_subindo:
        l = origem[0] - 1
        c = origem[1] - 1
        while(l>=destino[0] and c>=destino[1]):
            if const.matriz[l][c] != const.vazio:
                if peca == 1 and (const.matriz[l][c] == const.pretas or const.matriz[l][c] == const.dama_preta):
                    return [False, False]
                elif peca == 2 and (const.matriz[l][c] == const.brancas or const.matriz[l][c] == const.dama_branca):
                    return [False, False]
                else:
                    return [False, (l-1, c-1, l, c)] #Diz que a movimentação não pode ocorrer, e diz a posição da peça
            l -= 1
            c -= 1
            
    if direita_descendo:
        l = origem[0] + 1
        c = origem[1] + 1
        while(l<=destino[0] and c<=destino[1]):
            if const.matriz[l][c] != const.vazio:
                if peca == 1 and (const.matriz[l][c] == const.pretas or const.matriz[l][c] == const.dama_preta):
                    return [False, False]
                elif peca == 2 and (const.matriz[l][c] == const.brancas or const.matriz[l][c] == const.dama_branca):
                    return [False, False]
                else:
                    return [False, (l+1, c+1, l, c)] #Diz que a movimentação não pode ocorrer, e diz a posição da peça
            l += 1
            c += 1
            
    if esquerda_descendo:
        l = origem[0] + 1
        c = origem[1] - 1
        while(l<=destino[0] and c>=destino[1]):
            if const.matriz[l][c] != const.vazio:
                if peca == 1 and (const.matriz[l][c] == const.pretas or const.matriz[l][c] == const.dama_preta):
                    return [False, False]
                elif peca == 2 and (const.matriz[l][c] == const.brancas or const.matriz[l][c] == const.dama_branca):
                    return [False, False]
                else:
                    return [False, (l+1, c-1, l, c)] #Diz que a movimentação não pode ocorrer, e diz a posição da peça
            l += 1
            c -= 1
            
    return [True, False]

def movimentacao(l_o, c_o, l_d, c_d, jogador):
    """Controle da movimentação de peças.
    
    Args:
        l_o (int): Linha de origem da jogada
        c_o (int): Coluna de origem da jogada
        l_d (int): Linha de destino da jogada
        c_d (int): Coluna de destino da jogada
        jogador (int): Tipo do jogador
        
    Returns:
        bool: Retorna um booleano representando a troca de jogador
    """
    # Condições para movimentações não possiveis
    if l_o == l_d:
        print('\033[31mMovimentação inválida, a peça só pode mover para a diagonal!\033[0;0m')
        return False

    if c_o == c_d:
        print('\033[31mMovimentação inválida, a peça só pode mover para a diagonal!\033[0;0m')
        return False

    if const.matriz[l_d][c_d] != const.vazio:
        print('\033[31mMovimentação inválida, já existe uma peça nessa posição!\033[0;0m')
        return False

    # Verifica se é dama
    eh_dama = const.matriz[l_o][c_o] == const.dama_preta or const.matriz[l_o][c_o] == const.dama_branca

    diagonal_proximo = [
        [l_o - 1, c_o - 1], # diagonal superior esquerda
        [l_o - 1, c_o + 1], # diagonal superior direita
        [l_o + 1, c_o + 1], # diagonal inferior direita
        [l_o + 1, c_o - 1]  # diagonal inferior esquerda
    ]

    # Para as peças pretas
    if jogador == 1:

        if const.obrigatorio_preta != [] and [l_d, c_d] in diagonal_proximo:
            print('\033[31mMovimentação inválida, você é obrigado capturar a peça rival!\033[0;0m')
            return False

        if eh_dama and const.matriz[l_o][c_o] == const.dama_preta:
            
            pos_validas = gera_posicoes(l_o, c_o)
            
            if [l_d, c_d] not in pos_validas:
                print('\033[31mMovimentação além do permitido!\033[0;0m')
                return False
            
            nao_tem_peca, peca_meio_1 = verificar_movimentacao_dama((l_o, c_o), (l_d, c_d), jogador)
            
            if nao_tem_peca:
                # Movimentação simples
                const.matriz[l_d][c_d] = const.dama_preta
                const.matriz[l_o][c_o] = const.vazio
                
                const.obrigatorio_preta = []
                const.obrigatorio_branca = []
                
                verifica_dama = verifica_diagonais_dama(l_d, c_d, const.brancas, const.obrigatorio_preta, jogador, True)
                verifica_peca = verifica_diagonais(l_d, c_d, const.brancas, const.obrigatorio_preta, True)  
                #verifica_diagonais(l_d, c_d, const.brancas)
            
                const.quant_jogadas_con_j1 += 1
                
                return True
            
            elif peca_meio_1 != False:
                nao_tem_peca, peca_meio_2 = verificar_movimentacao_dama((peca_meio_1[0], peca_meio_1[1]), (l_d, c_d), jogador)
                if nao_tem_peca and not peca_meio_2:
                    #Captura

                    # Altera a posição da dama
                    const.matriz[l_d][c_d] = const.dama_preta
                    const.matriz[l_o][c_o] = const.vazio

                    const.matriz[peca_meio_1[2]][peca_meio_1[3]] = const.vazio
                    const.quant_pecas_j2 -= 1
                    
                    const.obrigatorio_preta = []
                    const.obrigatorio_branca = []

                    ret = True
                    
                    verifica_dama = verifica_diagonais_dama(l_d, c_d, const.brancas, const.obrigatorio_preta, jogador, True)
                    verifica_peca = verifica_diagonais(l_d, c_d, const.brancas, const.obrigatorio_preta, True)
                    
                    if verifica_dama or verifica_peca:
                        ret = False
                    verifica_diagonais(l_d, c_d, const.brancas, const.obrigatorio_branca)
                    
                    const.quant_jogadas_con_j1 = 0
                    return ret
                
                else:
                    print('\033[31mJogada inválida. Você só pode capturar uma peça de cada vez!\033[0;0m')
                    return False
            else:
                print('\033[31mMovimentação além do permitido!\033[0;0m')
                return False
        elif eh_dama and const.matriz[l_o][c_o] != const.dama_preta:
            print('\033[31mJogada inválida. Vez do jogador 2!\033[0;0m')
            return False
        else:
            #verifica_diagonais(l_o, c_o, const.brancas, const.obrigatorio_preta, True)
            #verifica_diagonais(l_o, c_o, const.brancas, const.obrigatorio_branca)
            # Movimentação simples (quando move apenas uma casa)
            if( (l_d == l_o - 1 and c_d == c_o + 1) or (l_d == l_o - 1 and c_d == c_o - 1)) and const.obrigatorio_preta == []:
                if (l_d != l_o - 1 or c_d != c_o - 1) and (l_d != l_o - 1 or c_d != c_o + 1):
                    print('\033[31mMovimentação além do permitido!\033[0;0m')
                    return False
                else:
                    const.matriz[l_d][c_d] = const.pretas
                    const.matriz[l_o][c_o] = const.vazio
                    
                    const.obrigatorio_preta = []
                    const.obrigatorio_branca = []
                    
                    verifica_diagonais(l_d, c_d, const.brancas, const.obrigatorio_preta, True)
                    verifica_diagonais(l_d, c_d, const.brancas, const.obrigatorio_branca)
                    
                    if l_d == 0:
                        const.matriz[l_d][c_d] = const.dama_preta
                    
                    const.quant_jogadas_con_j1 = 0
                    
                    return True
                
            # Movimentação de captura
            elif const.obrigatorio_preta != []:
                # Se houver alguma peca obrigatoria para capturar
                #peca_a_capturar(l_o, c_o, l_d, c_d, jogador) -> perguntar para que serve...
                if [l_d, c_d] not in const.obrigatorio_preta:
                    print('\033[31mMovimentação inválida, você é obrigado capturar a peça rival!\033[0;0m')
                    return False

                captura(l_o, c_o, l_d, c_d, jogador)
                const.obrigatorio_preta = []
                const.obrigatorio_branca = []
                
                const.quant_jogadas_con_j1 = 0
                
                # Procura nas diagonais se há mais alguma peça inimiga para capturar
                if verifica_diagonais(l_d, c_d, const.brancas, const.obrigatorio_preta, True):
                    # caso haja...
                    # Ainda tem coisa para esse jogador pra fazer,
                    return False    # por isso retorna False para voltar a vez pra ele de novo.
                else:
                    # caso não haja inimigos, verifica se essa peça ficou em uma posição vulnerável
                    verifica_diagonais(l_d, c_d, const.brancas, const.obrigatorio_branca)
                    # caso tenha ficado, adiciona ela na lista de captura dos inimigos
                    return True
            else:
                print('\033[31mMovimentação inválida, a peça só pode mover na diagonal para frente!\033[0;0m')
                return False

    # Para as peças brancas
    elif jogador == 2:

        if const.obrigatorio_branca != [] and [l_d, c_d] in diagonal_proximo:
            print('\033[31mMovimentação inválida, você é obrigado capturar a peça rival!\033[0;0m')
            return False

        if eh_dama and const.matriz[l_o][c_o] == const.dama_branca:
            
            pos_validas = gera_posicoes(l_o, c_o)
            
            if [l_d, c_d] not in pos_validas:
                print('\033[31mMovimentação além do permitido!\033[0;0m')
                return False
            
            nao_tem_peca, peca_meio_1 = verificar_movimentacao_dama((l_o, c_o), (l_d, c_d), jogador)
            
            if nao_tem_peca:
                # Movimentação simples
                const.matriz[l_d][c_d] = const.dama_branca
                const.matriz[l_o][c_o] = const.vazio
                
                const.obrigatorio_preta = []
                const.obrigatorio_branca = []
                
                verifica_diagonais_dama(l_d, c_d, const.pretas, const.obrigatorio_branca, jogador, True)
                verifica_diagonais(l_d, c_d, const.pretas, const.obrigatorio_preta)
                
                const.quant_jogadas_con_j2 += 1
                
                return True
            
            elif peca_meio_1 != False:
                nao_tem_peca, peca_meio_2 = verificar_movimentacao_dama((peca_meio_1[0], peca_meio_1[1]), (l_d, c_d), jogador)
                if nao_tem_peca and not peca_meio_2:
                    #Captura

                    const.matriz[l_d][c_d] = const.dama_branca
                    const.matriz[l_o][c_o] = const.vazio

                    const.matriz[peca_meio_1[2]][peca_meio_1[3]] = const.vazio
                    const.quant_pecas_j1 -= 1
                    
                    const.obrigatorio_preta = []
                    const.obrigatorio_branca = []
                                        
                    ret = True
                    
                    verifica_dama = verifica_diagonais_dama(l_d, c_d, const.pretas, const.obrigatorio_branca, jogador, True)
                    verifica_peca = verifica_diagonais(l_d, c_d, const.pretas, const.obrigatorio_branca, True)
                    
                    if verifica_dama or verifica_peca:
                        ret = False

                    verifica_diagonais(l_d, c_d, const.pretas, const.obrigatorio_preta)
                    
                    const.quant_jogadas_con_j2 = 0
                    
                    return ret
                else:
                    print('\033[31mJogada inválida. Você só pode capturar uma peça de cada vez!\033[0;0m')
                    return False
            else:
                print('\033[31mMovimentação além do permitido!\033[0;0m')
                return False
        elif eh_dama and const.matriz[l_o][c_o] != const.dama_branca:
            print('\033[31mJogada inválida. Vez do jogador 2!\033[0;0m')
            return False
        else:
            #verifica_diagonais(l_o, c_o, const.pretas, const.obrigatorio_branca, True)
            #verifica_diagonais(l_o, c_o, const.pretas, const.obrigatorio_preta)
            # Movimentação simples (quando move apenas uma casa)
            if ((l_d == l_o + 1 and c_d == c_o + 1) or (l_d == l_o + 1 and c_d == c_o - 1)) and const.obrigatorio_branca == []:
                if (l_d != l_o + 1 or c_d != c_o - 1) and (l_d != l_o + 1 or c_d != c_o + 1):
                    print('\033[31mMovimentação além do permitido!\033[0;0m')
                    return False
                else:
                    const.matriz[l_d][c_d] = const.brancas
                    const.matriz[l_o][c_o] = const.vazio
                    
                    const.obrigatorio_preta = []
                    const.obrigatorio_branca = []
                    
                    verifica_diagonais(l_d, c_d, const.pretas, const.obrigatorio_branca, True)
                    verifica_diagonais(l_d, c_d, const.pretas, const.obrigatorio_preta)
                    
                    const.quant_jogadas_con_j2 = 0
                    
                    if l_d == 7:
                        const.matriz[l_d][c_d] = const.dama_branca
                    
                    return True
                
            # Movimentação de captura
            elif const.obrigatorio_branca != []:
                # Se houver alguma peca obrigatoria para capturar
                #peca_a_capturar(l_o, c_o, l_d, c_d, jogador) -> perguntar para que serve...
                if [l_d, c_d] not in const.obrigatorio_branca:
                    print('\033[31mMovimentação inválida, você é obrigado capturar a peça rival!\033[0;0m')
                    return False

                captura(l_o, c_o, l_d, c_d, jogador)
                
                const.obrigatorio_preta = []
                const.obrigatorio_branca = []
                
                const.quant_jogadas_con_j2 = 0

                # Procura nas diagonais se há mais alguma peça inimiga para capturar
                if verifica_diagonais(l_d, c_d, const.pretas, const.obrigatorio_branca, True):
                    # caso haja...
                    print("Captura em sequência!")
                    # Ainda tem coisa para esse jogador pra fazer,
                    return False    # por isso retorna False para voltar a vez pra ele de novo.
                else:
                    # caso não haja inimigos, verifica se essa peça ficou em uma posição vulnerável
                    verifica_diagonais(l_d, c_d, const.pretas, const.obrigatorio_preta)
                    # caso tenha ficado, adiciona ela na lista de captura dos inimigos
                    return True
            else:
                print('\033[31mMovimentação inválida, a peça só pode mover na diagonal para frente!\033[0;0m')
                return False

    return True