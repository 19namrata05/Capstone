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
		self.speed = 5
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
		self.goto(random.randint(-250,250),random.randint(-250,250))	
		self.setheading(random.randint(0,360))
		
class Enemy(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 9
		self.goto(random.randint(-250,250),random.randint(-250,250))	
		self.setheading(random.randint(0,360))
		
		#Border Checking
		if self.xcor() > 290 or self.xcor() < -290:
				self.left(60)
		if self.ycor() > 390 or self.ycor() < -390:
				self.left(60)
		
	def jump(self):
		self.goto(random.randint(-250,250),random.randint(-250,250))	
		self.setheading(random.randint(0,360))	

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

class Enemy2(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 9
		self.goto(random.randint(-250,250),random.randint(-250,250))	
		self.setheading(random.randint(0,360))
		
		#Border Checking
		if self.xcor() > 290 or self.xcor() < -290:
				self.left(60)
		if self.ycor() > 390 or self.ycor() < -390:
				self.left(60)
		
	def jump(self):
		self.goto(random.randint(-250,250),random.randint(-250,250))	
		self.setheading(random.randint(0,360))	

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


		
# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black","Namrata capstone porject", 0)
game.set_background("galaxy_stars_universe_light_planet_63624_800x600.gif")

# Create Sprites
goal = Goal("square", "green", 340, -150)

goal.set_image("7-2-earth-png-pic-thumb.gif", 200, 200)

player = Player("circle", "blue", -390, 0)
player.set_image("Webp.net-resizeimage copy 2.gif", 79, 78)

points = []

for count in range(9):
	points.append(Point("Webp.net-resizeimage copy 3.gif", "yellow", 42, 48))
	
enemies = []
for count in range(4):
	enemies.append(Enemy("Webp.net-resizeimage-2.gif", "red", 54, 54))
	
enemies2 = []
for count in range(4):
	enemies2.append(Enemy2("Webp.net-resizeimage copy 4.gif", "red", 49, 44))

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
	for enemy in enemies:
		if game.is_collision(player, enemy):
			player.score -= 10
			enemy.goto(random.randint(-390,390),random.randint(-290,290))
			score_label.update("Score: {}".format(player.score))
			
	for enemy2 in enemies2:
		if game.is_collision(player, enemy2):
			player.score -= 10
			enemy2.goto(random.randint(-390,390),random.randint(-290,290))
			score_label.update("Score: {}".format(player.score))
	
	# Check player point collision
	for point in points:
		if game.is_collision(player, point):
			player.score += 10
			point.destroy()
			score_label.update("Score: {}".format(player.score))
	
	# Check player goal collision    
	if game.is_collision(player, goal):
		exit()
		
		

    
    
    
    
    
    
    
    
