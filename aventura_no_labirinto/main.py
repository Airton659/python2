import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto, mover_jogador, verificar_item
from aventura_pkg.jogador import iniciar_jogador, mover, pontuar
from aventura_pkg.utils import imprime_instrucoes, animacao_vitoria
from time import sleep

MAX_MOVIMENTOS = 50  # Número máximo de movimentos permitidos

def menu():
    """Exibe o menu inicial e retorna a escolha do jogador."""
    print("\nBem-vindo à Aventura no Labirinto!")
    print("1. Instruções")
    print("2. Jogar")
    print("3. Sair")
    
    escolha = input("Escolha uma opção (1-3): ")
    return escolha

def iniciar_jogo(nome_jogador, tamanho_labirinto):
    """Inicia o jogo com um loop principal e controla os movimentos do jogador."""
    
    labirinto, itens = criar_labirinto(tamanho_labirinto, num_itens=3)  # Gerar labirinto e itens
    pos_jogador, pontos = iniciar_jogador()
    movimentos = 0

    while True:
        imprimir_labirinto(labirinto)
        print(f"\nJogador: {nome_jogador} | Pontuação: {pontos} | Movimentos restantes: {MAX_MOVIMENTOS - movimentos} | Itens coletados: {3 - len(itens)}")
        
        tecla = input("Movimento (WASD): ").lower()
        nova_posicao = mover(pos_jogador, tecla, labirinto)

        if nova_posicao != pos_jogador:  # Verifica se houve movimento
            pos_jogador = mover_jogador(pos_jogador, nova_posicao, labirinto)
            movimentos += 1  # Incrementa o contador de movimentos

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
