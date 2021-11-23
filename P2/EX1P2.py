import subprocess
import os
def EX1P2():
    videos = list()
    files = os.listdir(os.getcwd())
    for file in files: #this is done in order to get all thee files in the directory that are videos .mp4 or .mov
        if os.path.isfile(file):
            if file[-4:] == (".mov") or file[-4:] == (".mp4"):
                videos.append(file)

    print("Select the image from the list of possible images in your current location: ")
    for i, x in enumerate(videos):
        print('{0}. {1}'.format(i, repr(x))) #all the possible videos that the user can select will be displayed in the screen with their corresponding number.
    video_Selected = videos[int(input("ENTER: "))] #here the user inputs the exercise number, and from the list of videos, it chooses the desired one
    N=int(input("Length you want your video to have: ")) #here the user inputs the length of the video (how much they want to conserve from the original video
    string= "00:00:"+str(N)
    subprocess.call(['ffmpeg', '-ss','00:00:00','-i', video_Selected, "-to", string,"-c","copy",'output.mp4']) #this is the code used to call the terminal with the ffmpeg instructions
    print("Image saved as: ", 'output.mp4') #this will show the user the name of the output file
