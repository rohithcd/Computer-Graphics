#Non Parametric (non Polar) Ellipse Generation Algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def ROUND(a):
    return (a + 0.4)

def init():
    glClearColor(1, 1, 1, 0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    NonPolarEllipseAlgo()
    glFlush()

def NonPolarEllipseAlgo():
    x = -rx
    b = ry
    a = rx
    
    while x < 0:
        y = b* (math.sqrt(1-((x/a)*(x/a))))
        plot(ROUND(x + xc),ROUND(y + yc))
        plot(ROUND(-x + xc), ROUND(y + yc))
        plot(ROUND(-x + xc), ROUND(-y + yc))
        plot(ROUND(x + xc), ROUND(-y + yc))
        x += 0.01

def plot(x, y):
    glColor3f(0, 1, 0)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    
def getInput():
    global rx, ry, xc, yc
    rx = int(input("Enter X-axis radius: "))
    ry = int(input("Enter Y-axis radius: "))
    xc = int(input("X Coordinate: "))
    yc = int(input("Y Coordinate: "))

def main():
    getInput()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Non Polar Ellipse Generation")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

main()