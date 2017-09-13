import time
import os

while True:
    os.system("adb shell input swipe 100 100 100 100 3000")
    time.sleep(0.1)
    os.system("adb shell input swipe 100 100 100 100 200")
    time.sleep(2)

