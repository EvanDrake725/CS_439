import simpleGE, pygame, random
class SpecialCake(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("End.png")
        self.setSize(50,50)   
        self.position=(320,280)
        self.hide()

class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.facing="R"
        self.setImage("finely_r.png")
        self.setSize(50,50)
        self.moveSpeed=2.5
        self.position = (320, 280)
    def process(self):     
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
            self.facing="L"
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            self.facing="R"
        if self.facing=="L":
            position = self.position
            self.setImage("finely_l.png")
            self.setSize(50,50)
            self.position = position
        if self.facing=="R":
            position = self.position
            self.setImage("finely_r.png")
            self.setSize(50,50)
            self.position = position
        if self.x<125:
            self.x=125
        if self.x>515:
            self.x=515
        if self.y<85:
            self.y=85
        if self.y>450:
            self.y=450

class Brat(simpleGE.Sprite):
    def __init__(self, scene, position):
        super().__init__(scene)
        self.position=(position)
        self.emotion="happy"
        self.colorRect("green", (20, 20))
        if self.emotion=="happy":
            self.timer=simpleGE.Timer()
            self.timer.totalTime=random.randint(5,8)
    def process(self):
        if self.emotion=="happy":
            position = self.position
            self.colorRect("green", (20, 20))
            self.position = position
            if self.timer.getTimeLeft()<=0:
                self.emotion="mad" 
        if self.emotion=="mad":
            position = self.position
            self.colorRect("red", (20, 20))
            self.position = position
            if self.collidesWith(self.scene.player):
                self.emotion="happy"
                self.timer.totalTime+=random.randint(6,9)
                self.scene.score+=100

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text="Score: 0"
        self.center=(100,30)

class Game(simpleGE.Scene):
    def __init__(self):       
        super().__init__()
        self.setImage("Background.png")
        self.setCaption("Finley in: Rushtime Madness")
        self.player=Player(self)
        self.brat=[Brat(self,(200,375)),Brat(self,(145,280)),Brat(self,(320,425)),Brat(self,(440,375)),
                   Brat(self,(495,280)),Brat(self,(200,185)),Brat(self,(440,185)),Brat(self,(320,135))]
        self.endCake=SpecialCake(self)
        self.timerEnd=simpleGE.Timer()
        self.score=0
        self.lblScore=LblScore()
        self.timerEnd.totalTime=30
        self.sprites=[self.endCake, self.player, self.brat, self.lblScore]
    def process(self):
        self.lblScore.text=f"Score: {self.score}"
        if self.timerEnd.getTimeLeft()<=0.2:
            self.endCake.show()
            if self.timerEnd.getTimeLeft()<=0:
                self.stop()


class PlayImage(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Play.png")
        self.setSize(75,35)
        self.position=(100,350)

class QuitImage(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Quit.png")
        self.setSize(75,35)
        self.position=(100,450)  

class BackImage(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Back.png")
        self.setSize(75,35)
        self.position=(100,400)  

class StoryImage(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Story.png")
        self.setSize(75,35)
        self.position=(100,400)  

class TitleScreen(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Finley in: Rushtime Madness")
        self.setImage("Title_back.png")
        self.playImg=PlayImage(self)
        self.storyImg=StoryImage(self)
        self.quitImg=QuitImage(self)
        self.sprites=[self.playImg, self.storyImg, self.quitImg]
    def process(self):
        if self.playImg.clicked:
            self.response="play"
            self.stop()
        if self.quitImg.clicked:
            self.response="quit"
            self.stop()
        if self.storyImg.clicked:
            self.response="story"
            self.stop()

class Story(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Finley in: Rushtime Madness")
        self.setImage("Story_back.png")
        self.backImg=BackImage(self)
        self.sprites=[self.backImg]
    def process(self):
        if self.backImg.clicked:
            self.response="back"
            self.stop()

def main():
    keepgoing=True
    while keepgoing:
        title=TitleScreen()
        title.start()
        if title.response=="play":
            game=Game()
            game.start()
        if title.response=="story":
            game=Story()
            game.start()
        else:
            keepgoing=False

if __name__=="__main__":
    main()
