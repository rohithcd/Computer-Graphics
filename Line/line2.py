#Symmetric DDA Line drawing Algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import ceil, log10

def ROUND(a):
    return int(a + 0.5)

def find_e(m):
    
    n = ceil(log10(m)/log10(2))
    return 2**(-n)

def init():
    glClearColor(1, 1, 1, 0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    SymmDDALineAlgo()
    glFlush()

def SymmDDALineAlgo():
    dx = x2 - x1
    dy = y2 - y1
    m = max(abs(dx), abs(dy))
    e = find_e(m)

    Xinc = float(dx*e)
    Yinc = float(dy*e)
    x,y = x1, y1
    
    setPixel(ROUND(x),ROUND(y))
    
    while round(x) != x2 or round(y) != y2:
        x += Xinc
        y += Yinc
        setPixel(ROUND(x),ROUND(y))

    setPixel(ROUND(x),ROUND(y)) 

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
    glutCreateWindow("Symmetric DDA Line Generation")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

main()