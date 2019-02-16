import pyaudio
import time
import os
import subprocess
import serial
import binascii
import Queue
from threading import Thread

############## AUDIO CONST ###############
REPEAT_NUM = 100
RAW_NAME = 'rawfile.raw'
BIN_NAME = 'binaryfile.bin'
FRAME_NUM_PER_PACKET = 3
CHUNK=1024
RATE=8000
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
#============== declaration =================#
lasttime = time.time()
frames = []
sendque = Queue.Queue()
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,
				channels = 1,
				rate = RATE,
				frames_per_buffer = CHUNK,
				input = True,
				output = False)
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
		return False
	else:
		return 
#=================================================#

def raw2c2(input):
	global frames
	frames.append(input)
	if len(frames)==FRAME_NUM_PER_PACKET:
		f = open(RAW_NAME,'wb')
		f.write(b''.join(frames))
		f.close()
		frames=[]
		subprocess.call(['c2enc','700',RAW_NAME,BIN_NAME])
		f = open(BIN_NAME,'rb')
		sendque.put(f.read())
		f.close()

def send920():
	global lasttime
	for i in range(REPEAT_NUM):
		while sendque.empty():
			time.sleep(0.1)
		while (time.time()-lasttime)<0.25:
			time.sleep(0.01)
		print ser.write(binascii.a2b_hex('24')+sendque.get())
		ser.flush()
		lasttime = time.time()
	#	print binascii.b2a_hex(binascii.a2b_hex('24')+data)
	#	print 'res : '+ser.readline()

if __name__ == '__main__':

	if es920lr_config():
		print '--- TX START ---'
	else:
		print 'ERROR : Please reset ES920LR and Try again.'

	Tr_send920 = Thread(target = send920)
	Tr_send920.start()

	for i in range(REPEAT_NUM*FRAME_NUM_PER_PACKET):
		raw2c2(stream.read(CHUNK))

	Tr_send920.join()

	stream.stop_stream()
	stream.close()
	p.terminate()
	print "--- TX CLOSED ---"
