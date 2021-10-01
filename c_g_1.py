from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Demo(object):
    def __init__(self):
        # self.geometry = geometry
        glutInit()  # 启动glut
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
        glutInitWindowSize(400, 400)
        glutCreateWindow(b"Hello OpenGL")  # 设定窗口标题
        glutDisplayFunc(self.draw_geometry)  # 调用函数绘制//设置当前窗口的显示回调函数
        self.init_condition()  # 设定背景
        glutMainLoop()

    @staticmethod
    def init_condition():
        glClearColor(1.0, 1.0, 1.0, 1.0)  # 定义背景为白色
        gluOrtho2D(-8.0, 8.0, -8.0, 8.0)  # 定义xy轴范围
        pass

    @staticmethod
    def draw_geometry():
        glClear(GL_COLOR_BUFFER_BIT)  # 背景色
        glColor3f(1.0, 0.0, 0.0)  # 设定颜色RGB#
        # glBegin(GL_QUADS)
        # # glVertex2f(-2, 2)
        # # glVertex2f(-2, 5)
        # # glVertex2f(-5, 5)
        # # glVertex2f(-5, 2)
        #
        # glEnd()
        glRectf(-2, 2, 5, -5)
        glColor3f(1.0, 0.0, 1.0)  # 设定颜色RGB#
        glRectf(-2, 4, 5, 2)
        glFlush()  # 执行绘图 处理所有的openGL程序


if __name__ == "__main__":
    Demo()
