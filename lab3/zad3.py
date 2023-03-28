#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy 
import math


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

def calculateX(u, v):
    return (-90 * pow(u, 5) + 225 * pow(u, 4) - 270 * pow(u, 3) + 180 * pow(u, 2) - 45 * u) * math.cos(v * math.pi)

def calculateY(u):
    return (160 * pow(u, 4) - 320 * pow(u, 3) + 160 * pow(u, 2) - 5)

def calculateZ(u, v):
    return (-90 * pow(u, 5) + 225 * pow(u, 4) + - 270 * pow(u, 3) + 180 * pow(u, 2) - 45 * u) * math.sin(v * math.pi)


def draw_egg(N):
    N = 40
    tab = numpy.zeros((N, N, 3))
    tabU = numpy.zeros(N)
    tabV = numpy.zeros(N)
    segment = 1.0 / (N - 1)
    val = 0

    for i in range(N):
        tabU[i] = val
        tabV[i] = val
        val += segment

    for u in range(N):
        for v in range(N):
            tab[u][v][0] = calculateX(tabU[u], tabV[v])
            tab[u][v][1] = calculateY(tabU[u])
            tab[u][v][2] = calculateZ(tabU[u], tabV[v])
    
    glColor3f(0.0, 1.0, 0.0)

    for u in range(N-1):
        for v in range(N-1):
            x = tab[u][v][0]
            y = tab[u][v][1]
            z = tab[u][v][2]

            nextX_v = tab[u][v + 1][0]
            nextY_v = tab[u][v + 1][1]
            nextZ_v = tab[u][v + 1][2]

            nextX_u = tab[u + 1][v][0]
            nextY_u = tab[u + 1][v][1]
            nextZ_u = tab[u + 1][v][2]

            nextX_uv = tab[u + 1][v + 1][0]
            nextY_uv = tab[u + 1][v + 1][1]
            nextZ_uv = tab[u + 1][v + 1][2]

            glBegin(GL_TRIANGLES)
            glVertex3f(x, y, z)
            glVertex3f(nextX_v, nextY_v, nextZ_v)
            glVertex3f(nextX_u, nextY_u, nextZ_u)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(nextX_v, nextY_v, nextZ_v)
            glVertex3f(nextX_u, nextY_u, nextZ_u)
            glVertex3f(nextX_uv, nextY_uv, nextZ_uv)
            glEnd()

#---------------------------------------------------------------------------------------------------------------------
def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)

def shutdown():
    pass


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 180 / 3.1415)
    axes()

    draw_egg(40)

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
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

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
