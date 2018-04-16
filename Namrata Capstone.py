# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import random

# Create Classes
class Goal(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 3
		self.score = 0
		
	def tick(self):
		self.move()
	
	def move(self):
		self.fd(self.speed)
		
		if self.xcor() > game.SCREEN_WIDTH / 2:
				self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

		if self.xcor() < -game.SCREEN_WIDTH /2 :
			self.goto(game.SCREEN_WIDTH / 2, self.ycor())

		if self.ycor() > game.SCREEN_HEIGHT / 2:
			self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

		if self.ycor() < -game.SCREEN_HEIGHT / 2:
			self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)

	def rotate_left(self):
		self.lt(30)

	def rotate_right(self):
		self.rt(30)

	def accelerate(self):
		self.speed += 1

	def decelerate(self):
		self.speed -= 1
		if self.speed < 0:
			self.speed = 0


class Point(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		
class Enemy(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)


		


		
# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "Namrata capstone porject", 0)

# Create Sprites
goal = Goal("square", "green", 390, 0)

player = Player("circle", "blue", -390, 0)
player.set_image("player.gif", 40, 45)

point = Point("triangle", "yellow", 0, 0)
enemy = Enemy("circle", "red", 100, 100)

# Create Labels
score_label = spgl.Label("Score: 0 ", "white", 300, 250, "Times New Roman" , 20)

 

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.accelerate)
game.set_keyboard_binding(spgl.KEY_DOWN, player.decelerate)
game.set_keyboard_binding(spgl.KEY_LEFT, player.rotate_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.rotate_right)
game.set_keyboard_binding(spgl.KEY_ESCAPE, game.exit)

while True:
	game.tick()

	# Check player enemy collision
	if game.is_collision(player, enemy):
		player.score -= 10
		enemy.goto(random.randint(-390,290),random.randint(-390,290))
		score_label.update("Score: {}".format(player.score))
	
	# Check player point collision
	if game.is_collision(player, point):
		player.score += 10
		point.destroy()
		score_label.update("Score: {}".format(player.score))
	
	# Check player goal collision    
	if game.is_collision(player, goal):
		exit()
		
		

    
    
    
    
    
    
    
    
