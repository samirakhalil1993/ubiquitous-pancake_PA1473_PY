#!/usr/bin/env pybricks-micropython

# Import libraries
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

from pybricks.hubs import EV3Brick
ev3 = EV3Brick()

# Vilka portar som hör till vad
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
left_light = ColorSensor(Port.S1)
right_light = ColorSensor(Port.S4)

# Definierar roboten
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=118)

# Driving variables
base_speed = 100
speed_modifier_while_turning = 0.8
turn_intensity = 90
light_sensitivity = 20 

# Körloopen
while True:
    # Sväng vänster
    if left_light.reflection() < light_sensitivity:

        # Intensity upskattar hur skarp svängen är
        intensity = (100 - left_light.reflection()) / 100

        # Sänker hastigheten i skarpa kurvor
        speed_mod = 1 - intensity

        # Sätter in alla värden
        # Första värdet är hastigheten, andra värdet är hur mycket roboten ska svänga
        robot.drive(base_speed * speed_mod * speed_modifier_while_turning, -turn_intensity * intensity)

    elif right_light.reflection() < light_sensitivity:

        # Intensity upskattar hur skarp svängen är
        intensity = (100 - right_light.reflection()) / 100

        # Sänker hastigheten i skarpa kurvor
        speed_mod = 1 - intensity

        # Sätter in alla värden
        # Första värdet är hastigheten, andra värdet är hur mycket roboten ska svänga
        robot.drive(base_speed * speed_mod * speed_modifier_while_turning, turn_intensity * intensity)

    else:

        robot.drive(base_speed, 0)