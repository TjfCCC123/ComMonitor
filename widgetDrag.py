from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt as qwe
#起别名qwe,防止与Pyqt5.qt冲突
from PyQt5 import QtGui
from PyQt5 import QtCore
'''由于软件界面继承QMainWindow，不能重写mouseEvent，所以在
软件上方画了一个widget对象，写一个widget类，重写mouseEvent'''

class widgetdrag(QWidget):

    pressDragFlag = 0
    def mousePressEvent(self, em):
        global pressDragFlag
        print("mousePressEvent")
        try:
            # 鼠标左键
            if em.button() == qwe.LeftButton:
                pressDragFlag = 1
                print("左键按下")
            else:
                print(456)
        except Exception as e:
            print("except:", e)

    def mouseMoveEvent(self, QMouseEvent):
        global pressDragFlag


        #获取当前鼠标指针在软件界面中的坐标
        #根据鼠标指针偏移量计算QRect，对当前软件界面重新绘制？

        print("mouseMoveEvent")
        try:
            # 鼠标左键
            if em.button() == qwe.LeftButton:
                pressDragFlag = 1
                print("左键按下")
            else:
                print(456)
        except Exception as e:
            print("except:", e)

    def mouseReleaseEvent(self, QMouseEvent):
        global pressDragFlag


        print("mouseReleaseEvent")
        try:
            # 鼠标左键
            if em.button() == qwe.LeftButton:
                pressDragFlag = 0
                print("左键按下")
            else:
                print(456)
        except Exception as e:
            print("except:", e)

