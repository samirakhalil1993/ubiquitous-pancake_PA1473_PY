#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

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



# Start following the line endlessly.
while True:
    print(line_sensor.reflection())

    if line_sensor.reflection() > 77:
        correction = (20-line_sensor.reflection())2
        robot.drive(-75,correction)

    elif line_sensor.reflection() < 20:
        robot.drive(DRIVE_SPEED - 20, line_sensor.reflection())

    elif 68 <= line_sensor.reflection() <= 77:
        robot.drive(DRIVE_SPEED - 14, line_sensor.reflection())
    else:


        correction = (20-line_sensor.reflection())*2
        robot.drive(-56,correction)
        print("fuck me again")
    #print("fuck me")