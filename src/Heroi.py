class Heroi:
    def __init__(self):
        self.posicao = (1, 1)
        self.tem_ouro = False
        self.tem_flecha = True
        self.vivo = True
        self.visitados = {(1, 1)}
        self.caminho = [(1, 1)]

    def andar(self, mundo, direcao):
        pass