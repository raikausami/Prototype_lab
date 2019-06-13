import es920lr
import MySQLdb
import os
import serial
import sys
import time


def send_to_gateway(lr, data_lst):
    #os.system("clear")
    time.sleep(0.1)
    #print(data_lst)
    for data in data_lst:
        print data

        lr.write(str(data))
    
    lr.write("END")


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="OWNER", passwd="12345", db="prototype_lab")
    cur = db.cursor()
    ser = serial.Serial("/dev/serial0", 115200)
    lr = es920lr.ES920LR(ser)
    lr.set_id("0001", "1111", "FFFF")

    #print "start configuration..."

    if lr.open():
        #print "finish configuration"
        pass

    else:
        #print "no need configuration"
        pass


    if cur.execute("SELECT DISTINCT LoRaId From Occupation_info;"):
        LoRaId_tpl = cur.fetchall()

    data_lst = list()
    
    try:

        for LoRaId in LoRaId_tpl:

            if cur.execute("SELECT * FROM Occupation_info WHERE (LoRaID = \""+str(LoRaId[0])+"\"" + ") AND (count = (SELECT MAX(count) FROM Occupation_info WHERE LoRaId = \""+str(LoRaId[0])+"\"));"): 
                rows = cur.fetchall()
                flag = False


                for row_tpl in rows:
                    if not flag: 
                        if cur.execute("SELECT RoomNo FROM MeetingRoom WHERE (DeviceId = \""+str(row_tpl[2])+"\");"):
                            a=cur.fetchall()[0][0]
                            #print("koko"+a+"koko")
                            data_lst.append("[" + str(a) + "]")
                            #print(data_lst)
                            flag = True
                    
                    if cur.execute("SELECT Name FROM Employee WHERE (iBeaconId = \""+str(row_tpl[1])+"\");"):
                        data_lst.append(cur.fetchall()[0][0])
                        #print data_lst
    
    except NameError:
        send_to_gateway(lr, ["None"])


    send_to_gateway(lr, data_lst)

    lr.close()
    cur.close()
    db.close()
