from turtle import Turtle,Screen,colormode
#import cv2
import PIL
from PIL import Image
import numpy as np
colormode(255)

img = Image.open("image_path.jpg")
height,width = img.size
print(height)
print(width)
#img = img.resize((height//2,width//2))
img.thumbnail((200,200))
arr = np.array(img)
print(len(arr))
t1= Turtle()
S1 =Screen()
t1.hideturtle()
t1.penup()
t1.speed(0)
k = 250
for j in range(len(arr)):
    if j % 2 == 0:
        t1.goto(-250,k)
        for i in range(len(arr[j])):
            if i%2 == 0:
                t1.color(arr[j][i])
                t1.dot()
                t1.forward(5)
        k-=5

S1.exitonclick()
