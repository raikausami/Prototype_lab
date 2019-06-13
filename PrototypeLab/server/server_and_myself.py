import es920lr
import time
import sys
import serial
import MySQLdb
import socket
import os
import threading



db = MySQLdb.connect(host="localhost", user="OWNER", passwd="12345", db="prototype_lab")
cur = db.cursor()


def get_uuid_from_others():
    ser = serial.Serial("/dev/serial0", 115200)
		
    #ser = serial.Serial("/dev/ttyUSB0", 115200)
    lr = es920lr.ES920LR(ser)
    lr.set_id("0001", "1111", "FFFF")

    #print "start configuration..."

    if lr.open():
        #print "finish configuration"
        pass
    
    else:
        #print "no need configuration"
        pass
    
    try:
        while True:
            payload = lr.read()
            #print(payload)
            if payload == None:
                pass
            
            else:
                payload_tpl = payload
                tmp = payload_tpl[2][:len(payload_tpl[2])-2]
                
                if tmp=='END':
                    #print("END2")
                    #commit_flag[0]=1
                    lr.close()
                    #cur.execute("TRUNCATE TABLE Occupation_info;")
                    
                    return 1
            
                #print(tmp)
                try:
                    counter_str = tmp.split(',')[0]
                    ibeaconId_str = tmp.split(',')[1]
                    LoRaId_str = payload_tpl[1]
                
                    sql_str = "INSERT INTO Occupation_info (Count, iBeaconId, LoRaId) VALUES(" + counter_str + ","
                    
                    cur.execute(sql_str + "\'" + ibeaconId_str +"\', " + "\'" + LoRaId_str+"\');")
                    db.commit()
                    #print "commit to db"
                
                except IndexError:
                    pass

            time.sleep(0.000001)

    except KeyboardInterrupt:
        lr.close()
        cur.execute("TRUNCATE TABLE Occupation_info;")
        cur.close()
        db.close()


def get_uuid_from_myself(counter):
    pro_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    pro_sock.bind("./socket_file")
    pro_sock.listen(1)

    try :
        while True :
            client, info = pro_sock.accept()
            recv_data = client.recv(4096)
            client.close()

            if recv_data == "":
                pass

            else:
                os.system("clear")
                #print("Check") 
                sql_str = "INSERT INTO Occupation_info (Count, iBeaconId, LoRaId) VALUES("+str(counter)+","
    
                try:
                    uuid_lst = eval(recv_data)
                except SyntaxError:
                    #print("ma")
                    os.remove("./socket_file")
                    return 1
                  

                for uuid in uuid_lst:
                    #print uuid

                    cur.execute(sql_str + "\'" + uuid + "\'"  + ", \'1111\');")
                    #print "commit to db"
                
                db.commit()
                 
                os.remove("./socket_file")
                counter += 1
                return 1

    except KeyboardInterrupt:
        os.remove("./socket_file")
    
    os.remove("./socket_file")

if __name__ == "__main__":
    counter = 1
    #thread1 = threading.Thread(target=get_uuid_from_others)
    #thread2 = threading.Thread(target=get_uuid_from_myself)

    #thread1.start()
    #thread2.start()
    try:
        while(1):
            if get_uuid_from_others():
                #print "finish get_uuid_from_others()"

                if get_uuid_from_myself(counter):
                    #print "yakiniku"
                    os.system("python display.py")
                    counter += 1
                    #os.system("ls")
                    #serialnokaihou
                    #print "yakiniku2"

    except KeyboardInterrupt:
        pass
                
