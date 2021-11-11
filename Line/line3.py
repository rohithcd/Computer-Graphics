# Generalized Integer Bresenham Line Drawing Algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def Sign(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0

def init():
    glClearColor(1, 1, 1, 0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    BresenLineAlgo()
    glFlush()

def BresenLineAlgo():
    x = x1
    y = y2
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    s1 = Sign(x2 - x1)
    s2 = Sign(y2 - y1)

    if dx > dy:
        dx, dy = dy, dx
        ic = 1
    else:
        ic = 0
    
    e = 2 * dy - dx

    for i in range(1, dx + 1):
        setPixel(x, y)
        while e >= 0:
            if ic == 1:
                x += s1
            else:
                y += s2
            e -= 2 * dx
        if ic == 1:
            y += s2
        else:
            x += s1
        e += 2 * dy

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
    glutCreateWindow("Bresenham Line Generation")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()
    
main()