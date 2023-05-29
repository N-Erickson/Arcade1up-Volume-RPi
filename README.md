# Arcade1up-Volume-RPi
Python script to control the volume of the original arcade1up cabinets. 

Script was written in 2018 for the original Street Fighet II Arcade1Up cabinet. 

After removing the original board, I connected the wires from the original volume control switch to the GPIO pins on the Raspberry Pi. 

The switch position corresponds to a button press and sets the volume level accordingly. 

Set the script to run on startup. 

You can use any valid pinout configuration, I used 16, 20, and 21.

![rp2_pinout](https://github.com/N-Erickson/Arcade1up-Volume-RPi/assets/16261609/4afe8aaa-22d3-47df-a2d8-30ba4e9c1596)
