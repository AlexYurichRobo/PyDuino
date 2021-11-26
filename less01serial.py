import serial
import time

ser = serial.Serial('COM3',9600)
time.sleep(2)
print (ser.readline())
print ("Enter 1 to turn ON LED and 0 to turn OFF LED")

try: 
    while True:
        var = input()
        print ("you entered", var )
        if (var == '1'):
            ser.write(b'1')
            print ("LED turned ON")
            time.sleep(1)
    
        if (var == '0'):
            ser.write(b'0')
            print ("LED turned OFF")
            time.sleep(1)

except KeyboardInterrupt:
    ser.close()
    print ("program stop")
