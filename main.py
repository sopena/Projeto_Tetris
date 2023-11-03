from um_jogador import Jogo
from dois_jogadores import Jogo_2

jogadores = int(input('Quantos jogadores vão jogar? Digite 1 ou 2: '))

# medidas das grades e dos quadrados
cor_fundo = 7
cor_grade = 13
lado = 15
q_largura = 10
q_altura = 20
var = 8

# Pontuação das linhas
pontuacao_lin = [100, 300, 500, 800]

# Níveis
level = [0, 1000, 2000, 3000, 5000, 7000, 9000, 11000, 13000, 15000]

nivel_txt = ['NIVEL 1', 'NIVEL 2', 'NIVEL 3', 'NIVEL 4', 'NIVEL 5', 'NIVEL 6', 'NIVEL 7', 'NIVEL 8', 'NIVEL 9', 'NIVEL 10']

# velocidade niveis
vel = 0.2
vels = [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]

print('oi')

if jogadores == 1:
    j = Jogo(q_largura, q_altura, lado, cor_fundo, cor_grade, var, level, vels, vel, pontuacao_lin, 1, nivel_txt)

if jogadores == 2:
    j = Jogo_2(q_largura, q_altura, lado, cor_fundo, cor_grade, var, level, vels, vel, pontuacao_lin, jogadores, nivel_txt)



    