# Tea pot using OpneGL Shader Language and Glut

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glutWireTeapot(0.5)
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 100)
    glutCreateWindow("My Second OGL Program")
    glutDisplayFunc(draw)
    glutMainLoop()
    
main()
