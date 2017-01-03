'''
Title    -  Communicating with Serial Ports  
Problem  -  want to read & write data over a serial port 
            interact with a hardware device 
'''

# pip install pySerial 
# serial 
import serial
# open serial connection 
ser = serial.Serial('/dev/tty.usbserial', # Device name 
                    baudrate=9600, 
                    bytesize=8,
                    parity='N',
                    stopbits=1)
# once open can read(), readline() write()
ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()
print(resp)

print('\n!---SECTION---\n')

