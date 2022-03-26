import pickle
import constantes

def savegame():
    """Realiza o salvamento das informações dentro da
        base de dados
    
    Returns:
        bool: Retorna um booleano referente ao salvamento
            correto dos dados
    """
    memory_card = open('savegame.pkl', 'wb')

    dados_pra_salvar = (
        1,
        constantes.pretas,
        constantes.brancas,
        constantes.vazio,
        constantes.dama_preta,
        constantes.dama_branca,
        constantes.J1,
        constantes.J2,
        constantes.ress,
        constantes.matriz,
        constantes.jogador_atual,
        constantes.quant_pecas_j1,
        constantes.quant_pecas_j2,
        constantes.quant_damas_j1,
        constantes.quant_damas_j2,
        constantes.obrigatorio_preta,
        constantes.obrigatorio_branca,
        constantes.quant_jogadas_con_j1,
        constantes.quant_jogadas_con_j2,
        constantes.quant_jogadas_j1,
        constantes.quant_jogadas_j2 
    )

    #print(f"----- Salvando dados: {dados_pra_salvar}")

    pickle.dump(dados_pra_salvar, memory_card)

    memory_card.close()
    return True


def loadgame():
    """Realiza a leitura das informações da base de dados
    
    Returns:
        bool: Retorna um booleano referente ao carregamento
            correto dos dados
    """
    memory_card = open('savegame.pkl', 'rb')
    dados_salvos = pickle.load(memory_card)

    #print(f"----- Carregando dados: {dados_salvos}")

    constantes.pretas = dados_salvos[1]
    constantes.brancas = dados_salvos[2]
    constantes.vazio = dados_salvos[3]
    constantes.dama_preta = dados_salvos[4]
    constantes.dama_branca = dados_salvos[5]
    constantes.J1 = dados_salvos[6]
    constantes.J2 = dados_salvos[7]
    constantes.ress = dados_salvos[8]
    constantes.matriz = dados_salvos[9]
    constantes.jogador_atual = dados_salvos[10]
    constantes.quant_pecas_j1 = dados_salvos[11]
    constantes.quant_pecas_j2 = dados_salvos[12]
    constantes.quant_damas_j1 = dados_salvos[13]
    constantes.quant_damas_j2 = dados_salvos[14]
    constantes.obrigatorio_preta = dados_salvos[15]
    constantes.obrigatorio_branca = dados_salvos[16]
    constantes.quant_jogadas_con_j1 = dados_salvos[17]
    constantes.quant_jogadas_con_j2 = dados_salvos[18]
    constantes.quant_jogadas_j1 = dados_salvos[19]
    constantes.quant_jogadas_j2 = dados_salvos[20]

    memory_card.close()
    return True


def verifica_memory_card():
    """Verifica a existencia de dados salvos
    
    Returns:
        bool: Retorna um booleano repesentado a existência
            de dados
    """
    
    try:
        memory_card = open('savegame.pkl', 'rb')
        dados_salvos = pickle.load(memory_card)

        if dados_salvos[0]:
            return True

        return False

    except:
        return False