# Python_Automation

This repository includes some of my python automation projects which are :
1. Controlling Volume using your fingers
2. Program to Count Number of fingers held up by a person(Left Hand minor change for right hand)
3. Controlling the Hill Climb Racing Game using your hand

For this we have created a Hand Tracking Module using OpenCv and MediaPipe

#1 Controlling Volume 

This program adjusts the volume of your system by tracking the distance between your thumb and index fingers
the more the distance the Volume will increase the smaller the distance gets the Volume of your system reduces
** distance may vary upon your hand placement from the camera 


#2 Number of Fingers of Left Hand 

This program counts the number of fingers held up by a person on his/her left hand 
the code change needed to make to convert this program to right hand is as follows:

In line 30  of CountFingers.py change the code from 
if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]: 
to
if lmList[tipIds[id]][2] > lmList[tipIds[id] - 2][2]:
now you can use this for right hand counting fingeres

#3 Controlling Hill Climb Racing 

This program allows you to play the game hill climb racing using your right hand 

1. To press on the gas paddle you just have to show 5 on your right hand 🖐🏻
2. To press on the break paddle show 0 i.e fold your right fist  ✊🏻
3. To restart the game  you can  show a peace sign ✌🏻


Hope this helps in using these codes for references

