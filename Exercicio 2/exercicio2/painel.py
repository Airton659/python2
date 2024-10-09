"""
    Exibe o texto em um painel.
"""
from rich.console import Console
from rich.panel import Panel

console = Console()

def exibir_painel(texto: str, isArquivo: bool) -> None:
    
    """
    Args:
        texto (str): O texto a ser exibido.
        isArquivo (bool): Determina se o texto é de um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    painel = Panel(texto, title="Painel de Texto", border_style="blue")
    console.print(painel)

def exibir_painel_com_borda(texto: str, isArquivo: bool) -> None:

    """
    Exibe o texto em um painel com borda estilizada.

    Args:
        texto (str): O texto a ser exibido.
        isArquivo (bool): Determina se o texto é de um arquivo.
    """

    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    painel = Panel(texto, title="Texto com Borda estilizada", border_style="red", padding=(1,2))
    console.print(painel)