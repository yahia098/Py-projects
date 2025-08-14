import pygame as pg
import sys
pg.init()
FPS = 60
screen_size = (1270,720)
screen = pg.display.set_mode(screen_size)
icon = pg.image.load("./ASSETS/Images/spaceships/ships/green.png").convert_alpha()
pg.display.set_caption("Space Pong")
pg.display.set_icon(icon)
background = pg.image.load("./ASSETS/Images/Background.jpg").convert()
class SpaceShip:
    def __init__(self,image,pos):
        self.image = image
        self.pos_x , self.pos_y = pos
    def move(self,x,y):
        self.pos_y+=y
        self.pos_x+=x
    def draw(self,screen):
        screen.blit(self.image,(self.pos_x,self.pos_y))

pc_img = pg.image.load("./ASSETS/Images/spaceships/ships/Gray1.png").convert_alpha()
pc_img = pg.transform.scale(pc_img, (128,128))
pc_img = pg.transform.rotate(pc_img,270)
player_img = pg.image.load("./ASSETS/Images/spaceships/ships/purple.png").convert_alpha()
player_img = pg.transform.scale(player_img, (128,128))
player_img = pg.transform.rotate(player_img,90)
pc = SpaceShip(pc_img,(10,300))
player = SpaceShip(player_img,(1132,300))
def main():
    run = True
    clock = pg.time.Clock()
    while run :
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False  
        draw_window(pc,player,screen)
    pg.quit()
    sys.exit()

def draw_window(pc,player,screen):
    screen.blit(background,(0,0))
    pc.draw(screen)
    player.draw(screen)
    pg.display.update()

if __name__ == "__main__":
    main()
    