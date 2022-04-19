#!/usr/bin/env pybricks-micropython
import sys
import __init__

def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())


# Import libraries
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

from pybricks.hubs import EV3Brick
ev3 = EV3Brick()

# Vilka portar som hör till vad
Left_drive=Port.C 
Right_drive=Port.B
Crane_motor=Port.A
Front_button=Port.S1
Light_sensor=Port.S3
Ultrasonic_sensor=Port.S4

# Definierar roboten
robot = DriveBase(Left_drive, Right_drive, wheel_diameter=56, axle_track=118)

# Driving variables
speed = 100
speed_modifier_while_turning = 0.8
turn_intensity = 90
light_sensitivity = 20 

# Körloopen
while True:
    # Sväng vänster
    if Light_sensor.reflection() < light_sensitivity:

        # Intensity upskattar hur skarp svängen är
        intensity = (100 -Light_sensor.reflection()) / 100

        # Sänker hastigheten i skarpa kurvor
        speed_mod = 1 - intensity

        # Sätter in alla värden
        # Första värdet är hastigheten, andra värdet är hur mycket roboten ska svänga
        robot.drive(speed * speed_mod * speed_modifier_while_turning, -turn_intensity * intensity)

    

    if Ultrasonic_sensor.distance() < 150:
        mod_speed = -0.1
        robot.drive(mod_speed * speed, 0)
    #    print(Ultrasonic_sensor.distance())

    else:

        robot.drive(speed, 0)