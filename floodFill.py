from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from line import bresenhamLine, sym_DDA


oldColor = (1,1,1)
newColor = (0,0,0)
vertices = []


def getVertices():
    n = int(input("Enter number of vertices: "))
    
    for i in range(n):
        print("Enter Vertices #"+str(i+1)," as (x y):",end=" ")
        (x,y) = map(int,input().split())
        vertices.append((x,y))

def drawPoly():
    glClear(GL_COLOR_BUFFER_BIT)
    global vertices
    n = len(vertices)
    for i in range(n-1):
        lineFunc(vertices[i][0],vertices[i][1],vertices[i+1][0],vertices[i+1][1])
    lineFunc(vertices[n-1][0],vertices[n-1][1],vertices[0][0],vertices[0][1])

def getPixelColor(x,y):
    pixData = glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT,None)
    return tuple(pixData[0][0])

def setPixelColor(x,y,newColor=newColor):
    glColor3f(newColor[0],newColor[1],newColor[2])
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()
    glFlush()

def floodFill(x,y,oldColor=oldColor,newColor=newColor):
    if(getPixelColor(x,y)==oldColor):
        setPixelColor(x,y,newColor=newColor)
        floodFill(x+1,y,oldColor,newColor)
        floodFill(x-1,y,oldColor,newColor)
        floodFill(x,y+1,oldColor,newColor)
        floodFill(x,y-1,oldColor,newColor)

def floodFill_nonRecursive(x,y,oldColor=oldColor,newColor=newColor):
    stack = []
    stack.append((x,y))
    while(True):
        (x,y) = stack.pop()
        setPixelColor(x,y,newColor)
        if(getPixelColor(x+1,y)==oldColor):
	        stack.append((x+1,y))
        if(getPixelColor(x-1,y)==oldColor):
	        stack.append((x-1,y))
        if(getPixelColor(x,y+1)==oldColor):
	        stack.append((x,y+1))
        if(getPixelColor(x,y-1)==oldColor):
	        stack.append((x,y-1))

def mouseEvent(bt,st,x,y):
    y = glutGet(GLUT_WINDOW_HEIGHT) - y
    if(bt==GLUT_LEFT_BUTTON):
        if(st==GLUT_DOWN):
            floodFunc(x,y,getPixelColor(x,y))

def init():
    glClearColor(1,1,1,1.0)   #bg color
    glColor3f(0,0,0)          #line color
    glPointSize(1)
    gluOrtho2D(0,glutGet(GLUT_WINDOW_WIDTH),0,glutGet(GLUT_WINDOW_HEIGHT))   #left, right, bottom, top
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

def main():
    getVertices()
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(800,800)
    glutInitWindowPosition(0,0)
    glutCreateWindow("FloodFill")
    init()
    glutMouseFunc(mouseEvent)
    glutDisplayFunc(drawPoly)    
    glutMainLoop()



lineFunc = bresenhamLine    #change me
floodFunc = floodFill_nonRecursive       #change me

main()

