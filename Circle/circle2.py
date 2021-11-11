# Parametric Equation Circle Generation

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
    PolarCircleAlgo()
    glFlush()

def PolarCircleAlgo():
    theta = 0
    factor = 500
    incr = 1 / factor
    target = math.pi / 4
    
    while (theta <= target):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        plot(x, y)
        theta += incr
   

def plot(x, y):
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glVertex2f(x + xc, y + yc)
    glVertex2f(-x + xc, -y + yc)
    glVertex2f(-x + xc, y + yc)
    glVertex2f(x + xc, -y + yc)
    glVertex2f(y + xc, x + yc)
    glVertex2f(-y + xc, -x + yc)
    glVertex2f(-y + xc, x + yc)
    glVertex2f(y + xc, -x + yc)
    glEnd()
    
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
    glutCreateWindow("Non parametric Circle Generation")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

main()