class Heroi:
    def __init__(self):
        self.posicao = (1, 1)
        self.tem_ouro = False
        self.tem_flecha = True
        self.vivo = True
        self.visitados = {(1, 1)}
        self.caminho = [(1, 1)]

    def andar(self, mundo, direcao):
        if not self.vivo:
            return "O herói está morto. Não pode se mover."
        
        if mundo.jogo_finalizado:
            return "O jogo já terminou. Nenhuma ação pode ser executada."
        
        movimentos = {
            "cima": (-1, 0),
            "baixo": (1, 0),
            "esquerda": (0, -1),
            "direita": (0, 1),
        }

        if direcao not in movimentos:
            return f"Direção inválida: {direcao}. Use cima, baixo, esquerda ou direita."
        
        self.direcao = direcao

        dl, dc = movimentos[direcao]
        linha, col = self.posicao
        nova_posicao = (linha + dl, col + dc)

        if not mundo.dentro_do_mapa(nova_posicao):
            percepcao = mundo.perceber(self, bump=True)
            return f"Você tentou andar para {direcao}, mas bateu na parede. Percepções: {percepcao}"
        
        self.posicao = nova_posicao
        self.visitados.add(nova_posicao)
        self.caminho.append(nova_posicao)

        percepcao = mundo.perceber(self)
        return f"Você andou para {direcao} e agora está em {self.posicao}. Percepções: {percepcao}"