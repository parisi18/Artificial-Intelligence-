class MundoWumpus:
    def __init__(self) -> None:
        self.tamanho = 4

        #Estado do mundo
        self.pos_heroi = (1,1)
        self.direcao_heroi = "direita"

        self.pos_ouro = (3,2)
        self.pos_wumpus = (4,3)
        self.buracos = {(2,3), (4,4)}
        self.jogo_finalizado = False
        self.vitoria = False

        #Estado da partida
        self.wumpus_vivo = True

    # Define se está dentro do mapa
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
        if self.jogo_finalizado:
            if self.morreu:
                return "O jogo terminou. O heroi morreu."
            return "O jogo terminou"
        
        percepcoes = []

        if self.wumpus_vivo and self.pos_wumpus in self.vizinhos(self.pos_heroi):
            percepcoes.append("Fedor")
        
        if any(p in self.vizinhos(self.pos_heroi) for p in self.buracos):
            percepcoes.append("Brisa")

        if self.pos_heroi == self.pos_ouro and not heroi.tem_ouro:
            percepcoes.append("Brilho")

        if bump:
            percepcoes.append("Impacto")

        if scream:
            percepcoes.append("Grito")

        #Verifica morte ao entrar na sala
        if self.pos_heroi in self.buracos:
            self.morreu = True
            self.jogo_finalizado = True
            percepcoes.append("Você caiu em um buraco e morreu")

        elif self.pos_heroi == self.pos_wumpus and self.wumpus_vivo:
            self.morreu = True
            self.jogo_finalizado = True
            percepcoes.append("O wumpus devorou você")

        if not percepcoes:
            return "nada"
        
        return ", ".join(percepcoes)
    
