from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def Sign(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0

def BresenLineAlgo(x1, y1, x2, y2):
    x = x1
    y = y1
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    s1 = Sign(x2 - x1)
    s2 = Sign(y2 - y1)

    if dx == 0:
        while(y <= y2):
            setPixel(x, y)
            y +=1
    elif dy == 0:
        while(x <= x2):
            setPixel(x, y)
            x +=1
    else:
        
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
    glFlush()

