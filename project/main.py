#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
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
BLUE = 80
PURPLE= 95
WHITE = 85
threshold = (BLUE + WHITE) / 2

# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = -30

# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 101.2 = 12 degrees per second.
PROPORTIONAL_GAIN = 1.2

# def forward():
#     robot.drive(DRIVE_SPEED, turn_rate)


#grÃ¶n 11-16
# Start following the line endlessly.
"""
def dont_excpect():
    start_time = time.time()
    s = 4
    for i in range (1, s):
        end_time = time.time()
        a = end_time - start_time
        return a"""
while True:
    print(line_sensor.reflection())

    if 11 <= line_sensor.reflection() <= 21:
        robot.drive(-30, line_sensor.reflection())
    elif line_sensor.reflection() < 11:
        right_motor.run(200)
        left_motor.run(-200)
        print("I turned")
        wait(2000)
    elif line_sensor.reflection() > 77:
        correction = (20-line_sensor.reflection())*2
        robot.drive(-20, correction)
        #print("yes yes")

    elif 66 <= line_sensor.reflection() <= 79:
        robot.drive(-30 , line_sensor.reflection())
        #print("i working her on pruprle")

    elif 56 <= line_sensor.reflection() <= 63:
        robot.drive(-30 , line_sensor.reflection())

    elif line_sensor.color() == Color.BLUE:
        wait(30000)
        print("Hello wrold")
    else:
        robot.drive(-43, line_sensor.reflection())

       # print("I dont know")
    if touch_sensor.pressed():

        crane_motor.dc(-120)
        print("gg boys")

    if ultra_sensor.distance() < 100:
        robot.stop()
        crane_motor.dc(10)
        wait(5000)
        DRIVE_SPEED = 100
        robot.stop()
        wait(5000)