import serial
import time
import sys

myPort = '/dev/ttyACM0'  # Check your actual port
myBaudRate = 115200

# ANSI color codes for terminal output
myColors = {
    '[ERROR]': '\033[91m', # Red
    '[VAR]': '\033[94m',   # Blue
    'RESET': '\033[0m'     # Reset color
}

try:
    mySerial = serial.Serial(myPort, myBaudRate)
    print(f"--- Connected to {myPort} at {myBaudRate} bps ---")
    while True:
        if mySerial.in_waiting > 0:
            myLine = mySerial.readline().decode('utf-8').strip()
            
            # Check for specific tags and apply color
            myColoredLine = myLine
            for myTag, myColor in myColors.items():
                if myTag in myLine:
                    myColoredLine = myColor + myLine + myColors['RESET']
                    break
            
            print(myColoredLine)

except serial.SerialException as e:
    print(f"Error opening serial port: {e}", file=sys.stderr)
    
except KeyboardInterrupt:
    print("\nExiting Smart Serial Monitor.")
    if 'mySerial' in locals() and mySerial.is_open:
        mySerial.close()
