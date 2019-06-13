import es920lr
import time
import socket
import sys
import os
import serial


def display(lr):
    flag = True

    while True:
        payload = lr.read()

        if payload == None:
            pass

        else:
            payload_tpl = payload
            data_str = payload_tpl[2][:len(payload_tpl[2])-2]

            if data_str == "END":
                #print "End of display()"
                break
            

            if payload_tpl[0] and payload_tpl[1] and payload_tpl[2] and (not data_str == "2"):
                if flag:
                    os.system("clear")
                    flag = False

            print data_str
#print payload_tpl[0]
#print payload_tpl[1]

    
def exec_send_beacon_uuid():
#print "get ibeaconid executing..."
    os.system("sudo node ../ibeacon/sender_beacon_uuid_none.js")
#print "get ibeaconid executed"


def send_to_server(lr, counter, data):
    payload_str_lst = eval(data[:len(data)])

    for payload_str in payload_str_lst:
        lr.write((str(counter) + "," + str(payload_str)))
#print "send to server", payload_str
    
    lr.write("END")
    lr.write("END")
    lr.write("END")
    lr.write("END")
    lr.write("END")

#print "End of send_to_server()"
    
    """
    for payload_str in payload_str_lst
        while True:
            if lr.write((str(counter) + "," + str(payload_str))):
                break

            else:
                pass
                #print "write error"
                
    while True:
        if lr.write("END"):
            break
    """


if __name__ == "__main__":
    counter = 1
    ser = serial.Serial("/dev/serial0", 115200)
    lr = es920lr.ES920LR(ser)
    lr.set_id("0001", "2222", "1111")
    
    ##print "start configurarion..."

    if lr.open():
        #print "finish configuration"
        pass
        
    
    else:
#       print "no need configuration"
        pass
    
    
    try:
        pro_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        pro_sock.bind("../socket_file")
        pro_sock.listen(1)
    
    except socket.error:
    #print "soket error"
        lr.close()
        sys.exit(1)


    try :
        while True :
            exec_send_beacon_uuid()
            client, info = pro_sock.accept()
            recv_data = client.recv(4096)
            client.close()

            if recv_data == "":
                pass

            else:
                send_to_server(lr, counter, recv_data)
                counter += 1                                     
                display(lr)

    except KeyboardInterrupt:
        lr.close()
        os.remove("../socket_file")
