from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt
import cv2
import os
import imghdr
import numpy as np

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

def applyDCT(inp, serie):
    try:
        im = cv2.imread(serie)
        if inp == 0:  # user selection is to convert input
            imF = dct2(im)

        if inp==1:

            imF = idct2(im)
        if inp==2:
            imF = dct2(im)
            imF = idct2(imF)

    except:
        im=serie
        if inp == 0:  # user selection is to convert input
            imF = dct(im)
        if inp == 1:
            imF = idct(im)
        if inp==2:
            imF = dct(im)
            imF = idct(imF)


    return imF


option=int(input("Enter 0 if you want to convert a random sequence, 1 if you want to write your own sequence or 2 if you want to convert an image: "))
if option==0:
    s=int(input("What random sequence do you prefer:\n 0: [[0,2,3,4],[0,1,2,1]] \n 1: [[0,0,0,0,4,4],[0,1,1,1,4,2],[4,1,9,1,4,2],[1,2,3,4,5,5]]\n"))
    if s==0:
        serie= [[0,2,3,4],[0,1,2,1]]
    if s==1:
        serie=[[0,0,0,0,4,4],[0,1,1,1,4,2],[4,1,9,1,4,2],[1,2,3,4,5,5]]
    d=applyDCT(0, serie)
    print("Result: ",d)
if option==1:
    rows= int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    serie=list()
    for i in range(rows):
        serie.append(list())
        for j in range(cols):
            value= int(input("Insert value: "))
            serie[i].append(value)
    d = applyDCT(0, serie)
    print("Result: ", d)


if option==2:
    images = list()
    files = os.listdir(os.getcwd())
    files = os.listdir(os.getcwd())
    for file in files:
        if os.path.isfile(file):
            if imghdr.what(file) != None and os.path.isfile(file):
                images.append(file)

    print(images)
    print(
        "Select the image from the list of possible images in your current location: ")
    for i, x in enumerate(images):
        print('{0}. {1}'.format(i, repr(x)))
    image_Selected = images[int(input("ENTER: "))]
    inp = int(input("Select 0 if you want to convert the sequence with DCT, 1 if you want to decode the sequence or 2 if you want both: "))
    d = applyDCT(inp, image_Selected)
    cv2.imwrite('imgDCT.jpeg', d)
    print("Result stored at imgDCT.jpeg.")
