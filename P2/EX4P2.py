import subprocess
import os

def EX4P2():
    videos = list()
    files = os.listdir(os.getcwd())
    for file in files:  # this is done in order to get all thee files in the directory that are videos .mp4 or .mov
        if os.path.isfile(file):
            if file[-4:] == (".mov") or file[-4:] == (".mp4"):
                videos.append(file)

    print(
        "Select the image from the list of possible images in your current location: ")
    for i, x in enumerate(videos):
        print('{0}. {1}'.format(i, repr(
            x)))  # all the possible videos that the user can select will be displayed in the screen with their corresponding number.
    video_Selected = videos[int(input("ENTER: "))]  # here the user inputs the exercise number, and from the list of videos, it chooses the desired one
    os.system("ffmpeg -i"+ video_Selected+ "-q:a 0 -map a stereo.mp3") #first we get just the audio of the selected video and we store it in the directory
    os.system("ffmpeg -i stereo.mp3 -ac 1 mono.mp3")  #now we convert the stereo audio into mono
    os.system("ffmpeg -i mono.mp3 -acodec flac -vcodec copy out.flac") # here the mono audio is converted into another audio codec. Which in this case is .flac
    os.system("ffmpeg -i output.mp4 -i out.flac -c:v copy -map 0:v:0 -map 1:a:0 new.mp4") #lastly, we put the resulting audio again in the original video
    print("Image saved as: ", 'new.mp4')


