import random
from colorama import Fore, Style

# Função para criar o tabuleiro vazio
def criar_tabuleiro():
    tabuleiro = [[' ' for _ in range(12)] for _ in range(12)]
    return tabuleiro

# Função para imprimir o tabuleiro com cores
def imprimir_tabuleiro(tabuleiro, posicoes_vitoria=None, posicoes_quase_vitoria=None):
    for i, linha in enumerate(tabuleiro):
        print('|', end='')
        for j, valor in enumerate(linha):
            cor = Style.RESET_ALL  # Reinicia a cor do texto
            if posicoes_vitoria and (i, j) in posicoes_vitoria:
                cor = Fore.RED  # Define a cor vermelha para a vitória
            elif posicoes_quase_vitoria and (i, j) in posicoes_quase_vitoria:
                cor = Fore.GREEN  # Define a cor verde para a quase vitória
            print(f'{cor} {valor} {Style.RESET_ALL}|', end='')
        print('\n' + '-' * 49)

# Função para realizar uma jogada no tabuleiro
def realizar_jogada(tabuleiro, linha, coluna, jogador):
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True
    return False

# Função para verificar se um jogador venceu
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in range(12):
        for coluna in range(12 - 2):
            if tabuleiro[linha][coluna] == tabuleiro[linha][coluna+1] == tabuleiro[linha][coluna+2] == jogador:
                return True

    # Verificar colunas
    for coluna in range(12):
        for linha in range(12 - 2):
            if tabuleiro[linha][coluna] == tabuleiro[linha+1][coluna] == tabuleiro[linha+2][coluna] == jogador:
                return True

    # Verificar diagonais
    for linha in range(12 - 2):
        for coluna in range(12 - 2):
            if tabuleiro[linha][coluna] == tabuleiro[linha+1][coluna+1] == tabuleiro[linha+2][coluna+2] == jogador:
                return True

    for linha in range(12 - 2):
        for coluna in range(2, 12):
            if tabuleiro[linha][coluna] == tabuleiro[linha+1][coluna-1] == tabuleiro[linha+2][coluna-2] == jogador:
                return True

    return False

# Função para avaliar o desempenho das IAs
def avaliar_desempenho(jogadores):
    for jogador in jogadores:
        print(f"Desempenho da IA {jogador.nome}:")
        print(f"Vitórias: {jogador.vitorias}")
        print(f"Derrotas: {jogador.derrotas}")
        print(f"Empates: {jogador.empates}")
        print()

# Classe para representar a IA
class IA:
    def __init__(self, nome):
        self.nome = nome
        self.vAqui = vAqui #está a continuação do código corrigido:

```python
        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0

    def realizar_jogada(self, tabuleiro):
        # Lógica para a IA fazer a jogada
        coluna = random.randint(0, 11)
        linha = random.randint(0, 11)
        while not realizar_jogada(tabuleiro, linha, coluna, self.nome):
            coluna = random.randint(0, 11)
            linha = random.randint(0, 11)

# Função para jogar uma fase de grupos
def jogar_fase_de_grupos(jogadores):
    partidas_por_jogador = len(jogadores) - 1
    for jogador1 in jogadores:
        for _ in range(partidas_por_jogador):
            jogador2 = random.choice([jogador for jogador in jogadores if jogador != jogador1])
            tabuleiro = criar_tabuleiro()
            vencedor = None
            jogador_atual = random.choice([jogador1, jogador2])
            while True:
                print(f"É a vez de {jogador_atual.nome}")
                if jogador_atual.nome.startswith('IA'):
                    jogador_atual.realizar_jogada(tabuleiro)
                else:
                    coluna = int(input("Digite a coluna: "))
                    linha = int(input("Digite a linha: "))
                    while not realizar_jogada(tabuleiro, linha, coluna, jogador_atual.nome):
                        print("Jogada inválida. Tente novamente.")
                        coluna = int(input("Digite a coluna: "))
                        linha = int(input("Digite a linha: "))
                imprimir_tabuleiro(tabuleiro)
                if verificar_vencedor(tabuleiro, jogador_atual.nome):
                    vencedor = jogador_atual
                    break
                jogador_atual = jogador1 if jogador_atual == jogador2 else jogador2
            if vencedor:
                print(f"O jogador {vencedor.nome} venceu a partida!")
                vencedor.vitorias += 1
                jogador_atual.derrotas += 1
            else:
                print("A partida terminou em empate!")
                jogador1.empates += 1
                jogador2.empates += 1
        print()

# Função principal para jogar o jogo da velha
def jogar_jogo_da_velha():
    # Criação das IAs
    jogadores = [IA('IA1'), IA('IA2'), IA('IA3'), IA('IA4')]

    # Variáveis de controle do jogo
    reiniciar_jogo = 's'
    partida = 0
    proximo_numero_ia = 5

    while reiniciar_jogo.lower() == 's':
        jogar_fase_de_grupos(jogadores)
        partida += 1
        if partida % 10 == 0:
            pior_ia = min(jogadores, key=lambda x: x.vitorias)
            jogadores.remove(pior_ia)
            novo_nome = f"IA-{proximo_numero_ia}"
            jogadores.append(IA(novo_nome))
            proximo_numero_ia += 1
        avaliar_desempenho(jogadores)
        reiniciar_jogo = input("Deseja reiniciar o jogo? (s/n): ")

jogar_jogo_da_velha()
