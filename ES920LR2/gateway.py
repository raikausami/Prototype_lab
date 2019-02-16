import es920lr
import time
import socket


lr = ES920LR()
lr.open()

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind("./socket_file")
server.listen(1)


try :
   while True :
        client, info = server.accept()
        payload = client.recv(4096)
        print payload
        lr.write(payload)

except KeyboardInterrupt:
    lr.close()