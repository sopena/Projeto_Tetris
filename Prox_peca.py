import pyxel as px

class Prox_peca:

    def __init__(self, x, y, tipo, lado):
        self.x = x
        self.y = y
        self.tipo = tipo
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

    def desenhar_prox_peca(self):
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
                        px.blt((self.x + self.lado*j) + self.lado/2, (self.y + self.lado*i) + self.lado/2, 1, 0, 0, self.lado, self.lado)
                    if self.tipo == 5:
                        px.blt((self.x + self.lado*j) - self.lado/2, (self.y + self.lado*i) - self.lado/2, 1, 15, 0, self.lado, self.lado)
                    if self.tipo == 6:
                        px.blt(self.x + self.lado*j, self.y + self.lado*i, 1, 75, 0, self.lado, self.lado)
                    if self.tipo == 7:
                        px.blt(self.x + self.lado*j, self.y + self.lado*i, 1, 45, 0, self.lado, self.lado)