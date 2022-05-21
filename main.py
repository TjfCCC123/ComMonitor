"""@name:     ComMonitor
   @author:   tangjf
   @date:     2022/5/7"""

#显示ui
import binascii

import gui
import sys
import time
import identifySerialPort as isp
from PyQt5 import QtCore
from PyQt5.Qt import *
from PyQt5.QtCore import Qt, QFile, QTextStream, QIODevice, QByteArray,QUrl
from binascii import unhexlify,hexlify
from crcmod import mkCrcFun
import csv
import re


#初始化
windowMaximinzedFlag = 0
#列表记录comboBox_port的序号到端口号的映射
comboBoxPortNoToportNo = []
msgNumber = 0
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




#创建一个串口test对象
ispInstance = isp.Communication("COM1",115200,0)

#slotMethod 槽函数



#------------------------------------------------------
#关闭窗口
def closeWindow():
    sys.exit(app.exec_())

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

#------------------------------------------------------




def updateChoosenPortInfo():
    #print("-"*20)
    #更新选中串口号
    portNo = ui.comboBox_port.currentText()
    comPortInfo["portNo"] = portNo
    #print(comPortInfo["portNo"])
    #更新波特率
    baudNo = ui.comboBox_Baud.currentIndex()
    comPortInfo["Baud"] = baudAllInfo[baudNo]
    #print(comPortInfo["Baud"])
    # 更新数据位
    dataBitNo = ui.comboBox_dataBit.currentIndex()
    comPortInfo["dataBit"] = dataBitsAllInfo[dataBitNo]
    #print(comPortInfo["dataBit"])
    # 更新校验位
    parityBitNo = ui.comboBox_parityBit.currentIndex()
    comPortInfo["parityBit"] = parityBitAllInfo[parityBitNo]
    #print(comPortInfo["parityBit"])
    # 更新停止位
    stopBitNo = ui.comboBox_stopBit.currentIndex()
    comPortInfo["stopBit"] = stopBitsAllInfo[stopBitNo]
    #print(comPortInfo["stopBit"])

#清除发送串口数据
def clearSendMessage():
    ui.textEdit_sendMessage.clear()


#打开串口
def openOrClosePort():
    global portStateFlag
    try:
        if portStateFlag == 0:
            isopen = openPort()
        #global portStateFlag
            if isopen:
                portStateFlag = 1
            else:
                portStateFlag = 0
            print("openOrClosePort---openPort")
        else:
            closePort()
        #global portStateFlag
            portStateFlag = 0
            print("openOrClosePort---closePort")
    except Exception as e:
        print("---异常---：", e)



#另一个文件
#接收信息类，使用线程接收
class receievMessage(QThread):
    def run(self):
        global msgNumber
        while True:
            receivedMsg = ispInstance.receievMsg()
            if len(receivedMsg)!=0:
                #如果数据不为空，那么添加到tableview里
                # 时间
                nowtime = time.strftime('%H：%M：%S', time.localtime(time.time()))
                item = QStandardItem(nowtime)
                model.setItem(msgNumber, 0, item)
                # 串口号
                item = QStandardItem(comboBoxPortNoToportNo[ui.comboBox_port.currentIndex()])
                model.setItem(msgNumber, 1, item)
                # 读/写
                item = QStandardItem('read')
                model.setItem(msgNumber, 2, item)
                # 长度
                item = QStandardItem(str(len(receivedMsg)))
                model.setItem(msgNumber, 3, item)
                # hex

                # ascii
                item = QStandardItem(receivedMsg.decode('utf-8'))
                model.setItem(msgNumber, 5, item)

                ui.tableView.setModel(model)
                msgNumber = msgNumber + 1
                print(receivedMsg)

recMsgInstance = receievMessage()


#打开串口
def openPort():
    print("openPort")
    isOpen = ispInstance.Open_Engine(comboBoxPortNoToportNo[ui.comboBox_port.currentIndex()],comPortInfo["Baud"],0)
    if isOpen:
        ui.label_status.setText("状态：串口开启")
        ui.label_status.setStyleSheet("color:green")
        ui.pushButton_openPort.setText("关闭串口")
        recMsgInstance.start()
        return True
    else:
        QMessageBox.warning(MainWindow, "警告", "串口打开失败！提示：串口可能已经被占用。", QMessageBox.Yes)
        return False

#关闭串口
def closePort():
    try:
        recMsgInstance.terminate()
        while True:
            if recMsgInstance.isFinished():
                print("线程已关闭")
                ispInstance.Close_Engine()
                break
            else:
                print("线程未关闭")
        ui.label_status.setText("状态：串口关闭")
        ui.label_status.setStyleSheet("color:red")
        ui.pushButton_openPort.setText("打开串口")
        print("closePort")
    except Exception as e:
        print("---关闭异常---：", e)

