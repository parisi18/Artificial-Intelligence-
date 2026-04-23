from .Heroi import Heroi
from .MundoWumpus import MundoWumpus

def main():
    mundo = MundoWumpus()
    heroi = Heroi()
    print("Posição do herói:", heroi.posicao)
    print("Tem ouro?", heroi.tem_ouro)
    print("Percepção inicial:", mundo.perceber(heroi))

    print(heroi.andar(mundo, "direita"))
    print("Posição atual:", heroi.posicao)
    print("Visitados:", heroi.visitados)
    print("Caminho:", heroi.caminho)

    print(heroi.andar(mundo, "esquerda"))
    print("Posição atual:", heroi.posicao)
    print("Visitados:", heroi.visitados)

    #testar colisão
    print(heroi.andar(mundo, "esquerda"))
    print("Posição atual:", heroi.posicao)
    print("Visitados:", heroi.visitados)

    print(heroi.andar(mundo, "baixo"))
    print("Posição atual:", heroi.posicao)
    print("Visitados:", heroi.visitados)
    print("Percepção manual:", mundo.perceber(heroi))

if __name__ == "__main__":
    main()
