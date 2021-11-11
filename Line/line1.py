#DDA Line drawing Algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(1, 1, 1, 0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    DDALineAlgo()
    glFlush()

def DDALineAlgo():
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    steps = 0
    
    if(abs(dx) > abs(dy)):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    Xinc = dx/steps
    Yinc = dy/steps

    for steps in range(1, steps+1):
        setPixel(round(x),round(y)) 
        x = x + Xinc
        y = y + Yinc

def setPixel(x, y):
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(3.0)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()
    
def getInput():
    global x1, y1, x2, y2
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    

def main():
    getInput()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("DDA Line Generation")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()
    
main()