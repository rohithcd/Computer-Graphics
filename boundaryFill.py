from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from line import bresenhamLine, sym_DDA


boundaryColor = (0,0,0)
newColor = (1,0,0)
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
    pixList = list(pixData)
    return (pixList[0][0][0],pixList[1][0][0],pixList[2][0][0])

def setPixelColor(x,y,newColor=newColor):
    glColor3f(newColor[0],newColor[1],newColor[2])
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()
    glFlush()

def boundaryFill(x,y,boundaryColor=boundaryColor,newColor=newColor):
    if((getPixelColor(x,y)!=boundaryColor) and (getPixelColor(x,y)!=newColor)):
        setPixelColor(x,y,newColor=newColor)
        boundaryFill(x+1,y,boundaryColor,newColor)
        boundaryFill(x-1,y,boundaryColor,newColor)
        boundaryFill(x,y+1,boundaryColor,newColor)
        boundaryFill(x,y-1,boundaryColor,newColor)

def boundaryFill_nonRecursive(x,y,boundaryColor=boundaryColor,newColor=newColor):
    stack = []
    stack.append((x,y))
    while(stack):
        (x,y) = stack.pop()
        setPixelColor(x,y,newColor)
        if((getPixelColor(x+1,y)!=boundaryColor) and (getPixelColor(x,y)!=newColor)):
	        stack.append((x+1,y))
        if((getPixelColor(x-1,y)!=boundaryColor) and (getPixelColor(x,y)!=newColor)):
	        stack.append((x-1,y))
        if((getPixelColor(x,y+1)!=boundaryColor) and (getPixelColor(x,y)!=newColor)):
	        stack.append((x,y+1))
        if((getPixelColor(x,y-1)!=boundaryColor) and (getPixelColor(x,y)!=newColor)):
	        stack.append((x,y-1))

def mouseEvent(bt,st,x,y):
    y = glutGet(GLUT_WINDOW_HEIGHT) - y
    if(bt==GLUT_LEFT_BUTTON):
        if(st==GLUT_DOWN):
            boundaryFunc(x,y)

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
    glutCreateWindow("boundaryFill")
    init()
    glutMouseFunc(mouseEvent)
    glutDisplayFunc(drawPoly)    
    glutMainLoop()



lineFunc = bresenhamLine    #change me
boundaryFunc = boundaryFill       #change me

main()
