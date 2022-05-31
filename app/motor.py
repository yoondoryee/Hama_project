import RPi.GPIO as GPIO
import sys
import time

class Motor(object):
	GPIO.setmode(GPIO.BCM)

	pin1 = 20
	pin2 = 21
	EN1 = 16
	pin3 = 19
	pin4 = 26
	EN2 = 13

	GPIO.setup(pin1, GPIO.OUT)
	GPIO.setup(pin2, GPIO.OUT)
	GPIO.setup(EN1, GPIO.OUT)
	GPIO.setup(pin3, GPIO.OUT)
	GPIO.setup(pin4, GPIO.OUT)
	GPIO.setup(EN2, GPIO.OUT)

	def motor1():
		GPIO.output(pin1, GPIO.HIGH)
		GPIO.output(pin2, GPIO.LOW)
		GPIO.output(EN1, GPIO.HIGH)

	def motor2():
		GPIO.output(pin3, GPIO.HIGH)
		GPIO.output(pin4, GPIO.LOW)
		GPIO.output(EN2, GPIO.HIGH)

	def motor1Stop():
		GPIO.output(pin1, GPIO.LOW)
		GPIO.output(pin2, GPIO.LOW)
		GPIO.output(EN1, GPIO.LOW)
		#GPIO.cleanup()
		
	def motor2Stop():
		GPIO.output(pin3, GPIO.LOW)
		GPIO.output(pin4, GPIO.LOW)
		GPIO.output(EN2, GPIO.LOW)
		#GPIO.cleanup()

