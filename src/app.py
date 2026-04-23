from src.models.Heroi import Heroi
from src.models.MundoWumpus import MundoWumpus

def main():
    heroi = Heroi()
    mundo = MundoWumpus()

    print("Wumpus:", mundo.pos_wumpus)
    print("Ouro:", mundo.pos_ouro)
    print("Buracos:", mundo.buracos)

    print("Memória inicial:", heroi.memoria)
    print("Percepção inicial:", mundo.perceber(heroi))
    print("Memória depois da percepção inicial:", heroi.memoria)

    heroi.posicao = mundo.pos_ouro
    heroi.tem_ouro = False
    print("Percepção na casa do ouro:", mundo.perceber(heroi))
    print("Memória final:", heroi.memoria)

if __name__ == "__main__":
    main()