def chooseHexadecimalFormat():
    flag = ui.checkBox_hexadecimal.isChecked()
    if flag:
        ispInstance.hexadecimalFlag = 1
    else:
        ispInstance.hexadecimalFlag = 0

#发送串口数据
def slot_sendMessage():
    global msgNumber
    message = ui.textEdit_sendMessage.toPlainText()
    hexORasciiMessage = []
    #如果是十六进制，那么检查是否非法0~F
    if ui.checkBox_hexadecimal.isChecked() == 1:
        hexFlag = 0
        # 十六进制形式组织信息
        #先检查非法字符
        islegal = True
        for i in range(len(message)):
            if isHex(message[i]) == 0:
                islegal = False
                break
        if islegal == False:
            hexFlag = 0
            QMessageBox.warning(MainWindow, "警告", "发送失败！提示：您的发送信息中含有非十六进制字符。", QMessageBox.Yes)
        else:
            list_message = message.split(" ")  # 先按空格分开
            addedmessage = ''
            showhexmessage = ''
            for spmsg in list_message:
                if len(spmsg) % 2 != 0:
                    newspmsg = list(spmsg)
                    newspmsg.insert(len(spmsg) - 1, '0')
                    spmsg = ''.join(newspmsg)
                addedmessage = addedmessage + spmsg


            #显示的hex信息
            text_list = re.findall(".{2}", addedmessage)
            showhexmessage = " ".join(text_list)

            finalmsg = bytes.fromhex(addedmessage)
            hexORasciiMessage.append(finalmsg)
            hexFlag = 1
    else:
        hexFlag = 1
        # 文本形式组织信息
        hexORasciiMessage.append(message)
    if hexFlag == 1:
        # 时间
        nowtime = time.strftime('%H：%M：%S', time.localtime(time.time()))
        item = QStandardItem(nowtime)
        model.setItem(msgNumber, 0, item)
        # 串口号
        item = QStandardItem(comboBoxPortNoToportNo[ui.comboBox_port.currentIndex()])
        model.setItem(msgNumber, 1, item)
        #读/写
        item = QStandardItem('write')
        model.setItem(msgNumber, 2, item)
        # 长度
        item = QStandardItem(str(len(hexORasciiMessage[0])))
        model.setItem(msgNumber, 3, item)
        #如果是ascii信息，那么显示
        if ui.checkBox_hexadecimal.isChecked() == 0:
            # ascii显示
            item = QStandardItem(hexORasciiMessage[0])
            model.setItem(msgNumber, 5, item)
            # ascii转hex显示
            h = hexlify(hexORasciiMessage[0].encode())
            newh = ''
            for i in range(0,len(h),2):
                newh+=h[i:i+2].decode('utf-8')
                newh+=' '
            item = QStandardItem(str(newh))
            model.setItem(msgNumber, 4, item)
        else:
            # hex显示
            item = QStandardItem(showhexmessage)
            model.setItem(msgNumber, 4, item)
            # hex转ascii显示
            str_data = hexORasciiMessage[0].decode('utf-8')
            #h = unhexlify(hexORasciiMessage[0])

            print(str_data)
            print(type(str_data))
            #df = ord(str_data)
            #print(df)
            #asciiMsg = binascii.a2b_hex(hexORasciiMessage[0])  # 转换成ASCii编码的字符串
            #s_byte = bytes.fromhex(hexORasciiMessage[0])
            #s = unhexlify(hexORasciiMessage[0])
            #s = hexORasciiMessage[0].fromhex()
            item = QStandardItem(str_data)
            model.setItem(msgNumber, 5, item)

        ui.tableView.setModel(model)
        ispInstance.sendMessage(hexORasciiMessage,ispInstance.hexadecimalFlag)
        msgNumber = msgNumber + 1



movedPosX = int()
movedPosY = int()
def moveToDragPos(movedPosX,movedPosY):
    print("moveToDragPos")
    newGe = QRect()
    nowGe = MainWindow.geometry()
    print(nowGe)
    MainWindow.setGeometry(nowGe.x()-movedPosX,nowGe.y()-movedPosY,nowGe.width(),nowGe.height())





def crc8():
    print("crc8-start")
    test_crc8 = 0x11   # 数据
    poly_crc8 = 0x11d  # 多项式
    for bit in range(8):
        if (test_crc8 & 0x80) != 0:   # 判断首位是否为1
            test_crc8 <<= 1           # 右移
            test_crc8 ^= poly_crc8    # 异或计算
        else:
            test_crc8 <<= 1           # 不等于1则直接移位
    print(hex(test_crc8))
    print("crc8-end")


