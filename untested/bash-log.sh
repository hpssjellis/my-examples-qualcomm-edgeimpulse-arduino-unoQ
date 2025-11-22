#!/bin/bash
# myMonitorLogs.sh

# Path to the App-Lab's Linux application log
myLinuxLog="/var/log/applab/app.log"
# Path to the Arduino serial port (may vary, check dmesg)
myArduinoPort="/dev/ttyACM0"
myBaudRate=115200

echo "Starting Unified Logger (Ctrl+C to stop)..."
echo "----------------------------------------"

# Use two separate terminal windows or use 'tmux/screen'
# Here, we will just tail the log and then open the serial monitor

# 1. Tail the Linux App Log in the background
tail -f $myLinuxLog &
LINUX_PID=$!
echo "--- Linux App Logs (PID $LINUX_PID) ---"

# 2. Use a simple cat/screen for the Arduino Serial
echo "--- Arduino Serial Monitor ---"
# Using 'screen' is often best for serial port access
screen $myArduinoPort $myBaudRate

# Kill the background process when done
kill $LINUX_PID
