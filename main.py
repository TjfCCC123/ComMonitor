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
from PyQt5.Qt import *
from PyQt5.QtCore import Qt, QFile, QTextStream, QIODevice, QByteArray,QUrl
import crcmod


#创建槽函数实例对象
slotMethodInstance = slotMethod.slotMethods()

#slotMethod 槽函数

#关闭窗口
def closeWindow():
    sys.exit(app.exec_())

#初始化
windowMaximinzedFlag = 0

#窗口最大化
def windowMaximized():
    global windowMaximinzedFlag
    if windowMaximinzedFlag!=1:
        windowMaximinzedFlag = 1
        MainWindow.showMaximized()
    else:
        windowMaximinzedFlag = 0
        MainWindow.showNormal()

#窗口最小化
def windowminimized():
    MainWindow.showMinimized()







#列表记录comboBox_port的序号到端口号的映射
comboBoxPortNoToportNo = []

sendMsgNumber = 0

portStateFlag = 0

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
def openOrClosePort():
    global portStateFlag
    if portStateFlag == 0:
        openPort()
        #global portStateFlag
        portStateFlag = 1
        print("openOrClosePort---openPort")
    else:
        closePort()
        #global portStateFlag
        portStateFlag = 0
        print("openOrClosePort---closePort")

#打开串口
def openPort():
    ispInstance.Open_Engine(comboBoxPortNoToportNo[ui.comboBox_port.currentIndex()],comPortInfo["Baud"],0)
    ui.label_status.setText("状态：串口开启")
    ui.label_status.setStyleSheet("color:green")
    ui.pushButton_openPort.setText("关闭串口")
    print("openPort")

#关闭串口
def closePort():
    ispInstance.main_engine.close()
    ui.label_status.setText("状态：串口关闭")
    ui.label_status.setStyleSheet("color:red")
    ui.pushButton_openPort.setText("打开串口")
    print("closePort")

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

    datalist=[0x0102]
    test_crc = 0xFFFF  # 预置1个16位的寄存器为十六进制FFFF（即全为1），称此寄存器为CRC寄存器；
    #poly = 0xa001
    poly=0x8005
    numl = len(datalist)
    for num in range(numl):
        data = datalist[num]
        test_crc = (data & 0xFF) ^ test_crc  # 把第一个8位二进制数据（既通讯信息帧的第一个字节）与16位的CRC寄存器的低8位相异或，把结果放于CRC寄存器，高八位数据不变；
        """
        （3）、把CRC寄存器的内容右移一位（朝低位）用0填补最高位，并检查右移后的移出位；
        （4）、如果移出位为0：重复第3步（再次右移一位）；如果移出位为1，CRC寄存器与多
            项式A001（1010 0000 0000 0001）进行异或；
        """
        # 右移动
        for bit in range(8):
            if (test_crc & 0x1) != 0:
                test_crc >>= 1
                test_crc ^= poly
            else:
                test_crc >>= 1
    print(hex(test_crc))
    print("test123")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)

    #槽函数
    ui.pushButton_close.clicked.connect(closeWindow)
    ui.pushButton_windowMaximized.clicked.connect(windowMaximized)
    ui.pushButton_windowminimized.clicked.connect(windowminimized)


    txtfile = open('./base.qss')
    qss = txtfile.read()
    MainWindow.setStyleSheet(qss)

    model = QStandardItemModel(20, 6)
    # 设置水平方向四个头标签文本内容
    model.setHorizontalHeaderLabels(['时间','串口号','读/写','长度','HEX','ASCII'])
    ui.tableView.setModel(model)
    ui.tableView.setColumnWidth(0, 90)#时间
    ui.tableView.setColumnWidth(1, 60)#串口号
    ui.tableView.setColumnWidth(2, 60)#读/写
    ui.tableView.setColumnWidth(3, 40)#长度
    ui.tableView.setColumnWidth(4, 200)#hex
    ui.tableView.setColumnWidth(5, 200)#ascii

    ui.label_git.setOpenExternalLinks(1)
    ui.label_git.setText(
        "<a style='color: green; text-decoration: none' href = https://github.com/TjfCCC123/ComMonitor>点击转到开源网址")
    ui.label_status.setText("状态：串口关闭")
    ui.label_status.setStyleSheet("color:red")



    MainWindow.resize(1228,700)
    #开始检测串口
    list_port = isp.Communication.Print_Used_Com()
    if(len(list_port)>0):
        # 建立信号槽函数连接
        ui.comboBox_port.currentIndexChanged.connect(updateChoosenPortInfo)
        ui.comboBox_Baud.currentIndexChanged.connect(updateChoosenPortInfo)
        ui.pushButton_openPort.clicked.connect(updateChoosenPortInfo)
        ui.pushButton_openPort.clicked.connect(openOrClosePort)
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
    #MainWindow.setAcceptDrops(True)
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)		#隐藏主窗口边界
    MainWindow.show()

    sys.exit(app.exec_())
