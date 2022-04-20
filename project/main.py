#!/usr/bin/env pybricks-micropython
import sys
import __init__

def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())


#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.

# Motor definitions
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
crane_motor= Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter= 56, axle_track= 120)
# Sensor definitions
left_light = ColorSensor(Port.S3)
ultra_sensor = UltrasonicSensor(Port.S4)
touch_sensor = TouchSensor(Port.S1)
# Your code goes here

#Declaring some varaibles for the robot
running = True

# line_color = Color.BLACK #Chosing to only detect black as the color
# floor_color = Color.WHITE #Floor is the white color
BLACK = 9
WHITE = 85
color_between = (BLACK + WHITE) / 2
default_speed = -100 #mm/s
PROPORTUINAL_GAIN = 1.2
#Making the robot move at normal speed

# left_motor.dc(default_speed)
# right_motor.dc(default_speed)

#Program loop

while running:
    deviation = left_ligt.reflection() - color_between
    turn_rate = PROPORTIONAL_GAIN * deviation  
    while touch_sensor.pressed():
        left_motor.stop()
        right_motor.stop() 
    while ultra_sensor.distance() < 100:
        left_motor.stop()
        right_motor.stop()     
    while left_light.reflection() == line_color:
        robot.drive(default_speed, turn_rate)
    whait(5)
    robot.stop()
    right_motor.brake()
    left_motor.brake()
        
"""PROPORTIONAL_GAIN = 1.2

# Start following the line endlessly.
while True:
    # Calculate the deviation from the threshold.
    deviation = line_sensor.reflection() - threshold

    # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation

    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)

    # You can wait for a short time or do other things in this loop.
    wait(10)"""