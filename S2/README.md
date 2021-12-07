# S2 - GUIDES

In this seminar, I have created a main.py file with a specific class that contains all the exercises and the functions used. The class has two attributes: the exercise number chosen by the user and the explanations of the different exercises.
Then, in main.py, what we do is to initialise a new object of that type of class. Then, the function printExercices() is called so that the user can see the possible exercises and their explanations. 
In the next step, the user is able to input the exercise, which will set the attribute exerciseNumber and will call the specific method for that exercise.

This are the general functions that are used in different exercises:
- selectVideo(): is used to let the user select the desired video from the list of possible ones.
- readCodecs() and readVideoProp(): these two functions are both used in exercise 3 and though they use similar code, they result in different outputs.
- executeExercise(): depending on the exerciseNumber attribute, it will call different functions.
- setExercise(): to set the value of the attribute exerciseNumber after the input of the user

For each different exercise, I will explain what I have implemented:

### EX1 
In this exercise, first it is called selectVideo() in which the user can choose the video he or she wants and then it creates a new video in which we can see the macroblocks and the motion vectors.
At the end, it displays the location at which the video has been saved (“output.mp4”)

### EX2 
In this exercise we want to create an mp4 container in which we have the BBB video with two specific audio tracks:
- aac with lower bitrate
- stereo mp3

In this case the videoSelected is specifically “bbb.mp4” and the user is not able to change it.
The first step is to create a copy of the video with a specific duration of 1 minute. Then, we store in different files the separate tracks: video track, an audio track converted to mp3 and another audio track converted to aac codec and with a lower quality (lower bit rate).

Now we have three streams, one with the original video in h264 codec and two audio streams: one aac and the other one mp3. The aac codec also has a reduced bit rate compared to the original.
Furthermore, if we display this video, we can hear this drop in quality when choosing the aac track.

### EX3
In this exercise the user is able to choose between 3 possible options:

   0. If you want to exit. 
   1. If you want to add an specific broadcasting standard.
   2. If you want to find the broadcasting standards matching your input MP4 container.
   3. If you want to show the characteristics of the video.
The initial proposal of the exercise was to find the broadcasting standards matching the input mp4 container. However, I have decided to also let the user add any specific broadcasting standard that is not already in the list and also to show other characteristics of the video that I found were interesting.
For doing so, I have created a new class broadcastingStandard and a list with all the standards (as objects of the new class).
In this way, it was easier to make the comparisons as all were objects of the same class.

### EX4
In this exercise, the user can add subtitles to a specific video (bbb.mp4). In this case, in the function, the subtitles are downloaded from my github repository, saved as subtitle.srt and finally integrated in the video.
As we can see we have added a new stream (0:2) which is the subtitle with some other information that I wanted to include like the language.
In this new video, we can choose if we want to see the videos with the subtitles or without them by changing the stream of subtitles from stream 1 to disable.



This is an example of a frame with subtitles (choosing the option: Stream 1):



