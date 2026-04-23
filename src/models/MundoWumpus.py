import random


class MundoWumpus:
    def __init__(self) -> None:
        self.tamanho = 4
        self.pos_ouro: tuple[int, int] | None = None
        self.pos_wumpus: tuple[int, int] | None = None
        self.buracos: set[tuple[int, int]] = set()
        self.jogo_finalizado = False
        self.vitoria = False

        self.wumpus_vivo = True

        self.gerar_mundo()

    def dentro_do_mapa(self, pos):
        linha, col = pos
        return 1 <= linha <= self.tamanho and 1 <= col <= self.tamanho

    def vizinhos(self, pos):
        linha, col = pos
        cells_vizinhas = [
            (linha - 1, col),
            (linha + 1, col),
            (linha, col - 1),
            (linha, col +1)
        ]
        return [p for p in cells_vizinhas if self.dentro_do_mapa(p)]

    def perceber(self, heroi, bump=False, scream=False):
        print("DEBUG: entrou em perceber")
        if self.jogo_finalizado:
            if not heroi.vivo:
                resultado = "O jogo terminou. O herói morreu."
                heroi.registrar_percepcao(resultado)
                return resultado
            resultado = "O jogo terminou."
            heroi.registrar_percepcao(resultado)
            return resultado
        
        percepcoes = []

        if self.wumpus_vivo and self.pos_wumpus in self.vizinhos(heroi.posicao):
            percepcoes.append("Fedor")
        
        if any(p in self.vizinhos(heroi.posicao) for p in self.buracos):
            percepcoes.append("Brisa")

        if heroi.posicao == self.pos_ouro and not heroi.tem_ouro:
            percepcoes.append("Brilho")

        if bump:
            percepcoes.append("Impacto")

        if scream:
            percepcoes.append("Grito")

        #Verifica morte ao entrar na sala
        if heroi.posicao in self.buracos:
            self.morreu = True
            self.jogo_finalizado = True
            percepcoes.append("Você caiu em um buraco e morreu")

        elif heroi.posicao == self.pos_wumpus and self.wumpus_vivo:
            self.morreu = True
            self.jogo_finalizado = True
            percepcoes.append("O wumpus devorou você")

        resultado = "nada" if not percepcoes else ", ".join(percepcoes)
        heroi.registrar_percepcao(resultado)
        return resultado
    
    def todas_as_posicoes(self):
        return [
            (linha, col)
            for linha in range(1, self.tamanho + 1)
            for col in range(1, self.tamanho + 1)
        ]
    
    def gerar_mundo(self):
        posicoes = self.todas_as_posicoes()

        area_segura_inicial = {
            (1, 1),
            (1, 2),
            (2, 1),
        }

        posicoes_permitidas = [p for p in posicoes if p not in area_segura_inicial]

        self.pos_wumpus = random.choice(posicoes_permitidas)

        restantes = [p for p in posicoes_permitidas if p != self.pos_wumpus]
        self.pos_ouro = random.choice(restantes)

        restantes = [p for p in restantes if p != self.pos_ouro]

        quantidade_buracos = 2
        self.buracos = set(random.sample(restantes, quantidade_buracos))
