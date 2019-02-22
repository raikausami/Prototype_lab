import time
import socket
import sys
import os
import serial
import MySQLdb



if __name__ == "__main__":
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
                sql_str = "SELECT Name FROM Employee WHERE iBeaconId = \'"
                
                if cur.execute(sql_str + recv_data + "\';"):
                    print cur.fetchall()[0][0]

    except Exception:
        lr.close()
        os.remove("./socket_file")
