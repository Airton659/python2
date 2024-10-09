from exercicio2.layout import exibir_layout, exibir_texto_colorido
from exercicio2.painel import exibir_painel, exibir_painel_com_borda
from exercicio2.progresso import exibir_progresso, exibir_progresso_simples
from exercicio2.estilo import exibir_estilo, exibir_estilo_enfase

# Testando funções do módulo layout
print("Testando layout:")
exibir_layout("Texto de teste para layout.", isArquivo=False)
exibir_texto_colorido("Texto de teste colorido.", isArquivo=False)

# Testando funções do módulo painel
print("\nTestando painel:")
exibir_painel("Texto de teste para painel.", isArquivo=False)
exibir_painel_com_borda("Texto com borda estilizada.", isArquivo=False)

# Testando funções do módulo progresso
print("\nTestando progresso:")
exibir_progresso("Texto para progresso.", isArquivo=False)
exibir_progresso_simples("Texto para progresso simples.", isArquivo=False)

# Testando funções do módulo estilo
print("\nTestando estilo:")
exibir_estilo("Texto em estilo.", isArquivo=False)
exibir_estilo_enfase("Texto em ênfase.", isArquivo=False)
