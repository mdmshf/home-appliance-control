
from firebase import firebase
from nanpy import (ArduinoApi , SerialManager)
import requests
import json
import signal
import sys
import time
from datetime import datetime
import pyrebase
config={
    "apiKey":"AIzaSyAjRGV4SyGiQBJ04yel9gnrWmaxTukRuNY",
    "authDomain":"raspberrypi-17a5b.firebasepp.com",
    "databaseURL":"https://raspberrypi-17a5b.firebaseio.com",
    "projectId":"raspberrypi-17a5b",
   "storageBucket":"raspberry-17a5b.appspot.com",
    "messagingSenderId":"270977256797"
    };
firebase2=pyrebase.initialize_app(config)
db1=firebase2.database()

print " For exit please enter Ctrl+C "  ###break code when needed
def signal_handler(signal,frame):
    print "Bye!see you soon :)"
    sys.exit(0)
        
signal.signal(signal.SIGINT,signal_handler)
#SERIAL check with arduino
try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
    print "Connected with arduino"
except:
    print("Failed to connect to arduino")
#vaiable intialise with arduino
relay1 =7;
relay2 =6;
current1 = 3;
current2 = 2;
a.pinMode(relay1,a.OUTPUT)
a.pinMode(relay2,a.OUTPUT)
a.pinMode(current1,a.INPUT)
a.pinMode(current2,a.INPUT)
##############firebase request and url
firebaseUrl= 'https://raspberrypi-17a5b.firebaseio.com/'
firebaseRef=firebase.FirebaseApplication(firebaseUrl,None)
print "Firebase Url excepted"
try:
    while True:
##############current and power calculation
        for i in range(5):
            print "getting on/off from firebase"
            val1=int(firebaseRef.get('devices','device1'))
            #time.sleep(2);
            print str(val1)
            val2=int(firebaseRef.get('devices','device2'))
            #time.sleep(2);
            print str(val2)
            if(val1 == 1 and val2 == 1):
                a.digitalWrite(relay1,a.LOW)
                a.digitalWrite(relay2,a.LOW)
                print "Both relays are ON"
            elif(val1 == 0 and val2 == 1):
                a.digitalWrite(relay1,a.HIGH)
                a.digitalWrite(relay2,a.LOW)
                print "Relay 1 OFF & Relay 2 ON"
            elif(val1 == 1 and val2 == 0):
                a.digitalWrite(relay1,a.LOW)
                a.digitalWrite(relay2,a.HIGH)
                print "Relay 1 ON & Relay 2 OFF"
            elif(val1 == 0 and val2 == 0):
                a.digitalWrite(relay1,a.HIGH)
                a.digitalWrite(relay2,a.HIGH)
                print "Both relays are OFF"
            else:
                print "only 0,1 is accepted"
        
        #power and timestamp upload
        I1 = a.analogRead(current1)
        I1= (I1-300)*0.025
        I2 = a.analogRead(current2)
        I2 = (I2-400)*0.025
        
        p1 = I1*4.06
        p2 = I2*4.06
        if(p1<0):
            p1 =0;
        if(p2<0):
            p2=0;
        print "power"
        p1=p1-21;
        p2=p2-11;
        print p1;
        print p2;
        abc = str(datetime.now())
        
        if(val1 == 1 and val2 == 1):
            data={'power_value' :p1,'timestamp' :abc}
            requests.post(firebaseUrl+'/device1.json',data=json.dumps(data))
            data={'power_value' :p2,'timestamp' :abc} 
            requests.post(firebaseUrl+'/device2.json',data=json.dumps(data))
            print "Both relays are ON"
        elif(val1 == 0 and val2 == 1):
            data={'power_value' :0,'timestamp' :abc}
            requests.post(firebaseUrl+'/device1.json',data=json.dumps(data))
            data={'power_value' :p2,'timestamp' :abc} 
            requests.post(firebaseUrl+'/device2.json',data=json.dumps(data))
            print "Relay 1 OFF & Relay 2 ON"
        elif(val1 == 1 and val2 == 0):
            data={'power_value' :p1,'timestamp' :abc}
            requests.post(firebaseUrl+'/device1.json',data=json.dumps(data))
            data={'power_value' :0,'timestamp' :abc} 
            requests.post(firebaseUrl+'/device2.json',data=json.dumps(data))
            print "Relay 1 ON & Relay 2 OFF"
        elif(val1 == 0 and val2 == 0):
            data={'power_value' :0,'timestamp' :abc}
            requests.post(firebaseUrl+'/device1.json',data=json.dumps(data))
            data={'power_value' :0,'timestamp' :abc} 
            requests.post(firebaseUrl+'/device2.json',data=json.dumps(data))
            print "Both relays are OFF"
        else:
            print "only 0,1 is accepted"
        
############### action and devices on firebase
        ##act=int(firebaseRef.get('users','actions'))
        ##dev=int(firebaseRef.get('users','device'))
#############time and minutes from firebase
        ##hor=int(firebaseRef.get('users','hours'))
        ##min=int(firebaseRef.get('users','minutes'))
        preference=db1.child("preference").get()
#for keys in preference.shallow().get().each():
#w=preference..get()
#print(db1.child("preference").keys.val())
        for i in preference.each():
            act=int(i.val()['action'])
            dev=int(i.val()['device'])
            hor=int(i.val()['hours'])
            min=int(i.val()['minutes'])
   
            li= datetime.now()
            T=int(li.strftime('%H'))
            M=int(li.strftime('%M'))
            
            print(act,dev,hor,min,li,T,M)
            if(T == hor and M == min):
                if(act==1):
                    if(dev ==1):  #on the device 1
                        a.digitalWrite(relay1,a.LOW)#relay1 control swtich 1
                        db1.child("devices").update({"device1":"1"})
                    elif(dev ==2): #on the device 2
                        a.digitalWrite(relay2,a.LOW)
                        db1.child("devices").update({"device2":"1"})
                    elif(dev==3): #on both the device
                        a.digitalWrite(relay1,a.LOW)
                        db1.child("devices").update({"device1":"1"})
                        a.digitalWrite(relay2,a.LOW)
                        db1.child("devices").update({"device2":"1"})
                    else:
                        print "PUT either 1,2 OR 3"
                elif(act==0):
                    if(dev ==1):  #off the device 1
                        a.digitalWrite(relay1,a.HIGH)
                        db1.child("devices").update({"device1":"0"})#relay1 control swtich 1
                    elif(dev ==2):   #off the device 2
                        a.digitalWrite(relay2,a.HIGH)
                        db1.child("devices").update({"device2":"0"})
                    elif(dev==3):   #off both the device
                        a.digitalWrite(relay1,a.HIGH)
                        db1.child("devices").update({"device1":"0"})
                        a.digitalWrite(relay2,a.HIGH)
                        db1.child("devices").update({"device2":"0"})
                    else:
                        print "PUT either 1,2 OR 3"
                else:
                    print "Plese put valid input (1 0r 0)"
    
        
        
##########for controlling the relay with firebase server
        
except KeyboardInterrupt:
    print "Quit"
