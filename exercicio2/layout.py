"""
    Exibe o texto em painel
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text


console = Console()

def exibir_layout(texto:str, isArquivo: bool) -> None:

    """
    Args:
        texto (str): O texto a ser exibido.
        isArquivo (bool): Determina se o texto é de um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    panel = Panel(texto, title="Texto em Layout")
    console.print(panel)

def exibir_texto_colorido (texto: str, isArquivo: bool) -> None:
    """
    Exibe o texto colorido em um painel.

    Args:
        texto (str): O texto a ser exibido.
        isArquivo (bool): Determina se o texto é de um arquivo.
    """

    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    colored_text = Text(texto, style="bold green")
    console.print(colored_text)
