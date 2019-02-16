import es920lr
import time


lr = ES920LR()
lr.open()


try:
    while True:
        print(lr.read())

except KeyboardInterrupt:
    lr.close()