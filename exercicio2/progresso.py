"""
    Exibe um progresso com o texto.
"""

from rich.console import Console
from rich.progress import Progress
import time

console = Console()

def exibir_progresso(texto: str, isArquivo: bool) -> None:

    """
    Args:
        texto (str): O texto a ser exibido.
        isArquivo (bool): Determina se o texto é de um arquivo.
    """

    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    console.print(texto)  
    with Progress() as progress:
        task = progress.add_task("Processando...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.1) 

def exibir_progresso_simples(texto:str, isArquivo: bool) -> None:
    """
    Exibe um progresso simples e o texto.

    Args:
        texto (str): O texto a ser exibido.
        isArquivo (bool): Determina se o texto é de um arquivo.
    """

    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    console.print("[bold blue]Iniciando processamento...[/bold blue]")
    for i in range(5):
        console.print(f"[cyan]{texto} - Passo {i +1}[/cyan]")
        time.sleep(1)