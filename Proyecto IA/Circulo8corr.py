import cv2
import numpy as np

import serial
import time
ser = serial.Serial('COM3',9600)
cap = cv2.VideoCapture(1)
#img = cv2.imread("cap") #la imagen se sustituye por el video

while True:

	_,frame = cap.read() 
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	grayImage=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	low_blue = np.array([94,80,2])
	high_blue = np.array([126,255,255]) #para detectar el color azul
    #dimensions = frame.shape
 
	
	height = frame.shape[0]
	width = frame.shape[1]
	channels = frame.shape[2]

	largo=height/2
	ancho=width/2
	
	output=frame.copy()
	circles=cv2.HoughCircles( grayImage,cv2.HOUGH_GRADIENT,2,4000, param1=50,param2=30,minRadius=40, maxRadius=90)
	circles=np.uint16(np.around(circles))
	for circuloActual in circles[0,:]:
		centroX=circuloActual[0]
		centroY=circuloActual[1]
		radio=circuloActual[2]
		cv2.circle(output,(centroX,centroY),radio,(50,255,50),2)
	cv2.imshow('Video',output)
	movx=int(centroX)-int(ancho)
	movy=int(centroY)-int(largo)
	if(movx<=0):
		ser.write(b'L')
		time.sleep(1)
	else:
		if(movx>=0):
			ser.write(b'R')
			time.sleep(1)
		else:
			ser.write(b' ')
			time.sleep(1)
	if(movy<=0):
		ser.write(b'U')
		time.sleep(1)
	else:
		if(movx>=0):
			ser.write(b'D')
			time.sleep(1)
		else:
			ser.write(b' ')
			time.sleep(1)
	tecla = cv2.waitKey(5) & 0xFF
	if tecla == 27:
		break
	
    
  
mask = cv2.inRange( hsv_frame, low_blue, high_blue)

cv2.imshow("Frame",frame)
cv2.imshow("Image", cap)
cv2.imshow("Mask", mask)


cv2.waitKey(1)
cap.release()
#cv2.destroyAllWindows()
cv2.destroyAllWindows()
    
    

   
