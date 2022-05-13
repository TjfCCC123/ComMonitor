"""@name:     ComMonitor
   @author:   tangjf
   @date:     2022/5/7"""

#显示ui
import gui
import sys
import slotMethod
import time
#from PyQt5.QtWidgets import QApplication, QMainWindow
import identifySerialPort as isp
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#创建槽函数实例对象
slotMethodInstance = slotMethod.slotMethods()

#列表记录comboBox_port的序号到端口号的映射
comboBoxPortNoToportNo = []

sendMsgNumber = 0

#串口信息
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
    print("-"*20)
    #更新选中串口号
    portNo = ui.comboBox_port.currentText()
    comPortInfo["portNo"] = portNo
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

#清除发送串口数据
def clearSendMessage():
    ui.textEdit_sendMessage.clear()

#创建一个串口test对象
ispInstance = isp.Communication("COM1",115200,0)


#打开串口
def openPort1():
    ispInstance.Open_Engine(comboBoxPortNoToportNo[ui.comboBox_port.currentIndex()],comPortInfo["Baud"],0)
    print("openPort1")

#关闭串口
def closePort():
    ispInstance.main_engine.close()

def chooseHexadecimalFormat():
    flag = ui.checkBox_hexadecimal.isChecked()
    if flag:
        slotMethodInstance.hexadecimalFlag = 1
    else:
        slotMethodInstance.hexadecimalFlag = 0

#发送串口数据
def slot_sendMessage():
    global sendMsgNumber
    message = ui.textEdit_sendMessage.toPlainText()
    hexMessageList = []
    #如果是十六进制，那么检查是否非法0~F
    if ui.checkBox_hexadecimal.isChecked() == 1:
        hexFlag = 0
        list_message = message.split(" ")  # 先按空格分开
        newlist_message = []
        print(len(list_message[0]))
        for msg in list_message:
            if len(msg) > 2:
                # 每两个字符分割
                ij = 0
                while ij <= len(msg):
                    if ij + 2 <= len(msg):
                        stra = msg[ij:ij + 2]
                        ij = ij + 2
                        newlist_message.append(stra)
                    else:
                        stra = msg[ij:ij + 1]
                        ij = ij + 1
                        newlist_message.append(stra)
            else:
                newlist_message.append(msg)  # 小于等于2，直接赋值
        try:
            for nmessage in newlist_message:
                if nmessage != '':
                    hstr = bytes.fromhex(nmessage)
                    hexMessageList.append(hstr)
            hexFlag = 1
        except Exception as e:
            hexFlag = 0
            print("---转换异常---：", e)
            # 弹窗报警
            QMessageBox.warning(MainWindow, "警告", "发送失败！提示：您的发送信息中含有非十六进制字符。", QMessageBox.Yes)
    else:
        hexFlag = 1
        # 文本形式组织信息
        hexMessageList.append(message)
    if hexFlag == 1:
        # 时间
        nowtime = time.strftime('%H：%M：%S', time.localtime(time.time()))
        item = QStandardItem(nowtime)
        model.setItem(sendMsgNumber, 0, item)
        # 串口号
        item = QStandardItem(comboBoxPortNoToportNo[ui.comboBox_port.currentIndex()])
        model.setItem(sendMsgNumber, 1, item)
        #读/写
        item = QStandardItem('write')
        model.setItem(sendMsgNumber, 2, item)
        # 长度
        if slotMethodInstance.hexadecimalFlag == 1:
            item = QStandardItem(str(len(hexMessageList)))
            model.setItem(sendMsgNumber, 3, item)
        else:
            item = QStandardItem(str(len(hexMessageList[0])))
            model.setItem(sendMsgNumber, 3, item)
        # hex

        # ascii
        item = QStandardItem(hexMessageList[0])
        model.setItem(sendMsgNumber, 5, item)

        ui.tableView.setModel(model)
        ispInstance.sendMessage(hexMessageList,slotMethodInstance.hexadecimalFlag)
        sendMsgNumber = sendMsgNumber + 1
        print(sendMsgNumber)

def test123():
    print("test123")
    #tableview写内容

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)

    model = QStandardItemModel(20, 6)
    # 设置水平方向四个头标签文本内容
    model.setHorizontalHeaderLabels(['时间','串口号','读/写','长度','HEX','ASCII'])
    ui.tableView.setModel(model)
    ui.tableView.setColumnWidth(0, 100)#时间
    ui.tableView.setColumnWidth(1, 60)#串口号
    ui.tableView.setColumnWidth(2, 60)#读/写
    ui.tableView.setColumnWidth(3, 40)#长度
    ui.tableView.setColumnWidth(4, 200)#hex
    ui.tableView.setColumnWidth(5, 200)#ascii
    #开始检测串口
    list_port = isp.Communication.Print_Used_Com()
    if(len(list_port)>0):
        # 建立信号槽函数连接
        ui.comboBox_port.currentIndexChanged.connect(updateChoosenPortInfo)
        ui.comboBox_Baud.currentIndexChanged.connect(updateChoosenPortInfo)
        ui.pushButton_openPort.clicked.connect(updateChoosenPortInfo)
        ui.pushButton_openPort.clicked.connect(openPort1)
        ui.pushButton_send.clicked.connect(slot_sendMessage)
        ui.checkBox_hexadecimal.stateChanged.connect(chooseHexadecimalFormat)
        countPortNum = 0
        for k in list_port:
            ui.comboBox_port.addItem("")
            comboBoxPortNoToportNo.append(k[0])
            ui.comboBox_port.setItemText(countPortNum, QtCore.QCoreApplication.translate("MainWindow", k[0]+"("+k[1]+")"))
            countPortNum += 1
        updateChoosenPortInfo()
    else:
        print("未检测到串口！")

    test123()

    MainWindow.show()
    sys.exit(app.exec_())
