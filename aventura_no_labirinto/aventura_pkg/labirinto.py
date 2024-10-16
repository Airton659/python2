import random

def criar_labirinto(tamanho=10, num_itens=3):
    """Gera um labirinto com um caminho garantido do início ao fim e caminhos adicionais."""
    # Inicializar o labirinto com paredes
    labirinto = [['#' for _ in range(tamanho)] for _ in range(tamanho)]

    # Função auxiliar para embaralhar direções
    def embaralhar_direcoes():
        direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Baixo, Cima, Direita, Esquerda
        random.shuffle(direcoes)
        return direcoes

    # Função para verificar se podemos escavar um caminho
    def pode_escavar(x, y):
        return 0 <= x < tamanho and 0 <= y < tamanho and labirinto[x][y] == '#'

    # Passo 1: Criar um caminho garantido do início ao fim
    def criar_caminho_principal():
        x, y = 0, 0
        labirinto[x][y] = ' '  # Ponto inicial
        while (x, y) != (tamanho - 1, tamanho - 1):
            # Tente mover para baixo ou para a direita para garantir o progresso
            if x < tamanho - 1 and random.choice([True, False]):
                x += 1
            elif y < tamanho - 1:
                y += 1
            else:
                x += 1  # Forçar movimento para baixo quando à direita

            labirinto[x][y] = ' '  # Criar o caminho principal

    criar_caminho_principal()

    # Passo 2: Adicionar caminhos extras e bifurcações
    def criar_caminho(x, y, profundidade=0, max_profundidade=50):
        if profundidade >= max_profundidade:
            return  # Limitar a profundidade para evitar loop infinito

        for dx, dy in embaralhar_direcoes():
            novo_x, novo_y = x + 2 * dx, y + 2 * dy
            meio_x, meio_y = x + dx, y + dy

            if pode_escavar(novo_x, novo_y):
                labirinto[meio_x][meio_y] = ' '  # Limpar o meio
                labirinto[novo_x][novo_y] = ' '  # Criar o caminho extra
                criar_caminho(novo_x, novo_y, profundidade + 1, max_profundidade)

    # Criar caminhos extras a partir de várias posições
    for i in range(tamanho // 2):  # Tentativas de criar caminhos extras
        x, y = random.randint(0, tamanho - 2), random.randint(0, tamanho - 2)
        criar_caminho(x, y)

    # Garantir que a saída esteja aberta
    labirinto[tamanho-1][tamanho-1] = ' '

    # Colocar itens aleatoriamente no labirinto
    itens_posicoes = []
    while len(itens_posicoes) < num_itens:
        item_x = random.randint(0, tamanho - 1)
        item_y = random.randint(0, tamanho - 1)

        # Verifica se a posição é válida (não é uma parede, não é a posição do jogador ou saída)
        if labirinto[item_x][item_y] == ' ' and (item_x, item_y) != (0, 0) and (item_x, item_y) != (tamanho - 1, tamanho - 1):
            labirinto[item_x][item_y] = 'I'  # 'I' para representar um item
            itens_posicoes.append((item_x, item_y))

    # Garantir que o jogador esteja na posição inicial
    labirinto[0][0] = 'J'

    return labirinto, itens_posicoes  # Retorna o labirinto e as posições dos itens

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
