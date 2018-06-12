import serial
import time
import requests
import json
import struct
import io

#check value type correctness
def isFloat(value):
 try:
  float(value)
  return True
 except:
  return False

#Your firebase url
firebase_url = 'https://arduinoraspberry-1d930.firebaseio.com/'

#Connect to serial port for reading data
serialPort = serial.Serial('/dev/ttyACM0', 9600, timeout=0)

#Set intervals you wanna how often you wanna read the data
intervalTime = 1

#Start infinite looping
while 1:
 try:
     
 #Read data from serial 
  serialData = serialPort.readline()
  
 #Temperatures in celcius
  tmpC= ''
  
 #Loop through the serial data
  for tempValue in serialData:
      
 #Get value to a variable
   tmpC=tmpC+chr(tempValue)

  if isFloat(tmpC) :
    tmpC=float(tmpC)
    
    if tmpC < 100:
 
    #Get Time and Date
      getTime = time.strftime('%H:%M:%S')
      getDate = time.strftime('%d/%m/%Y')

    #Create a data object
      data = {'date':getDate,'time':getTime,'value':tmpC}
 
    #Post result to a  Firebase
      result = requests.post(firebase_url + '/temperatures.json',
 data=json.dumps(data))
    
   #Wait your internal period
      time.sleep(intervalTime)
      
    else:
      print('Unrealistic high temperature: ' + str(tmpC))
      
 except IOError:
    print('Ups! Something unexpected happened!')
    time.sleep(intervalTime)