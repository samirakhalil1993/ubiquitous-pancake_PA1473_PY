#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()
# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
ultra_sensor = UltrasonicSensor(Port.S4)
#Crane_motor=Port.A
Front_button=Port.S1
crane_motor= Motor(Port.A)
touch_sensor = TouchSensor(Port.S1)
# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Calculate the light threshold. Choose values based on your measurements.


WHITE = 81
ROSE= 60
PURPLE=15
DARK_GREEN = 20
BLUE= 12
GREEN = 13


# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = -83



def line_follwing():
    correction = (30 - line_sensor.reflection())*3
    robot.drive(DRIVE_SPEED , correction )
    

def correction():
    robot.drive(-70, line_sensor.reflection())
    robot.drive(50,200)
    robot.drive(-100,200)


def white():
    robot.drive(50,-100 )




  
  

print(line_sensor.reflection()) 
    
while True:
        if line_sensor.reflection() <= DARK_GREEN :
            line_follwing()
            print("DARK_GREEN")
            
            
            
        elif BLUE < line_sensor.reflection() < WHITE:
            line_follwing()
            print("ROSE")

        elif PURPLE < line_sensor.reflection() < ROSE:
            line_follwing()
            print("BLUE")

        elif GREEN < line_sensor.reflection() < BLUE:
            line_follwing()
            print("PURPLE")
            

        elif DARK_GREEN < line_sensor.reflection() < PURPLE :
            line_follwing()
            print("GREEN")
        
        elif WHITE > line_sensor.reflection() > ROSE :
            correction()
            print("WHITE/2")
        
        else:
            white()
            print("WHITE")

        

        if touch_sensor.pressed():

            crane_motor.dc(-120)
           # robot.distance(50)
            

        if ultra_sensor.distance() < 100:
            robot.stop()
            crane_motor.dc(10)
            wait(5000)
            DRIVE_SPEED = 100
            robot.stop()
            wait(5000)


    # #     # else:
    # #     #     robot.drive(-43, line_sensor.reflection())

    # Start following the line endlessly.

