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
    error_depth = target_depth - auv.get_depth()
    power_depth = 20 * error_depth
    set_vertical_power(-power_depth)
    sleep(0.1)

def keep_yaw(target_yaw):
    error_yaw = target_yaw - auv.get_yaw()
    power_yaw = 0.5 * error_yaw
    set_rotate_power(power_yaw)
    sleep(0.1)
    
#    if target_yaw < auv.get_yaw():
#        set_rotate_power(+power_yaw)
#        sleep(0.5)
#        print(error_yaw, '<')
#    elif target_yaw > auv.get_yaw():
#        set_rotate_power(-power_yaw)
#        sleep(0.5)
#        print(error_yaw, '>')
#    else:
#        stop()
        
        
# speed  = 50

while True:  


      
#    p_yaw = 0.3
#    yaw = auv.get_yaw()
#    error_yaw = target_yaw - yaw
#    power_yaw = p_yaw * error_yaw
#    
#    depth = auv.get_depth()
#    error_depth = target_depth - depth
#    power_depth = -50
#    power_depth = p_depth * error_depth
    
    
    
    
#   релейный регулятор высоты
#
#    if (error_depth > 0):
#        set_vertical_power(-speed) 
#        
#    elif(error_depth < 0):
#        set_vertical_power(+speed)
#        
#    else:
#        set_vertical_power(0)
    
     
# пропорциональный регулятор высоты
#    power_depth = p_depth * error_depth
#    set_vertical_power(power_depth)
    
    
# релейный регулятор поворота:
#    if (error_yaw > target_yaw):
#        set_rot(-powr, +powr)       
#    elif (error_yaw < target_yaw):
#        set_rot(+powr, -powr)
#    else:
#        set_rot(0, 0)
        
#пропорциональный регулятор поворота
#    set_rotate_power(power_yaw)
    keep_depth(2.5)