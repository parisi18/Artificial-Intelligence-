from .MundoWumpus import MundoWumpus

def main():
    jogo = MundoWumpus()
    print("Posição inicial:", jogo.pos_heroi)
    print("Vizinhos da posição inicial:", jogo.vizinhos(jogo.pos_heroi))
    print("Percepção inicial:", jogo.perceber())

if __name__ == "__main__":
    main()
