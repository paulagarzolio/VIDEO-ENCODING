import os

class chooseExercise():
    def __init__(self,ex=0):
        self.exerciseNumber = ex
        self.exercices = list(["Convert a desired video format into different codecs. ","Choose two video codecs and export them in the same video output. ",
                               "Create a live streaming of the BBB video in thee following IP address: 127.0.0.1:23000. ","Select the desired IP address to broadcast the streaming BBB video. "])

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

    def selectVideo(self,direction):
        videos = list()
        files = os.listdir(os.getcwd()+"/"+direction)
        for file in files:  # this is done in order to get all thee files in the directory that are videos .mp4 or .mov
            if file[-4:] == (".mp4"):
                    videos.append(file)
        print(
            "Select the video from the list of possible videos in your current location: ")
        for i, x in enumerate(videos):
            print('{0}. {1}'.format(i, repr(
                x)))  # all the possible videos that the user can select will be displayed in the screen with their corresponding number.
        video_Selected = videos[int(input("ENTER: "))]  # here the user inputs the exercise number, and from the list of videos, it chooses the desired one

        return video_Selected

    def selectVideoCodec(self):
        codecs = list(["VP8","VP9","h265","AV1"])
        print(
            "\nSelect the new video codec from the list of possible ones: ")
        for i, x in enumerate(codecs):
            print('{0}. {1}'.format(i, repr(
                x)))  # all the possible videos that the user can select will be displayed in the screen with their corresponding number.
        codec_Selected = int(input(
            "ENTER: "))  # here the user inputs the exercise number, and from the list of videos, it chooses the desired one

        return codec_Selected

    def EX1(self):
        video_Selected = "formats/"+self.selectVideo("formats")
        codec_Selected = self.selectVideoCodec()

        codes = list(["ffmpeg -i "+video_Selected+" -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis VP8.mkv",
                      "ffmpeg -i "+video_Selected+" -c:v libvpx-vp9 -crf 30 -b:v 0 VP9.mkv",
                      "ffmpeg -i "+video_Selected+" -c:v libx265 h265.mkv",
                      "ffmpeg -i "+video_Selected+" -c:v libaom-av1 -crf 30 -b:v 0 AV1.mkv"])
        directories = list(["VP8.webm","VP9.webm","h265.webm","AV1.webm"])
        os.system(codes[codec_Selected])
        print("Video saved as: ", directories[codec_Selected])

    def EX2(self):
        print("Now you have to select two videeo codecs in order to see the comparison: ")
        codecs = list(["VP8", "VP9", "h265", "AV1"])
        videoCodec1 = self.selectVideoCodec()
        videoCodec2 = self.selectVideoCodec()
        directories = list(["VP8.webm", "VP9.webm", "h265.webm", "AV1.webm"])
        os.system("ffmpeg -i "+directories[videoCodec1]+" -i "+directories[videoCodec2]+ " -filter_complex hstack EX2Output.mp4")

    def EX3(self, IP="127.0.0.1:23000"):
        video_Selected = "bbb.mp4"
        os.system("ffmpeg -i lowquality.mp4 -v 0 -vcodec mpeg4 -f mpegts udp:// "+IP)

    def EX4(self):
        IP = int(input("Choose the IP to broadcast the bbb video (<ip>:<port>. "))
        self.EX3(IP)
    def printExercices(self):
        print("List of exercices: ")
        for i, x in enumerate(self.exercices):
            print('{0}. {1}'.format(i + 1, repr(
                x)))


exercise = chooseExercise()
exercise.printExercices()
exercise.executeExercise(int(input("Input exercise: ")))
