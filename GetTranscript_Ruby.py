# first, please download ffmpeg package, numpy package and have your account that can use Google API
import os
from Set_wav import audio_path
from SpeechRecognition_GoogleCloud_Ruby import transcribe_gcs_with_word_time_offsets
from Transform_video_to_audio import convert_video


def getTranscript(video):
    speech_file = audio_path(video)
    convert_video(video, speech_file)

    transcribe_gcs_with_word_time_offsets(speech_file)

    os.remove(speech_file)


getTranscript("C:/Users/taotao/Desktop/research/test/HHcut.mp4")