#!/bin/python
from gpiozero import Button
from signal import pause
from subprocess import Popen
 
def middle_volume():
    Popen(['amixer', 'set', 'PCM', 'unmute'])
	  Popen(['amixer', 'set', 'PCM', '35%'])

def max_volume():
    Popen(['amixer', 'set', 'PCM', 'unmute'])
	  Popen(['amixer', 'set', 'PCM', '80%'])
 
def mute_volume():
    Popen(['amixer', 'set', 'PCM', '15%'])
 
muteSwitch = Button(16)
middleSwitch = Button(20)
rightSwitch = Button(21)

muteSwitch.when_pressed = mute_volume

middleSwitch.when_pressed = mute_volume
middleSwitch.when_released = middle_volume
rightSwitch.when_pressed = max_volume
rightSwitch.when_released = middle_volume
pause()
