import setup as myfunc
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
    correction = (30 - myfunc.line_sensor.reflection())*3
    myfunc.robot.drive(DRIVE_SPEED , correction )
def correction():
    myfunc.robot.drive(-70, myfunc.line_sensor.reflection())
    myfunc.robot.drive(50,200)
    myfunc.robot.drive(-100,200)
def white():
    myfunc.robot.drive(50,-100 )
while True:
        if myfunc.line_sensor.reflection() <= DARK_GREEN :
            line_follwing()
            print("DARK_GREEN")



        elif BLUE < myfunc.line_sensor.reflection() < WHITE:
            line_follwing()
            print("ROSE")

        elif PURPLE < myfunc.line_sensor.reflection() < ROSE:
            line_follwing()
            print("BLUE")

        elif GREEN < myfunc.line_sensor.reflection() < BLUE:
            line_follwing()
            print("PURPLE")


        elif DARK_GREEN < myfunc.line_sensor.reflection() < PURPLE :
            line_follwing()
            print("GREEN")

        elif WHITE > myfunc.line_sensor.reflection() > ROSE :
            correction()
            print("WHITE/2")

        else:
            white()
            print("WHITE")



        if myfunc.touch_sensor.pressed():

            myfunc.crane_motor.dc(-120)
           # robot.distance(50)


        if myfunc.ultra_sensor.distance() < 100:
            myfunc.robot.stop()
            myfunc.crane_motor.dc(10)
            myfunc.robot.drive(100,100)
            myfunc.wait(5000)