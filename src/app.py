from .Heroi import Heroi
from .MundoWumpus import MundoWumpus

def main():
    mundo = MundoWumpus()
    heroi = Heroi()
    
    heroi.posicao = (2, 3)

    #Forçando matar o wumpus
    print(heroi.atirar(mundo, "baixo"))
    print("Wumpus vivo?", mundo.wumpus_vivo)
    print("Herói tem flecha?", heroi.tem_flecha)

if __name__ == "__main__":
    main()
