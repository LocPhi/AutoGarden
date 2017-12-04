# com.py V1.0 - 03/12/2017

import serial
import subprocess



def initCom():

    global arduino1
    global arduino2

    msg = 0
    nbtry = 10


    print("Init. Com :")


    print("Looking for Arduino ...")

    #---------------- ACM0 ----------------#

    print('__check for ACM0__')
    nb = nbtry

    while (msg != '1') and (msg != '2') and (nb > 0) :


        try:
            connect = serial.Serial('/dev/ttyACM0',9600,timeout=1)
            connect.write('W'.encode('ascii'))
            msg = str(connect.readline(1), 'ascii')
            
        except Exception as e:
            print(e)
            print("Error ... ?")      
            return -1

        nb = nb - 1
    
    print("msg= {}".format(msg))
    print("I find an Arduino ! And it's ...")

    if '2' == msg :
        print("A boy ! (2 - SMC)")
        arduino2 = connect
              
    elif '1' == msg :
        print("A girl ! (1 - Sensor)")
        arduino1 = connect

    else:
        print("What's that ?!? Hmmm ...")
        print(msg)
        print("i dunno ...")

    print('__check for ACM0 finished__')

    #---------------- ACM1 ----------------#

    print('__check for ACM1__')

    nb = nbtry
    msg = 0

    while (msg != '1') and (msg != '2') and (nb > 0) :


        try:
            connect = serial.Serial('/dev/ttyACM1',9600,timeout=1)
            connect.write('W'.encode('ascii'))
            msg = str(connect.readline(1), 'ascii')
            
        except Exception as e:
            print(e)
            print("Error ... ?")      
            return -1

        nb = nb - 1

    print('msg= {}'.format(msg))   
    print("I find an Arduino ! And it's ...")

    if '2' == msg :
        print("A boy ! (2 - SMC)")
        arduino2 = connect
              
    elif '1' == msg :
        print("A girl ! (1 - Sensor)")
        arduino1 = connect

    else:
        print("What's that ?!? Hmmm ...")
       

    print('__check for ACM1 finished__')

    #---------------- Init ArduinoSMC ----------------#

    arduino2.write("I;".encode('ascii'))
    arduino2.readline()
    arduino1.readline()
    arduino2.reset_input_buffer()
    arduino1.reset_input_buffer()
    return 0


def goTo(x,y):

    msg = ('G') + str(x) + str(y) + (';')
    arduino2.write(msg.encode('ascii'))

    return 0


def getTemperature():

    msg = ""

    arduino1.write('T'.encode('ascii'))

    try:
        while len(msg) < 5 :
            msg += str(arduino1.read(), 'ascii')
        arduino1.reset_output_buffer()
        arduino1.reset_input_buffer()
        
    except IOError:
        subprocess.call(['ls', '/dev/tty*'])

    return float(msg)


def getHumidity():

    msg = ""
    
    arduino1.write('H'.encode('ascii'))

    try:
        while len(msg) < 5 :
            msg += str(arduino1.read(), 'ascii')
        arduino1.reset_output_buffer()
        arduino1.reset_input_buffer()
        
    except IOError:
        subprocess.call(['ls', '/dev/tty*'])
    
    return int(float(msg))



def getMoisture():

    msg = ""

    arduino1.write('M'.encode('ascii'))
    
    try:
        while len(msg) < 5 :
            msg += str(arduino1.read(), 'ascii')
        arduino1.reset_output_buffer()
        arduino1.reset_input_buffer()
        
    except IOError:
        subprocess.call(['ls', '/dev/tty*'])

    return int(float(msg))


def getLuminosity():

    msg = ""

    arduino1.write('L'.encode('ascii'))

    try:
        while len(msg) < 5 :
            msg += str(arduino1.read(), 'ascii')
        arduino1.reset_output_buffer()
        arduino1.reset_input_buffer()
        
    except IOError:
        subprocess.call(['ls', '/dev/tty*'])

    return int(float(msg))
