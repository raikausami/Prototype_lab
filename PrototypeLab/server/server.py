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
                sql_str = "SELECT Name FROM Employee WHERE iBeaconId = \'"
                ibeaconId_str = payload_tpl[2]
                ibeaconId_str = ibeaconId_str[:len(ibeaconId_str)-2]
            
            if cur.execute(sql_str + ibeaconId_str + "';"):
                print cur.fetchall()[0][0]
            
            time.sleep(0.01)

    except KeyboardInterrupt:
        lr.close()
                cur.close()
                db.close()
