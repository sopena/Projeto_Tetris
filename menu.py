import pyxel as px
from um_jogador import Jogo

class Menu:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.tela_start = True

        px.init(largura, altura, 'Tetris', 60)
        px.run(self.update, self.draw)
    
    def start_tela(self, largura, altura):
        px.cls(5)
        px.blt(0, 0, 0, 0, 0, 256, 171)
        px.text(largura//2, altura//2, 'PRESSIONE 1 PARA UM JOGADOR\n PRESSIONE 2 PARA DOIS JOGADORES', 0)

    def load_images(self):
        #carrega a imagem da tela de start
        px.image(0).load(0, 0, 'tela_start.png')

    def verificar_players(self):
        if  px.btnp(px.KEY_1):
            self.tela_start = False
            return 1
        if  px.btnp(px.KEY_2):
            self.tela_start = False
            return 2
        
    def update(self):
        self.load_images()
        self.verificar_players()
    
    def draw(self):
        if self.tela_start:
            self.start_tela(self.largura, self.altura)            
            return 0