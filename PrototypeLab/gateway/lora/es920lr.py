import time



class ES920LR:
    def __init__(self, ser):
        self._ser = ser
        self._node = 2
        self._bw = 6
        self._sf = 10
        self._channel = 5
        self._pan_id = "0001"
        self._own_id = "1111"
        self._dst_id = "2222"
        self._ack = 2
        self._rssi = 2
        self._size = 50
        self._scode = '\r\n'
        self._rcvid = 1
        
    
    
    def set_id(self, pan_id, own_id, dst_id):
        self._pan_id = pan_id
        self._own_id = own_id
        self._dst_id = dst_id

    
    def open(self):
        self._ser.timeout = 0.1    
        res = self._ser.read(self._size)

        self._ser.write('2'+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))
        
        self._ser.write('load'+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))

        self._ser.write('save'+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))

        self._ser.write('node '+str(self._node)+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))
        
        self._ser.write('bw '+str(self._bw)+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))
        
        self._ser.write('sf '+str(self._sf)+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))
        
        self._ser.write('channel '+str(self._channel)+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))
        
        self._ser.write('panid '+str(self._pan_id)+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))
        
        self._ser.write('ownid '+str(self._own_id)+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))
        
        self._ser.write('dstid '+str(self._dst_id)+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))
        
        self._ser.write('ack '+str(self._ack)+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        ##print str(res.replace('\r\n',''))
        
        self._ser.write('rssi '+str(self._rssi)+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))
        
        self._ser.write('rcvid '+str(self._rcvid)+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))
        
        self._ser.write('save'+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print str(res.replace('\r\n',''))

        self._ser.write('start'+self._scode)
        self._ser.flush()
        res = self._ser.read(self._size)
        #print 'start : ',

        if (res.replace(self._scode,'')=='OK'):
            return True
        else:
            return False


    def close(self):
        self._ser.close()


    def read(self):
        payload_str = self._ser.readline().decode('utf-8')

        if payload_str == "":
            return None
            
        return (payload_str[:4], payload_str[4:8], payload_str[8:])


    def write(self, payload_str):
        self._ser.write(str(payload_str + self._scode).encode('utf-8'))