ch = ''
def isHex(ch):
    if ch>='0'and ch<='9'or ch>='a'and ch<='z'or ch>='A'and ch<='Z'or ch == ' ':
        return 1
    else :
        return 0





def test():
    print("test123-start")


    message = '12346    789 1'


    #aa = bytes.fromhex(stringaa)
    #print(addedmessage)
    #self.main_engine.write(b'\x12\x34')  # 十六进制发送数据


    '''message = '12 345'
    list_message = message.split(" ")  # 先按空格分开
    list_message1 = []
    for i in list_message:
        stra = i
        strb = bytes.fromhex(stra)
        list_message1.append(strb)

    temp = []
    for j in range(len(list_message1)):
        for i in list_message1[j]:
            temp.append('%02x' % i)
    print(temp)'''
    #hstr = bytes.fromhex('02 13 89')
    #print(nmessage.isdecimal())
    #输入str
    #输出正确的校验码

    #crc = "89"
    #ploy = "8005"
    #test_crc = int(crc, 16)  # 将str类型转化成16进制
    #poly_crc8 = int(ploy, 16)  # 将str类型转化成16进制

    '''test_crc = '89'
    ploy = '8005'
    test_crc16 = int(test_crc, 16)  # 将str类型转化成16进制
    poly_crc16 = int(ploy, 16)  # 将str类型转化成16进制
    print(poly_crc16)
    print(test_crc16)
    #补0
    for i in range(15):
        test_crc16<<=1
    print(test_crc16)

    #转换为2进制
    #test_crc_2 = int(test_crc_10,2)
    #test_crc_2 = bin(test_crc)
    #poly_crc8_2 = bin(poly_crc8)
    #print(test_crc_2)
    #test_crc_2.
    #for i in range(15):
        #test_crc_2 << = 0

    while test_crc16.bit_count()!=15:
        while test_crc16 & 0x800000 == 0 :
            test_crc >>= 1
        test_crc16 ^= poly_crc16

    print(hex(test_crc))'''

    print("test123-end")


# CRC16/MODBUS
def crc16_modbus(s):
    crc16 = mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    return get_crc_value(s, crc16)

# common func
def get_crc_value(s, crc16):
    data = s.replace(' ', '')
    crc_out = hex(crc16(unhexlify(data))).upper()
    str_list = list(crc_out)
    if len(str_list) == 5:
        str_list.insert(2, '0')  # 位数不足补0
    crc_data = ''.join(str_list[2:])
    #加高低位
    if ui.comboBox_LSBMSB.currentIndex() == 0:
        return crc_data[2:] + ' ' + crc_data[:2]
    else:
        return crc_data[:2] + ' ' + crc_data[2:]

#添加校验码
def addCheck():
    #获取发送数据
    sendMsg = ui.textEdit_sendMessage.toPlainText()
    if ui.comboBox_check.currentIndex() == 0:
        # CRC16/MODBUS
        print("CRC16/MODBUS")
        crcMsg = crc16_modbus(sendMsg)
        newMsg = sendMsg+' '+crcMsg
        ui.textEdit_sendMessage.setText(newMsg)

#以CSV文件保存
def saveCsv():

    headers = ['class', 'name', 'sex', 'height', 'year']

    rows = [
        [1, 'xiaoming', 'male', 168, 23],
        [1, 'xiaohong', 'female', 162, 22],
        [2, 'xiaozhang', 'female', 163, 21],
        [2, 'xiaoli', 'male', 158, 21]
    ]

    with open('test.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    #槽函数
    ui.pushButton_close.clicked.connect(closeWindow)
    ui.pushButton_windowMaximized.clicked.connect(windowMaximized)
    ui.pushButton_windowminimized.clicked.connect(windowminimized)
    ui.pushButton_addCheck.clicked.connect(addCheck)

    # 将事件与槽建立关联
    #nowPos = QPoint()
    #widgetDragInstance.getMovePosSignal(0x01).connect(moveToDragPos(0x01))
    ui.widget_drag.getMovePosSignal.connect(moveToDragPos)
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
        "<a style='color: green; text-decoration: none' href = https://github.com/TjfCCC123/ComMonitor>点击转至开源网址https://github.com/TjfCCC123/ComMonitor")
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

    test()
    #saveCsv()
    #openPort
    #ispInstance.Open_Engine()
    #ispInstance.main_engine.write(0x12)
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)		#隐藏主窗口边界
    MainWindow.show()
    sys.exit(app.exec_())
