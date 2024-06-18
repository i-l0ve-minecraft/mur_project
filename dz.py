import pymurapi as mur
from time import sleep
import cv2
auv = mur.mur_init()
print('OpenCV version:', cv2.__version__)


def stop():
    auv.set_motor_power(0, 0)
    auv.set_motor_power(1, 0)    
    auv.set_motor_power(2, 0)    
    auv.set_motor_power(3, 0)
    auv.set_motor_power(4, 0)
    


def set_vertical_power(power):
    auv.set_motor_power(2, power)
    auv.set_motor_power(3, power)
    
def shoot():
    auv.shoot()
    
def set_rotate_power(power):
    auv.set_motor_power(0, +power)
    auv.set_motor_power(1, -power)
    
def keep_depth(target_depth):
    depth = auv.get_depth()
    error_depth = target_depth - auv.get_depth()
    power_depth = 20 * error_depth
    set_vertical_power(-power_depth)
    sleep(0.1)

def keep_yaw(target_yaw):
    error_yaw = target_yaw - auv.get_yaw()
    power_yaw = 0.5 * error_yaw
    set_rotate_power(power_yaw)
    sleep(0.1)
    
def move_forvart(rep):
    while rep > 0:
        auv.set_motor_power(0, 50)
        auv.set_motor_power(2, 50)
        rep = rep - 1
        
def move_back(rep):
    while rep > 0:
        auv.set_motor_power(0, -500)
        auv.set_motor_power(2, -500)
        rep = rep - 1

    

gg = 0
while gg < 200:
    keep_depth(3.7)
    gg = gg + 1
    print('keep_depth')
print('gg = 0')
gg = 0
print('move_back')
while gg < 220:
    auv.set_motor_power(0, -50)
    auv.set_motor_power(1, -50)
    sleep(0.001)
    gg = gg + 1
    print('move_back')
stop()
auv.set_motor_power(0, 50)
auv.set_motor_power(1, 50)
stop()



    