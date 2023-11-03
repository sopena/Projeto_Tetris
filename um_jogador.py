import pyxel as px
import random

from Tela import Tela
from Peca import Peca
from Prox_peca import Prox_peca

class Jogo:
    
    def __init__(self, q_largura, q_altura, lado, cor_fundo, cor_grade, var, level, vels, vel, pontuacao_lin, jogadores, nivel_txt):
        self.level = level
        self.nivel_txt = nivel_txt
        self.vels = vels
        self.vel = vel
        self.pontos = 0
        self.linhas_eliminadas = 0
        self.pontuacao_lin = pontuacao_lin
        self.cor_fundo = cor_fundo
        self.jogador_1_jogando = True
        self.game_over_j1 = False

        self.tela_start = True
        
        self.t = Tela(q_largura, q_altura, lado, cor_grade, var, 1)
        self.p = Peca(self.t.largura//2 - self.t.lado, -self.t.lado, random.randint(1, 7), self.t.largura, self.t.altura, self.t.lado)
        self.p1 = Prox_peca(11*self.t.lado, 5*self.t.lado, random.randint(1, 7), self.t.lado)
        self.p2 = Prox_peca(11*self.t.lado, 10*self.t.lado, random.randint(1, 7), self.t.lado)
        self.p3 = Prox_peca(11*self.t.lado, 15*self.t.lado, random.randint(1, 7), self.t.lado)

        px.init(self.t.largura + self.t.lado*5, self.t.altura, title='Tetris', fps=60)
        px.run(self.update, self.draw)
            
    # Adiciona a peça na matriz
    def add_peca(self):
        for i in range(self.p.size):
            for j in range(self.p.size):
                if self.p.grade[i][j] == 1:
                    self.t.grade[int(self.p.y + self.t.lado*i) //self.t.lado][int(self.p.x + self.t.lado*j)//self.t.lado] = 1      

    # Muda a velocidade de caida da peça de acordo com o nivel
    def mudar_vel(self):
        for i in range(len(self.level)):
            if self.pontos >= self.level[i]:
                self.vel = self.vels[i]

    def nivel(self):
        for i in range(len(self.vels)):
            if self.vel == self.vels[i]:
                px.text(11*self.t.lado, 1.85*self.t.lado + 4, f'{self.nivel_txt[i]}', 0)
                nivel = f'{i + 1}'
        return nivel

    def eliminar(self):
        eliminou = 0
        for i in range(self.t.q_altura, 0, -1):
            if self.t.grade[i] == [1]*self.t.q_largura + [self.t.var]*2:
                self.t.grade[i] = [0]*self.t.q_largura + [self.t.var]*2
                eliminou += 1
                self.linhas_eliminadas += 1

        # sistema de pontuação pela quantidade de linhas eliminadas
        if eliminou == 1:
            self.pontos += self.pontuacao_lin[0]
        if eliminou == 2:
            self.pontos += self.pontuacao_lin[1]
        if eliminou == 3:
            self.pontos += self.pontuacao_lin[2]
        if eliminou == 4:
            self.pontos += self.pontuacao_lin[3]

    def start_tela(self):
        px.cls(5)
        px.blt((self.t.largura + self.t.lado*5)//2 - 128, (self.t.altura)//2 - 85.5, 0, 0, 0, 256, 171)
        px.text((self.t.largura + self.t.lado*5)//2 - self.t.lado*3 + 5, ((self.t.altura)//2) + self.t.lado, 'PRESS SPACE TO START', 0)

    def load_images(self):
        #carrega a imagem da tela de start
        px.image(0).load(0, 0, 'tela_start.png')

        #carregas as imagnes dos blocos coloridos
        px.image(1).load(0, 0, 'blocos_coloridos.png')

        #carrega o bloco do score
        px.image(2).load(0, 0, 'bloco_fundo_score.png')
    
    def game_over(self, desceu, jogador):
        # Verifica se deu game over para o jogador 1
        if jogador == 1:
            if (desceu == 0):
                if self.p.y < 0:
                    return True
        return False

    def update(self):
        self.load_images()

        #Enquanto não clicar enter o jogo não começa
        if self.tela_start:
            if  px.btnp(px.KEY_SPACE):
                self.tela_start = False
            return 0

        # Ativa a Função descer e cria uma nova peça
        self.desceu = self.p.descer(self.vel, self.t, 1)

        # Verifica se deu game over
        self.game_over_j1 = self.game_over(self.desceu, 1)
        if self.game_over_j1:
            self.jogador_1_jogando = False
            return 0 

        if self.desceu == 0:
            self.add_peca()
            self.eliminar()
            self.t.descer_linha()
            self.t.descer_linha()
            self.t.descer_linha()
            self.t.descer_linha()

            # Fazer a permutação do Tipo das peças e randomizar a última
            self.p = Peca(self.t.largura//2 - self.t.lado, -self.t.lado, self.p1.tipo, self.t.largura, self.t.altura, self.t.lado)
            self.p1 = Prox_peca(11*self.t.lado, 5*self.t.lado, self.p2.tipo, self.t.lado)
            self.p2 = Prox_peca(11*self.t.lado, 10*self.t.lado, self.p3.tipo, self.t.lado)
            self.p3 = Prox_peca(11*self.t.lado, 15*self.t.lado, random.randint(1, 7), self.t.lado)

            # atribui a variavel a velocidade que o jogo tem que estar naquele nivel
            self.mudar_vel()

        # Movimentação
        if px.btnp(px.KEY_RIGHT):
            self.p.direita(self.t, 1)

        if px.btnp(px.KEY_LEFT):
            self.p.esquerda(self.t, 1)

        if px.btn(px.KEY_DOWN):
            self.p.baixo(self.t, 1)
            if self.p.y > -self.t.lado/2:
                self.pontos += 0.3

        if px.btnp(px.KEY_UP):
            self.p.rotacao(self.t, 1)

    def draw(self):
        if self.tela_start:
            self.start_tela()            
            if  px.btnp(px.KEY_DELETE):
                self.tela_start = False
            return 0
        
        px.cls(self.cor_fundo)

        #ativa a função para desenhar a grade
        self.t.desenhar_grade(0, 1)

        # ativa a função para desenhar a peça principal
        self.p.desenhar_peca()

        # desenha o quadrado das próximas peças        
        px.blt(self.t.q_largura*self.t.lado, self.t.lado*4, 2, 0, 60, 75, 90)
        px.blt(self.t.q_largura*self.t.lado, self.t.lado*4 + 90, 2, 75, 0, 75, 150)

        # ativa as funções para desenhar as próximas peças
        self.p1.desenhar_prox_peca()
        self.p2.desenhar_prox_peca()
        self.p3.desenhar_prox_peca()

        # Desenha o quadrado de fundo da pontuação
        px.blt(self.t.q_largura*self.t.lado, 0, 2, 0, 0, 75, 60)

        # desenha a pontuação
        px.text(11*self.t.lado, 0.5*self.t.lado, 'SCORE', 0)
        px.text(11*self.t.lado, 1.25*self.t.lado, str(round(self.pontos)), 0)

        # Desenha o nivel que o jogador tá
        nivel = self.nivel()
        
        # Desenha quantas linhas o jogador eliminou
        px.text(11*self.t.lado, 3*self.t.lado, f'LINHAS: {self.linhas_eliminadas}', 0)

        # verifica se deu game over e mostra a tela vermelha
        if self.game_over_j1:
            self.jogador_1_jogando = False
            px.cls(4)
            px.text((self.t.largura + self.t.lado*4)/2 - self.t.lado, self.t.altura/2 - self.t.lado*2, 'GAME OVER', 0)
            px.text((self.t.largura + self.t.lado*3)/2 - self.t.lado, self.t.altura/2 - self.t.lado, f'YOUR SCORE : {round(self.pontos)}', 0)
            px.text((self.t.largura + self.t.lado*4)/2 - self.t.lado, self.t.altura/2, f'NIVEL: {nivel}', 0)