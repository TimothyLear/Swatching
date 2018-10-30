#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

northPin = 32
southPin = 28
eastPin = 26
westPin = 24
trigPin = 22

GPIO.setup(northPin, GPIO.OUT)
GPIO.setup(southPin, GPIO.OUT)
GPIO.setup(eastPin, GPIO.OUT)
GPIO.setup(westPin, GPIO.OUT)
GPIO.setup(trigPin, GPIO.OUT)


for i in range(1):

	print("All On Lights On.")
	GPIO.output(northPin,southPin,eastPin,westPin, GPIO.HIGH)
	time.sleep(2.0)
	print.("Capturing All On Image")
	GPIO.output(trigPin, GPIO.HIGH)
	time.sleep(1.0)
	GPIO.output(trigPin, GPIO.LOW)
	print("All On Lights Off.")
	GPIO.output(northPin,southPin,eastPin,westPin, GPIO.LOW)

	print("North Lights On.")
	GPIO.output(northPin, GPIO.HIGH)
	time.sleep(2.0)
	print.("Capturing North Image")
	GPIO.output(trigPin, GPIO.HIGH)
	time.sleep(1.0)
	GPIO.output(trigPin, GPIO.LOW)
	print("North Lights Off.")
	GPIO.output(northPin, GPIO.LOW)

	print("South Lights On.")
	GPIO.output(southPin, GPIO.HIGH)
	time.sleep(2.0)
	print.("Capturing South Image")
	GPIO.output(trigPin, GPIO.HIGH)
	time.sleep(1.0)
	GPIO.output(trigPin, GPIO.LOW)
	print("South Lights Off.")
	GPIO.output(southPin, GPIO.LOW)

	print("East Lights On.")
	GPIO.output(eastPin, GPIO.HIGH)
	time.sleep(2.0)
	print.("Capturing East Image")
	GPIO.output(trigPin, GPIO.HIGH)
	time.sleep(1.0)
	GPIO.output(trigPin, GPIO.LOW)
	print("East Lights Off.")
	GPIO.output(eastPin, GPIO.LOW)

	print("West Lights On.")
	GPIO.output(westPin, GPIO.HIGH)
	time.sleep(2.0)
	print.("Capturing West Image")
	GPIO.output(trigPin, GPIO.HIGH)
	time.sleep(1.0)
	GPIO.output(trigPin, GPIO.LOW)
	print("West Lights Off.")
	GPIO.output(westPin, GPIO.LOW)

