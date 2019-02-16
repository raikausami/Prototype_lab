import es920lr
import time


lr = ES920LR()
lr.open()


try:
    while True:
        lr.write("test")
        time.sleep(1)

except KeyboardInterrupt:
    lr.close()