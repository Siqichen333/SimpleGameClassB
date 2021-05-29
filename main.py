from SimpleGame.Scene import Scene
from SimpleGame.Sprite import Sprite
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
		self.spaceship = Sprite(self, "spaceship100.png", 100, 93)
		
	def updateGame(self):
		print("My Update")
		self.spaceship.x +=1
		self.spaceship.update()

myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())


# Sean's Sprite Sheet
# https://opengameart.org/content/cat-fighter-sprite-sheet
# Cat by DogChicken @ OpenGameArt.org

#Lucas' sprite sheet
#https://opengameart.org/content/esquire-animated-classic-hero-edit
#Knight by Umz @http://umzgames.com/


#Siqi's sprite sheet
#


#Qingyun's sprite sheet
#https://opengameart.org/content/cute-monster-sprite-sheet

## Alex's sprite sheet
#cartoon-rogue by 
#