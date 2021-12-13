# Python with OpenGL Introduction 
# Code that draws a point in the middle of the screen
# Code by Sharun E Rajeev

# PyOpenGL Imports
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Init function
def init(w,h):
    # Set the background colour
    glClearColor(1.0,1.0,1.0,1.0)
    # Defines in Screen Coordinates system
    gluOrtho2D(0,w,h,0)

# function to plot point
def plot(w,h):
    # Clear the screen with the background colour
    glClear(GL_COLOR_BUFFER_BIT)
    # Set the colour to draw the point
    glColor3f(0,0,0)
    # Draw the point
    glPointSize(1)
    # Tells the computer that we are going to draw a point
    glBegin(GL_POINTS)
    # Draw the point
    glVertex2f(w/2,h/2)
    # Tells the computer that we are done drawing a point
    glEnd()
    # Swap the buffers
    glFlush()

# main function
def main():
    # Initialise the GLUT library
    glutInit()
    # Set the display mode
    glutInitDisplayMode(GLUT_RGB)
    # Set the window size
    width = glutGet(GLUT_SCREEN_WIDTH)
    height = glutGet(GLUT_SCREEN_HEIGHT)
    # Set the window size
    glutInitWindowSize(width,height)
    # Set the window position
    glutInitWindowPosition(0,0)
    # Create the window
    glutCreateWindow("Introduction to Python OpenGL")
    # Define the callback functions
    glutDisplayFunc(lambda: plot(width,height))
    # Set the init function
    init(width,height)
    # Enter the main loop
    glutMainLoop()

# Call the main function
main()