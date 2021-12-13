# Python with OpenGL Introduction 
# Line Clipping using Cohen-Sutherland Algorithm
# Code by Sharun E Rajeev

# PyOpenGL Imports
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# import primitive line drawing function
from bressenhamLineImport import BresenLineAlgo

# define screen coordinates
xl,yt,xr,yb = 0,0,0,0
# define line coordinates
x1,y1,x2,y2 = 0,0,0,0

# function to read line coordinates
def readLine():
    global x1,y1,x2,y2, width, height
    width = int(input("Enter window width: "))
    height = int(input("Enter window height: "))
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

# function to read window coordinates
def readWindow():
    global xl,yt,xr,yb
    xl = int(input("Enter x min: "))
    yb = int(input("Enter y min: "))
    xr = int(input("Enter x max: "))
    yt = int(input("Enter y max: "))

# function to draw clipping window using DDA algorithm
def drawClippingWindow():
    BresenLineAlgo(xl,yt,xl,yb)
    BresenLineAlgo(xl,yb,xr,yb)
    BresenLineAlgo(xr,yb,xr,yt)
    BresenLineAlgo(xr,yt,xl,yt)

# function to draw line using DDA algorithm
def drawLine():
    BresenLineAlgo(x1,y1,x2,y2)

# Constants that indicate which side of the clipping window a point is on
INSIDE = 0
LEFT = 4
RIGHT = 1
BOTTOM = 8
TOP = 2

# function to calculate code for a point
def getCode(x,y):
    global xl,yt,xr,yb
    code = INSIDE
    if x<xl:
        code |= LEFT
    elif x>xr:
        code |= RIGHT
    if y < yb:
        code |=BOTTOM
    elif y>yt:
        code |= TOP
    return code

# function to perform Cohen-Sutherland clipping
def cohenSutherlandClipping():
    global x1,y1,x2,y2
    global xl,yb,xr,yt
    code1 = getCode(x1,y1)
    code2 = getCode(x2,y2)
    accept = False
    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2)!=0:
            break
        else:
            x,y = 0.0,0.0
            temp_code = code1
            if temp_code==0:
                temp_code = code2
            if LEFT & temp_code:
                print("LEFT CLIPPING: ")
                x = xl
                y = y1 + (y2-y1)*(xl-x1)/(x2-x1)
            elif temp_code & RIGHT:
                print("RIGHT CLIPPING: ")
                x = xr
                y = y1 + (y2-y1)*(xr-x1)/(x2-x1)
            elif temp_code & BOTTOM:
                print("TOP CLIPPING: ")
                x = x1+(x2-x1)*(yb-y1)/(y2-y1)
                y = yb
            elif temp_code & TOP:
                print("BOTTOM CLIPPING: ")
                x = x1 + (x2-x1)*(yt-y1)/(y2-y1)
                y = yt
        if temp_code == code1:
            glColor3f(1,1,1)
            BresenLineAlgo(int(x1),int(y1),int(x+0.5),int(y+0.5))
            x1,y1 = int(x),int(y)
            code1 = getCode(x1,y1)
        else:
            glColor3f(1,1,1)
            BresenLineAlgo(int(x2),int(y2),int(x+0.5),int(y+0.5))
            x2,y2 = int(x),int(y)
            code2 = getCode(x2,y2)
        print("New Coordinates: ",x1,y1,x2,y2)
    if not accept:
        print("Rejected")
        glColor3f(1,1,1)
        BresenLineAlgo(x1,y1,x2,y2)

# function that displays the line and clipping window and calls Cohen-Sutherland clipping
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawLine()
    readWindow()
    drawClippingWindow()
    cohenSutherlandClipping()

# function to initialize the display and point properties
def init():
    glClearColor(1,1,1,1.0) # set background color to white
    glColor3f(0,0,0) # set pointer color to black
    glPointSize(1)
    gluOrtho2D(0,width,height,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

# main function
def main():
    # accept line coordinates
    readLine()
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Line Clipping using Cohen Sutherland Algorithm")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()

