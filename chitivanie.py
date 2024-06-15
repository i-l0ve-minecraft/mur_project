import pymurapi as mur
from time import sleep
import cv2

auv = mur.mur_init()

print('OpenCV version:', cv2.__version__)
while True:

    img_front = auv.get_image_front()
    img_bottom = auv.get_image_bottom()

    cv2.imshow('front', img_front)
    
    
    img_cropped = img_front[50:250, 50:150]
    cv2.imshow('crop', img_cropped)

    yaw = auv.get_yaw()
    
    height = img_front.shape[0]
    width = img_front.shape[1]
    
    print('width:', width, 'height:', height)
    new_size = (int(width / 2), int(height / 2))
    img_resized = cv2.resize(img_front, new_size)
    cv2.imshow('img_resized', img_resized)    


    img_flipped = cv2.flip(img_front, 0)
    cv2.imshow('img_flipped', img_flipped)
    
    img_drawing = img_front.copy()
    cv2.line(img_drawing, (10,10), (width-10,10), (225,0,0), 1)
    cv2.rectangle(img_drawing, (50,50), (100,100), (0, 225, 0), 10)
    cv2.circle(img_drawing, (150,50), 15, (0, 225, 55), 5)
 
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img_drawing, f'yaw: {yaw}', (100, 50), font, 1, (0,0,0), 1)
        
    cv2.imshow('img_drawing', img_drawing)
    
    
    cv2.waitKey(10)
    