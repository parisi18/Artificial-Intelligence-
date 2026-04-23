from .Heroi import Heroi
from .MundoWumpus import MundoWumpus

def main():
    mundo = MundoWumpus()
    heroi = Heroi()
    print("Posição do herói:", heroi.posicao)
    print("Tem ouro?", heroi.tem_ouro)
    print("Percepção inicial:", mundo.perceber(heroi))

if __name__ == "__main__":
    main()
