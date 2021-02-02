import turtle
from random import randint

window = turtle.Screen() # open a new windows
turtle.bgcolor("black") # Change the background colour of the screen
turtle.color("yellow") # Choose a color for the star
turtle.speed(0) # How quickly the star is drawn

# The code to draw a single star
def draw_star():
	turns = 5
	turtle.begin_fill()

	while turns > 0:
		turtle.forward(25)
		turtle.left(145)
		turns = turns - 1
	turtle.end_fill()

num_stars = 0
while num_stars < 50:
	x = randint (-300, 300) # Choose a random x-coordinate
	y = randint (-300, 300) # Choose a random y-coordinate
	draw_star() # Call up the draw_star function from above
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	num_stars = num_stars + 1

window.exitonclick # Close the windows when clicked
