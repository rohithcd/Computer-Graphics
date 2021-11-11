# Importing everything from libraries GL, GLU & GLUT

from OpenGL.GL import * 
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(0, 0, 0, 1) #Setting color specified to GL_COLOR_BUFFER_BIT flag 
    gluOrtho2D(-100, 100, -100, 100) #Setting X & Y coordinates for program

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_POINTS)
    glVertex2f(0, 0)
    glEnd()
    glFlush() #pushes the graphics specified to the screen

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("OpenGL Program")
    glutDisplayFunc(draw)
    init()
    glutMainLoop() #To run the program continuously

main()
