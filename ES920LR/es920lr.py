import time
import serial



############# SERIAL CONST #############
SERIALPORT = '/dev/ttyUSB0'
BAUDRATE = 115200
NODE = 2
BW = 6
SF = 10
CHANNEL = 5
PANID = 0001
OWNID = 1111
DSTID = 2222
ACK = 2
RETRY = 0
RECVID = 2
RSSI = 2
SIZE = 50
RCODE = '\n'
SCODE = '\r\n'
FORMAT = 2
#########################################






class ES920LR(object):
    def __init__(self):
        self.ser = serial.Serial(SERIALPORT, baudrate=BAUDRATE)
        
    def open(self):
        self.ser.timeout = 0.1    
        res = self.ser.read(SIZE)

        self.ser.write('2'+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print str(res.replace('\r\n',''))
        
        self.ser.write('node '+str(NODE)+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print str(res.replace('\r\n',''))
        
        self.ser.write('bw '+str(BW)+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print str(res.replace('\r\n',''))
        
        self.ser.write('sf '+str(SF)+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print str(res.replace('\r\n',''))
        
        self.ser.write('channel '+str(CHANNEL)+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print str(res.replace('\r\n',''))
        
        self.ser.write('panid '+str(PANID)+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print str(res.replace('\r\n',''))
        
        self.ser.write('ownid '+str(OWNID)+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print str(res.replace('\r\n',''))
        
        self.ser.write('dstid '+str(DSTID)+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print str(res.replace('\r\n',''))
        
        self.ser.write('ack '+str(ACK)+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        ##print str(res.replace('\r\n',''))
        
        self.ser.write('rssi '+str(RSSI)+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print str(res.replace('\r\n',''))
        
        self.ser.write('format '+str(FORMAT)+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print str(res.replace('\r\n',''))
        
        self.ser.write('save'+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print str(res.replace('\r\n',''))

        self.ser.write('start'+SCODE)
        self.ser.flush()
        res = self.ser.read(SIZE)
        #print 'start : ',

        if (res.replace('\r\n','')=='OK'):
            return True
        else:
            return False


    def cloase(self):
        self.ser.close()


    def read(self):
        return self.ser.readline().decode('utf-8')[8:]


    def write(self, payload_str):
        self.ser.write(payload_str.encode('utf-8'))