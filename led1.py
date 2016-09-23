#import RPi.GPIO as GPIO

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


import time

slow = 1.0
fast = 0.1
ch_in = 11  #pin 11
ch_out = 16 #pin 16
ch_out = 40 #pin 40
 
dur = slow



# event handler - change speed of led flash
def my_callback(ch):
    global dur
    if dur == fast:
        dur = slow
    else:
        dur = fast



def main():
    rev = GPIO.RPI_INFO['P1_REVISION']
    print(rev)

    GPIO.setmode(GPIO.BOARD)
      # or
    #GPIO.setmode(GPIO.BCM)


    GPIO.setup(ch_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(ch_out, GPIO.OUT)

    GPIO.add_event_detect(ch_in, GPIO.RISING, callback=my_callback, bouncetime=200)

    # flash led 50 times, 50% duty cycle
    for i in range(0, 50):
            GPIO.output(ch_out, GPIO.HIGH)
            time.sleep(dur)
            GPIO.output(ch_out, GPIO.LOW)
            time.sleep(dur)
            



    GPIO.cleanup()



main()
