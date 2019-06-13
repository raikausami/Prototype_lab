import es920lr
import time
import socket
import sys
import os
import serial
import RPi.GPIO as GPIO



def display(lr):
    os.system("clear")

    while True:
        payload = lr.read()

        if payload == None:
            pass

        else:
            payload_tpl = payload

            if payload_tpl[2] == "END":
                break

            else:
                print payload_tpl[0]
                print payload_tpl[1]
                print payload_tpl[2]

    
def exec_send_beacon_uuid():
    os.system("sudo node ../ibeacon/sender_beacon_uuid")


def send_to_server(lr, counter, data):
    payload_str_lst = eval(data[:len(data)])
    os.system("clear")
    print counter

    for payload_str in payload_str_lst:
        print payload_str
        lr.write(str(counter) + "," + str(payload_str))
    
    lr.write("END")


if __name__ == "__main__":
    counter = 1
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
