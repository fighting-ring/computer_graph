from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Demo(object):
    global iPointNum
    global x1
    global x2
    global y1
    global y2
    global winWidth
    global winHeight
    iPointNum = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    winWidth = 400
    winHeight = 400

    def initial(self):
        # glutInit()  # 启动glut
        # glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
        # glutInitWindowSize(400, 400)
        # glutCreateWindow(b"Hello OpenGL")  # 设定窗口标题
        # glutDisplayFunc(self.draw_geometry)  # 调用函数绘制//设置当前窗口的显示回调函数
        # self.init_condition()  # 设定背景
        # glutMainLoop()

        glutInit()  # 启动glut
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
        glutInitWindowSize(400, 300)
        glutInitWindowPosition(100, 100)
        glutCreateWindow(b"Hello OpenGL")  # 设定窗口标题
        glutDisplayFunc(self.display)  # 调用函数绘制//设置当前窗口的显示回调函数
        glutReshapeFunc(self.changeSize)
        print(1)
        glutMouseFunc(self.MousePlot)
        glutPassiveMotionFunc(self.PassiveMouseMove())
        self.init_condition()  # 设定背景
        glutMainLoop()
    def init_condtion(self):
        glClearColor(1.0, 1.0, 1.0, 1.0)  # 定义背景为白色
    def changeSize(self, w,  h):
        global winWidth
        global winHeight
        winWidth = w
        winHeight = h
        glViewport(0, 0, w, h)      #指定窗口显示的区域
        glMatrixMode(GL_PROJECTION)     #指定设置投影参数
        glLoadIdentity()          #调用单位矩阵，去掉之前的投影参数设置
        gluOrtho2D(0, winWidth, 0, winHeight)  #设置投影参数
    def display(self ):
        global iPointNum
        global x1
        global x2
        global y1
        global y2
        glClear(GL_COLOR_BUFFER_BIT) #用当前背景色填充窗口
        glColor3f(1.0, 0, 0)   #指定当前的绘图颜色
        if iPointNum >= 1:
            glBegin(GL_LINES)  #绘制直线段
            glVertex2i(x1, y1)
            glVertex2i(x2, y2)
            glEnd()
        glutSwapBuffers()
    def MousePlot(self, button, action):
        global xMouse
        global yMouse
        global iPointNum
        global x1
        global x2
        global y1
        global y2
        if button == GLUT_LEFT_BUTTON and  action == GLUT_DOWN:
            if iPointNum == 0 or iPointNum == 2:
                iPointNum =1
                x1 = xMouse
                y1 = winHeight - yMouse
            else:
                iPointNum = 2
                x2 =xMouse
                y2 = winHeight
                glutPostRedisplay()
        if button == GLUT_RIGHT_BUTTON and action == GLUT_DOWN:
            iPointNum = 0
            glutPostRedisplay()
    def PassiveMouseMove(self):
        global xMouse
        global yMouse
        global iPointNum
        global winHeight
        global x2
        global y2
        if iPointNum == 1:
            x2 = xMouse
            y2 = winHeight - yMouse
            glutPostRedisplay()



    # def init_condition(self):
    #     glClearColor(1.0, 1.0, 1.0, 1.0)  # 定义背景为白色
    #     gluOrtho2D(-8.0, 8.0, -8.0, 8.0)  # 定义xy轴范围    def render(self):
    #     pass
    #
    # def draw_geometry(self):
    #     glClear(GL_COLOR_BUFFER_BIT)  # 背景色
    #     glColor3f(1.0, 0.0, 0.0)  # 设定颜色RGB#
    #     # glBegin(GL_QUADS)
    #     # # glVertex2f(-2, 2)
    #     # # glVertex2f(-2, 5)
    #     # # glVertex2f(-5, 5)
    #     # # glVertex2f(-5, 2)
    #     #
    #     # glEnd()
    #     glRectf(-2, 2, 5, -5)
    #     glColor3f(1.0, 0.0, 1.0)  # 设定颜色RGB#
    #     glRectf(-2, 4, 5, 2)
    #     glFlush()  # 执行绘图 处理所有的openGL程序


if __name__ == "__main__":
    Demo()
