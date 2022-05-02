#!/usr/bin/env python3
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

left_motor = Motor(Port.A) 
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=152) 



light = ColorSensor(Port.S1)
reflection = 60
speed =300
yellow_line = Color.YELLOW

while True :
    if  yellow_line:
        mod_speed = speed/2
        correction = (reflection - light.reflection()) *2*speed/150
        robot.drive(mod_speed ,correction)
    else:
        robot.drive(speed ,0)