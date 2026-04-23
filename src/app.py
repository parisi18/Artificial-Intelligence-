from .Heroi import Heroi
from .MundoWumpus import MundoWumpus

def main():
    mundo = MundoWumpus()
    heroi = Heroi() 


    heroi.posicao = (3, 2)
    
    #Forçando matar o wumpus
    print(heroi.pegar_ouro(mundo))
    print("Herói tem ouro?", heroi.tem_ouro)

    print(heroi.pegar_ouro(mundo))

if __name__ == "__main__":
    main()
