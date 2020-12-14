
import requests
import serial

#comPort = "/dev/ublox7"
#comPort = "/dev/ublox8"
comPort = "/dev/ublox9"
#comPort = "/dev/ttyUSB0"

myToken = "<please fill in your token>"

print("Connecting to u-blox")
r = requests.get("http://online-live1.services.u-blox.com/GetOnlineData.ashx?token=" + myToken + ";gnss=gps,glo,qzss,bds,gal;datatype=eph,alm,aux", stream=True)
print("Downloading AssistNowOnline Data")

ser = serial.Serial(comPort, 38400)

print("Waiting for GPS")
drainer = True
while drainer:
    drainer = ser.inWaiting()
    ser.read(drainer)

print("Writing AssistNowOnline Data")
ser.write(r.content)
print("Done")
