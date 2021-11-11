from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def init():
    glClearColor(1, 1, 1, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    drawCircle()
    glFlush()


def drawCircle():
    x = r 
    y = 0  
    
    plot(x+xc,y+yc)
    
    if (r > 0) : 
        
        plot(x+xc,-y+yc)
        plot(y+xc,x+yc)
        plot(y+xc,x+yc)
        plot(-y+xc,x+yc)
 
    P = 1 - r  
  
    while x > y: 
      
        y += 1
 
        if P <= 0:  
            P = P + 2 * y + 1
 
        else:          
            x -= 1
            P = P + 2 * y - 2 * x + 1

        if (x < y): 
            break
 
        plot(x+xc,y+xc)  
        plot(-x+xc,y+xc)  
        plot(x+xc,-y+xc)  
        plot(-x+xc,-y+xc)  
         

        if x != y: 
            plot(y+xc,x+xc)  
            plot(-y+xc,x+xc)  
            plot(y+xc,-x+xc)  
            plot(-y+xc,-x+xc) 

# def circle(xc, yc, r):


def plot(x, y):
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glVertex2i(x + xc, y + yc)
    glEnd()


def main():
    global r, xc, yc
    r = int(input("Enter radius: "))
    xc = int(input("X Coordinate: "))
    yc = int(input("Y Coordinate: "))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("MidPoint Circle Generation")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()


main()
