import pyaudio
import os
import serial
import binascii
import subprocess
import time


############## AUDIO CONST ###############
REPEAT_NUM = 100
RECIEVE_BIN_NAME = 'rcvfile.bin'
DECODED_RAW_NAME = 'decodedrawfile.raw'
CHUNK=1024
RATE=8000
############# SERIAL CONST #############
SERIALPORT = '/dev/ttyUSB1'
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
#============== declaration =================#
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,
				channels = 1,
				rate = RATE,
				frames_per_buffer = CHUNK,
				input = False,
				output = True)
ser = serial.Serial(SERIALPORT, baudrate=BAUDRATE)
#============================================#

#================= ES920LR CONFIG ==================#
def es920lr_config():
	ser.timeout = 0.1	
	res = ser.read(SIZE)
	ser.write('2'+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.write('node '+str(NODE)+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.write('bw '+str(BW)+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.write('sf '+str(SF)+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.write('channel '+str(CHANNEL)+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.write('panid '+str(PANID)+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.write('ownid '+str(OWNID)+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.write('dstid '+str(DSTID)+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.write('ack '+str(ACK)+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.write('rssi '+str(RSSI)+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.write('format '+str(FORMAT)+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.write('save'+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print str(res.replace('\r\n',''))
	ser.flush()

	ser.write('start'+SCODE)
	ser.flush()
	res = ser.read(SIZE)
	print 'start : ',
	if (res.replace('\r\n','')=='OK'):
		return True
	else:
		return False
#=================================================#

if __name__ == "__main__":

	if es920lr_config():
		print '--- RX START ---'
	else:
		print 'ERROR : Please reset ES920LR and Try again.'

	ser.timeout = None
	for i in range(REPEAT_NUM):
		res = ser.read(37)
#		print binascii.b2a_hex(res[1:37])
		f = open(RECIEVE_BIN_NAME,'wb')
		f.write(res[1:37])
		f.close()
		subprocess.call(['c2dec','700',RECIEVE_BIN_NAME,DECODED_RAW_NAME])
		f = open(DECODED_RAW_NAME,'rb')
		output = stream.write(f.read())
		f.close()

	stream.stop_stream()
	stream.close()
	p.terminate()
	print "--- RX CLOSED ---"
