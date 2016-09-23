#import RPi.GPIO as GPIO

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


import time

ch_in_up = 11  #pin 11
ch_in_down = 13  #pin 13

ch_out = 16 #pin 16
ch_out = 40 #pin 40
 

wait = 50

freq = 50 #Hz
dutycycle = 50.0 #%


# event handler - 
def my_callbackUp(ch):
    global dutycycle
    global p
    dutycycle += 5
    if dutycycle >= 100:
        dutycycle = 100.0
    p.ChangeDutyCycle(dutycycle)

def my_callbackDown(ch):
    global dutycycle
    global p
    dutycycle -= 5
    if dutycycle <= 0:
        dutycycle = 0
    p.ChangeDutyCycle(dutycycle)


def main():
    rev = GPIO.RPI_INFO['P1_REVISION']
    print(rev)
    global p
    global dutycycle

    GPIO.setmode(GPIO.BOARD)
      # or
    #GPIO.setmode(GPIO.BCM)


    GPIO.setup(ch_in_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(ch_in_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(ch_out, GPIO.OUT)

    GPIO.add_event_detect(ch_in_up, GPIO.RISING, callback=my_callbackUp, bouncetime=200)
    GPIO.add_event_detect(ch_in_down, GPIO.RISING, callback=my_callbackDown, bouncetime=200)

            
    p = GPIO.PWM(ch_out, freq)

    p.start(dutycycle)


    time.sleep(wait)


    p.stop()

    GPIO.cleanup()



main()
