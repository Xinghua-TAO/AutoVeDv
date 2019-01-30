# first, please download ffmpeg package, numpy package and have your account that can use Google API
from SpeechRecognition_GoogleCloud_Plus import transcribe_gcs_with_word_time_offsets
from Transform_video_to_audio import convert_video
FFMPEG_BIN = "C:/ffmpeg/bin/ffmpeg.exe"
import subprocess as sp


def get_transcript(video, speech_file, csv_file):
    convert_video(video, speech_file)
    transcribe_gcs_with_word_time_offsets(speech_file, csv_file)


get_transcript("C:/Users/taotao/Desktop/research/test/HHcut.mp4", "C:/Users/taotao/Desktop/research/test/HHcut.wav", "C:/Users/taotao/Desktop/research/test/HHcut.csv")
