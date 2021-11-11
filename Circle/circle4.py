# Bresenham Integer Circle Generation

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
    BresenIntCircleAlgo()
    glFlush()

def BresenIntCircleAlgo():
    def mh(x, y, D):
        x = x+1
        D = D + (2*x) + 1
        return x, y, D

    def md(x, y, D):
        x = x+1
        y = y-1
        D = D+(2*x)-(2*y)+2
        return x, y, D

    def mv(x, y, D):
        y = y-1
        D = D-(2*y)+1
        return x, y, D
  
    x = 0.0
    y = r
    d = 2*(1-r)
    limit = 0
    v = 1
    
    while(y >= limit):
        setPixel((xc+x)/v, (yc+y)/v)
        setPixel((xc-x)/v, (yc+y)/v)
        setPixel((xc+x)/v, (yc-y)/v)
        setPixel((xc-x)/v, (yc-y)/v)
        setPixel((xc+y)/v, (yc+x)/v)
        setPixel((xc-y)/v, (yc+x)/v)
        setPixel((xc+y)/v, (yc-x)/v)
        setPixel((xc-y)/v, (yc-x)/v)

        if(d < 0):
            k1 = (2*d)+(2*y)-1
            if(k1 <= 0):
                x, y, d = mh(x, y, d)
            else:
                x, y, d = md(x, y, d)
        elif(d > 0):
            k2 = (2*d)-(2*x)-1
            if(k2 <= 0):
                x, y, d = md(x, y, d)
            else:
                x, y, d = mv(x, y, d)
        else:
            x, y, d = md(x, y, d)
    
def setPixel(x, y):
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(3.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
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
    glutCreateWindow("Bresenhan Integer Circle Generation")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

main()