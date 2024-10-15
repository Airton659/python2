def iniciar_jogador():
    """Inicializa o jogador no ponto de partida."""
    posicao_inicial = (0, 0)
    pontuacao = 0
    return posicao_inicial, pontuacao

def mover(posicao, tecla, labirinto):
    """Movimenta o jogador baseado na tecla pressionada."""
    x, y = posicao
    if tecla == 'w' and x > 0 and labirinto[x-1][y] != '#':
        x -= 1
    elif tecla == 's' and x < len(labirinto) - 1 and labirinto[x+1][y] != '#':
        x += 1
    elif tecla == 'a' and y > 0 and labirinto[x][y-1] != '#':
        y -= 1
    elif tecla == 'd' and y < len(labirinto[0]) - 1 and labirinto[x][y+1] != '#':
        y += 1
    return (x, y)

def pontuar(pontos, coletado):
    """Atualiza a pontuação se um item foi coletado."""
    if coletado:
        pontos += 10
    return pontos
