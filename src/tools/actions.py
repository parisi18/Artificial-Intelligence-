from src.models.Heroi import Heroi
from src.models.MundoWumpus import MundoWumpus

mundo = MundoWumpus()
heroi = Heroi()

def andar(direcao):
    return heroi.andar(mundo, direcao)

def atirar(direcao):
    return heroi.atirar(mundo, direcao)

def pegar_ouro():
    return heroi.pegar_ouro(mundo)

def escalar_saida():
    return heroi.escalar_saida(mundo)