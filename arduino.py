import db
import serial
import time 
 

arduino = serial.Serial('com3',9600)
time.sleep(2) 
print ("Welcome to student attendance system")
db.checktoday()
curr_staff = 0
while 1:
    tag = arduino.readline()
    if(curr_staff==0):
        curr_staff = db.scanstaff(tag)
    db.addattendance(tag,curr_staff)