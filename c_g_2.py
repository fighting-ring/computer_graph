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

    def __init__(self):

        glutInit()  # 启动glut
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # 使用双缓存及RGB模型
        glutInitWindowSize(400, 300)
        glutInitWindowPosition(100, 100)
        glutCreateWindow(b"Hello OpenGL")  # 设定窗口标题
        glutDisplayFunc(self.display)  # 调用函数绘制//设置当前窗口的显示回调函数
        glutReshapeFunc(self.changeSize)
        # print(1)
        glutMouseFunc(self.MousePlot)
        glutPassiveMotionFunc(self.PassiveMouseMove)
        glutKeyboardFunc(self.Key)  # 指定键盘回调函数
        self.init_condition()  # 设定背景
        glutMainLoop()
    def init_condition(self):
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
    def MousePlot(self, button, action, xMouse, yMouse):
        global iPointNum
        global x1
        global y1
        global x2
        global y2
        if button == GLUT_LEFT_BUTTON and  action == GLUT_DOWN:
            if iPointNum == 0 or iPointNum == 2: # 要么没有顶点，要么两个顶点都有，这时候需要重新绘制直线
                # 确定直线段的第一个端点
                iPointNum = 1
                x1 = xMouse
                y1 = winHeight - yMouse
            else:
                iPointNum = 2
                x2 =xMouse
                y2 = winHeight - yMouse
                glutPostRedisplay()  # 指定窗口重新绘制
        if button == GLUT_RIGHT_BUTTON and action == GLUT_DOWN: # 鼠标右键被按下
            iPointNum = 0
            glutPostRedisplay() # 清空界面
    def PassiveMouseMove(self,xMouse,yMouse):
        global iPointNum
        global x1
        global y1
        global x2
        global y2
        if iPointNum == 1:
            x2 = xMouse
            y2 = winHeight - yMouse
            glutPostRedisplay()
    def Key(self, key, x, y):
        global iPointNum
        global x1
        global y1
        global x2
        global y2
        if key == b'p':
            #确定直线的第一个端点
            if iPointNum == 0 or iPointNum == 2:
                iPointNum = 1
                x1 = x
                y1 = winHeight - y
            else:
                # 确定直线的第二个端点
                iPointNum = 2
                x2 = x
                y2 = winHeight - y
                glutPostRedisplay()
if __name__ == "__main__":
    Demo()
