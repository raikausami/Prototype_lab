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
OWNID = 2222
DSTID = 1111
ACK = 2
RETRY = 0
RECVID = 2
RSSI = 2
SIZE = 50
RCODE = '\n'
SCODE = '\r\n'
FORMAT = 2
#########################################

ser = serial.Serial(SERIALPORT, baudrate=BAUDRATE)

def es920lr_open(self):
    ser.timeout = 0.1
    res = ser.read(SIZE)

    ser.write('2'+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print str(res.replace('\r\n',''))

    ser.write('node '+str(NODE)+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print str(res.replace('\r\n',''))

    ser.write('bw '+str(BW)+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print str(res.replace('\r\n',''))

    ser.write('sf '+str(SF)+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print str(res.replace('\r\n',''))

    ser.write('channel '+str(CHANNEL)+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print str(res.replace('\r\n',''))

    ser.write('panid '+str(PANID)+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print str(res.replace('\r\n',''))

    ser.write('ownid '+str(OWNID)+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print str(res.replace('\r\n',''))

    ser.write('dstid '+str(DSTID)+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print str(res.replace('\r\n',''))

    ser.write('ack '+str(ACK)+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    ##print str(res.replace('\r\n',''))

    ser.write('rssi '+str(RSSI)+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print str(res.replace('\r\n',''))

    ser.write('format '+str(FORMAT)+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print str(res.replace('\r\n',''))

    ser.write('save'+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print str(res.replace('\r\n',''))

    ser.write('start'+SCODE)
    ser.flush()
    res = ser.read(SIZE)
    #print 'start : ',

    if (res.replace('\r\n','')=='OK'):
        return True
    else:
        return False


def es920lr_cloase(self):
    ser.close()


def es920lr_read(self):
    return ser.readline().decode('utf-8')[8:]


def es920lr_write(self, payload_str):
    ser.write(payload_str.encode('utf-8'))




if __name__ == "__main__":
    es920lr_open()
    
    try:
        while True:
            es920lr_read()
            time.sleep(1)

    except KeyboardInterrupt:
        es920lr_cloase()