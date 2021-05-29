from SimpleGame.Scene import Scene
from SimpleGame.Sprite import Sprite
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
		self.spaceship = Sprite(self, "spaceship100.png", 100, 93)
		self.spaceship.y = 
		
	def updateGame(self):
		print("My Update")
		
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
#https://opengameart.org/content/wizard-warrior----hero
#https://opengameart.org/content/dark-alchemyst----villain


#Qingyun's sprite sheet
#https://opengameart.org/content/cute-monster-sprite-sheet

#Anthony's sprite sheet
# https://opengameart.org/content/dog-platformer-fighter
# No attribution needed

#
#Justin's sprite sheet
#https://opengameart.org/content/pixel-art-mini-golem
#By PixElthen



#Alex's sprite sheet