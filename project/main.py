#!/usr/bin/env pybricks-micropython
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
"""Left_drive=Port.C 
Right_drive=Port.B
Crane_motor=Port.A
Front_button=Port.S1
Light_sensor=Port.S3
Ultrasonic_sensor=Port.S4"""
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
default_speed_crane = 0
time = 100 #ms
default_speed_touch = 100
default_speede = 0
#Making the robot move at normal speed
#left_motor.dc(default_speed)
#right_motor.dc(default_speed)

#Program loop
while running:
    if touch_sensor.pressed():

        crane_motor.dc(default_speed_crane - 100)
        print("gg boys")
        if not touch_sensor.pressed():
            correction = (30-left_light.reflection())*2
            robot.drive(-100,correction)
            print("gg girls")
            
    #if not touch_sensor.pressed():
     #   crane_motor.dc(default_speed_crane+50)
     #   correction = (30-left_light.reflection())*2
      #  robot.drive(-100,correction)

    while left_light.reflection() == line_color:

        right_motor.dc(default_speed - 20)
        left_motor.dc(default_speed -20)
        print("hello world")

    if ultra_sensor.distance() < 200:
        robot.stop()
        wait(10)

    crane_motor.dc(default_speed_crane+50)
    correction = (20-left_light.reflection())*2
    robot.drive(-100,correction)

    
    
        
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