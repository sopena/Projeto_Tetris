import pyxel as px
import random

from Tela import Tela
from Peca import Peca
from Prox_peca import Prox_peca

class Jogo_2:

    def __init__(self, q_largura, q_altura, lado, cor_fundo, cor_grade, var, level, vels, vel, pontuacao_lin, jogadores, nivel_txt):
        self.level = level
        self.nivel_txt = nivel_txt
        self.vels = vels
        self.vel = vel
        self.vel_j2 = vel
        self.pontos = 0
        self.pontos_j2 = 0
        self.linhas_eliminadas = 0
        self.linhas_eliminadas_j2 = 0
        self.pontuacao_lin = pontuacao_lin
        self.cor_fundo = cor_fundo
        self.jogador_1 = 1
        self.jogador_2 = 2
        self.cont_peca_j1 = 0
        self.cont_peca_j2 = 0
        self.jogador_1_jogando = True
        self.jogador_2_jogando = True
        self.game_over_j1 = False
        self.game_over_j2 = False
        

        self.tela_start = True

        #lista que guarda a sequancia de peças criadas
        self.peca_aleatoria = [random.randint(1, 7), random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)]
        


        #Jogador 1
        self.t = Tela(q_largura, q_altura, lado, cor_grade, var, jogadores)
        self.p = Peca(self.t.largura//2 - lado, -lado, self.peca_aleatoria[0], self.t.largura, self.t.altura, lado)
        self.p1 = Prox_peca(11*lado, 5*lado, self.peca_aleatoria[1], lado)
        self.p2 = Prox_peca(11*lado, 10*lado, self.peca_aleatoria[2], lado)
        self.p3 = Prox_peca(11*lado, 15*lado, self.peca_aleatoria[3], lado)

        #Jogador 2
        self.t_j2 = Tela(q_largura, q_altura, lado, cor_grade, var, jogadores)
        self.p_j2 = Peca((self.t_j2.largura//2 - lado) + (self.t_j2.largura + lado*5), -lado, self.peca_aleatoria[0], self.t_j2.largura, self.t_j2.altura, self.t.lado)
        self.p1_j2 = Prox_peca(11*lado + (self.t_j2.largura + lado*5), 5*lado, self.peca_aleatoria[1], lado)
        self.p2_j2 = Prox_peca(11*lado + (self.t_j2.largura + lado*5), 10*lado, self.peca_aleatoria[2], lado)
        self.p3_j2 = Prox_peca(11*lado + (self.t_j2.largura + lado*5), 15*lado, self.peca_aleatoria[3], lado)

        px.init((self.t.largura + lado*5)*2, self.t.altura, title='Tetris', fps=60)
        px.run(self.update, self.draw)
            
    # Adiciona a peça na matriz
    def add_peca(self, jogador):
        #jogador 1
        if jogador == 1:
            for i in range(self.p.size):
                for j in range(self.p.size):
                    if self.p.grade[i][j] == 1:
                        self.t.grade[int(self.p.y + self.t.lado*i)//self.t.lado][int(self.p.x + self.t.lado*j)//self.t.lado] = 1 
            self.cont_peca_j1 += 1 

        #jogador 2
        if jogador == 2:
            for i in range(self.p_j2.size):
                for j in range(self.p_j2.size):
                    if self.p_j2.grade[i][j] == 1:
                        self.t_j2.grade[int(self.p_j2.y + self.t.lado*i)//self.t.lado][int(self.p_j2.x - (self.t_j2.largura + self.t_j2.lado*5) + self.t.lado*j)//self.t.lado] = 1     
            self.cont_peca_j2 += 1 

    def criar_prox_peca(self, jogador):
        #Se o contador de peças do jogador 1 for maior que a do jogador 2, então adiciona uma nova peça aleatória na lista de peças
        if jogador == 1:
            if self.cont_peca_j1 > self.cont_peca_j2:
                self.peca_aleatoria.append(self.peca_ale)
            
            # O +3 serve para pular as peças que já existem na lista
            # Se o contador de peças do jogador 1 for menor que o tamanho da lista de peças,
            # ele vai retornar uma peça a partir do valor do contador
            if self.cont_peca_j1 + 3 < len(self.peca_aleatoria):
                return self.peca_aleatoria[self.cont_peca_j1 + 3]
            
        #Se o contador de peças do jogador 2 for maior que a do jogador 1, então adiciona uma nova peça aleatória na lista de peças
        if jogador == 2:
            if self.cont_peca_j2 > self.cont_peca_j1:
                self.peca_aleatoria.append(self.peca_ale)
            
            if self.cont_peca_j2 + 3 < len(self.peca_aleatoria):
                return self.peca_aleatoria[self.cont_peca_j2 + 3]
        
    def randomizar_peca(self):
        self.peca_ale = random.randint(1, 7)

    # Muda a velocidade de caida da peça de acordo com o nivel
    def mudar_vel(self, pontos):
        for i in range(len(self.level)):
            if pontos >= self.level[i]:
                vel = self.vels[i]
        return vel
    
    def nivel(self, vel, distancia):
        for i in range(len(self.vels)):
            if vel == self.vels[i]:
                px.text(11*self.t.lado + distancia, 1.85*self.t.lado + 4, f'{self.nivel_txt[i]}', 0)
                nivel = f'{i + 1}'
        return nivel

    def eliminar(self, pontos):
        if pontos == self.pontos:        
            eliminou = 0
            for i in range(self.t.q_altura, 0, -1):
                if self.t.grade[i] == [1]*self.t.q_largura + [self.t.var]*2:
                    self.t.grade[i] = [0]*self.t.q_largura + [self.t.var]*2
                    eliminou += 1
                    self.linhas_eliminadas += 1
        
        if pontos == self.pontos_j2:
            eliminou = 0
            for i in range(self.t.q_altura, 0, -1):
                if self.t_j2.grade[i] == [1]*self.t.q_largura + [self.t.var]*2:
                    self.t_j2.grade[i] = [0]*self.t.q_largura + [self.t.var]*2
                    eliminou += 1
                    self.linhas_eliminadas_j2 += 1

        # sistema de pontuação pela quantidade de linhas eliminadas
        if eliminou == 1:
            pontos += self.pontuacao_lin[0]
        if eliminou == 2:
            pontos += self.pontuacao_lin[1]
        if eliminou == 3:
            pontos += self.pontuacao_lin[2]
        if eliminou == 4:
            pontos += self.pontuacao_lin[3]
        return pontos
    
    def start_tela(self):
        px.cls(5)

        px.blt((self.t.largura + self.t.lado*5) - 128, (self.t.altura)//2 - 85.5, 0, 0, 0, 256, 171)
        px.text((self.t.largura + self.t.lado*5) - self.t.lado*3 + 5, ((self.t.altura)//2) + self.t.lado, 'PRESS SPACE TO START', 0)

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

        if jogador == 2:
            if (desceu == 0):
                if self.p_j2.y < 0:
                    return True
        return False
    
    def ganhou(self, nivel, distancia, pontos):
                px.rect(distancia, 0, self.t.largura + self.t.lado*5, self.t.altura, 11)
                px.rectb(distancia, 0, self.t.largura + self.t.lado*5, self.t.altura, 0)

                px.text(((self.t.largura + self.t.lado*4)/2 - self.t.lado) + distancia, self.t.altura/2 - self.t.lado*2, 'YOU WIN!', 0)
                px.text(((self.t.largura + self.t.lado*3)/2 - self.t.lado) + distancia, self.t.altura /2 - self.t.lado, f'YOUR SCORE : {round(pontos)}', 0)
                px.text(((self.t.largura + self.t.lado*4)/2 - self.t.lado) + distancia, self.t.altura/2, f'NIVEL: {nivel}', 0)

    def jogador_um(self):
        # Ativa a Função descer e cria uma nova peça
        self.desceu = self.p.descer(self.vel, self.t, self.jogador_1)

        #verifica se deu game over
        self.game_over_j1 = self.game_over(self.desceu, self.jogador_1)
        if self.game_over_j1:
            self.jogador_1_jogando = False
            return 0 
        
        if self.desceu == 0:
            self.add_peca(self.jogador_1)
            self.pontos = self.eliminar(self.pontos)
            self.t.descer_linha()
            self.t.descer_linha()
            self.t.descer_linha()
            self.t.descer_linha()
            self.randomizar_peca()
            self.peca_aleatoria_5 = self.criar_prox_peca(self.jogador_1)

            # Fazer a permutação do Tipo das peças e randomizar a última jogador 1
            self.p = Peca((self.t.largura//2 - self.t.lado), -self.t.lado, self.p1.tipo, self.t_j2.largura, self.t_j2.altura, self.t.lado)
            self.p1 = Prox_peca(11*self.t.lado, 5*self.t.lado, self.p2.tipo, self.t.lado)
            self.p2 = Prox_peca(11*self.t.lado, 10*self.t.lado, self.p3.tipo, self.t.lado)
            self.p3 = Prox_peca(11*self.t.lado, 15*self.t.lado, self.peca_aleatoria_5, self.t.lado)

        # atribui a variavel a velocidade que o jogo tem que estar naquele nivel
        #jogador 1
        self.vel = self.mudar_vel(self.pontos)

        # MOVIMENTAÇÃO JOGADOR 1
        if px.btnp(px.KEY_D):
            self.p.direita(self.t, self.jogador_1)

        if px.btnp(px.KEY_A):
            self.p.esquerda(self.t, self.jogador_1)

        if px.btn(px.KEY_S):
            self.p.baixo(self.t, self.jogador_1)
            if self.p.y > -self.t.lado/2:
                self.pontos += 0.3

        if px.btnp(px.KEY_W):
            self.p.rotacao(self.t, self.jogador_1)

    def jogador_dois(self):

        # Ativa a função descer do jogador 2
        self.desceu_j2 = self.p_j2.descer(self.vel_j2, self.t_j2, self.jogador_2)

        #verifica se deu game over
        self.game_over_j2 = self.game_over(self.desceu_j2, self.jogador_2)
        if self.game_over_j2:
            self.jogador_2_jogando = False
            return 0
        
        if self.desceu_j2 == 0:
            self.add_peca(self.jogador_2)
            self.pontos_j2 = self.eliminar(self.pontos_j2)
            self.t_j2.descer_linha()
            self.t_j2.descer_linha()
            self.t_j2.descer_linha()
            self.t_j2.descer_linha()
            self.randomizar_peca()
            self.peca_aleatoria_5 = self.criar_prox_peca(self.jogador_2)

            # Fazer a permutação do Tipo das peças e randomizar a última jogador 1
            self.p_j2 = Peca((self.t_j2.largura//2 - self.t.lado) + (self.t_j2.largura + self.t.lado*5), -self.t.lado, self.p1_j2.tipo, self.t_j2.largura, self.t_j2.altura, self.t.lado)
            self.p1_j2 = Prox_peca(11*self.t.lado + (self.t_j2.largura + self.t.lado*5), 5*self.t.lado, self.p2_j2.tipo, self.t.lado)
            self.p2_j2 = Prox_peca(11*self.t.lado + (self.t_j2.largura + self.t.lado*5), 10*self.t.lado, self.p3_j2.tipo, self.t.lado)
            self.p3_j2 = Prox_peca(11*self.t.lado + (self.t_j2.largura + self.t.lado*5), 15*self.t.lado, self.peca_aleatoria_5, self.t.lado)

            # atribui a variavel a velocidade que o jogo tem que estar naquele nivel
            #jogador 2
            self.vel_j2 = self.mudar_vel(self.pontos_j2)

        # MOVIMENTAÇÃO JOGADOR 2
        if px.btnp(px.KEY_RIGHT):
            self.p_j2.direita(self.t_j2, self.jogador_2)

        if px.btnp(px.KEY_LEFT):
            self.p_j2.esquerda(self.t_j2, self.jogador_2)

        if px.btn(px.KEY_DOWN):
            self.p_j2.baixo(self.t_j2, self.jogador_2)
            if self.p_j2.y > -self.t_j2.lado/2:
                self.pontos_j2 += 0.3

        if px.btnp(px.KEY_UP):
            self.p_j2.rotacao(self.t_j2, self.jogador_2)
    
    def update(self):
        self.load_images()

        #Enquanto não clicar enter o jogo não começa
        if self.tela_start:
            if  px.btnp(px.KEY_SPACE):
                self.tela_start = False
            return
        
        #testa se o jogador 1 pode continuar jogando
        if self.jogador_1_jogando:
            self.jogador_um()

        #testa se o jogador 2 pode continuar jogando
        if self.jogador_2_jogando:
            self.jogador_dois()

    def draw(self):
        if self.tela_start:
            self.start_tela()            
            if  px.btnp(px.KEY_DELETE):
                self.tela_start = False
            return

        px.cls(self.cor_fundo)
        
        #jogador 1
        self.t.desenhar_grade(0, self.jogador_1)

        #jogador2
        self.t_j2.desenhar_grade((self.t_j2.largura + self.t_j2.lado*5), self.jogador_2)

        #jogador 1
        self.p.desenhar_peca()

        #jogador 2
        self.p_j2.desenhar_peca()

        # desenha o quadrado de fundo das proximas peças do jogador 1
        px.blt(self.t.q_largura*self.t.lado, self.t.lado*4, 2, 0, 60, 75, 90)
        px.blt(self.t.q_largura*self.t.lado, self.t.lado*4 + 90, 2, 75, 0, 75, 150)

        # desenha o quadrado de fundo das proximas peças do jogador 2
        px.blt(self.t.q_largura*self.t.lado + (self.t_j2.largura + self.t_j2.lado*5), self.t.lado*4, 2, 0, 60, 75, 90)
        px.blt(self.t.q_largura*self.t.lado + (self.t_j2.largura + self.t_j2.lado*5), self.t.lado*4 + 90, 2, 75, 0, 75, 150)

        # ativa as funções para desenhar as próximas peças do jogador 1
        self.p1.desenhar_prox_peca()
        self.p2.desenhar_prox_peca()
        self.p3.desenhar_prox_peca()

        # ativa as funções para desenhar as próximas peças do jogador 2
        self.p1_j2.desenhar_prox_peca()
        self.p2_j2.desenhar_prox_peca()
        self.p3_j2.desenhar_prox_peca()

        # Desenha o quadrado de fundo da pontuação do jogador 1
        px.blt(self.t.q_largura*self.t.lado, 0, 2, 0, 0, 75, 60)

        # Desenha o quadrado de fundo da pontuação do jogador 2
        px.blt(self.t.q_largura*self.t.lado + (self.t_j2.largura + self.t_j2.lado*5), 0, 2, 0, 0, 75, 60)

        # desenha a pontuação do jogador 1
        px.text(11*self.t.lado, 0.5*self.t.lado, 'SCORE', 0)
        px.text(11*self.t.lado, 1.25*self.t.lado, str(round(self.pontos)), 0)

        # desenha a pontuação do jogador 2
        px.text(11*self.t.lado + (self.t_j2.largura + self.t_j2.lado*5), 0.5*self.t.lado, 'SCORE', 0)
        px.text(11*self.t.lado + (self.t_j2.largura + self.t_j2.lado*5), 1.25*self.t.lado, str(round(self.pontos_j2)), 0)


        # Desenha o nivel que o jogador 1 está
        nivel = self.nivel(self.vel, 0)
        
        # Desenha o nivel que o jogador 2 está
        nivel_j2 = self.nivel(self.vel_j2, (self.t_j2.largura + self.t.lado*5))


        # Desenha quantas linhas o jogador 1 eliminou
        px.text(11*self.t.lado, 3*self.t.lado, f'LINHAS: {self.linhas_eliminadas}', 0)

        # Desenha quantas linhas o jogador 2 eliminou
        px.text(11*self.t.lado + (self.t_j2.largura + self.t_j2.lado*5), 3*self.t.lado, f'LINHAS: {self.linhas_eliminadas_j2}', 0)


        # verifica se deu game over e mostra a tela vermelha para o jogador 1
        if self.game_over_j1:
            self.jogador_1_jogando = False

            px.rect(0, 0, self.t.largura + self.t.lado*5, self.t.altura, 4)
            px.rectb(0, 0, self.t.largura + self.t.lado*5, self.t.altura, 0)

            px.text((self.t.largura + self.t.lado*4)/2 - self.t.lado, self.t.altura/2 - self.t.lado*2, 'GAME OVER', 0)
            px.text((self.t.largura + self.t.lado*3)/2 - self.t.lado, self.t.altura /2 - self.t.lado, f'YOUR SCORE : {round(self.pontos)}', 0)
            px.text((self.t.largura + self.t.lado*4)/2 - self.t.lado, self.t.altura/2, f'NIVEL: {nivel}', 0)

        # verifica se deu game over e mostra a tela vermelha para o jogador 2
        if self.game_over_j2:
            self.jogador_2_jogando = False

            px.rect(self.t.largura + self.t.lado*5, 0, self.t.largura + self.t.lado*5, self.t.altura, 4)
            px.rectb(self.t.largura + self.t.lado*5, 0, self.t.largura + self.t.lado*5, self.t.altura, 0)

            px.text(((self.t.largura + self.t.lado*4)/2 - self.t.lado) + (self.t_j2.largura + self.t_j2.lado*5), self.t.altura/2 - self.t.lado*2, 'GAME OVER!', 0)
            px.text(((self.t.largura + self.t.lado*3)/2 - self.t.lado) + (self.t_j2.largura + self.t_j2.lado*5), self.t.altura /2 - self.t.lado, f'YOUR SCORE : {round(self.pontos_j2)}', 0)
            px.text(((self.t.largura + self.t.lado*4)/2 - self.t.lado) + (self.t_j2.largura + self.t_j2.lado*5), self.t.altura/2, f'NIVEL: {nivel_j2}', 0)

        #Verifica qual player ganhou
        if (self.jogador_1_jogando == False):
            if (self.jogador_2_jogando == False):
                if self.pontos > self.pontos_j2:
                    self.ganhou(nivel, 0, self.pontos)
                
                if self.pontos_j2 > self.pontos:
                    self.ganhou(nivel_j2, (self.t_j2.largura + self.t_j2.lado*5), self.pontos_j2)