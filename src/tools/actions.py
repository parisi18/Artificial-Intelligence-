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

def call_tool(nome, **kwargs):
    if nome == "andar":
        direcao = kwargs.get("direcao")
        if direcao is None:
            return "Erro: a ferramenta 'andar' exige o argumento 'direcao'."
        return andar(direcao)

    elif nome == "atirar":
        direcao = kwargs.get("direcao")
        if direcao is None:
            return "Erro: a ferramenta 'atirar' exige o argumento 'direcao'."
        return atirar(direcao)

    elif nome == "pegar_ouro":
        return pegar_ouro()

    elif nome == "escalar_saida":
        return escalar_saida()

    else:
        return f"Ferramenta desconhecida: {nome}"