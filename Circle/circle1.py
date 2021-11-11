# MidPoint Circle Generation Algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(1, 1, 1, 0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    MidpointCircleAlgo()
    glFlush()

def MidpointCircleAlgo():
    x = 0
    y = r 
    P = 1 - r   
    
    plot(x+xc,y+yc)
    
    if (r > 0) : 
        
        plot(x+xc,-y+yc)
        plot(y+xc,x+yc)
        plot(y+xc,x+yc)
        plot(-y+xc,x+yc)
 
    while x < y: 
      
        x += 1
 
        if P <= 0:  
            P = P + 2 * x + 1
 
        else:          
            y -= 1
            P = P + 2 * x - 2 * y + 1

        if (y < x): 
            break
 
        plot(x+xc, y+xc)  
        plot(-x+xc, y+xc)  
        plot(x+xc, -y+xc)  
        plot(-x+xc, -y+xc)  
         

        if x != y: 
            plot(y+xc, x+xc)  
            plot(-y+xc, x+xc)  
            plot(y+xc, -x+xc)  
            plot(-y+xc, -x+xc) 

def plot(x, y):
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
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
    glutCreateWindow("MidPoint Circle Generation")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

main()
