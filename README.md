# gcodeSender
A tiny Python script to send gcode to a 3D printer with a Linux machine attached over USB. This software is in a very early stage so keep that in mind if you use it.

# Requirements
- Python3
- Printrun (https://github.com/kliment/Printrun)

# Installation (untested)
Printer linux machine:
- Set the right USB serial port and the right baudrate in gcodeReceiver.py
- Put gcodeReceiver.py in autostart

Your Machine:
- Set the folder of the gcode file(s) in gcodeSender.py
- Set the IP of the linux machine of your printer in gcodeSender.py
- Put gcodeSender.py in autostart if you want
