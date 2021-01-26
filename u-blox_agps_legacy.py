
import requests
import serial
import argparse

parser = argparse.ArgumentParser(description='Retrieve aiding data and update GPS module')
parser.add_argument('-t', '--token', required=True, help='your token to access AssistNow data site')
parser.add_argument('-d', '--device', required=True, help='the device/port where to reach the GPS device')

args = parser.parse_args()

print('Connecting to u-blox')

r = requests.get("http://online-live1.services.u-blox.com/GetOnlineData.ashx?token={args.token};gnss=gps;datatype=eph,alm,aux,pos;format=aid", stream=True)

print('Downloading AssistNowOnline Data')

ser = serial.Serial(args.device, 38400)

print('Waiting for GPS')

drainer = True
while drainer:
    drainer = ser.inWaiting()
    ser.read(drainer)

print('Writing AssistNowOnline Data')

ser.write(r.content)

print('Done')
