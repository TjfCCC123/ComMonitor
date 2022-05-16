# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1161, 728)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_port = QtWidgets.QLabel(self.groupBox)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout.addWidget(self.label_port)
        self.comboBox_port = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_port.setObjectName("comboBox_port")
        self.horizontalLayout.addWidget(self.comboBox_port)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Baud = QtWidgets.QLabel(self.groupBox)
        self.label_Baud.setObjectName("label_Baud")
        self.horizontalLayout_3.addWidget(self.label_Baud)
        self.comboBox_Baud = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Baud.setObjectName("comboBox_Baud")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_Baud)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_dataBit = QtWidgets.QLabel(self.groupBox)
        self.label_dataBit.setObjectName("label_dataBit")
        self.horizontalLayout_4.addWidget(self.label_dataBit)
        self.comboBox_dataBit = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_dataBit.setObjectName("comboBox_dataBit")
        self.comboBox_dataBit.addItem("")
        self.comboBox_dataBit.addItem("")
        self.comboBox_dataBit.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_dataBit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_parityBit = QtWidgets.QLabel(self.groupBox)
        self.label_parityBit.setObjectName("label_parityBit")
        self.horizontalLayout_5.addWidget(self.label_parityBit)
        self.comboBox_parityBit = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_parityBit.setObjectName("comboBox_parityBit")
        self.comboBox_parityBit.addItem("")
        self.comboBox_parityBit.addItem("")
        self.comboBox_parityBit.addItem("")
        self.comboBox_parityBit.addItem("")
        self.comboBox_parityBit.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_parityBit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_stopBit = QtWidgets.QLabel(self.groupBox)
        self.label_stopBit.setObjectName("label_stopBit")
        self.horizontalLayout_6.addWidget(self.label_stopBit)
        self.comboBox_stopBit = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_stopBit.setObjectName("comboBox_stopBit")
        self.comboBox_stopBit.addItem("")
        self.comboBox_stopBit.addItem("")
        self.comboBox_stopBit.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_stopBit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_status = QtWidgets.QLabel(self.groupBox)
        self.label_status.setObjectName("label_status")
        self.horizontalLayout_7.addWidget(self.label_status)
        self.pushButton_openPort = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_openPort.setObjectName("pushButton_openPort")
        self.horizontalLayout_7.addWidget(self.pushButton_openPort)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.label_git = QtWidgets.QLabel(self.centralwidget)
        self.label_git.setObjectName("label_git")
        self.verticalLayout_4.addWidget(self.label_git)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableView = QtWidgets.QTableView(self.groupBox_3)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_hexadecimal = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_hexadecimal.setObjectName("checkBox_hexadecimal")
        self.gridLayout_2.addWidget(self.checkBox_hexadecimal, 0, 1, 1, 1)
        self.pushButton_send = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_send.setObjectName("pushButton_send")
        self.gridLayout_2.addWidget(self.pushButton_send, 0, 2, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout_2.addWidget(self.pushButton_clear, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setStyleSheet("font: 9pt \"幼圆\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.comboBox_check = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_check.setObjectName("comboBox_check")
        self.comboBox_check.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_check, 1, 0, 1, 1)
        self.pushButton_addCheck = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_addCheck.setObjectName("pushButton_addCheck")
        self.gridLayout_2.addWidget(self.pushButton_addCheck, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.textEdit_sendMessage = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_sendMessage.setObjectName("textEdit_sendMessage")
        self.gridLayout.addWidget(self.textEdit_sendMessage, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ComMonitor"))
        self.groupBox.setTitle(_translate("MainWindow", "串口设置"))
        self.label_port.setText(_translate("MainWindow", "端口："))
        self.label_Baud.setText(_translate("MainWindow", "波特率："))
        self.comboBox_Baud.setItemText(0, _translate("MainWindow", "115200"))
        self.comboBox_Baud.setItemText(1, _translate("MainWindow", "57600"))
        self.comboBox_Baud.setItemText(2, _translate("MainWindow", "56000"))
        self.comboBox_Baud.setItemText(3, _translate("MainWindow", "38400"))
        self.comboBox_Baud.setItemText(4, _translate("MainWindow", "19200"))
        self.comboBox_Baud.setItemText(5, _translate("MainWindow", "14400"))
        self.comboBox_Baud.setItemText(6, _translate("MainWindow", "9600"))
        self.comboBox_Baud.setItemText(7, _translate("MainWindow", "4800"))
        self.comboBox_Baud.setItemText(8, _translate("MainWindow", "2400"))
        self.comboBox_Baud.setItemText(9, _translate("MainWindow", "1200"))
        self.comboBox_Baud.setItemText(10, _translate("MainWindow", "600"))
        self.comboBox_Baud.setItemText(11, _translate("MainWindow", "300"))
        self.comboBox_Baud.setItemText(12, _translate("MainWindow", "110"))
        self.label_dataBit.setText(_translate("MainWindow", "数据位："))
        self.comboBox_dataBit.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox_dataBit.setItemText(1, _translate("MainWindow", "7"))
        self.comboBox_dataBit.setItemText(2, _translate("MainWindow", "6"))
        self.label_parityBit.setText(_translate("MainWindow", "校验位："))
        self.comboBox_parityBit.setItemText(0, _translate("MainWindow", "无"))
        self.comboBox_parityBit.setItemText(1, _translate("MainWindow", "奇校验"))
        self.comboBox_parityBit.setItemText(2, _translate("MainWindow", "偶校验"))
        self.comboBox_parityBit.setItemText(3, _translate("MainWindow", "Mark"))
        self.comboBox_parityBit.setItemText(4, _translate("MainWindow", "空格校验"))
        self.label_stopBit.setText(_translate("MainWindow", "停止位："))
        self.comboBox_stopBit.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_stopBit.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboBox_stopBit.setItemText(2, _translate("MainWindow", "2"))
        self.label_status.setText(_translate("MainWindow", "状态："))
        self.pushButton_openPort.setText(_translate("MainWindow", "打开串口"))
        self.label_git.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "问题反馈:tjf_1105@163.com"))
        self.groupBox_3.setTitle(_translate("MainWindow", "串口信息"))
        self.groupBox_2.setTitle(_translate("MainWindow", "数据发送"))
        self.checkBox_hexadecimal.setText(_translate("MainWindow", "16进制"))
        self.pushButton_send.setText(_translate("MainWindow", "发送"))
        self.pushButton_clear.setText(_translate("MainWindow", "清空"))
        self.label_7.setText(_translate("MainWindow", "  发送区1"))
        self.comboBox_check.setItemText(0, _translate("MainWindow", "CRC校验"))
        self.pushButton_addCheck.setText(_translate("MainWindow", "添加校验"))
