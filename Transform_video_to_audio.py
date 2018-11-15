FFMPEG_BIN = "C:/ffmpeg/bin/ffmpeg.exe"
import subprocess as sp

# define a new function and its parameters are the path of input and output materials
def convert_video(video_input, video_output):
    command = [FFMPEG_BIN,
               "-i", video_input,  # input path
               "-f", "wav",  # format
               "-vn",  # disable video recording
               "-ar", "44100",  # sets the sampling rate for audio streams
               "-ac", "2",  # set the number of audio channels
               "-b:a", "1640k",  # set the audio bit
               video_output]  # output path
    sp.Popen(command)

# test new function
convert_video("C:/Users/taotao/Desktop/research/test.mp4", "C:/Users/taotao/Desktop/research/test.wav")
