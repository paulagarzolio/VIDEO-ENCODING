import os
import imghdr
import subprocess

def EX2P1():
    images = list()
    files = os.listdir(os. getcwd())

    for file in files:
        if os.path.isfile(file):
            if imghdr.what(file)!= None and os.path.isfile(file):
                images.append(file)

    print("Select the image from the list of possible images in your current location: ")
    for i, x in enumerate(images):
        print('{0}. {1}'.format(i, repr(x)))

    image_Selected = images[int(input("ENTER: "))]
    quality = str(input("Quality value: "))
    subprocess.call(['ffmpeg', '-i',str(image_Selected), '-q:v', quality,'LowQualityImage.jpeg'])
    print("Image saved as: ", 'LowQualityImage.jpeg')
