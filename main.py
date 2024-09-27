import pygame 
import sys
from setings import *

class Game:
    def __init__(self):
        pygame.init()
        
        #resolução tela
        self.screen = pygame.display.set_mode(res)

        #tempo da tela
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

        def new_game(self):
            self.map = Map(self)
            self.player = Player(self)

        def update(self):
            self.player.update()
            pygame.display.flip()
            self.delta_time = self.clock.tick(fps)
            pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

        def draw(self):
            #exibir tela
            self.screen.fill('black')
            self.map.draw()
            self.player.draw()
        
        def check_events(self): # chegar eventos e fechar tela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        def rin(self): #loop
            while True:
                self.check_events()
                self.update()
                self.draw()

#executar game
if __name__ == "__main__":
    game = Game()
    game.run()