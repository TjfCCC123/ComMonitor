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
        MainWindow.resize(1191, 819)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 1151, 771))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 341, 321))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_port = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_port.setObjectName("label_port")
        self.verticalLayout_2.addWidget(self.label_port)
        self.label_Baud = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_Baud.setObjectName("label_Baud")
        self.verticalLayout_2.addWidget(self.label_Baud)
        self.label_dataBit = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_dataBit.setObjectName("label_dataBit")
        self.verticalLayout_2.addWidget(self.label_dataBit)
        self.label_parityBit = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_parityBit.setObjectName("label_parityBit")
        self.verticalLayout_2.addWidget(self.label_parityBit)
        self.label_stopBit = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_stopBit.setObjectName("label_stopBit")
        self.verticalLayout_2.addWidget(self.label_stopBit)
        self.label_status = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_status.setObjectName("label_status")
        self.verticalLayout_2.addWidget(self.label_status)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_port = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_port.setObjectName("comboBox_port")
        self.verticalLayout_3.addWidget(self.comboBox_port)
        self.comboBox_Baud = QtWidgets.QComboBox(self.horizontalLayoutWidget)
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
        self.verticalLayout_3.addWidget(self.comboBox_Baud)
        self.comboBox_dataBit = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_dataBit.setObjectName("comboBox_dataBit")
        self.comboBox_dataBit.addItem("")
        self.comboBox_dataBit.addItem("")
        self.comboBox_dataBit.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_dataBit)
        self.comboBox_parityBit = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_parityBit.setObjectName("comboBox_parityBit")
        self.comboBox_parityBit.addItem("")
        self.comboBox_parityBit.addItem("")
        self.comboBox_parityBit.addItem("")
        self.comboBox_parityBit.addItem("")
        self.comboBox_parityBit.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_parityBit)
        self.comboBox_stopBit = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_stopBit.setObjectName("comboBox_stopBit")
        self.comboBox_stopBit.addItem("")
        self.comboBox_stopBit.addItem("")
        self.comboBox_stopBit.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_stopBit)
        self.pushButton_openPort = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_openPort.setObjectName("pushButton_openPort")
        self.verticalLayout_3.addWidget(self.pushButton_openPort)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_2.setGeometry(QtCore.QRect(3, 16, 561, 361))
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 40, 741, 89))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.pushButton_clear = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.pushButton_send = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout.addWidget(self.pushButton_send)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ComMonitor"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_port.setText(_translate("MainWindow", "端口："))
        self.label_Baud.setText(_translate("MainWindow", "波特率："))
        self.label_dataBit.setText(_translate("MainWindow", "数据位："))
        self.label_parityBit.setText(_translate("MainWindow", "校验位："))
        self.label_stopBit.setText(_translate("MainWindow", "停止位："))
        self.label_status.setText(_translate("MainWindow", "状态："))
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
        self.comboBox_dataBit.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox_dataBit.setItemText(1, _translate("MainWindow", "7"))
        self.comboBox_dataBit.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox_parityBit.setItemText(0, _translate("MainWindow", "无"))
        self.comboBox_parityBit.setItemText(1, _translate("MainWindow", "奇校验"))
        self.comboBox_parityBit.setItemText(2, _translate("MainWindow", "偶校验"))
        self.comboBox_parityBit.setItemText(3, _translate("MainWindow", "Mark"))
        self.comboBox_parityBit.setItemText(4, _translate("MainWindow", "空格校验"))
        self.comboBox_stopBit.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_stopBit.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboBox_stopBit.setItemText(2, _translate("MainWindow", "2"))
        self.pushButton_openPort.setText(_translate("MainWindow", "打开串口"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_7.setText(_translate("MainWindow", "发送区1"))
        self.pushButton_clear.setText(_translate("MainWindow", "清空"))
        self.pushButton_send.setText(_translate("MainWindow", "发送"))
