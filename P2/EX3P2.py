import subprocess
import os
import imghdr
def EX3P2():
    files = os.listdir(os. getcwd())
    videoOutputs=list(["1280:720", "720:480", "360:240", "160:120"])
    print("Select the resolution you want your output video to have from the list of possible ones: ")
    for i, x in enumerate(videoOutputs):
        print('{0}. {1}'.format(i, repr(x))) #this will display all the possible resolutions that the video can have so that the user can choose the option they want

    option= int(input())
    resolution= videoOutputs[option]
    res="scale="+str(resolution)+",setsar=1:1" #this is the string used to know how the video is going to be scaled

    videos = list()
    files = os.listdir(os.getcwd())
    for file in files:  # this is done in order to get all thee files in the directory that are videos .mp4 or .mov
        if os.path.isfile(file):
            if file[-4:] == (".mov") or file[-4:] == (".mp4"):
                videos.append(file)

    print(
        "Select the video from the list of possible videos in your current location: ")
    for i, x in enumerate(videos):
        print('{0}. {1}'.format(i, repr(
            x)))  # all the possible videos that the user can select will be displayed in the screen with their corresponding number.
    video_Selected = videos[int(input("ENTER: "))]  # here the user inputs the exercise number, and from the list of videos, it chooses the desired one

    subprocess.call(["ffmpeg","-i",video_Selected,"-vf",res,'scaledVideo.mp4']) #ffmpeg code to scale the video
    print("Video saved as: ", 'scaledVideo.mp4')
