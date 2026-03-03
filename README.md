# ♟️ Projeto Damas (Python)

Jogo de **Damas** desenvolvido em **Python**, executado no **terminal**, com regras essenciais (incluindo **captura obrigatória** e **promoção para dama**) e opção de **salvar / carregar** o progresso via “memory card” (`savegame.pkl`).

---

## ✨ Funcionalidades

- ✅ Jogo de damas no terminal (2 jogadores)
- ✅ Tabuleiro 8x8
- ✅ Movimentação de peças e **dama**
- ✅ **Captura de peças**
- ✅ **Captura obrigatória** quando disponível
- ✅ Condição de vitória (quando um jogador fica sem peças)
- ✅ Detecção de empate (ex.: repetição/estagnação por sequência de jogadas com dama sem captura)
- ✅ **Save/Load** automático via arquivo `savegame.pkl` (tipo “memory card”)

---

## 🧠 Como funciona a entrada

Durante o jogo, o programa solicita:

1) A posição da peça (linha e coluna)  
2) A posição de destino (linha e coluna)

Os valores devem estar entre **0 e 7**.

Exemplo (digitando com espaço):

2 3

3 4

---

## ▶️ Como executar

### Requisitos
- Python 3.x instalado

### Passo a passo

1. Clone o repositório:
```bash
git clone https://github.com/caiodantass/Projeto_Damas.git
```

### Entre na pasta:
```bash
cd Projeto_Damas
```

### Execute:
```bash
python main.py
```

### No Windows, se necessário:
```bashpy
 main.py
```


## 💾 Salvamento (Memory Card)

O projeto utiliza um arquivo chamado savegame.pkl para guardar o estado do jogo.

Se esse arquivo existir, ao iniciar o jogo você poderá escolher:

1: continuar de onde parou

0: começar um novo jogo

Resetar progresso

Para iniciar do zero (apagando o “memory card”), basta deletar o arquivo:

savegame.pkl

## 🧩 Estrutura do projeto

main.py — loop principal do jogo e fluxo das jogadas

tabuleiro.py — criação/impressão do tabuleiro

movimentacao.py — regras de movimento/captura e validações

constantes.py — constantes e estado global do jogo

banco_de_dados.py — salvar/carregar partida com pickle

## 🚀 Melhorias futuras (ideias)

 Interface gráfica (ex.: Pygame)

 Modo contra IA

 Validação mais amigável de inputs

 Log das jogadas / histórico

 Testes unitários para regras

## 👤 Autor

### Feito por Caio Dantas
Se curtir o projeto, deixa uma ⭐ no repositório!
