import sys, time
import RPi.GPIO as GPIO
from gpiozero import MotionSensor

#set up light
redPin = 16
greenPin = 20
bluePin = 21

#set up motion sensor
pir = MotionSensor(15)

#Different methods for different colors
def blink(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)
	

def turnOff(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

def redOn():
	blink(redPin)

def greenOn():
	blink(greenPin)

def blueOn():
	blink(bluePin)
def yellowOn():
	blink(redPin)
	blink(greenPin)

def cyanOn():
	blink(greenPin)
	blink(bluePin)

def magentaOn():
	blink(redPin)
	blink(bluePin)

def whiteOn():
	blink(redPin)
	blink(greenPin)
	blink(bluePin)

def redOff():
	turnOff(redPin)

def greenOff():
	turnOff(greenPin)

def blueOff():
	turnOff(bluePin)

def yellowOff():
	turnOff(redPin)
	turnOff(greenPin)

def cyanOff():
	turnOff(greenPin)
	turnOff(bluePin)

def magentaOff():
	turnOff(redPin)
	turnOff(bluePin)

def whiteOff():
	turnOff(redPin)
	turnOff(greenPin)
	turnOff(bluePin)
#main function
def main():

	while True: 
		pir.wait_for_motion()
		redOn()
		print ("Motion!")
		pir.wait_for_no_motion()
		redOff()
		print ("No Motion!")

main()


