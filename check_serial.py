import time
import serial
ser=serial.Serial("/dev/ttyACM0",9600)
var=ser.readline()
val=var.split(',')
value=" ".join(val)
print value
#print val
        #time.sleep(1)
