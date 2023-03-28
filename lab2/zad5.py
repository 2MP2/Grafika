import sys
import math
from tkinter import S

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def draw_fractal(x, y, a, s=1):
    draw_triangle(0, 100, 200)
    divide(x, y, a, s)

def divide(x, y, a, s=1):
    if (s == 0):
        return
    draw_reverse_small_triangle(x, y, a)

    divide(x, y, a/2 , s-1)
    divide(x-a/4,y-a/4*math.sqrt(3), a/2, s-1)
    divide(x+a/4,y-a/4*math.sqrt(3), a/2, s-1)



def draw_triangle(x, y, a):
    glColor3f(0.5,1,0.5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x,y)
    glVertex2f(x-a/2,y-a/2*math.sqrt(3))
    glVertex2f(x+a/2,y-a/2*math.sqrt(3))
    glEnd()

def draw_reverse_small_triangle(x, y, a):
    glColor3f(0.5,0.5,0.5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x,y-a/2*math.sqrt(3))
    glVertex2f(x-a/4,y-a/4*math.sqrt(3))
    glVertex2f(x+a/4,y-a/4*math.sqrt(3))
    glEnd()

    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x,y-a/2*math.sqrt(3))
    glVertex2f(x-a/4,y-a/4*math.sqrt(3))
    glVertex2f(x+a/4,y-a/4*math.sqrt(3))
    glEnd()

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    draw_fractal(0, 100, 200, 3)
    glFlush()

#----------------------------------------------------------------------------------------

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