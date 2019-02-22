import es920lr
import time
import socket
import sys
import os
import serial



def send_to_server(lr, data):
    payload_str_lst = eval(data[:len(data)])
    
    for payload_str in payload_str_lst:
        print payload_str
        lr.write(str(payload_str))
        time.sleep(0.3)



if __name__ == "__main__":
    ser = serial.Serial("/dev/serial0", 115200)
    lr = es920lr.ES920LR(ser)
    lr.set_id("0001", "2222", "1111")

    if lr.open():
        print "OK"
    
    else:
        lr.close()
        print "NG"
        sys.exit(1)

    pro_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    pro_sock.bind("../socket_file")
    pro_sock.listen(1)


    try :
        while True :
            client, info = pro_sock.accept()
            recv_data = client.recv(4096)
            client.close()

        if recv_data == "":
            pass

        else:
            send_to_server(lr, recv_data)
 
    except Exception:
        lr.close()
        os.remove("../socket_file")
