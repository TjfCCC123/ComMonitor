#识别串口
#串口操作类
import serial
import serial.tools.list_ports
import gui
class Communication():

  #初始化
  def __init__(self,com,bps,timeout):
    self.port = com
    self.bps = bps
    self.timeout = timeout

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

  # 打印可用串口列表
  @staticmethod
  def Print_Used_Com():
    port_list = list(serial.tools.list_ports.comports())
    print('*' * 50)
    #print(port_list)
    for portN in port_list:
      print("端口号："+portN[0]+"端口名："+portN[1])
    print('*' * 50)
    return port_list

  #打开串口
  def Open_Engine(self,port,bps,timeout):
    self.port = port
    self.bps = bps
    self.timeout = timeout
    try:
      # 打开串口，并得到串口对象
      self.main_engine= serial.Serial(self.port,self.bps,timeout=self.timeout)
      # 判断是否打开成功
      if (self.main_engine.is_open):
        print("串口打开成功！")
    except Exception as e:
      print("---异常---：", e)

  #关闭串口
  def Close_Engine(self):
    print("关闭串口")
    self.main_engine.close()
    print(self.main_engine.is_open) # 检验串口是否打开

  #发送信息
  def sendMessage(self,message,flag):
    if flag:
      self.main_engine.write(message)# 十六进制发送数据
    else:
      self.main_engine.write(message.encode('utf-8'))

  def test_sendMessage(self):
    str = ''
    hstr = bytes.fromhex(str)
    self.main_engine.write(hstr)
   # instr = int(str,base = 16)
    #self.main_engine.write(chr(instr).encode('utf-8'))  # 十六制发送一个数据
    #self.main_engine.write(chr(0x12).encode("utf-8")) # 十六制发送一个数据
    self.main_engine.write('12'.encode('utf-8'))
