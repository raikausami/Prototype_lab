import time
import socket
import sys
import os
import serial
import MySQLdb




if __name__ == "__main__":
    counter = 1
    db = MySQLdb.connect(host="localhost", user="OWNER", passwd="12345", db="prototype_lab")
    cur = db.cursor()
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
                #sql_str = "SELECT Name FROM Employee WHERE iBeaconId = \'"
                os.system("clear")
                
                sql_str = "INSERT INTO Occupation_info (Count, iBeaconId, LoRaId) VALUES("+str(counter)+","
    
                uuid_lst = eval(recv_data)
                

                for uuid in uuid_lst:
                    print uuid
                    #print sql_str + "\'" + uuid + "\'"  + ", \'1111\');"

                    if cur.execute(sql_str + "\'" + uuid + "\'"  + ", \'1111\');"):
                        print "commit to db"
                        db.commit()

                
                counter += 1


    except KeyboardInterrupt:
        os.remove("./socket_file")
