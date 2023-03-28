import sys

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

red = random.random()
green = random.random()
blue = random.random()


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

# Rysuje prostokąt o bokach a i b za pomocą dwóch trójkątów.
# Punkt (x,y) wskazuje lewy dolny róg prostkąta.
# Argument d przeskalowuje rozmiary boków a i b.
def draw_rectangle(x, y, a, b , d = 0):

    if (d == 0):
        d = 1
    a*=d
    b*=d

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
    draw_rectangle(-10, -10, 40, 100, 0.5)
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