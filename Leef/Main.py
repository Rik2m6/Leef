import random
import pygame as pg
from pygame import display 
from pygame.sprite import Sprite as Spr
from Translate import conversorKeyName
from ChunksConfig import ChuncksConfig

class Parede(Spr):

    def __init__(self, pX, pY):
        super().__init__()
        self.color = (58, 58, 58, 86)
        self.image = pg.surface.Surface((10, 10))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = pX
        self.rect.y = pY

class folha(Spr):

    def __init__(self, pX, pY):
        super().__init__()
        self.color = (77, 117, 11)
        self.image = pg.surface.Surface((5, 5))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = pX
        self.rect.y = pY

class BIOrect(Spr):

    def __init__(self, color, posX, posY, key):
        super().__init__()
        self.key = key
        self.color = color #(51, 245, 113)
        self.image = pg.surface.Surface((50, 50))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
def AnchorBuild(anchor: str) -> int:

    """Uma classe que Recebe um valor anchor, uma string que contem o nome da chunck que vai ser analisada as suas chunck adjancentes.\n
    O valor que vai entrar na chunck consiste no nome da mesma que é gerado com as coordenadas do fim da area daquela chunck.\n
    Exp.: x100y100, x100 é o valor aonde se encontra o fim dela no eixo X e y100 é aonde se encontra o final da chunck no eixo Y.\n
    *Se souber o tamanho da chunk para encontra o seu inicio ou nome das chunks adjacentes."""

    matriz = []
    left = None
    center = None
    right = None 
    x = -50
    y = -50 
    coord = conversorKeyName(anchor)

    return 0 

class Construct():

    def __init__(self, chunks):
        self.posX = 10
        self.posY = 10  
        self.top = False
        self.bottom = False
        self.left = False
        self.right = False
        self.listCollision = []
        self.collisionCoord = []
        self.listNotCollision = []
        self.chunks = chunks

    def create_lim(self):
        for i in range(78):
            self.listCollision.append(Parede(self.posX, self.posY))
            self.collisionCoord.append((self.posX, self.posY))
            self.posX += 10
        self.top = True

        if self.top:
            self.posX = 10
            for i in range(58):
                self.listCollision.append(Parede(self.posX, self.posY))
                self.collisionCoord.append((self.posX, self.posY))
                self.posY += 10
            self.left = True

        if self.left:
            self.posX = 780
            self.posY = 10
            for i in range(58):
                self.listCollision.append(Parede(self.posX, self.posY))
                self.collisionCoord.append((self.posX, self.posY))
                self.posY += 10
            self.right = True

        if self.right:
            self.posX = 10
            self.posY = 580
            for i in range(78):
                self.listCollision.append(Parede(self.posX, self.posY))
                self.collisionCoord.append((self.posX, self.posY))
                self.posX += 10
            self.bottom = True

    def create_leaf(self):
        count = 0 

        while True:
            if count >= 150:
                break
            else:
                corX = random.randint(21, 764)
                corY = random.randint(21, 564)
                target = None

                for i in self.chunks:
                    target = self.chunks[i]["range"]

                    if target["InitX"] <= corX and target["EndX"] >= corX:

                        if target["InitY"] <= corY and target["EndY"] >= corY:

                            if self.chunks[i]["folhasLim"] > self.chunks[i]["folhas"]:
                                self.listNotCollision.append(folha(corX, corY))
                                self.listNotCollision.append(folha(corX+5, corY+5))
                                self.listNotCollision.append(folha(corX+10, corY))
                                self.chunks[i]["folhas"] += 1
                                count += 1

                            if self.chunks[i]["folhasLim"] > 2:
                                self.chunks[i]["bio"] = "old"
                                anchor = f"x{target["EndX"]}y{target["EndY"]}"
                                AnchorBuild(anchor)

class Background():

    def __init__(self, chunks):
        self.xPosIni = 0
        self.yPosIni = 0
        self.target = 0
        self.chunks = chunks
        self.chunksLoad = []

    def start(self): 
        for x, infoRect in enumerate(self.chunks):

            if self.target == 600:
                self.target = 0
                self.yPosIni = 0
                self.xPosIni += 50

            if self.chunks[infoRect]["bio"] == 'old':
                self.chunksLoad.append(BIOrect((120, 220 - (self.chunks[infoRect]["folhas"] * 10), 60), self.xPosIni, self.yPosIni, infoRect))
            
            else:
                self.chunksLoad.append(BIOrect((115, 220, 30), self.xPosIni, self.yPosIni, infoRect))
            
            self.target += 50
            self.yPosIni += 50

def main():
    pg.init()

    chunks = ChuncksConfig()
    window = display.set_mode((800,600))

    build = Construct(chunks)
    build.create_lim()
    listCollision = build.listCollision
    listNotCollision = build.listNotCollision
    collisionCoord = build.collisionCoord
    build.create_leaf()

    canvas = Background(chunks)
    canvas.start()

    running = True 
    chunksLoad = canvas.chunksLoad
    chunksGroup = pg.sprite.Group()
    groupCollision =  pg.sprite.Group()
    groupSpritNotCollision = pg.sprite.Group()

    for classObj in chunksLoad:
        chunksGroup.add(classObj)

    for classObj in listCollision:
        groupCollision.add(classObj)

    for classObj in listNotCollision:
        groupSpritNotCollision.add(classObj)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        chunksGroup.draw(window)
        groupCollision.draw(window)
        groupSpritNotCollision.draw(window)

        pg.display.update()
        
if __name__ == "__main__":
    main()