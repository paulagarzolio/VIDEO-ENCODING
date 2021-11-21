from functions import RGBtoYUV, YUVtoRGB
import os
def EX1P1():
    option= int(input("Enter 1 if you want to translate from YUV to RGB: \nEnter 2 if you want to translate from RGB to YUV:"))
    a= int(input("First coordinate: "))
    b= int(input("Second coordinate: "))
    c= int(input("Third coordinate: "))

    if option==1:
        print("RGB coordinates= " ,YUVtoRGB(a,b,c))


    if option==2:
        print("YUV coordinates= " ,RGBtoYUV(a,b,c))

