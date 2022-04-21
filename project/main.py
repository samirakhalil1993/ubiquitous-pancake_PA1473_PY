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
ev3.speaker.beep()

# Motor definitions
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
crane_motor= Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter= 56, axle_track= 118)
# Sensor definitions
left_light = ColorSensor(Port.S3)
#right_light = ColorSensor(Port.S4) #La till denna själv ty enligt bilden ska det finnas två sensorer
ultra_sensor = UltrasonicSensor(Port.S4)
touch_sensor = TouchSensor(Port.S1)
# Your code goes here

#Declaring some varaibles for the robot
running = True

line_color = Color.BLACK #Chosing to only detect black as the color
floor_color = Color.WHITE #Floor is the white color
default_speed = -40 #mm/s

#Making the robot move at normal speed
#left_motor.dc(default_speed)
#right_motor.dc(default_speed)

#Program loop
gg  = 0
while running:
    if touch_sensor.pressed():
        crane_motor == (Button.LEFT_UP, Button.LEFT_DOWN)
        print("ewjwngv")
    while ultra_sensor.distance() < 100:
            left_motor.stop()
            right_motor.stop()
            print("gewef")
    while left_light.color() == line_color:
        robot.drive(-40,15)

            # right_motor.dc(default_speed + 5)
            # left_motor.dc(default_speed + 5)
        print("hello world")
        
    
        
