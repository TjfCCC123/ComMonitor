#识别串口

import serial
import serial.tools.list_ports
import gui
class Communication():

  #初始化
  def __init__(self,com,bps,timeout):
    self.port = com
    self.bps = bps
    self.timeout =timeout
    global Ret
    try:
      # 打开串口，并得到串口对象
       self.main_engine= serial.Serial(self.port,self.bps,timeout=self.timeout)
      # 判断是否打开成功
       if (self.main_engine.is_open):
        Ret = True
    except Exception as e:
      print("---异常---：", e)

  # 打印设备基本信息
  def Print_Name(self):
    print(self.main_engine.name) #设备名字
    print(self.main_engine.port)#读或者写端口
    print(self.main_engine.baudrate)#波特率
    print(self.main_engine.bytesize)#字节大小
    print(self.main_engine.parity)#校验位
    print(self.main_engine.stopbits)#停止位
    print(self.main_engine.timeout)#读超时设置
    print(self.main_engine.writeTimeout)#写超时
    print(self.main_engine.xonxoff)#软件流控
    print(self.main_engine.rtscts)#软件流控
    print(self.main_engine.dsrdtr)#硬件流控
    print(self.main_engine.interCharTimeout)#字符间隔超时

  #打开串口
  def Open_Engine(self):
    self.main_engine.open()

  #关闭串口
  def Close_Engine(self):
    self.main_engine.close()
    print(self.main_engine.is_open) # 检验串口是否打开

  # 打印可用串口列表
  @staticmethod
  def Print_Used_Com():
    port_list = list(serial.tools.list_ports.comports())
    print('*' * 50)
    print(port_list)
    print('*' * 50)
    return port_list
