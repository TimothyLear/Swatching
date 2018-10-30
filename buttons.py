import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

northPin = 32
southPin = 28
eastPin = 26
westPin = 24
trigPin = 22

#when each button is pressed, the selected lights will turn on for the set time amount then off.

#All On Lights
for i in range(1):
    print("All On Lights On.")
    GPIO.output(northPin, southPin, eastPin, westPin, GPIO.HIGH)
    time.sleep(5.0)
    print("All On Lights Off.")
    GPIO.output(northPin, southPin, eastPin, westPin, GPIO.LOW)
#North Lights
for i in range(1):
    print("North Lights On.")
	GPIO.output(northPin, GPIO.HIGH)
	time.sleep(5.0)
	print("North Lights Off.")
	GPIO.output(northPin, GPIO.LOW)
#South Lights
for i in range(1):
    print("South Lights On.")
	GPIO.output(southPin, GPIO.HIGH)
	time.sleep(5.0)
	print("South Lights Off.")
	GPIO.output(southPin, GPIO.LOW)
#East Lights
for i in range(1):
    print("East Lights On.")
	GPIO.output(eastPin, GPIO.HIGH)
	time.sleep(5.0)
	print("East Lights Off.")
	GPIO.output(eastPin, GPIO.LOW)
#West Lights
for i in range(1):
    print("West Lights On.")
	GPIO.output(westPin, GPIO.HIGH)
	time.sleep(5.0)
	print("West Lights Off.")
	GPIO.output(westPin, GPIO.LOW)
#Camera Trigger
for i in range(1):
    print("Triggering Camera.")
	GPIO.output(trigPin, GPIO.HIGH)
	time.sleep(1.0)
	print("Triggering Camera.")
	GPIO.output(trigPin, GPIO.LOW)
