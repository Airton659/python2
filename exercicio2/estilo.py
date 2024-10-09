"""
    Exibe o texto com estilo.
"""
from rich.console import Console

console = Console()

def exibir_estilo(texto: str, isArquivo: bool) -> None:

    """
    Args:
        texto (str): O texto a ser exibido.
        isArquivo (bool): Determina se o texto é de um arquivo.
    """
    if isArquivo:
        with open (texto, 'r') as file:
            texto = file.read()
    console.print(f"[bold magenta]{texto}[/bold magenta]")

def exibir_estilo_enfase(texto: str, isArquivo: bool) -> None:
    """
    Exibe o texto em estilo de ênfase.

    Args:
        texto (str): O texto a ser exibido.
        isArquivo (bool): Determina se o texto é de um arquivo.
    """

    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    console.print(f"[bold yellow][underline]{texto}[/underline][/bold yellow]")