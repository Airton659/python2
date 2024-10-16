import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto, mover_jogador, verificar_item
from aventura_pkg.jogador import iniciar_jogador, mover, pontuar
from aventura_pkg.utils import imprime_instrucoes, animacao_vitoria
from time import sleep

def menu():
    """Exibe o menu inicial e retorna a escolha do jogador."""
    print("\nBem-vindo à Aventura no Labirinto!")
    print("1. Instruções")
    print("2. Jogar")
    print("3. Sair")
    
    escolha = input("Escolha uma opção (1-3): ")
    return escolha

def calcular_max_movimentos(tamanho_labirinto):
    """Calcula o número máximo de movimentos baseado no tamanho do labirinto."""
    return tamanho_labirinto * 5  # Multiplica o tamanho por 5 para ajustar os movimentos

def iniciar_jogo(nome_jogador, tamanho_labirinto):
    """Inicia o jogo com um loop principal e controla os movimentos do jogador."""
    
    simbolo_jogador = nome_jogador[0].upper()  # Usa a primeira letra do nome do jogador
    labirinto, itens = criar_labirinto(tamanho_labirinto, num_itens=3, simbolo_jogador=simbolo_jogador)  # Usar a primeira letra do nome como símbolo
    pos_jogador = (0, 0)  # O jogador sempre começa em 0,0
    pontos = 0  # Inicializa a pontuação
    movimentos = 0
    MAX_MOVIMENTOS = calcular_max_movimentos(tamanho_labirinto)  # Define o número máximo de movimentos

    # Mostrar labirinto na inicialização
    imprimir_labirinto(labirinto)

    while True:
        print(f"\nJogador: {nome_jogador} | Pontuação: {pontos} | Movimentos restantes: {MAX_MOVIMENTOS - movimentos} | Itens coletados: {3 - len(itens)}")
        
        # Ler o movimento do jogador
        tecla = input("Movimento (WASD): ").lower()
        nova_posicao = mover(pos_jogador, tecla, labirinto)

        if nova_posicao != pos_jogador:  # Verifica se houve movimento
            pos_jogador = mover_jogador(pos_jogador, nova_posicao, labirinto, simbolo_jogador)  # Passa o símbolo do jogador
            movimentos += 1  # Incrementa o contador de movimentos

        # Mostrar o labirinto atualizado após o movimento
        imprimir_labirinto(labirinto)

        coletado = verificar_item(pos_jogador, itens)
        pontos = pontuar(pontos, coletado)

        # Verifica condição de vitória ou derrota
        if pos_jogador == (tamanho_labirinto - 1, tamanho_labirinto - 1):  # Supondo que a saída é o canto inferior direito
            print(f"\nParabéns, {nome_jogador}! Você venceu o jogo!")
            animacao_vitoria()  # Animação recursiva
            break
        elif movimentos >= MAX_MOVIMENTOS:
            print(f"\nVocê perdeu, {nome_jogador}. Número máximo de movimentos atingido!")
            break


def main():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto")
    parser.add_argument('--dificuldade', type=int, choices=[10, 15, 20], default=10, help='Escolha o tamanho do labirinto')
    args = parser.parse_args()

    tamanho_labirinto = args.dificuldade

    while True:
        escolha = menu()

        if escolha == '1':
            imprime_instrucoes()
        elif escolha == '2':
            nome_jogador = input("Digite o nome do jogador: ")
            iniciar_jogo(nome_jogador, tamanho_labirinto)
        elif escolha == '3':
            print("Saindo do jogo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == '__main__':
    main()
