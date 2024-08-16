import time
import psutil
#import RPi.GPIO as GPIO
from  datetime import datetime

#GPIO.setmode(GPIO.BCM)
Gled = 18
Yled = 22
Rled = 23

# GPIO.setup(Gled, GPIO.OUT)
# GPIO.setup(Yled, GPIO.OUT)
# GPIO.setup(Rled, GPIO.OUT)

def cpu_usage_log():
    cpu_usage = psutil.cpu_percent(interval=1 , percpu=False)   
    print("CPU Usage: ", cpu_usage, "%")

    time_stamp = datetime.now()

    open("cpu_usage_log.txt", "a").write(f"CPU usage: {cpu_usage}% - {time_stamp}\n")

    if cpu_usage < 50:
        #GPIO.output(Gled, GPIO.HIGH)
        #GPIO.output(Yled, GPIO.LOW)
        #GPIO.output(Rled, GPIO.LOW)
        print("Green LED ON")
    elif cpu_usage < 80:
        #GPIO.output(Gled, GPIO.LOW)
        #GPIO.output(Yled, GPIO.HIGH)
        #GPIO.output(Rled, GPIO.LOW)
        print("Yellow LED ON")
    else:
        #GPIO.output(Gled, GPIO.LOW)
        #GPIO.output(Yled, GPIO.LOW)
        #GPIO.output(Rled, GPIO.HIGH)
        print("Red LED ON")

    return cpu_usage

while True:
    cpu_usage_log()


