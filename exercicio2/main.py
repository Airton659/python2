import argparse
from exercicio2 import layout, painel, progresso, estilo

def main():
    parser = argparse.ArgumentParser(description="Exibe texto formatado.")
    parser.add_argument("texto", help="Texto ou nome do arquivo que deseja imprimir formatado.")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Ativa se o argumento é um caminho para um arquivo.")
    parser.add_argument("-m", "--modulo", choices=['layout', 'painel', 'progresso', 'estilo'], required=True, help="Módulo que deseja acessar.")
    parser.add_argument("-f", "--funcao", choices=['exibir_layout', 'exibir_painel', 'exibir_progresso', 'exibir_estilo'], required=True, help="Função do módulo que deseja acessar.")

    args = parser.parse_args()

    if args.modulo == 'layout':
        layout.exibir_layout(args.texto, args.arquivo)
    elif args.modulo == 'painel':
        painel.exibir_painel(args.texto, args.arquivo)
    elif args.modulo == 'progresso':
        progresso.exibir_progresso(args.texto, args.arquivo)
    elif args.modulo == 'estilo':
        estilo.exibir_estilo(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
