import random

def criar_labirinto(tamanho=10, num_itens=3):
    """Gera um labirinto com pelo menos um caminho garantido do início ao fim e itens."""
    # Inicializar o labirinto com paredes
    labirinto = [['#' for _ in range(tamanho)] for _ in range(tamanho)]

    # Posições iniciais do jogador
    x, y = 0, 0
    labirinto[x][y] = 'J'  # Posicionar o jogador no início

    # Adicionar um caminho aleatório do início ao fim
    caminho = [(x, y)]
    while (x, y) != (tamanho - 1, tamanho - 1):
        # Obter direções válidas
        direcoes = []
        if x < tamanho - 1:  # Para baixo
            direcoes.append((x + 1, y))
        if x > 0:  # Para cima
            direcoes.append((x - 1, y))
        if y < tamanho - 1:  # Para a direita
            direcoes.append((x, y + 1))
        if y > 0:  # Para a esquerda
            direcoes.append((x, y - 1))

        # Escolher uma direção aleatória
        if direcoes:
            x, y = random.choice(direcoes)
            caminho.append((x, y))
            labirinto[x][y] = ' '  # Criar o caminho

    # Colocar itens aleatoriamente no labirinto
    itens_posicoes = []
    while len(itens_posicoes) < num_itens:
        item_x = random.randint(0, tamanho - 1)
        item_y = random.randint(0, tamanho - 1)
        
        # Verifica se a posição é válida (caminho vazio e não é a posição do jogador ou saída)
        if labirinto[item_x][item_y] == ' ' and (item_x, item_y) != (0, 0) and (item_x, item_y) != (tamanho - 1, tamanho - 1):
            labirinto[item_x][item_y] = 'I'  # 'I' para representar um item
            itens_posicoes.append((item_x, item_y))

    return labirinto, itens_posicoes  # Retorna também as posições dos itens

def imprimir_labirinto(labirinto):
    """Imprime o labirinto no terminal."""
    for linha in labirinto:
        print(' '.join(linha))

def mover_jogador(posicao_atual, nova_posicao, labirinto):
    """Atualiza o labirinto com o movimento do jogador."""
    x_atual, y_atual = posicao_atual
    x_novo, y_novo = nova_posicao

    # Limpar a posição atual do jogador
    labirinto[x_atual][y_atual] = ' '

    # Colocar o jogador na nova posição
    labirinto[x_novo][y_novo] = 'J'

    return nova_posicao  # Retorna a nova posição do jogador

def verificar_item(pos_jogador, itens):
    """Verifica se o jogador está na mesma posição que um item e o coleta."""
    if pos_jogador in itens:
        itens.remove(pos_jogador)
        return True  # Item coletado
    return False
