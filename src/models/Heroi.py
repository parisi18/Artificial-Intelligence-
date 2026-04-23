class Heroi:
    def __init__(self):
        self.posicao = (1, 1)
        self.direcao = "direita"
        self.tem_ouro = False
        self.tem_flecha = True
        self.vivo = True
        self.visitados = {(1, 1)}
        self.caminho = [(1, 1)]
        self.memoria = {}

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
    
    def atirar(self, mundo, direcao):
        if not self.vivo:
            return "O herói está morto. Não pode atirar."
        
        if mundo.jogo_finalizado:
            return "O jogo já terminou. Nenhuma ação pode ser executada."
        
        if not self.tem_flecha:
            return "O herói já usou a flecha."
        
        movimentos_validos = {
            "cima", 
            "baixo", 
            "esquerda", 
            "direita"
        }

        if direcao not in movimentos_validos:
            return f"Direção inválida: {direcao}. Use cima, baixo, esquerda, direita."
        
        self.tem_flecha = False

        linha_h, col_h = self.posicao
        linha_w, col_w = mundo.pos_wumpus

        acertou = False

        if direcao == "cima" and col_h == col_w and linha_w < linha_h:
            acertou = True
        elif direcao == "baixo" and col_h == col_w and linha_w > linha_h:
            acertou = True
        elif direcao == "esquerda" and linha_h == linha_w and col_w < col_h:
            acertou = True
        elif direcao == "direita" and linha_h == linha_w and col_w > col_h:
            acertou = True

        if acertou and mundo.wumpus_vivo:
            mundo.wumpus_vivo = False
            percepcao = mundo.perceber(self, scream=True)
            return f"Você atirou para {direcao} e matou o Wumpus. Percepções: {percepcao}"
        
        percepcao = mundo.perceber(self)
        return f"Você atirou para {direcao}, mas errou. Percepções: {percepcao}."
    
    def pegar_ouro(self, mundo):
        if not self.vivo:
            return "O herói está morto. Não pode pegar o ouro."
        
        if mundo.jogo_finalizado:
            return "O jogo já terminou. Nenhuma ação pode ser executada."
        
        if self.tem_ouro:
            return "O herói já está com o ouro."
        
        if self.posicao != mundo.pos_ouro:
            percepcao = mundo.perceber(self)
            return f"Não há ouro nesta posição. Percepções: {percepcao}"
        
        self.tem_ouro = True
        return "Você pegou o ouro com sucesso"
    
    def escalar_saida(self, mundo):
        if not self.vivo:
            return "O herói está morto. Não pode sair da caverna."
        
        if mundo.jogo_finalizado:
            return "O jogo já terminou. Nenhuma ação pode ser executada."
        
        if self.posicao != (1,1):
            percepcao = mundo.perceber(self)
            return f"A saída só pode ser usada na posição inicial (1,1). Percepções: {percepcao}."
        
        mundo.jogo_finalizado = True

        if self.tem_ouro:
            mundo.vitoria = True
            return "Você saiu da caverna com o ouro. Vitória!"
        
        mundo.vitoria = False
        return "Você saiu da caverna sem o ouro."
    
    def registrar_percepcao(self, percepcao: str):
        self.memoria[self.posicao] = percepcao

    def formatar_memoria(self) -> str:
        if not self.memoria:
            return "Nenhuma célula conhecida ainda."

        linhas = ["Mapa conhecido até agora:"]
        for posicao in sorted(self.memoria.keys()):
            percepcao = self.memoria[posicao]
            linhas.append(f"{posicao}: {percepcao}")

        return "\n".join(linhas)