from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import Qt
'''由于软件界面继承QMainWindow，不能重写mouseEvent，所以在
软件上方画了一个widget对象，写一个widget类，重写mouseEvent'''

class widgetdrag(QWidget):

    def mousePressEvent(self, em):
        print("mousePressEvent")
        try:
            # 鼠标左键
            if em.button() == 1
                print(123)
            else:
                print(456)
        except Exception as e:
            print("except:", e)
