# Aventura no Labirinto

## Descrição

**Aventura no Labirinto** é um jogo interativo jogado via terminal. O jogador controla um personagem que explora um labirinto, coletando itens e tentando encontrar a saída. O labirinto é gerado aleatoriamente em cada nova partida, garantindo uma experiência única a cada jogo.

O objetivo principal é **coletar todos os itens** e **alcançar a saída do labirinto** (canto inferior direito), antes que o número máximo de movimentos seja atingido.

---

## Funcionalidades

- **Movimento via teclado**: Use as teclas `W`, `A`, `S`, `D` para mover o jogador pelo labirinto.
- **Coleta de Itens**: O labirinto contém itens que podem ser coletados ao se mover sobre eles.
- **Animação de Vitória**: Ao encontrar a saída, o jogo exibe uma animação de vitória.
- **Labirinto gerado aleatoriamente**: Cada jogo possui um layout diferente.

---

## Screenshots

![image](https://github.com/user-attachments/assets/4a075c61-3e1f-44ed-a33d-f84ab2ad35a5)

![image](https://github.com/user-attachments/assets/17f50e68-edab-442a-96ed-e566a27f4774)

![image](https://github.com/user-attachments/assets/2d432d43-a3b7-4ae0-9eca-9bf43181be34)

![image](https://github.com/user-attachments/assets/8b7ea2d1-bd67-4cc8-9324-52c99b6abb95)

![image](https://github.com/user-attachments/assets/bbe84f27-cb90-4705-b005-74ab3584a809)

![image](https://github.com/user-attachments/assets/c6e57503-0462-481c-877a-6f2449303a6c)



---


### Pré-requisitos

1. **Python 3.x** instalado no sistema.
2. Instale as dependências listadas no `requirements.txt`.

## Como Executar
1. Entre no diretório do projeto:
   ```bash
   cd aventura_no_labirinto
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
4. Execute o jogo com a dificuldade desejada (10, 15 ou 20):
   ```bash
   python main.py --dificuldade 10

### Instruções
1. O jogo começa com o jogador posicionado no canto superior esquerdo do labirinto (J).
2. O objetivo é alcançar o canto inferior direito do labirinto enquanto coleta os itens espalhados (I).
3. Movimente-se pelo labirinto usando as teclas:
   * W para mover para cima
   * A para mover para a esquerda
   * S para mover para baixo
   * D para mover para a direita
4. Durante o jogo, você verá o número de itens coletados e a quantidade de movimentos restantes.
5. O jogo termina quando você encontra a saída ou atinge o número máximo de movimentos.
