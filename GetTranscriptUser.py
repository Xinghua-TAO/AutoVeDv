# first, please download ffmpeg package, numpy package and have your account that can use Google API
import os

from Set_wav import audio_path
from Set_csv import csv_path
from SpeechRecognition_GoogleCloud_Plus import transcribe_gcs_with_word_time_offsets
from Transform_video_to_audio import convert_video


def getTranscript(video):
    speech_file = audio_path(video)
    print(speech_file)

    convert_video(video, speech_file)
    csv_file = csv_path(video)

    transcribe_gcs_with_word_time_offsets(speech_file, csv_file)

    os.remove(speech_file)


getTranscript("C:/Users/taotao/Desktop/research/test/HHcut.mp4")
