import es920lr
import time
import sys
import serial
import MySQLdb



if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="OWNER", passwd="12345", db="prototype_lab") 
    cur = db.cursor()
    ser = serial.Serial("/dev/ttyUSB0", 115200)
    lr = es920lr.ES920LR(ser)
    lr.set_id("0001", "1111", "FFFF")

    if lr.open():
        print "OK"
        time.sleep(3)
    
    else:
        lr.close()
        print "NG"
        sys.exit(1)
    
    try:
        while True:
            payload = lr.read()
            
            if payload == None:
                pass
            
            else:
                payload_tpl = payload
                tmp = payload_tpl[2][:len(payload_tpl[2])-2]
                counter_str = tmp.split(',')[0]
                ibeaconId_str = tmp.split(',')[1]
                LoRaId_str = payload_tpl[1]
                
                sql_str = "INSERT INTO Occupation_info (Count, iBeaconId, LoRaId) VALUES(" + counter_str + ","
                
                if cur.execute(sql_str + "\'" + ibeaconId_str +"\', " + "\'" + LoRaId_str+"\');"):
                    print "commit to db"
                    db.commit()
            
            time.sleep(0.000001)

    except KeyboardInterrupt:
        lr.close()
        cur.execute("TRUNCATE TABLE Occupation_info;")
        cur.close()
        db.close()
