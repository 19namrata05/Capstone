import turtle 
import random
import math



wn = turtle.Screen()
wn.bgcolor("black")
wn.title("My Game")

class Border(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.color("white")
		self.pensize(3)
		
	def draw_border(self):
		self.penup()
		self.goto(-360, -360)
		self.pendown()
		self.goto(-360, 360)
		self.goto(360, 360)
		self.goto(360, -360)
		self.goto(-360, -360)
		
		
class Goal(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.shape("square")
		self.color("green")
		self.goto(360,0)

	
		
		
		


	
#Instances
border = Border()
goal = Goal()

border.draw_border()


#keyboard binding 



#main loop 
while True:
	wn.update()


































































