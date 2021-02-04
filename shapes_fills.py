import turtle
import random

hidde = turtle.Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

# set colors for turtle
hidde.color('red', 'blue')

# set pen width
hidde.width(3)

# Fill in shape with color
hidde.begin_fill()
hidde.circle(50)
hidde.end_fill()

hidde.penup()
hidde.forward(150)
hidde.pendown()

hidde.color('yellow', 'black')

hidde.begin_fill()
for x in range(4):
	hidde.forward(100)
	hidde.right(90)
hidde.end_fill()

hidde.setpos(-200, -150)

for x in range(5):
	randColor = random.randrange(0, len(colors))
	hidde.color(colors[randColor])
	rand1 = random.randrange(-300, 300)
	rand2 = random.randrange(-300, 300) 
	hidde.penup()

	hidde.setpos((rand1, rand2))
	hidde.pendown()
	hidde.begin_fill()
	hidde.circle(random.randrange(0, 80))
	hidde.end_fill()