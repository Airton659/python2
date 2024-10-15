from rich.console import Console
from time import sleep
import emoji  # Adicionando a biblioteca emoji

def imprime_instrucoes():
    """Imprime as instruções do jogo usando rich text."""
    console = Console()
    console.print("[bold blue]Bem-vindo à Aventura no Labirinto![/bold blue]")
    console.print("Use as teclas [bold]W[/bold], [bold]A[/bold], [bold]S[/bold], [bold]D[/bold] para mover.")
    console.print("Colete os itens e tente chegar ao final do labirinto!")
    console.print("Boa sorte!")

def animacao_vitoria(passos=5):
    """Animação simples de vitória com rich text, usando recursão."""
    if passos <= 0:
        return

    # Usando a biblioteca emoji para exibir os emojis de forma confiável
    console = Console()
    console.print(emoji.emojize(f"[bold green]Parabéns! Você venceu![/bold green] {':partying_face:' * passos}"))

    sleep(0.5)  # Pausa para efeito
    animacao_vitoria(passos - 1)  # Chama recursivamente para diminuir o número de emojis
