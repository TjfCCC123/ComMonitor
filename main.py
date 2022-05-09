"""@name:     ComMonitor
   @author:   tangjf
   @date:     2022/5/7"""

#显示ui
import gui
import sys
import slotMethod
from PyQt5.QtWidgets import QApplication, QMainWindow
import identifySerialPort as isp
from PyQt5 import QtCore

#创建槽函数实例对象
slotMethodInstance = slotMethod.slotMethods()

#创建一个字典存储串口默认信息
comPortInfo = { "portNo":1,
                "Baud":115200,
                "dataBit":8,
                "parityBit":0,
                "stopBit":1
                }
#创建元组存储波特率数值
baudAllInfo = (115200,57600,56000,38400,19200,14400,9600,4800,2400,1200,600,300,110)

#创建元组存储数据位
dataBitsAllInfo = (8,7,6)

#创建元组存储校验位
parityBitAllInfo = (8,7,6)

#创建元组存储停止位
stopBitsAllInfo = (1,1.5,2)

def updateChoosenPortInfo():
    #更新选中串口号
    portNo = ui.comboBox_port.currentIndex()
    comPortInfo["portNo"] = portNo+1
    print(comPortInfo["portNo"])
    #更新波特率
    baudNo = ui.comboBox_Baud.currentIndex()
    comPortInfo["Baud"] = baudAllInfo[baudNo]
    print(comPortInfo["Baud"])
    # 更新数据位
    dataBitNo = ui.comboBox_dataBit.currentIndex()
    comPortInfo["dataBit"] = dataBitsAllInfo[dataBitNo]
    print(comPortInfo["dataBit"])
    # 更新校验位
    parityBitNo = ui.comboBox_parityBit.currentIndex()
    comPortInfo["parityBit"] = parityBitAllInfo[parityBitNo]
    print(comPortInfo["parityBit"])
    # 更新停止位
    stopBitNo = ui.comboBox_stopBit.currentIndex()
    comPortInfo["stopBit"] = stopBitsAllInfo[stopBitNo]
    print(comPortInfo["stopBit"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)


    #开始检测串口
    list_port = isp.Communication.Print_Used_Com()
    if(len(list_port)>0):
        # 创建串口实例对象
        # 如果有串口那么就创建该对象(默认）
        #ispInstance = isp.Communication("COM1",115200,0)
        # 建立信号槽函数连接
        ui.comboBox_port.currentIndexChanged.connect(updateChoosenPortInfo)
        ui.comboBox_Baud.currentIndexChanged.connect(updateChoosenPortInfo)
        #ui.pushButton_openPort.clicked.connect(lambda: ispInstance.Open_Engine())
        portNum = 0
        serialCOM = "COM"
        #serialName = ""
        str(portNum)
        for k in list_port:
            ui.comboBox_port.addItem("")
            serialName = serialCOM + str(portNum+1)
            ui.comboBox_port.setItemText(portNum, QtCore.QCoreApplication.translate("MainWindow", serialName))
            portNum += 1
            serialName = ""
    else:
        print("未检测到串口！")

    MainWindow.show()
    sys.exit(app.exec_())

#获取当前串口
