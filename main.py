"""@name:     ComMonitor
   @author:   tangjf
   @date:     2022/5/7"""

#显示ui
import gui
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import identifySerialPort as isp
from PyQt5 import QtCore

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    list_port = isp.Communication.Print_Used_Com()
    if(len(list_port)>0):
        portNum = 0
        serialCOM = "COM"
        str(portNum)
        for k in list_port:
            ui.comboBox.addItem("")
            serialName = serialCOM + str(portNum+1)
            ui.comboBox.setItemText(portNum, QtCore.QCoreApplication.translate("MainWindow", serialName))
            portNum += 1
            serialName = ""
    else:
        print("未检测到串口！")

    MainWindow.show()
    sys.exit(app.exec_())

#获取当前串口


#test = isp.Communication("COM6",9600,timeout=1)


