import os
import imghdr
import subprocess
images = list()
files = os.listdir(os. getcwd())

for file in files:
    if imghdr.what(file)!= None:
        images.append(file)

print(images)
print("Select the image from the list of possible images in your current location: ")
for i, x in enumerate(images):
    print('{0}. {1}'.format(i, repr(x)))

image_Selected = images[int(input("ENTER: "))]
print(image_Selected)

subprocess.call(['ffmpeg', '-i', str(image_Selected), "-vf", "format=gray",'BWImage.jpeg'])