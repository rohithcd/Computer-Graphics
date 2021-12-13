# Python with OpenGL Introduction 
# Import Code for DDA line drawing
# Code by Sharun E Rajeev

# PyOpenGL Imports
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Round off the number to nearest integer
def ROUND(a):
	return int(a+0.5)

# Function to set pixel at a given coordinate
def setPixel(x,y):
	glBegin(GL_POINTS)
	glVertex2i(x,y)
	glEnd()
	glFlush()

# function to draw line using DDA algorithm
def plotLine(x0,y0,xEnd,yEnd):
	delta_x=xEnd-x0
	delta_y=yEnd-y0
	dx=abs(xEnd-x0)
	dy=abs(yEnd-y0)
	x,y=x0,y0
	steps=dx if dx>dy else dy
	if steps !=0:
		change_x=dx/float(steps)
		change_y=dy/float(steps)
	else:
		change_x=0
		change_y=0
	setPixel(ROUND(x),ROUND(y))
	
	for k in range(steps):
		if delta_x >= 0:  
			x+=change_x
		else:
			x-=change_x
		if delta_y >= 0:
			y+=change_y
		else:
			y-=change_y
		setPixel(ROUND(x),ROUND(y))
