# P2
In this folder we have:
- The different exercices of practice 2 (EX1, EX2, EX3, EX4) as well as a main menu from where we can execute all the different exercices.
- One video (bbb.mp4) with 1 min of duration

Each different exercise has a corresponding file with its corresponding function.
They all need to be in the same folder in order to work. 
Necessary packages for this project: subprocess, os

## EX1
In this first exercise, the user is asked to select the video that wants to use from all the videos in his corresponding repository, by entering the list number.
Then, it will be asked to input the length N that wants the video to have.
In this case, it will cut the remaining part and the resulting video will go from 00:00:00 to 00:00:N of the original video.
Finally the resulting video will be stored as "output.mp4".

## EX2
The user also has to select the desired video first and then it automatically saves the resulting ovelayed video (YUV histogram + original video) as "histVideo.mp4".

## EX3
The user is first asked to select the desired video outputs from a list (720p, 480p, 360:240,160:120) and then asks to select the desireed video.
Once the process is finished, the resulting video is saves as "scaledVideo.mp4".

# EX4
Again the user has to select the video option and then there are several processes that take place.
* Firstly the audio is separed from the video and saved as "stereo.mp3".
* Secondly it takes this video and after converting it to mono, it saves it as "mono.mp3"
* Then, this audio is converted from mp3 codec to flac.
* Finally, the resulting audio is again added into the original video.

Therefore, in "new.mp4" we have the original video with the modified audio.


