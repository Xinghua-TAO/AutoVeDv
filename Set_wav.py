import os


def audio_path(video):
    current_path = os.path.abspath(video)
    speech_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + 'temp_file.wav')

    return speech_path
