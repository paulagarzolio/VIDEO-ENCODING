import os
import requests

class broadcastingStandard:
    def __init__(self, audio, video, name):
        self.audio = audio
        self.video =video
        self.name =name
    def getCodecs(self):
        return self.audio +self.video
    def getName(self):
        return self.name

class chooseExercise():
    def __init__(self,ex=0):
        self.exerciseNumber = ex
        self.exercices = list(["Output a video that shows the macroblocks and the motion vectors. ","Create a new BBB container with stereo mp3 and lower bitrate aac as audio tracks.",
                               "Read the tracks from an MP4 container and find which broadcasting standards would fit or add new broadcasting standard. ","Download subtitles, integrate them and output a video with printed subtitles. "])

    def setExercise(self,ex):
        self.exerciseNumber=ex

    def executeExercise(self,ex):
        self.setExercise(ex)
        if self.exerciseNumber ==1: self.EX1()
        if self.exerciseNumber == 2: self.EX2()
        if self.exerciseNumber == 3: self.EX3()
        if self.exerciseNumber == 4: self.EX4()

    def readVideoProp(self,videoName):
        os.system(
            "ffprobe -v error -show_format " + videoName + " >containerInfo.txt")
        f = open("containerInfo.txt", "r")
        result = dict(title="",artist="",genre="",duration="",format_name="",size="",bit_rate="")
        mensaje = f.readlines(0)
        for key in  result.keys():
            for i in range(len(mensaje)):
                if key in mensaje[i]:
                    startPoint = mensaje[i].find("=")
                    result[key]= (mensaje[i][startPoint + 1:-1])
        f.close()
        return result
    def readCodecs(self,videoName):
        os.system(
            "ffprobe -v error -show_entries stream=index,codec_name " + videoName + " >containerInfo.txt")
        f = open("containerInfo.txt", "r")
        videoCodecs = list()
        mensaje = f.readlines(0)
        for i in range(len(mensaje)):
            if mensaje[i].startswith("codec_name"):
                startPoint = len("codec_name")
                videoCodecs.append(mensaje[i][startPoint + 1:-1])
        f.close()
        return videoCodecs

    def selectVideo(self):
        videos = list()
        files = os.listdir(os.getcwd())
        for file in files:  # this is done in order to get all thee files in the directory that are videos .mp4 or .mov
            if os.path.isfile(file):
                if file[-4:] == (".mp4"):
                    videos.append(file)
        print(
            "Select the video from the list of possible videos in your current location: ")
        for i, x in enumerate(videos):
            print('{0}. {1}'.format(i, repr(
                x)))  # all the possible videos that the user can select will be displayed in the screen with their corresponding number.
        video_Selected = videos[int(input(
            "ENTER: "))]  # here the user inputs the exercise number, and from the list of videos, it chooses the desired one
        return video_Selected
    def EX1(self):
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
        video_Selected = videos[int(input(
            "ENTER: "))]  # here the user inputs the exercise number, and from the list of videos, it chooses the desired one
        os.system(
            "ffmpeg -flags2 +export_mvs -i " + video_Selected + " -vf codecview=mv=pf+bf+bb output.mp4")
        print("Video saved as: ", 'output.mp4')
    def EX2(self):
        video_Selected = "bbb.mp4"
        os.system(
            'ffmpeg -ss 00:00:00 -i ' + video_Selected + ' -to 00:01:00 -c copy bbb1min.mp4')
        os.system(
            "ffmpeg -i bbb1min.mp4 -an video.mp4")  # we save only the video in a separate file
        os.system(
            "ffmpeg -i bbb1min.mp4 -vn stereo.mp3")  # first we get just the audio of the selected video and we store it in the directory

        os.system(
            "ffmpeg -i bbb1min.mp4 -vn -c:a aac -b:a 50k output.aac")  # we convert the audio into aac codec and we also low the quality
        os.system(
            "ffmpeg -i video.mp4 -i output.aac -i stereo.mp3 -map 0:0 -map 1:0 -map 2:0 -c copy result.mp4")  # we store all the files in a mp4 container.
        print("Video saved as: ", 'result.mp4')

    def EX3(self):
        DVB = broadcastingStandard(["aac", "ac3", "mp3"],
                                   ["mpeg2video", "h264"], "DVB")
        ISDB = broadcastingStandard(["aac"], ["mpeg2video", "h264"], "ISDB")
        ISDB_Tb = broadcastingStandard(["aac_latm"], ["h264"], "ISDB_Tb")
        ATSC = broadcastingStandard(["ac3"], ["mpeg2video", "h264"], "ATSC")
        DTMB = broadcastingStandard(["ac3", "dra", "aac", "mp2", "mp3"],
                                    ["mpeg2video", "h264", "avs", "avs+"],
                                    "DTMB")

        standards = list([DVB, ISDB, ISDB_Tb, ATSC, DTMB])

        selection = 1
        while (selection != 0):
            print(
                "Options: \n 0. If you want to exit. \n 1. If you want to add an specific broadcasting standard.\n 2. If you want to find the broadcasting standards matching your input MP4 container.\n 3.If you want to show the characteristics of the video.")
            selection = int(input("ENTER: "))
            if selection == 1:
                name = str(input("Enter the name of the standard: "))
                audioT = int(input(
                    "Enter the total of audio Codecs that you want to add: "))
                audios = list()
                for i in range(audioT):
                    audios.append(input("Audio codec name: "))
                videoT = int(
                    input(
                        "Enter the total of Video Codecs that you want to add: "))
                videos = list()
                for i in range(videoT):
                    audios.append(input("Video codec name: "))
                standards.append(broadcastingStandard(audios, videos, name))
            if selection == 2:
                videoName = self.selectVideo()
                videoCodecs = self.readCodecs(videoName)
                validStandards = list()
                for standard in standards:
                    standardCodecs = standard.getCodecs()
                    result = all(
                        element in standardCodecs for element in videoCodecs)
                    if result:
                        validStandards.append(standard.getName())

                if len(validStandards) > 0:
                    print(
                        "This are the valid broadcasting standards that would fit: \n",
                        validStandards)
                else:
                    print(
                        "ERROR: This MP4 container does not fit any possible broadcasting standards")

            if selection==3:
                videoName = self.selectVideo()
                print("VIDEO CHARACTERISTICS: ")
                print(self.readVideoProp(videoName))
                print("\n")


    def EX4(self):
        url= "https: // raw.githubusercontent.com / paulagarzolio / VIDEO - ENCODING / main / S2 / content / subtitle.srt"
        os.system("wget "+url)
        os.system(
            "ffmpeg -i bbb.mp4 -vf subtitles=subtitle.srt -c:s mov_text -metadata:s:s:0 language=eng subtitles.mp4")
        print("Video saved as: ", 'subtitles.mp4')
    def printExercices(self):
        print("List of exercices: ")
        for i, x in enumerate(self.exercices):
            print('{0}. {1}'.format(i + 1, repr(
                x)))


exercise = chooseExercise()
exercise.printExercices()
exercise.executeExercise(int(input("Input exercise: ")))
