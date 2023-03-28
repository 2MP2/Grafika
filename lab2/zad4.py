import sys
from tkinter import S

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

def draw_fractal(x, y, a, b, s=1):
    draw_rectangle(x, y, a, b,0.5,1,0.5)
    divide(x, y, a, b, s)


def divide (x, y, a, b, s=1):
    if (s == 0):
        return
    
    draw_contour(x, y, a, b)
    for i in range (3):
        for j in range (3):
            newX = x + j*a/3
            newY = y + i*b/3
            divide(newX,newY,a/3,b/3,s-1)
    
    draw_rectangle(x+a/3, y+b/3, a/3, b/3, 0.5, 0.5, 0.5)


def draw_contour(x, y, a, b):

    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(x, y+b/3)
    glVertex2f(x+a, y+b/3)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(x, y+b*2/3)
    glVertex2f(x+a, y+b*2/3)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(x+a/3, y)
    glVertex2f(x+a/3, y+b)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(x+a*2/3, y)
    glVertex2f(x+a*2/3, y+b)
    glEnd()



def draw_rectangle(x, y, a, b, red, green, blue):

    glBegin(GL_TRIANGLES)
    glColor3f(red, green, blue)
    glVertex2f(x, y)
    glVertex2f(x, y + b)
    glVertex2f(x + a, y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(red, green, blue)
    glVertex2f(x, y + b)
    glVertex2f(x + a, y)
    glVertex2f(x + a, y + b)
    glEnd()

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    draw_fractal(-100,-100,200,200,3)
    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)



    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()