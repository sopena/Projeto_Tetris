import pyxel as px

class Tela:

    def __init__(self, q_largura, q_altura, lado, cor_grade, var, jogadores):
        self.q_largura = q_largura
        self.q_altura = q_altura
        self.lado = lado
        self.cor_grade = cor_grade
        self.var = var
        self.largura = q_largura*lado
        self.altura =  q_altura*lado
        self.jogadores = jogadores

        if jogadores == 1:
            # Criar a Matriz da Tela do jogador 1
            self.grade = [[0 for i in range(self.q_largura)] for j in range(self.q_altura)]

            # Adiciona a coluna de 1 da direita da matriz do jogador 1
            for i in range(len(self.grade)):
                self.grade[i].append(self.var)

            for i in range(len(self.grade)):
                self.grade[i].append(self.var)

            # Adiciona a as duas linhas de 1 da matriz
            self.grade.append([self.var for i in range(10)])
            self.grade.append([self.var for i in range(10)])
            self.grade[20].append(0)
            self.grade[21].append(0)

        if jogadores == 2:
            # Criar a Matriz da Tela do jogador 1
            self.grade = [[0 for i in range(self.q_largura)] for j in range(self.q_altura)]

            # Adiciona a coluna de 1 da direita da matriz do jogador 1
            for i in range(len(self.grade)):
                self.grade[i].append(self.var)

            for i in range(len(self.grade)):
                self.grade[i].append(self.var)

            # Adiciona a as duas linhas de 1 da matriz
            self.grade.append([self.var for i in range(10)])
            self.grade.append([self.var for i in range(10)])
            self.grade[20].append(0)
            self.grade[21].append(0)
        
            # Criar a Matriz da Tela do jogador 2
            self.grade_j2 = [[0 for i in range(self.q_largura)] for j in range(self.q_altura)]

            # Adiciona a coluna de 1 da direita da matriz do jogador 2
            for i in range(len(self.grade_j2)):
                self.grade_j2[i].append(self.var)

            for i in range(len(self.grade_j2)):
                self.grade_j2[i].append(self.var)

            # Adiciona a as duas linhas de 1 da matriz
            self.grade_j2.append([self.var for i in range(10)])
            self.grade_j2.append([self.var for i in range(10)])
            self.grade_j2[20].append(0)
            self.grade_j2[21].append(0)

    def descer_linha(self):

        if self.jogadores == 1:
            for i in range(self.q_altura, 0, -1):
                for j in range(self.q_largura, 0, -1):
                    if self.grade[i] == [0]*10 + [self.var]*2:
                        self.grade[i] = self.grade[i-1]
                        self.grade[i-1] = [0]*10 + [self.var]*2
        
        if self.jogadores == 2:
            #desce a linha do jogador 1
            for i in range(self.q_altura, 0, -1):
                for j in range(self.q_largura, 0, -1):
                    if self.grade[i] == [0]*10 + [self.var]*2:
                        self.grade[i] = self.grade[i-1]
                        self.grade[i-1] = [0]*10 + [self.var]*2
            
            #desce a linha do jogador 2
            for i in range(self.q_altura, 0, -1):
                for j in range(self.q_largura, 0, -1):
                    if self.grade_j2[i] == [0]*10 + [self.var]*2:
                        self.grade_j2[i] = self.grade_j2[i-1]
                        self.grade_j2[i-1] = [0]*10 + [self.var]*2

    def desenhar_grade(self, distancia, jogador):

        # Desenha a Grade da matriz na tela
        for x in range(self.q_largura):
            for y in range(self.q_altura):
                #desenha a grade do jogador 1
                px.rectb((x * self.lado) + distancia, (y * self.lado), self.lado, self.lado, self.cor_grade)

        if jogador == 1:
            # Desenha cada bloco na grade da tela do jogador 1
            for i in range(len(self.grade)):
                for j in range(len(self.grade[i])):
                    if self.grade[i][j] == 1:
                        px.blt(self.lado*j, self.lado*i, 1, 105, 0, self.lado, self.lado)
        
        if jogador == 2:
            # Desenha cada bloco na grade da tela do jogador 2
            for i in range(len(self.grade)):
                for j in range(len(self.grade[i])):
                    if self.grade[i][j] == 1:
                        px.blt(self.lado*j + distancia, self.lado*i, 1, 120, 0, self.lado, self.lado)