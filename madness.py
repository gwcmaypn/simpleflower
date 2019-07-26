#author: May Phuc Nguyen
#module: Madness pt.2
#desc: Turtle

import turtle
""" Draw a flower in Pyhton"""

def draw_square(square):
	for i in range(0,2):
		square.forward(100)
		square.right(30)
		square.forward(100)
		square.right(150)


def draw_flower():
	window = turtle.Screen()
	window.bgcolor("white")

	pen = turtle.Turtle()
	pen.fillcolor("lightblue")
	pen.shape("turtle")
	pen.color("pink")


	for i in range(0,4):
		pen.circle(50)
		pen.right(90)
	pen.right(90)
	pen.forward(300)
	pen.right(90)

draw_flower()
