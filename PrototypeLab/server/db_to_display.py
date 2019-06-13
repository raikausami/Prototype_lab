import MySQLdb
import time
import os

""" setting MySQL """
db = MySQLdb.connect(host="localhost", user="OWNER", passwd="12345", db="prototype_lab")
cur = db.cursor()
sql = 'show tables'
cur.execute(sql)


while True:
    db = MySQLdb.connect(host="localhost", user="OWNER", passwd="12345", db="prototype_lab")
    cur = db.cursor()
    if cur.execute("SELECT DISTINCT LoRaId From Occupation_info;"):
        LoRaId_tpl = cur.fetchall()


    for LoRaId in LoRaId_tpl:
        if cur.execute("SELECT * FROM Occupation_info WHERE (LoRaID = \""+str(LoRaId[0])+"\"" + ") AND (count = (SELECT MAX(count) FROM Occupation_info WHERE LoRaId = \""+str(LoRaId[0])+"\"));"): 
            rows = cur.fetchall()
            flag = False


            for row_tpl in rows:
                if not flag: 
                    if cur.execute("SELECT RoomNo FROM MeetingRoom WHERE (DeviceId = \""+str(row_tpl[2])+"\");"):
                        print(cur.fetchall()[0][0])
                        flag = True
                
                if cur.execute("SELECT Name FROM Employee WHERE (iBeaconId = \""+str(row_tpl[1])+"\");"):
                    print(cur.fetchall()[0][0])

            print
            


    time.sleep(6)
    os.system("clear")




cur.close()
db.close()
