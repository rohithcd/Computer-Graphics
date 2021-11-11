# Non Parametric Equation Circle Generation

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init():
    glClearColor(1, 1, 1, 0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    NonPolarCircleAlgo()
    glFlush()

def NonPolarCircleAlgo():
    glColor3f(0.0,1.0,0.5)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    x = xc - r
    target = xc + r
    glVertex2f(x, yc)
    glVertex2f(target, yc)
    factor = 7500
    incr = 1 / factor
    x += incr
    while x < target:
        adder = math.sqrt(r * r - (x - xc) * (x - xc))
        glVertex2f(x, yc + adder)
        glVertex2f(x, yc - adder)
        x += incr
    glEnd()
    glFlush()
    
def getInput():
    global r, xc, yc
    r = int(input("Enter radius: "))
    xc = int(input("X Coordinate: "))
    yc = int(input("Y Coordinate: "))

def main():
    getInput()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Polar Circle Generation")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

main()