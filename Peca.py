import pyxel as px

class Peca:

    def __init__(self, x, y, tipo, largura, altura, lado):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.largura = largura
        self.altura = altura
        self.lado = lado

        if self.tipo == 1:  # T
            self.grade = [[0, 0, 0], [1, 1, 1], [0, 1, 0]]
            self.size = 3
            self.cor_peca = 2

        if self.tipo == 2:  # Z
            self.grade = [[0, 0, 0], [1, 1, 0], [0, 1, 1]]
            self.size = 3
            self.cor_peca = 8

        if self.tipo == 3:  # J
            self.grade = [[0, 0, 0], [1, 0, 0], [1, 1, 1]]
            self.size = 3
            self.cor_peca = 1

        if self.tipo == 4:  # Q
            self.grade = [[1, 1], [1, 1]]
            self.size = 2
            self.cor_peca = 10

        if self.tipo == 5:  # I
            self.grade = [[0, 0, 0, 0], [0, 0, 0, 0],
                          [1, 1, 1, 1], [0, 0, 0, 0]]
            self.size = 4
            self.cor_peca = 6

        if self.tipo == 6:  # S
            self.grade = [[0, 0, 0], [0, 1, 1], [1, 1, 0]]
            self.size = 3
            self.cor_peca = 11

        if self.tipo == 7:  # L
            self.grade = [[0, 0, 0], [0, 0, 1], [1, 1, 1]]
            self.size = 3
            self.cor_peca = 9

    def rotacao(self, t, jogador):
        transposta = [[0 for i in range(self.size)] for j in range(self.size)]
        for l in range(self.size):
            for c in range(self.size):
                transposta[self.size-1-c][l] = self.grade[l][c]

        # Testa a descida para poder girar
        for i in range(self.size):
            for j in range(self.size):
                if transposta[i][j]*(self.y + self.size*self.lado) >= self.altura:
                    return 0

                if jogador == 1:
                    if ((t.grade[int(self.y + i*self.lado + self.lado)//self.lado][int(self.x + self.lado*j)//self.lado])*transposta[i][j] != 0):
                        return 0

                if jogador == 2:
                    if ((t.grade[int(self.y + i*self.lado + self.lado)//self.lado][int(self.x - (self.largura + self.lado*5) + self.lado*j)//self.lado])*transposta[i][j] != 0):
                        return 0

        # Permuta as linhas e colunas das matrizes e rotaciona a peça
        for i in range(self.size):
            for j in range(self.size):
                self.grade[i][j] = transposta[i][j]

    def descer(self, vel, t, jogador):
            for i in range(self.size):
                for j in range(self.size):
                    if self.grade[i][j]*(self.y + i*self.lado) >= self.altura:
                        return 0
                    
                    if jogador == 1:
                        if ((t.grade[int(self.y + i*self.lado + self.lado)//self.lado][int(self.x + self.lado*j)//self.lado])*self.grade[i][j] != 0):
                            return 0
                    if jogador == 2:
                        if ((t.grade[int(self.y + i*self.lado + self.lado)//self.lado][int(self.x - (self.largura + self.lado*5) + self.lado*j)//self.lado])*self.grade[i][j] != 0):
                            return 0
            self.y = self.y + vel
            return 1

    def direita(self, t, jogador):
        for i in range(self.size):
            for j in range(self.size):
                if jogador == 1:
                    if self.grade[i][j]*(self.x + j*self.lado + 1) >= self.largura:
                        return 0
                    if (t.grade[int(self.y + self.lado*i + self.lado//2 + 1)//self.lado][int(self.x + j*self.lado + self.lado)//self.lado])*self.grade[i][j] != 0:
                        return 0
                    
                if jogador == 2:
                    if self.grade[i][j]*(self.x + j*self.lado + 1) >= (self.largura*2 + 10*self.lado):
                        return 0
                    if (t.grade[int(self.y + self.lado*i + self.lado//2 + 1)//self.lado][int((self.x  + j*self.lado + self.lado) - (self.largura + self.lado*5))//self.lado])*self.grade[i][j] != 0:
                        return 0

        self.x = self.x + self.lado
        return 1

    def esquerda(self, t, jogador):
        for i in range(self.size):
            for j in range(self.size):
                if self.grade[i][j]*(self.x + self.lado*j - 1) < 0:
                    return 0

                if jogador == 1:
                    if t.grade[int(self.y + self.lado*i + self.lado//2 + 1)//self.lado][int(self.x + self.lado*j - 1)//self.lado]*self.grade[i][j] != 0:
                        return 0
                if jogador == 2:
                    if t.grade[int(self.y + self.lado*i + self.lado//2 + 1)//self.lado][int(self.x - (self.largura + self.lado*5) + self.lado*j - 1)//self.lado]*self.grade[i][j] != 0:
                        return 0

        self.x = self.x - self.lado
        return 1

    def baixo(self, t, jogador):
        for i in range(self.size):
            for j in range(self.size):
                if self.grade[i][j]*(self.y + self.size*self.lado) >= self.altura:
                    return 0
                
                if jogador == 1:
                    if t.grade[int(self.y + self.lado + i*self.lado)//self.lado][int(self.x + self.lado*j)//self.lado]*self.grade[i][j] != 0:
                        return 0
                if jogador == 2:
                    if t.grade[int(self.y + self.lado + i*self.lado)//self.lado][int(self.x - (self.largura + self.lado*5) + self.lado*j)//self.lado]*self.grade[i][j] != 0:
                        return 0

        # evitar que a peça nasça caindo já quando estiver apertando o botão baixo
        if self.y > -self.lado/2:
            self.y = self.y + self.lado//3
        return 1

    def desenhar_peca(self):
        #desenha a peça do jogador
        for i in range(len(self.grade)):
            for j in range(len(self.grade[i])):
                if self.grade[i][j] == 1:
                    if self.tipo == 1:
                        px.blt(self.x + self.lado*j, self.y + self.lado*i, 1, 60, 0, self.lado, self.lado)
                    if self.tipo == 2:
                        px.blt(self.x + self.lado*j, self.y + self.lado*i, 1, 90, 0, self.lado, self.lado)
                    if self.tipo == 3:
                        px.blt(self.x + self.lado*j, self.y + self.lado*i, 1, 30, 0, self.lado, self.lado)
                    if self.tipo == 4:
                        px.blt(self.x + self.lado*j, self.y + self.lado*i, 1, 0, 0, self.lado, self.lado)
                    if self.tipo == 5:
                        px.blt(self.x + self.lado*j, self.y + self.lado*i, 1, 15, 0, self.lado, self.lado)
                    if self.tipo == 6:
                        px.blt(self.x + self.lado*j, self.y + self.lado*i, 1, 75, 0, self.lado, self.lado)
                    if self.tipo == 7:
                        px.blt(self.x + self.lado*j, self.y + self.lado*i, 1, 45, 0, self.lado, self.lado)
                    
                    