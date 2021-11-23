import subprocess
import os
#os.system("ffmpeg -i bbb.mp4 -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay test.mp4")
def EX2P2():
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

    subprocess.call(["ffmpeg","-i",video_Selected,"-vf","split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay","histVideo.mp4"])
    print("Video saved as: ", 'histVideo.mp4')
